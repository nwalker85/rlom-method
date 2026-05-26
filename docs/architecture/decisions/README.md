# Architecture Decision Records

This directory holds ADRs (Architecture Decision Records) for the Ravenhelm Linear Operating Method. In a code repo, ADRs document architecture decisions. In this docs repo, the equivalent is **doctrine decisions** — changes to the numbered principles (`P-#`), the workflow canon, the operating surface, or the tier-install path.

## When to write an ADR

Per [CONTRIBUTING.md](../../../CONTRIBUTING.md), every change to numbered principles requires an ADR. Specifically:

- Adding a new principle (`P-29`, `P-30`, ...).
- Retiring an existing principle.
- Renumbering an existing principle.
- Materially changing the rule, rationale, or counter-example of an existing principle.

ADRs are also encouraged (not required) for:

- Changing the workflow canon (the nine states).
- Adding or removing a chapter from the canonical 12-chapter ordering.
- Restructuring the operating surface (label namespaces, required views, templates).
- Changing tier-boundary signals.

## Format

Use [`0000-template.md`](0000-template.md) as the starting point. ADRs are sequentially numbered (`0001-`, `0002-`, ...) and never renumbered after merge.

## Index

| # | Title | Status |
|---|---|---|
| _none yet_ | | |

ADRs are listed here as they're merged. Status values: `proposed`, `accepted`, `superseded by NNNN`, `retired`.
