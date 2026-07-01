# Ravenhelm Linear Operating Method (RLOM)

A freemium consulting deliverable by Ravenhelm LLC. RLOM is a tiered, human-centric operating model for running a software team on Linear — installable by a single PM in a week, scalable across Linear's plan tiers as the team grows, and designed to make work legible upward to leadership without inventing structure from scratch.

## Who this is for

A single PM running a 3-person team — one operator/PM, two engineers — reporting to a vague "leadership team." Technical enough to install Linear; not senior enough to have designed an operating model from scratch.

## What's inside

Fourteen chapters, ~34,500 words. Ten of them are usable on Linear Free immediately; the rest cover Basic, Business, Enterprise, and the edge of self-install.

| # | Chapter | Words |
|---|---|---|
| 1 | [What This Is and Who It's For](docs/chapters/01-what-this-is.md) | 1,633 |
| 2 | [The Seven Operating Layers](docs/chapters/02-seven-layers.md) | 2,098 |
| 3 | [The Numbered Principles](docs/chapters/03-numbered-principles.md) | 3,722 |
| 4 | [The PM Operator Role](docs/chapters/04-operator-role.md) | 1,993 |
| 5 | [The Operating Surface: Labels, Views, Templates](docs/chapters/05-operating-surface.md) | 2,559 |
| 6 | [Tier 1: Linear Free Install](docs/chapters/06-tier-1-free.md) | 2,814 |
| 7 | [Tier 2: Linear Basic Upgrade](docs/chapters/07-tier-2-basic.md) | 1,641 |
| 8 | [Tier 3: Linear Business and the Edge of Self-Install](docs/chapters/08-tier-3-business.md) | 3,803 |
| 9 | [Tier 4: Linear Enterprise and the Method as Operating System](docs/chapters/09-tier-4-enterprise.md) | 2,624 |
| 10 | [Workflow Canon and the Validation Gate](docs/chapters/10-workflow-canon.md) | 2,400 |
| 11 | [Cycles, Roadmaps & Cadence](docs/chapters/11-cycles-roadmaps-cadence.md) | 2,072 |
| 12 | [Code Host Integration: GitHub Primary, GitLab Parallel](docs/chapters/12-code-host-integration.md) | 2,404 |
| 13 | [Reporting Up](docs/chapters/13-reporting-up.md) | 3,259 |
| 14 | [The Assessment](docs/chapters/14-the-assessment.md) | 1,572 |

## How to read it

- **In order.** The chapters build on each other. Chapter 3 (Principles) is cited by every later chapter as `P-#`.
- **By role.** A PM at a 3-person team starting on Linear Free should read chapters 1, 2, 4, 5, 6, 10, 13 (the install path) and skim the rest.
- **By need.** A team already on Basic wanting to deepen practice reads 10, 11, 12, 13 first.

## Repository layout

```
.
├── docs/
│   ├── chapters/           # The 14-chapter deliverable
│   ├── _shared/            # Authoring spec
│   │   ├── CONTEXT.md      # Voice, neutralization rules, callout formats, rubric
│   │   └── PRINCIPLES.md   # Canonical P-1..P-28 scaffold
│   └── architecture/
│       ├── README.md
│       ├── repo-structure.md  # Structural template + this repo's conformance
│       └── decisions/         # ADRs for doctrine evolution
├── scripts/
│   └── compile.sh          # Concatenate chapters into a single document
├── .github/                # PR and issue templates, lint workflow
├── README.md
├── LICENSE                 # TODO — placeholder pending license research
├── CHANGELOG.md
├── CONTRIBUTING.md         # Voice, neutralization, PR process
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── CODEOWNERS
```

This repo conforms to **Tier 2** of the Ravenhelm Repository Structure Template. See [`docs/architecture/repo-structure.md`](docs/architecture/repo-structure.md) for the full template and the specific decisions this repo made. The same convention governs all sibling repos under [`~/src/products/rlom/`](../README.md).

## Building a single-file edition

```bash
./scripts/compile.sh > build/rlom.md
```

Concatenates the 14 chapters in order with a generated table of contents.

## Contributing

Contributions are scoped — see [CONTRIBUTING.md](CONTRIBUTING.md). Doctrine changes (adding, retiring, or renumbering principles) require a doctrine ADR in `docs/architecture/decisions/`.

## License

See [LICENSE](LICENSE). Final license boilerplate is pending; current file is a TODO marker matching the headers in each chapter file.

## Authors

Ravenhelm LLC. Drafting orchestrated through a 12-agent fanout against the spec in `docs/_shared/CONTEXT.md`.
