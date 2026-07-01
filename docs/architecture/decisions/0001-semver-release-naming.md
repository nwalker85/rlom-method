# ADR-0001 — Adopt Semantic Versioning as a numbered principle (P-29)

- **Status:** accepted
- **Date:** 2026-07-01
- **Decider:** @nwalker85
- **Affected:** P-29 (new); Chapter 12 (Code Host Integration); Chapter 3 (Numbered Principles); `_shared/PRINCIPLES.md`; `README.md`; `docs/README.md`

## Context

The Method covered how work flows to Done but was silent on how the delivered artifact — the release — is named. As a team's release surface grows (multiple pipelines, multiple environments, the occasional hand-cut hotfix), an ad-hoc release scheme becomes unanswerable: "which version shipped the auth fix?" has no reliable answer when the tags are `v2`, `final`, `hotfix-2`, and `july-build`. The feature-completeness audit added a self-hosted code-host section and `semantic-release` / `release-please` guidance (Chapter 12), which produce Semantic Versioning as a byproduct of Conventional Commits — making SemVer the natural, enforceable release-naming law. Release naming was judged a first-class operating conviction, not an optional convention, and elevated to doctrine.

## Decision

Add **P-29 — Releases are named with Semantic Versioning** to the numbered principles.

- **New principle.**
  - **Rule.** Every release carries a `MAJOR.MINOR.PATCH` version — MAJOR for a breaking change, MINOR for a backward-compatible feature, PATCH for a fix — derived from Conventional Commits by `semantic-release` (or `release-please`), not chosen by hand.
  - **Rationale.** SemVer makes the version, the changelog, and the tag a byproduct of commit discipline rather than a manual decision, so the release history stays legible as it grows, and the code host (not a human) keeps it honest (P-25).
  - **Counter-example.** A team hand-tags `1.0`, `1.0-real`, `1.0-real-final`, then `prod-2026-06`, and three months later cannot bisect which deploy carried which fix.

## Consequences

- **For chapters:** Chapter 12 gains a "Naming releases: Semantic Versioning" section citing P-29; Chapter 3 gains the P-29 expansion under a new **Group J — Releases**, and its intro ("29 principles… ten groups A–J") and footer citation list are updated.
- **For tooling / `_shared/`:** `_shared/PRINCIPLES.md` gains the P-29 entry and an updated derivation note; `README.md` and `docs/README.md` bump `P-1..P-28` → `P-1..P-29` and "28 numbered principles" → "29".
- **For the reader:** a reader adopting Releases now sees release naming as a rule with a number — the same weight as Validation or the workflow canon — not a footnote.

## Alternatives considered

- **Keep SemVer as a chapter section only, no numbered principle.** Rejected: release naming was judged a load-bearing convention to be enforced with principle-level weight; a section is easier to skip than a numbered rule.
- **Do nothing — let teams name releases however they like.** Rejected: ad-hoc release naming is exactly the drift the Method exists to prevent, and it fails the "which version shipped what" test that release evidence (P-9) depends on.

## References

- Chapter 12 (Code Host Integration) — self-hosted forge + SemVer sections (Stream D).
- Source doctrine R-5 (GitFlow retired; trunk-based + `release-please`) in the internal doctrine.
- Pull request implementing the change: the Stream D feature-completeness PR.
