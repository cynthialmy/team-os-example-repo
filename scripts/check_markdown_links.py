#!/usr/bin/env python3
"""Check markdown files for broken local links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IGNORE_FILE = REPO_ROOT / ".linkcheck-ignore.txt"


def strip_fenced_code_blocks(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            lines.append("")
            continue
        if not in_fence:
            lines.append(line)
        else:
            lines.append("")
    return "\n".join(lines)


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git/" not in path.as_posix() and "/.cursor/" not in path.as_posix()
    )


def normalize_link_target(raw_target: str) -> str:
    # Remove optional title: [text](path "title")
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()

    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0].strip()
    return target


def should_skip_target(target: str) -> bool:
    return (
        not target
        or target.startswith("#")
        or target.startswith(("http://", "https://", "mailto:", "tel:"))
    )


def resolve_target(source_file: Path, target: str) -> Path:
    if target.startswith("/"):
        return (REPO_ROOT / target.lstrip("/")).resolve()
    return (source_file.parent / target).resolve()


def main() -> int:
    markdown_files = iter_markdown_files(REPO_ROOT)
    broken: list[tuple[Path, str]] = []
    checked_links = 0
    ignored = load_ignored_links()

    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        text = strip_fenced_code_blocks(text)
        for match in LINK_PATTERN.finditer(text):
            target = normalize_link_target(match.group(1))
            if should_skip_target(target):
                continue

            link_path = target.split("#", 1)[0].strip()
            if should_skip_target(link_path):
                continue

            checked_links += 1
            resolved = resolve_target(markdown_file, link_path)
            relative_doc = markdown_file.relative_to(REPO_ROOT)
            if not resolved.exists() and (relative_doc.as_posix(), target) not in ignored:
                broken.append((relative_doc, target))

    if broken:
        print("markdown link check failed. Broken local links:")
        for doc_path, target in broken:
            print(f"  - {doc_path}: {target}")
        print(f"\nchecked {checked_links} local links across {len(markdown_files)} markdown files")
        return 1

    print(f"markdown link check passed ({checked_links} local links, {len(markdown_files)} markdown files)")
    return 0


def load_ignored_links() -> set[tuple[str, str]]:
    if not IGNORE_FILE.exists():
        return set()

    ignored: set[tuple[str, str]] = set()
    for raw_line in IGNORE_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" not in line:
            continue
        doc_path, target = (part.strip() for part in line.split("|", 1))
        if doc_path and target:
            ignored.add((doc_path, target))
    return ignored


if __name__ == "__main__":
    raise SystemExit(main())
