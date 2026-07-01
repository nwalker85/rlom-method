# Documentation

The full Ravenhelm Linear Operating Method lives here.

## Layout

```
docs/
├── chapters/         # 14 chapters + the Operations-Team appendix
├── _shared/          # Authoring spec — load-bearing for any editorial work
│   ├── CONTEXT.md    # Voice, neutralization, callout formats, rubric, chapter ordering
│   └── PRINCIPLES.md # Canonical P-1..P-29 — every chapter cites from here
└── architecture/
    └── decisions/    # ADRs for doctrine evolution (new / retired / renumbered P-#)
```

## Chapter index

Read in order on first pass. Cross-references between chapters use the canonical ordering below.

1. [What This Is and Who It's For](chapters/01-what-this-is.md)
2. [The Seven Operating Layers](chapters/02-seven-layers.md)
3. [The Numbered Principles](chapters/03-numbered-principles.md)
4. [The PM Operator Role](chapters/04-operator-role.md)
5. [The Operating Surface: Labels, Views, Templates](chapters/05-operating-surface.md)
6. [Tier 1: Linear Free Install](chapters/06-tier-1-free.md)
7. [Tier 2: Linear Basic Upgrade](chapters/07-tier-2-basic.md)
8. [Tier 3: Linear Business and the Edge of Self-Install](chapters/08-tier-3-business.md)
9. [Tier 4: Linear Enterprise and the Method as Operating System](chapters/09-tier-4-enterprise.md)
10. [Workflow Canon and the Validation Gate](chapters/10-workflow-canon.md)
11. [Cycles, Roadmaps & Cadence](chapters/11-cycles-roadmaps-cadence.md)
12. [Code Host Integration: GitHub Primary, GitLab Parallel](chapters/12-code-host-integration.md)
13. [Reporting Up: Project Updates, Initiative Health, Monthly Review](chapters/13-reporting-up.md)
14. [The Assessment: What This Document Doesn't Cover](chapters/14-the-assessment.md)

**Appendix A.** [The Operations-Team Variant](chapters/appendix-a-operations-team.md) — opt-in; adapts the Method for operations / PMO / Center-of-Excellence teams (the demand-side intake and governance front-half).

## Reading paths

- **Install-now PM (Linear Free, 3-person team).** 1 → 2 → 4 → 5 → 6 → 10 → 13. Skim 3 once. Defer 7, 8, 9, 11, 12, 14 until needed.
- **PM already on Basic.** 1 → 3 → 7 → 10 → 11 → 12 → 13. Then revisit 5 to tune labels and views.
- **PM evaluating Business / agent layer.** 3 → 8 → 13 → 14.
- **PM scaling across teams (Enterprise).** 1 → 4 → 9 → 11 → 13.
- **Leadership / executive.** 1 → 13 → 14.
- **Operations / PMO / CoE team.** 1 → 2 → 5 → 8 → 13 → Appendix A. The appendix swaps in the demand-side intake and governance front-half.

## Doctrine

The 29 numbered principles (`P-1`..`P-29`) are the spine. Every chapter cites them. The canonical list with one-line rules lives in [`_shared/PRINCIPLES.md`](_shared/PRINCIPLES.md); the full chapter-3 expansion (rule, rationale, counter-example) lives in [`chapters/03-numbered-principles.md`](chapters/03-numbered-principles.md).

To propose a doctrine change, see [CONTRIBUTING.md](../CONTRIBUTING.md) and the ADR template at [`architecture/decisions/0000-template.md`](architecture/decisions/0000-template.md).

## Authoring spec

[`_shared/CONTEXT.md`](_shared/CONTEXT.md) is the load-bearing spec for editorial work: voice rules, neutralization, callout formats, license header, the rubric every chapter must pass. Read it before opening any chapter PR.
