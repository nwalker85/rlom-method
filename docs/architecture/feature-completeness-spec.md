# RLOM Feature-Completeness & APEX-Port — Edit Spec (Phase 0)

> **Status: SPEC / REVIEW GATE (PR #1).** This is the blueprint. No chapter prose is
> written until this spec is approved. Phases 1–3 implement what is approved here.
> Companion: [`linear-feature-matrix.md`](./linear-feature-matrix.md) (DRY tier facts).

## Why this exists

An audit of RLOM against the current Linear feature set (mid-2026) found: (1) the
tier spine is factually wrong (mis-gated features, "Plus" is now "Basic"); (2) several
core primitives are uncovered (Cycles, Roadmaps, Pulse, relations); (3) the agent
chapter predates Linear's 2026 AI-coding wave; (4) the code-host chapter omits
self-hosted forges; (5) no Enterprise tier chapter exists. Separately, the APEX CoE
operating model was mined for portable mechanics.

## Locked decisions

1. **Tiers = Free / Basic / Business / Enterprise.** Rename ch.07 "Plus"→"Basic". Re-tier
   per the matrix (Initiatives/Customer Requests/Cycles/Releases/Pulse → Free; Insights →
   Business; Dashboards/Asks-web-forms → Enterprise).
2. **Add a Tier-4 Enterprise chapter.**
3. **APEX = fold + variant, not a fork.** General-purpose mechanics fold into core;
   CoE-specific mechanics ship as an opt-in **"Operations-Team variant"** appendix.
   APEX stays a separate potential consulting product; here it is a donor only.
4. **SemVer is KEPT** as a first-class release-organization principle (owner decision).
   The earlier "drop SemVer on everything" recommendation is overruled.
5. **Currency:** Product Intelligence → Triage Intelligence; fix the EPAS genericity leak.

## Proposed target TOC

(Renumbering is a single mechanical commit owned by Stream A; numbers below are the target.)

| # | Chapter | Change |
|---|---|---|
| 01–05 | what-this-is, seven-layers, principles, operator-role, operating-surface | edits only |
| 06 | Tier 1 — Free | rewrite (re-tier) |
| 07 | Tier 2 — **Basic** | rewrite + rename |
| 08 | Tier 3 — Business | rewrite (re-tier) |
| 09 | **Tier 4 — Enterprise** | **NEW** |
| 10 | Workflow Canon | edits |
| 11 | **Cycles, Roadmaps & Cadence** | **NEW** |
| 12 | Code-Host Integration | edits (self-hosted + SemVer) |
| 13 | Reporting Up | edits (Pulse, computed-RAG, QBR) |
| 14 | The Assessment | edits |
| App. A | **Operations-Team Variant (CoE)** | **NEW** |

## Workstream ownership & sequencing

| Stream | Owns (files) | Depends on |
|---|---|---|
| **0** (this PR) | `linear-feature-matrix.md`, this spec, currency sweep (Product Intelligence rename, EPAS fix) | — |
| **A** Tiers + Enterprise | 06, 07, 08, new 09, README/TOC, renumber | 0 |
| **B** Primitives | new 11 (Cycles/Roadmaps), 13 (Pulse/RAG), 05/10 (relations/recurring), 03 (principles) | A (tier defs) |
| **C** Agents/AI | agent sections of 08, 03 (P-14/15) | A |
| **D** Code-host | 12 (self-hosted forge + SemVer/semantic-release) | A |
| **E** Ops-Team variant | App. A; + core field-discipline edits to 03/Issues | A, B |
| **3** Integration | TOC/numbering, cross-refs, CHANGELOG, markdownlint | A–E |
| **4** Mapping | (separate) Ravenhelm conformance report | 3 |

Each stream runs in its own worktree off `main` after A merges; each lands as a PR you approve.

## Per-stream edit blueprint

### A — Tier spine + Enterprise

- **06 Free:** add Initiatives, Customer Requests, **Cycles**, Releases (≤15 pipelines),
  Pulse, native relations. State the 2-team / 250-issue ceiling. Remove the false
  "Free omissions" (Initiatives, Customer Requests, Releases were wrongly excluded).
- **07 Basic:** rename from "Plus". State what Basic *actually* adds: 5 teams, unlimited
  issues, unlimited uploads, admin roles. (Stop attributing Initiatives/CR/Insights here.)
- **08 Business:** keep Triage Intelligence, Asks (core), SLAs, agent automations; **add
  Insights** (moved up from "Plus"); move Dashboards & Asks-web-forms *out* to Enterprise.
- **09 Enterprise (NEW):** SSO/SAML, SCIM, audit log, IP restrictions, private teams,
  guests, multi-level sub-teams, **Dashboards**, Asks web forms, Salesforce/Gong/Airbyte,
  app review. Frame as the "scale the method across teams" tier — absorbs APEX's
  **federated hub-and-spoke + Community of Practice** as the multi-team operating shape.

### B — Missing primitives (incl. your Cycles + Roadmaps)

- **New 11 — Cycles, Roadmaps & Cadence:** Cycles (when cycles vs. update-cadence;
  capacity entry before a cycle; cycle automations) — resolves the **P-26 inconsistency**.
  **Roadmaps**: timeline view, swimlane-by-project, **Plan-of-Record vs. What-If** (APEX),
  cross-initiative dependencies.
- **13 Reporting:** add **Pulse** (digests). Add the **computed-RAG health spec** (APEX):
  the deterministic Red/Amber/Green ladder (blocked / overdue+low-%-done → Red; slipping or
  blocked >7d → Amber; else Green), recommended as automation that writes Linear Project
  Health, gating Validation→Done.
- **05/10:** native issue relations (blocking/related/duplicate), recurring issues,
  "promote loose labels → typed fields" principle.
- **12/principle:** **SemVer** as the canonical release-naming convention (kept).

### C — Agent / AI-coding modernization

- Rewrite agent content (currently in 08): Linear Agent + **Skills**, AI Agents/`delegate`,
  **MCP**, **Code Intelligence**, **Coding Sessions** (Claude Code/Codex), **Linear Diffs**,
  **Write-with-Agent** updates, Triage Automations, "open in coding tool".
- Reframe agents from coordinators → executors that write/ship code; update **P-14/P-15**.
- Add APEX's **AI intake-classification agent** (intake agent vs. build agent).

### D — Self-hosted code-host

- **12:** add a self-hosted section (Forgejo/Gitea/Bitbucket) + the webhook-bridge pattern
  (`Fixes <ID>` → Linear GraphQL → issue state + attachment). Mirror-back strategy.
  Tie SemVer to `semantic-release` / `release-please`. Keep GitHub/GitLab as the defaults.

### E — Operations-Team variant (CoE) — APEX harvest

- **Appendix A (opt-in):** the demand-side front-half for service/ops/PMO/CoE teams:
  - **Intake layer** + an optional pre-Backlog "Intake Review" state; intake dwell-time metric.
  - **Service Catalog / request types** → Linear Asks templates that pre-tag team/project/labels.
  - **Governance cadence**: daily/weekly/monthly + **QBR**; **charter-approval gate** before a
    project starts; **RACI** on initiatives.
  - **Service SLAs** (time-to-first-response / resolution) on Triage + Asks.
  - Optional label axes: `layer:` (capability/delivery/impact) and `customer:` (internal/external).
- **Core field-discipline edits** (general, land in 03/Issues): the **"Rule of One"
  required-field validator** (hard create-time block), the **per-issue-type required-field
  matrix**, and **mandatory OKR/initiative linkage** per parent issue.

## APEX port map

| Port | Stream | Lands in | General / Variant |
|---|---|---|---|
| Computed-RAG health spec | B | 13 Reporting | General |
| Roadmap: Plan-of-Record vs What-If | B | 11 | General |
| SemVer release naming (**kept**) | B/D | 12 + principle | General |
| Federated hub-and-spoke + CoP | A | 09 Enterprise | General (scaling) |
| Rule-of-One validator | E→core | 03 / Issues | General |
| Per-type required-field matrix | E→core | Issues / templates | General |
| Mandatory OKR/Goal linkage | E→core | Initiatives | General |
| Intake layer + Intake-Review state | E | App. A | Variant |
| Service Catalog / request types | E | App. A | Variant |
| Governance cadence + QBR + charter + RACI | E | App. A / 13 | Variant |
| Service SLAs | E | App. A | Variant |
| `layer:` / `customer:` label axes | E | App. A | Variant |
| AI intake-classification agent | C/E | agent ch / App. A | Variant |

## Numbered-principle changes

- **P-26** (cycles): fix the inconsistency — now backed by the new Cycles chapter.
- **P-14 / P-15** (agents): update to reflect agents that write/ship code.
- **New:** a computed-health principle; a SemVer release-naming principle; a value /
  business-case principle (lightweight — RLOM currently has no value/ROI concept).

## Leave behind (Jira-isms not ported)

Components-as-typed-field; RAG/lifecycle-as-labels; the Google-Site/Apps-Script RAG
plumbing; raw JQL / `customfield_*` IDs / Jira-automation JSON; `needs-triage` sentinels;
manual sub-task label inheritance. **NOT on this list: SemVer — kept.** Porting principle:
loose labels → native primitives / typed fields (this is APEX's own `rag-*`→typed-field lesson).

## Phase 4 — map the Ravenhelm instance against the result

After the product is current, audit Ravenhelm's `linear-guidebook` + live `RAV` workspace
against corrected RLOM → conformance/remediation backlog (states 14→9, label pruning,
project health, enable Releases/Asks/Triage Intelligence, activate agent delegation, the
Cycles decision). This is the product's paid "Operating Assessment" run on the author's
own workspace.

## Reviewer checklist (this PR)

- [ ] Tier corrections in the matrix are accurate.
- [ ] Target TOC / renumbering is acceptable.
- [ ] APEX port map: right items folded to core vs. variant.
- [ ] SemVer treatment is correct (kept as principle).
- [ ] Nothing in "leave behind" should actually be kept.
