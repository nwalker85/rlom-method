# Security Policy

This repository contains licensed editorial material, not executable code. The relevant "security" surface is:

1. **Confidentiality of unreleased chapters.** Drafts in feature branches and unmerged PRs are not for redistribution.
2. **License header integrity.** Every chapter file opens with the license marker in `docs/_shared/CONTEXT.md` §8. Tampering with this header is a license violation, not a security incident, but it is reportable here.
3. **Supply-chain risk in CI.** GitHub Actions workflows (`.github/workflows/`) and dependabot updates apply. Standard supply-chain hygiene.

## Reporting a concern

Use GitHub's private vulnerability reporting (if enabled on this repo) or contact the maintainer listed in `CODEOWNERS` directly. Do not open a public issue.

## Supported versions

The most recent tagged release is supported. Historical versions are not patched; corrections land in `main` and ship in the next release.
