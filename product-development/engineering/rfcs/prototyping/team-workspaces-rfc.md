# Team Workspaces - Engineering RFC

| Field | Value |
|-------|-------|
| **Author** | Morgan Wu (Engineer) |
| **Status** | Draft |
| **Last Updated** | 2026-04-09 |
| **Related PRD** | `product/PRDs/prototyping/team-workspaces-prd.md` |

---

## Summary

Add a workspace domain model and authorization layer to support shared ownership, role-based access control, and invitation workflows.

## Proposed Design

1. Add `workspaces`, `workspace_members`, and `workspace_roles` tables.
2. Scope projects to workspaces and enforce permission checks in API middleware.
3. Add invitation tokens with expiry and acceptance audit logs.
4. Backfill existing projects into personal default workspaces.

## Rollout

- Internal dogfood with migration safeguards.
- Progressive rollout by workspace tier.
- Full release after permission-related error rate stays within guardrails.
