# Agent Guide - rlom-method

This file is authoritative for the `rlom-method` repository, **Book I of the Ravenhelm Operations Methodology** (*The Sovereign Engineering Trilogy: RLOM · RDOM · RROM*). Update it when repository authority, CI, release surfaces, or doctrine boundaries change.

## Source of Truth

- Canonical repository: `https://github.com/nwalker85/rlom-method` (public publication candidate).
- Human documentation: `README.md`, `docs/README.md`, and `docs/chapters/`.
- Project work: GitHub Issues, Pull Requests, and Discussions.
- Author: Nathan Walker (`https://nwalker.cc`) / Ravenhelm LLC (`https://ravenhelm.co`).

## Repository Posture

- Always work from a dedicated git worktree when editing this repo. Checkouts obey the Checkout Custody Standard.
- Never push directly to `main`. Every change lands via a Pull Request.
- Merging a PR requires Nate's explicit approval for that specific PR.
- Conventional Commits (`feat(chapter)`, `fix(chapter)`, `feat(doctrine)`, `chore(repo)`, `docs(meta)`).
- CI runs automated markdownlint and chapter rubric/license header checks on every pull request and push to `main`.

## Authority and Editorial Doctrine

- The manuscript is authoritative. Substantive prose is authored material by Nathan Walker.
- Every chapter obeys the unified voice and mechanical rules in `STYLE-GUIDE.md` and `docs/_shared/CONTEXT.md`: zero prose em-dashes (use `;` or ` - `), crime-scene openers on the workbench, showing the corpse of v1, high-low collision (cathedral math + shop-floor nouns), bench imperatives, and exact numbers from the ledger.
- Any change to the 29 numbered principles (`P-1`..`P-29`) requires an Architecture Decision Record (ADR) in `docs/architecture/decisions/`.
- Every chapter conforms to the authoring specification in `docs/_shared/CONTEXT.md` and ends with a `RUBRIC_CHECK` comment block.

## Terminology and Data Boundaries

- No secrets, API keys, credentials, or private keys.
- No private customer names or confidential employer data.
- **Zero Myth / Codex vocabulary leakage:** Personal codex terms (*Wyrd Rune*, *Saga's Vow*, *Althing*, *Ráð*, *Four Codices*, *Valknut OKR*, *Jarl*, *Thegn*, *Skald*, *Berserkr*) never appear in operations methodology text.
- Real running Ravenhelm estate systems (`Bifrost`, `Heimdall`, `Vitki`, `Ullr`/`Yager`, `Idunn`, `Doom`/`Doomcourt`, `EAT`, `Snotra`, `Harbor`, `OpenBao`, `Valkyrie`, `Norns`) and operational lineage receipts (TNI 300-person XMPP floor management, J3B counterintelligence verification) are valid architectural receipts when grounded with their functional role and concrete verification history.

## Validation & Build

```bash
# Validate markdown syntax
npx markdownlint-cli 'docs/**/*.md' 'README.md' 'CONTRIBUTING.md' 'CHANGELOG.md' 'AGENTS.md' 'SUPPORT.md' --config .markdownlint.yml

# Build single-file compiled edition
./scripts/compile.sh > build/rlom.md

# Build Light and Dark PDF editions
python3 scripts/build-pdf.py
```
