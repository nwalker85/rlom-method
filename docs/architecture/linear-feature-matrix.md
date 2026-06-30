# Linear Feature × Tier Coverage Matrix

> Reference artifact for the RLOM feature-completeness initiative.
> Snapshot of Linear's feature set and plan gating as of 2026-06-30, cross-referenced
> against current RLOM chapter coverage. This file is the DRY source the chapter
> edits cite — do not duplicate tier facts elsewhere; link here.

## Plan tiers (current)

Linear's tiers are **Free / Basic / Business / Enterprise**. "Plus" is **not** a current
tier name (it was a pre-2024 name). RLOM ch.07 currently says "Tier 2 — Plus" and must be
renamed to **Basic**.

| Tier | Price (annual) | Headline gating |
|---|---|---|
| **Free** | $0 | 2 teams, 250-issue cap, 10 MB uploads; issues, projects, **cycles, initiatives, customer requests, project/initiative updates, Pulse**, API + webhooks, up to 15 release pipelines |
| **Basic** | $10/user/mo | 5 teams, **unlimited issues**, unlimited uploads, admin roles |
| **Business** | $16/user/mo | Unlimited + private teams, guests, **Triage Intelligence, Insights, Asks, SLAs**, agent automations (beta), Code Intelligence (beta), Zendesk/Intercom, login-method restrictions, Google SSO |
| **Enterprise** | Custom | SAML + SCIM, audit log, IP restrictions, **Dashboards**, multi-level sub-teams, private-team issue sharing, Asks web forms, Salesforce/Gong/Airbyte, app review |

## Tier-gating corrections (the load-bearing fixes)

RLOM's tier chapters mis-place these features. Correcting them is workstream A.

| Feature | RLOM places at | Actual tier | Direction of error |
|---|---|---|---|
| Initiatives (+ updates, health) | Tier 2 "Plus" | **Free** | gated too high |
| Customer Requests (core) | Tier 2 "Plus" | **Free** | gated too high |
| Cycles | *omitted* | **Free** | missing |
| Releases (≤15 pipelines) | "Plus+/cross-tier" | **Free** | gated too high |
| Pulse | *omitted* | **Free** | missing |
| Insights | Tier 2 "Plus" | **Business** | gated too low |
| Dashboards | Tier 3 Business | **Enterprise** | gated too low |
| Asks web forms | Tier 3 Business | **Enterprise** | gated too low |
| Tier name "Plus" | — | **Basic** | renamed |

Net effect: **Basic ($10) actually unlocks little** (5 teams, unlimited issues, uploads,
admin roles). Initiatives, Customer Requests, Cycles, Releases, and Pulse are **all on
Free** — which makes the free funnel chapter substantially more powerful once corrected.

## Coverage matrix

Legend: ✓ covered (chapter) · ⚠ covered but mis-tiered/understated · ✗ not covered ·
→ action in this initiative.

### Workspace / Teams

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| Single team, renamed to remit | Free | ✓ ch.06 | — |
| Team limits (2/5/∞) | by tier | ⚠ not stated | A: state per tier |
| Private teams | Business | ✗ | A: Enterprise/Business ch |
| Guests | Business | ✗ | A |
| Sub-teams (multi-level, 5) | Enterprise | ✗ | A: Enterprise ch |
| Team documents (home pages) | Free | ✗ | B: views/surface |

### Issues

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| Statuses/workflow, priority, estimates, labels | Free | ✓ ch.06/05/09 | — |
| Sub-issues, templates | Free | ✓ | — |
| Native relations (blocking/related/duplicate) | Free | ⚠ only "Blocked" state | B: add relations |
| Recurring issues | Free | ✗ | B |
| Duplicate as status type | Free | ⚠ via Triage Intelligence | B |
| Open in coding tool (Cursor/Claude Code/Codex) | Free | ✗ | C |
| `delegate` to agent (human stays owner) | Free | ✓ ch.08 | C: deepen |

### Triage / Intake

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| Triage inbox | Free | ✓ ch.06 | — |
| Triage Rules / Responsibility / on-call rotation | Business | ✗ | E (CoE intake) |
| Triage Intelligence (AI) | Business | ✓ ch.08 | rename note¹ |
| Triage Automations (agent actions) | Business | ⚠ | C |
| Asks (Slack/email) | Business | ✓ ch.08 | E: service catalog |
| Asks Agent | Business | ✗ | C/E |
| Asks Web Forms | **Enterprise** | ⚠ placed at Business | A/E re-tier |
| Service catalog / request types | (pattern) | ✗ | E (APEX port) |

