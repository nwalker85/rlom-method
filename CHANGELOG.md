# Changelog

All notable changes to the Ravenhelm Linear Operating Method are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Doctrine versions follow the same scheme: a major bump indicates a breaking change to a numbered principle (rename, renumber, or removal), a minor bump indicates a new principle or expanded chapter, a patch bump indicates editorial revision without doctrine change.

## [Unreleased]

## [1.0.2] — 2026-10-06

### Added

- Adopted the **RLOM Community License 1.0** in `LICENSE`, permitting free informational redistribution and internal organizational implementation while reserving commercial services, derivative publications, and training to Ravenhelm LLC.
- Public repository infrastructure: authoritative `AGENTS.md`, `SUPPORT.md`, `CITATION.cff`, and structured issue templates (`config.yml`, `method-defect.md`, `enhancement-proposal.md`).

### Changed

- Enhanced `README.md` as an authoritative public front door with complete 14-chapter TOC, 29-principle operating model overview, and clear commercial boundaries.
- Replaced draft contact placeholders across all 15 manuscript chapters and `docs/_shared/CONTEXT.md` with direct contact path (`nate@ravenhelm.co`).
- Repaired principle count in Chapter 14 (corrected to twenty-nine numbered principles).
- Neutralized workstation filesystem paths and repaired broken relative link (`../README.md`).
- Added single-file compile verification to CI lint workflow.

## [0.2.0] — 2026-07-01

Feature-completeness release. RLOM was audited against Linear's current (mid-2026) feature set and rebuilt to leverage every major surface. The Method grew from 12 chapters to **14 chapters plus an Operations-Team appendix**, gained a 29th numbered principle (Semantic Versioning) and the project's first doctrine ADR, and corrected its plan-tier model to Linear's current Free / Basic / Business / Enterprise.

### Added

- `docs/architecture/linear-feature-matrix.md` and `docs/architecture/feature-completeness-spec.md` — the feature × tier audit and per-chapter edit blueprint.
- Chapter 9 — Tier 4: Linear Enterprise and the Method as Operating System (scale across teams: SSO/SCIM, sub-teams, workspace Dashboards, and the hub-and-spoke + community-of-practice operating pattern).
- Chapter 11 — Cycles, Roadmaps & Cadence (cycles as an optional execution-rhythm overlay; the timeline/roadmap view with the Plan-of-Record vs. What-If discipline).
- Computed health (the RAG operating model) and Pulse sections in the Reporting chapter — a deterministic Red/Amber/Green ladder recommended as automation that writes Linear's Project Health field.
- Issue relations (blocking/related/duplicate) and recurring-issues guidance, plus a "prefer typed fields over labels" note, in the Operating Surface chapter.
- Chapter 12 gains a self-hosted-forge **webhook-bridge** section (magic-word `Fixes <ISSUE-ID>` → Linear GraphQL, for teams on Forgejo/Gitea/Bitbucket, with a mirror-back migration strategy) and a **Semantic Versioning** release-naming section.
- **P-29 — Releases are named with Semantic Versioning** — a new numbered principle (Group J), with doctrine **ADR-0001** (`docs/architecture/decisions/0001-semver-release-naming.md`).
- **Appendix A — The Operations-Team Variant** (opt-in): the demand-side front-half for operations / PMO / Center-of-Excellence teams — an intake layer with a pre-Backlog Intake-Review pipeline, a service catalog (request types → Asks templates), governance cadence + QBR + charter-approval gate + RACI, service SLAs, CoE-grade field discipline (Rule of One + per-issue-type required-field matrix), and the `layer:` / `customer:` label axes.

### Changed

- Corrected tier gating to current Linear plans (Free / Basic / Business / Enterprise). Tier 2 renamed "Plus" → "Basic". Initiatives, Customer Requests, Cycles, Releases, and Pulse are now documented as **Free**; Insights moved to **Business**; Dashboards and Asks web forms moved to **Enterprise**. Re-tiered chapters 06 (Free), 07 (Basic), 08 (Business), and renumbered the later chapters: Workflow Canon → 10, Cycles/Roadmaps → 11, Code Host → 12, Reporting → 13, Assessment → 14.
- Modernized the AI-agent surfaces in the Business chapter to Linear's current line — AI Agents / `delegate`, agent guidance + Skills, MCP, Code Intelligence, Coding Sessions (agents that write and ship code), Linear Diffs, Write-with-Agent, Triage Automations — reframed around the escalation from planning help to code-shipping, with the AI-PM build kept as the upsell.
- P-14 and P-15 sharpened for coding-session agents; P-26 (capacity) now cross-references the Cycles chapter and clarifies that cycles are optional.
- Numbered principles: 28 → 29 (added Group J — Releases); `P-1..P-28` → `P-1..P-29` across the README and docs.
- Corrected the workflow chapter's claim that PR-merge → Validation automation is a paid feature — the code-host integration and its PR-status automation are available on Free.
- Fixed `scripts/compile.sh` — its hardcoded chapter list referenced pre-rename filenames and would have failed on a missing file; updated to the current 14 chapters + appendix and taught the table-of-contents generator to match `## Appendix` headings.

## [0.1.0] — 2026-05-26

Initial draft.

- Initial 12-chapter draft (~27,000 words) authored against the spec in `docs/_shared/CONTEXT.md`, written by parallel agent fanout.
- Canonical principle scaffold — 28 numbered principles (`P-1..P-28`) in `docs/_shared/PRINCIPLES.md`, canonicalized from internal doctrine.
- Repository scaffolding (Tier 2 layout per the Ravenhelm Repository Structure Template); `docs/architecture/repo-structure.md` (vendored template + conformance table) and `docs/architecture/README.md`.
- `.markdownlint.yml` tuned to the chapter style.
