# Architecture

This directory holds load-bearing structural documentation for the Ravenhelm Linear Operating Method repo. In a code repo, "architecture" means component diagrams and service boundaries. In this docs repo, the equivalent is **structural conventions** — how the repo is laid out, how doctrine evolves, how cross-references hold.

## Contents

| File / dir | Purpose |
|---|---|
| [`repo-structure.md`](repo-structure.md) | The Ravenhelm Repository Structure Template, vendored. Names the tier this repo conforms to and the decisions made against each of the template's six decision points. |
| [`decisions/`](decisions/) | ADRs (Architecture Decision Records) for doctrine evolution — new, retired, or restated numbered principles (`P-#`). |

## What does NOT live here

- **Content rules** (voice, neutralization, callout formats, the chapter rubric) — those live in [`../_shared/CONTEXT.md`](../_shared/CONTEXT.md).
- **Doctrine** (the `P-#` principles themselves) — those live in [`../_shared/PRINCIPLES.md`](../_shared/PRINCIPLES.md) and are expanded in chapter 3.
- **Reading guidance** (chapter index, reading paths) — that lives in [`../README.md`](../README.md).

`docs/architecture/` is for *how the repo is shaped*. `docs/_shared/` is for *how the content is written*. Keep them separate.
