# Contributing to the Ravenhelm Linear Operating Method

This document is licensed material. Contributions are scoped to maintainers and approved collaborators. If you've been invited to contribute, this guide explains how.

## What this document is

RLOM is a freemium consulting deliverable. Every chapter doubles as a sales artifact for the Ravenhelm Operating Assessment. Editorial discipline is high — see `docs/_shared/CONTEXT.md` for the authoritative voice, formatting, neutralization, and rubric rules.

## Local setup

No build dependencies. Authoring is plain Markdown. Optional tooling:

- `markdownlint-cli` for lint (`npm i -g markdownlint-cli`)
- A Markdown previewer (VS Code, Obsidian, Marked)

## Branch strategy

- Trunk: `main`.
- Feature branches: `chapter/<n>-<slug>`, `doctrine/<topic>`, `editorial/<topic>`.
- Branches live 1–3 days. Squash-merge to `main`.

## Commit convention

Conventional Commits. The relevant scopes for this repo:

- `feat(chapter): ...` — net-new content (a new section, new template, new callout).
- `fix(chapter): ...` — editorial correction, broken link, typo.
- `feat(doctrine): ...` — a new numbered principle (requires an ADR).
- `refactor(doctrine): ...` — restating a principle without changing meaning.
- `chore(repo): ...` — repo plumbing, lint, CI.
- `docs(meta): ...` — README, CHANGELOG, this file.

Examples:

```
feat(chapter 9): add the five-evidence-types taxonomy
fix(chapter 3): correct P-7 counter-example wording
feat(doctrine): add P-29 on intake-source attribution
chore(repo): wire markdownlint to CI
```

## What requires an ADR

Any change to the **numbered principles** (`P-#`) requires a doctrine ADR in `docs/architecture/decisions/`. This includes:

- Adding a new principle.
- Retiring or renumbering an existing principle.
- Materially changing the rule, rationale, or counter-example of an existing principle.

ADRs use the template in `docs/architecture/decisions/0000-template.md`. The ADR PR is separate from the content PR that cites the new doctrine.

## Voice and editorial rules

The complete rules are in `docs/_shared/CONTEXT.md`. Highlights:

- **Voice.** Compressed, peer-level, expert. No hedging, no filler, no marketing-speak.
- **Neutralization.** No Norse names, no Ravenhelm-internal jargon, no real client / employer names. The 3-person team is the canonical example.
- **Citations.** Every non-obvious claim ties to a `P-#`.
- **Callouts.** Every chapter (except Chapter 12) has exactly one "Augmentation Surface" box and one "Where this gets hard" box at the end, both in the standard format.
- **License header.** Every chapter file opens with the standard license block.

## Self-check before opening a PR

Every chapter PR must pass the rubric in `docs/_shared/CONTEXT.md` §12. Each chapter file ends with a `<!-- RUBRIC_CHECK: ... -->` block that records the self-check. PRs without this block, or with `fail` entries, will be sent back.

## Review

- Editorial PRs: one maintainer.
- Doctrine PRs (new or renumbered `P-#`): two maintainers, one of whom owns the doctrine file.
- Cross-chapter consistency changes: a doctrine ADR plus the content PRs that cite it.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
