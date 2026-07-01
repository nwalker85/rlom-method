# Changelog

All notable changes to the Ravenhelm Linear Operating Method are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Doctrine versions follow the same scheme: a major bump indicates a breaking change to a numbered principle (rename, renumber, or removal), a minor bump indicates a new principle or expanded chapter, a patch bump indicates editorial revision without doctrine change.

## [Unreleased]

### Added

- Initial 12-chapter draft authored against the spec in `docs/_shared/CONTEXT.md`.
- Canonical principle scaffold (P-1..P-28) in `docs/_shared/PRINCIPLES.md`.
- Repository scaffolding (Tier 2 layout per the Ravenhelm Repo Structure Template).
- `docs/architecture/repo-structure.md` — vendored template + conformance decisions table; travels with the repo so the convention does not depend on an external standards file.
- `docs/architecture/README.md` — index for the architecture directory.
- `.markdownlint.yml` tuned to the chapter style (preserves the directive-period principle headings, the multi-paragraph callout blockquotes, the vendored-document multi-H1 case, etc.); structural rules remain active.
- Chapter 9 — Tier 4: Linear Enterprise and the Method as Operating System (scale across teams: SSO/SCIM, sub-teams, workspace Dashboards, and the hub-and-spoke + community-of-practice operating pattern). Existing chapters renumbered: Workflow Canon → 10, Code Host Integration → 11, Reporting Up → 12, The Assessment → 13.
- `docs/architecture/linear-feature-matrix.md` and `docs/architecture/feature-completeness-spec.md` — Phase-0 feature-completeness audit (feature × tier matrix) and per-chapter edit blueprint.
- Chapter 11 — Cycles, Roadmaps & Cadence (cycles as an optional execution-rhythm overlay; the timeline/roadmap view with the Plan-of-Record vs. What-If discipline; the cadence tie-together). Existing chapters renumbered: Code Host Integration → 12, Reporting Up → 13, The Assessment → 14.
- Computed health (the RAG operating model) and Pulse sections added to the Reporting chapter — a deterministic Red/Amber/Green ladder recommended as automation that writes Linear's Project Health field, plus Pulse as the digest-consumption layer.
- Issue relations (blocking/related/duplicate) and recurring-issues guidance, plus a "prefer typed fields over labels" note, added to the Operating Surface chapter.
- Chapter 12 gains a self-hosted-forge **webhook-bridge** section (magic-word `Fixes <ISSUE-ID>` → Linear GraphQL, for teams on Forgejo/Gitea/Bitbucket, with a mirror-back migration strategy) and a **Semantic Versioning** release-naming section.
- **P-29 — Releases are named with Semantic Versioning** — a new numbered principle (Group J), with doctrine **ADR-0001**.
- `docs/architecture/decisions/0001-semver-release-naming.md` — the first doctrine ADR.

### Changed

- Corrected tier gating to current Linear plans (Free / Basic / Business / Enterprise). Tier 2 renamed "Plus" → "Basic". Initiatives, Customer Requests, Cycles, Releases, and Pulse are now documented as **Free**; Insights moved to **Business**; Dashboards and Asks web forms moved to **Enterprise**. Re-tiered chapters 06 (Free), 07 (Basic), 08 (Business) accordingly.
- P-26 (capacity) now cross-references the new Cycles chapter and clarifies that cycles are optional — the seventy-percent rule applies to whatever planning horizon the team commits against.
- Modernized the AI-agent surfaces in the Business chapter to Linear's current line — AI Agents / `delegate`, agent guidance + Skills, MCP, Code Intelligence, Coding Sessions (agents that write and ship code), Linear Diffs, Write-with-Agent, Triage Automations — reframed around the escalation from planning help to code-shipping, with the Ravenhelm AI-PM build kept as the upsell.
- P-14 and P-15 sharpened for coding-session agents: the human assignee owns what the agent ships; the validation command is the acceptance test the Operator runs instead of re-reading generated code.
- Numbered principles: 28 → 29 (added Group J — Releases); `P-1..P-28` → `P-1..P-29` across the README and docs.
- Corrected the workflow chapter's claim that PR-merge→Validation automation is a paid feature — the code-host integration and its PR-status automation are available on Free.

### Pending

- Final license boilerplate (`LICENSE` is currently a TODO marker).
- Single-file build via `scripts/compile.sh`.

## [0.1.0] — 2026-05-26

Initial draft.

- 12 chapters, ~27,000 words, written by parallel agent fanout.
- 28 numbered principles canonicalized from internal doctrine.
- Repository structure conforms to Tier 2 of the EPAS Repository Structure Template.
