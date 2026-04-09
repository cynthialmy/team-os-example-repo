#!/usr/bin/env python3
"""Validate that local file paths in product-development/feature-index.yaml exist."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FEATURE_INDEX = REPO_ROOT / "product-development" / "feature-index.yaml"
PATH_PATTERN = re.compile(r"^[A-Za-z0-9._-]+(?:/[A-Za-z0-9._-]+)+/?$")


def extract_candidates(text: str) -> list[tuple[int, str]]:
    candidates: list[tuple[int, str]] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        # Remove inline comments and ignore empty lines.
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue

        value = ""
        if line.startswith("- "):
            value = line[2:].strip()
        elif ":" in line:
            _, rhs = line.split(":", 1)
            value = rhs.strip()
        else:
            continue

        value = value.strip("'\"")
        if not value or value.startswith(("http://", "https://")):
            continue
        if value.startswith("FORGE/"):
            continue
        if not PATH_PATTERN.match(value):
            continue

        candidates.append((line_number, value))

    return candidates


def main() -> int:
    if not FEATURE_INDEX.exists():
        print(f"error: feature index not found: {FEATURE_INDEX}")
        return 1

    candidates = extract_candidates(FEATURE_INDEX.read_text(encoding="utf-8"))
    if not candidates:
        print("error: no path candidates found in feature-index.yaml")
        return 1

    missing: list[tuple[int, str]] = []
    for line_number, rel_path in candidates:
        target = REPO_ROOT / "product-development" / rel_path
        if not target.exists():
            missing.append((line_number, rel_path))

    if missing:
        print("feature-index validation failed. Missing paths:")
        for line_number, rel_path in missing:
            print(f"  - line {line_number}: {rel_path}")
        print(f"\nchecked {len(candidates)} path references")
        return 1

    print(f"feature-index validation passed ({len(candidates)} path references)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
