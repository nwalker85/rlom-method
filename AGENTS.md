# Agent Guide — rlom-method

This file is authoritative for the `rlom-method` repository. Update it when repository authority, CI, release surfaces, or doctrine boundaries change.

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
- Agents may fix objective publication defects (broken links, malformed markdown, anchor mismatches, inconsistent paths, deterministic metadata errors).
- Agents may NOT silently rewrite paragraphs, change arguments, alter doctrine/principles, invent evidence, or change chapter structure.
- Any change to the 29 numbered principles (`P-1`..`P-29`) requires an Architecture Decision Record (ADR) in `docs/architecture/decisions/`.
- Every chapter conforms to the authoring specification in `docs/_shared/CONTEXT.md` and ends with a `RUBRIC_CHECK` comment block.

## Privacy and Data Boundaries

- No secrets, API keys, credentials, or private keys.
- No private customer names, customer-specific data, internal hostnames, or confidential employer data.
- Strict neutralization rules: no internal Ravenhelm Norse system names (Mimir, Heimdall, Bifrost, etc.) or private Valknut doctrine in public prose.

## Validation & Build

```bash
# Validate markdown syntax
npx markdownlint-cli 'docs/**/*.md' 'README.md' 'CONTRIBUTING.md' 'CHANGELOG.md' --config .markdownlint.yml

# Build single-file compiled edition
./scripts/compile.sh > build/rlom.md
```
