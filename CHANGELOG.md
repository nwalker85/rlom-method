# Changelog

All notable changes to the Ravenhelm Linear Operating Method are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Doctrine versions follow the same scheme: a major bump indicates a breaking change to a numbered principle (rename, renumber, or removal), a minor bump indicates a new principle or expanded chapter, a patch bump indicates editorial revision without doctrine change.

## [Unreleased]

### Added
- Initial 12-chapter draft authored against the spec in `docs/_shared/CONTEXT.md`.
- Canonical principle scaffold (P-1..P-28) in `docs/_shared/PRINCIPLES.md`.
- Repository scaffolding (Tier 2 layout per the EPAS structure template).

### Pending
- Final license boilerplate (`LICENSE` is currently a TODO marker).
- ADR template and first doctrine ADR.
- Markdownlint rules tuned for chapter conventions (callout boxes, license header).
- Single-file build via `scripts/compile.sh`.

## [0.1.0] — 2026-05-26

Initial draft.

- 12 chapters, ~27,000 words, written by parallel agent fanout.
- 28 numbered principles canonicalized from internal doctrine.
- Repository structure conforms to Tier 2 of the EPAS Repository Structure Template.
