# Onboarding: Data Engineering

Data engineering-specific setup and orientation for data engineers joining Forge.

## Setup

### Shared Tools (everyone gets these)

See [General Onboarding](onboarding-general.md#shared-tools-everyone-gets-these).

### Function-Specific Tools

| Tool | Purpose | Access |
|------|---------|--------|
| Snowflake | Data warehouse | Request access from Casey Nguyen |
| dbt | Data transformations and modeling | Access via `forge-data` repo |
| Fivetran | Data ingestion pipelines | Admin access from Casey Nguyen |
| Airflow | Pipeline orchestration | Access via `forge-data` repo |
| AWS Console | S3, Lambda, data infrastructure | Request from Alex Rivera |

### Repos

| Repo | Why |
|------|-----|
| `forge-data` | dbt models, Airflow DAGs, pipeline configs |
| `forge-infra` | Terraform for data infrastructure |
| `forge-product` | Analytics schemas, metric definitions |

### Environment Setup

1. Complete [General Onboarding](onboarding-general.md) setup first
2. Clone `forge-data` and follow its `CONTRIBUTING.md` for local setup
3. Get Snowflake access and connect your SQL client
4. Get Fivetran access and review current connector configurations
5. Set up local dbt and run a test build against the dev schema
6. Review Airflow DAGs and understand the current pipeline schedule

## Key Documents

- [Analytics CLAUDE.md](../../product-development/analytics/CLAUDE.md) - metrics glossary, data sources, schema docs
- [Analytics Schemas](../../product-development/analytics/schemas/) - table definitions and column descriptions
- [Product CLAUDE.md](../../product-development/product/CLAUDE.md) - product context for understanding what data matters

## Slack Channels

| Channel | Purpose |
|---------|---------|
| `#forge-eng` | Engineering discussion, relevant for pipeline dependencies |
| `#forge-analytics` | Downstream analytics and dashboard dependencies |
| `#forge-incidents` | Incidents that may affect data pipelines |
| `#forge-launches` | Release notifications that may affect pipeline loads |

## People to Meet

| Person | Why |
|--------|-----|
| Casey Nguyen | Data/analytics lead - pipeline priorities and data consumers |
| Drew Martinez | Strategy & Ops stakeholder for business reporting dependencies |
| Alex Rivera | Engineering management - system architecture and ownership |
| Morgan Wu | Infrastructure - shared infra and deployment |

## Org Chart

Data engineering works closely with Analytics (downstream consumers) and Engineering (upstream data sources). Data/analytics lead: Casey Nguyen. Infrastructure partner: Morgan Wu.

## First Tasks

- [ ] Get Snowflake, Fivetran, and dbt access configured
- [ ] Run a local dbt build against the dev schema
- [ ] Review the current Airflow DAG schedule and pipeline dependencies
- [ ] Trace one data pipeline end-to-end (source → ingestion → transformation → dashboard)
- [ ] Meet with Grace for architecture walkthrough and current priorities
- [ ] Pick up a small pipeline task from Linear / Jira / Asana (your manager will assign one)
