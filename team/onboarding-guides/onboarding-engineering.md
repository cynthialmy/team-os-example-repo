# Onboarding: Engineering

Engineering-specific setup and orientation for developers joining Forge.

## Setup

### Shared Tools (everyone gets these)

See [General Onboarding](onboarding-general.md#shared-tools-everyone-gets-these).

### Function-Specific Tools

| Tool | Purpose | Access |
|------|---------|--------|
| Datadog | Monitoring, alerting, APM | Request access from Alex Rivera |
| PagerDuty | On-call rotation and incident management | Added by EM after first month |
| Vercel | Frontend deployments | `forge-labs` org |
| AWS Console | Infrastructure (read access initially) | Request from Alex Rivera |

### Repos

| Repo | Why |
|------|-----|
| `forge-app` | Main application - frontend (React/Next.js) + backend API |
| `forge-ai` | AI generation pipeline and model serving |
| `forge-infra` | Terraform, Kubernetes configs, CI/CD pipelines |
| `forge-docs` | Public documentation site |
| `forge-product` | PRDs and specs for feature context |

### Environment Setup

1. Complete [General Onboarding](onboarding-general.md) setup first
2. Clone `forge-app`, `forge-ai`, and `forge-infra`
3. Follow `CONTRIBUTING.md` in `forge-app` for local dev setup
4. Run the test suite locally and verify it passes
5. Complete a test generation on staging and deploy it
6. Set up Datadog and bookmark the [Forge service dashboard](https://app.datadoghq.com)

## Key Documents

- [Engineering CLAUDE.md](../../product-development/engineering/CLAUDE.md) - engineering conventions and folder map
- [Engineering Plans](../../product-development/engineering/plans/) - technical design and implementation plans
- [Product Context](../../product-development/product/product-context/CLAUDE.md) - system reference docs
- [Platform Overview](../../product-development/product/product-context/forge-platform-overview.md) - what Forge does end-to-end

## Slack Channels

| Channel | Purpose |
|---------|---------|
| `#forge-eng` | Engineering discussion, architecture decisions |
| `#forge-standup` | Daily async standup posts |
| `#forge-incidents` | Production incidents and on-call alerts |
| `#forge-launches` | Launch and release coordination |
| `#forge-random` | Team-wide announcements and social chat |

## People to Meet

| Person | Why |
|--------|-----|
| Alex Rivera | EM - team structure, sprint process, growth plan |
| Jordan Kim | Engineering architecture and code review norms |
| Sam Chen | Frontend patterns and delivery workflow |
| Riley Patel | AI pipeline context |
| Morgan Wu | Infrastructure and deployment context |
| Hannah Stulberg | Product context and prioritization |

## Org Chart

Engineering reports to Alex Rivera (EM). The team covers frontend, backend, AI pipeline, and infrastructure. Cross-functional partners: Product (Hannah Stulberg), Design (Taylor Brooks, Jamie Ortiz), Analytics (Casey Nguyen).

## First Tasks

- [ ] Get local dev environment running and passing tests
- [ ] Complete a test generation on staging
- [ ] Read the frontend conventions doc and one recent TDD
- [ ] Review 2-3 recent PRs to understand code review norms
- [ ] Pick up a starter bug or small feature from Linear / Jira / Asana (your manager will assign one)
- [ ] Shadow an on-call shift after your first month
