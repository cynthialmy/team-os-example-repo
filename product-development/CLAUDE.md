# Product Development

All product development artifacts for Forge - product, engineering, analytics, data engineering, and design.

Navigation ownership note: top-level documentation routing is owned by [`../CLAUDE.md`](../CLAUDE.md). Keep this file focused on product-development-level routing and update the root index first when paths move.

## Doc Index

| Path | Description |
|------|-------------|
| [product/CLAUDE.md](product/CLAUDE.md) | PRDs, strategy, customers, competitive research, launch emails, sales enablement, workstreams |
| [engineering/CLAUDE.md](engineering/CLAUDE.md) | Engineering plans, RFCs, bug investigations - organized by product area |
| [analytics/CLAUDE.md](analytics/CLAUDE.md) | Metrics glossary, SQL queries, table schemas, dashboards, experiments, investigations |
| [data-engineering/CLAUDE.md](data-engineering/CLAUDE.md) | Data pipeline plans and RFCs - organized by product area |
| [design/CLAUDE.md](design/CLAUDE.md) | Design docs (stub - design artifacts live in Figma, linked from PRDs) |
| `feature-index.yaml` | Master feature index - every feature mapped to its PRDs, RFCs, plans, schemas, experiments, tickets |
| `analytics/data-catalog.yaml` | Data warehouse table registry - descriptions, owners, refresh cadence, upstream sources |
| [product/customers/CLAUDE.md](product/customers/CLAUDE.md) | Customer accounts routing table - named accounts, segments, data source pointers |

## Validation Checks

- Validate `feature-index.yaml` references before merging large doc changes:
  - `python3 scripts/validate_feature_index.py`
- Validate markdown local links:
  - `python3 scripts/check_markdown_links.py`
- CI workflow: `.github/workflows/docs-hygiene.yml` runs these checks on PRs, pushes to `main`, and a weekly schedule.
