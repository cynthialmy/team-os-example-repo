# SSO Integration - Product Requirements Document

| Field | Value |
|-------|-------|
| **Author** | Hannah Stulberg (PM) |
| **Status** | Draft |
| **Last Updated** | 2026-04-09 |
| **Related RFC** | `engineering/rfcs/billing/sso-integration-rfc.md` |

---

## Overview

Add enterprise SAML/OIDC single sign-on so organizations can authenticate through their identity provider and manage access with existing IT controls.

## Problem Statement

Enterprise teams evaluating Forge require centralized identity controls. Without SSO, security reviews stall and larger contracts do not progress.

## Goals

1. Enable SAML and OIDC login for enterprise workspaces.
2. Support just-in-time user provisioning with domain restrictions.
3. Provide admin visibility into auth configuration health.

## Success Metrics

| Metric | Target |
|--------|--------|
| Enterprise opportunities blocked on auth | -50% within 1 quarter |
| SSO login success rate | >99.5% |
| Time to complete SSO setup | <30 minutes median |

## Requirements

- Workspace admins can configure SAML or OIDC via an admin settings screen.
- Login supports IdP-initiated and SP-initiated flows.
- Users from approved domains can be auto-provisioned.
- Audit logs capture SSO setup changes and authentication events.

## Non-Goals

- SCIM lifecycle automation (handled in a separate initiative).
- Multi-IdP routing in a single workspace.