### Projects / Initiatives / Cycles

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| Projects, milestones, statuses, documents | Free | ✓ | — |
| Project health (On track/At risk/Off track) | Free | ⚠ manual, no criteria | B: computed-RAG spec (APEX) |
| Project predictions, project graph | Free/varies | ✗ | B (light) |
| Project & initiative comments | Free | ✗ | — (minor) |
| **Initiatives** (+ updates, health, graph) | **Free** | ⚠ placed at "Plus" | A re-tier |
| **Cycles** (+ automations, capacity) | **Free** | ✗ omitted | B: new Cycles ch |
| Roadmap / timeline view | Free | ✗ | B: Roadmaps treatment |

### Updates / Reporting

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| Project/initiative updates, health, reminders | Free | ✓ ch.11 | — |
| "Write with Agent" update drafting | new | ✗ | C |
| **Pulse** (update digests, audio) | **Free** | ✗ | B: reporting |
| **Insights** | **Business** | ⚠ placed at "Plus" | A re-tier |
| **Dashboards** | **Enterprise** | ⚠ placed at Business | A re-tier |

### Code integration / Releases

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| GitHub + GitLab PR/MR automation, branch naming | Free | ✓ ch.10 | — |
| Self-hosted (Forgejo/Gitea/Bitbucket) + webhook bridge | n/a | ✗ | D (new) |
| **Releases** / pipelines (≤15 Free) | **Free** | ⚠ implied higher | A/D re-tier |
| Release notes generation (agent) | with Releases | ✗ | D |
| **SemVer release naming** (MAJOR/MINOR/PATCH) | convention | ⚠ in `release:*` only | B/D: KEEP as principle² |
| Linear Diffs (native review), Reviews inbox | new | ✗ | C/D |
| GitHub Enterprise Cloud | Enterprise | ✗ | A (note) |

### AI / Agents

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| AI Agents (app users), `@`-mention, assign, `delegate` | Free framework | ✓ ch.08 | C: deepen |
| Agent automations | Business | ⚠ | C |
| Agent guidance + shared Skills | new | ✗ | C |
| MCP server support | new | ⚠ named | C |
| Code Intelligence (reads codebase) | Business beta | ✗ | C |
| Coding Sessions (agent writes/ships code) | Business+ | ✗ | C |
| Intake-classification agent | (pattern) | ✗ | E (APEX port) |

### Other integrations

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| Slack (issues, project channels, Asks) | varies | ✓ | — |
| Sentry | Free | ✓ ch.08 | — |
| Figma, Notion | Free | ✗ | C/B (light) |
| Microsoft Teams | new | ✗ | — (note) |
| Intercom / Zendesk / Front (support) | Business | ⚠ | E |
| Salesforce / Gong / Airbyte | Enterprise | ✗ | A (Enterprise) |

### Customer Requests

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| Customers, requests→issues/projects, attributes, impact | **Free** | ⚠ placed at "Plus" | A re-tier |
| Customer pages / views | Free | ✗ | B (light) |
| Intercom/Zendesk/Front/Salesforce request sources | Business/Ent | ⚠ | E |

### Admin / API / Security (the absent tier)

| Feature | Tier | RLOM today | Action |
|---|---|---|---|
| GraphQL API, webhooks, OAuth apps, API keys | Free | ⚠ ch.10 only | D |
| SSO/SAML, SCIM, audit log, IP restrictions | Enterprise | ✗ | A: Enterprise ch |
| Login-method restrictions | Business | ✗ | A |
| Data export (CSV, copy-for-LLM, Sheets, Airbyte) | varies | ✗ | A/B (light) |
| Import / migration assistants | Free | ✗ | A (onboarding note) |

## Currency / naming fixes

1. **Product Intelligence → Triage Intelligence** — renamed Aug 2025. Sweep any
   "Product Intelligence" reference.
2. **SemVer** — KEPT as an RLOM release-organization principle (owner decision,
   2026-06-30). Earlier audit recommended dropping "SemVer on everything"; that is
   overruled. SemVer-named releases are the canonical way to keep releases organized and
   align with `semantic-release` / `release-please`.
3. Agent narrative is understated — Linear agents now run Coding Sessions and open Diffs;
   the June-2026 wave (Releases as a formal feature, Team documents, MCP, Coding Sessions,
   Write-with-Agent updates) post-dates RLOM's source inventory.

## Sources

Linear official docs, pricing, changelog, features/AI pages (mid-2026 snapshot);
RLOM `docs/chapters/01-12`; APEX CoE operating model (mined for ports — see edit spec).
