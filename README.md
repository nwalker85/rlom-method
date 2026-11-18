# Ravenhelm Linear Operating Method (RLOM)

> **Book I of the Ravenhelm Operations Methodology** (*The Sovereign Engineering Trilogy: RLOM · RDOM · RROM*) - A tiered, receipt-driven operating model for running a software team and agent fleet on Linear; installable by a single PM Operator in a week, scalable across plan tiers as the organization grows, and grounded in twenty-nine numbered principles.

Authored by **[Nathan Walker](https://nwalker.cc)** · Published by **[Ravenhelm LLC](https://ravenhelm.co)**  
Current Release: **v1.0.3** · [PDF (Light)](RLOM-v1.0.3.pdf) · [PDF (Dark)](RLOM-v1.0.3-dark.pdf) · [Changelog](CHANGELOG.md) · [Principles](docs/_shared/PRINCIPLES.md) · [Start Reading ->](docs/chapters/01-what-this-is.md)

---

## What Problem This Solves

You opened Linear this morning and found 200+ issues in a flat backlog, 14 custom workflow states, ~160 ad-hoc labels, and 0 of 45 active projects with a health status set. Merged pull requests flip issues straight to `Done` before anyone checks whether the service redeployed or the runtime actually works. When leadership asks for the status of platform work, your answer is a guess.

Even the architect of a clean operating model will watch a workspace rot if its maintenance is not mechanized. And when autonomous coding agents enter the workspace, the social layer that kept human teams honest disappears: humans ask when confused and feel shame when caught guessing; agents fail literal, brittle, and silent.

The **Ravenhelm Linear Operating Method (RLOM)** is the first *dōmbōc* ("what is laid down; the judgment") of the **Ravenhelm Operations Methodology**, governing the work graph so the ledger never lies about what is done:

- An **active seven-layer work graph** where issues belong to deliverable projects and durable initiatives (`P-1`, `P-2`, `P-3`, `P-4`);
- A **load-bearing Validation gate** separating implemented code from trusted production reality (`Merged != Built != Running`, `P-6`, `P-7`, `P-9`);
- A **three-tier upward reporting cadence** that separates raw measurement from interpretation and ends with an explicit decision table (`P-19`, `P-21`, `P-27`, `P-28`);
- An **honest four-tier adoption ladder** (Free, Basic, Business, Enterprise) that runs ten of fourteen chapters on Linear Free and upgrades only when concrete operational ceilings are hit.

```text
                  THE RAVENHELM OPERATIONS METHODOLOGY
             (The Sovereign Engineering Trilogy: RLOM · RDOM · RROM)

   ┌────────────────────────────────────────────────────────────────────────┐
   │ Book I: RLOM - Ravenhelm Linear Operating Method (The Work Graph)      │
   │    Governs: The Work Graph, Demand Intake, Validation Gates, Reporting │
   │    Axiom: "Merged != Built != Running; evidence beats assertion."      │
   │    Status: v1.0.3 · 29 Principles (P-1..P-29)                          │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼ (Issues dispatched to engineering)
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Book II: RDOM - Ravenhelm Development Operations Methodology           │
   │    Governs: Topological Waves, Concurrency, Agent Slices, TDD, EAT     │
   │    Axiom: "Wave N+1 never opens on a promise; only on verified green." │
   │    Foundation: The Ehwaz Doctrine (ᛖ), Critical Chain, Six Sigma, JIT  │
   │    Status: v1.0.0 · 24 Principles (DP-1..DP-24)                        │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼ (Merged code ready for compilation)
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Book III: RROM - Ravenhelm Release Operations Methodology              │
   │    Governs: Build Once, Artifact Custody, Multi-Surface Rails, GitOps  │
   │    Axiom: "Builds are the unit; releases are names."                   │
   │    Status: v1.0.0 · 18 Principles (RP-1..RP-18)                        │
   └────────────────────────────────────────────────────────────────────────┘
```

## Who This Is For

The primary reader is a single **PM Operator (product manager, technical lead, or fleet supervisor)** running a 3-person team (the Operator, Engineer A, and Engineer B) who reports to a leadership audience wanting trustworthy status without logging into the tracker. It scales cleanly from a 3-person seed team up to multi-contract enterprises supervising hundreds of human engineers and autonomous coding agents.

*Running an operations, PMO, or internal Center-of-Excellence team?* See [Appendix A](docs/chapters/appendix-a-operations-team.md) for the demand-side intake variant.

---

## Start Reading

The book is organized into **14 chapters plus an Operations-Team appendix** (42,942 words). Ten chapters are usable on Linear Free immediately.

| # | Chapter | Key Focus | Words |
|---|---|---|---|
| 01 | [What This Is and Who It's For](docs/chapters/01-what-this-is.md) | The workspace rot confession, floor-manager lineage, and opening contract | 2,272 |
| 02 | [The Seven Operating Layers](docs/chapters/02-seven-layers.md) | Initiatives, projects, issues, views, intake, delivery evidence, analytics | 2,376 |
| 03 | [The Numbered Principles](docs/chapters/03-numbered-principles.md) | The 29 canonical principles (`P-1`..`P-29`) with rationales and estate receipts | 4,296 |
| 04 | [The PM Operator Role](docs/chapters/04-operator-role.md) | Air-traffic control, counterintelligence judgment, and the 5-level practice ladder | 2,291 |
| 05 | [The Operating Surface: Labels, Views, Templates](docs/chapters/05-operating-surface.md) | Curing 160-label noise, the 6 core views, and templates that price oversight low | 2,785 |
| 06 | [Tier 1: Linear Free Install](docs/chapters/06-tier-1-free.md) | **Start here to install.** Avoiding the Hal Problem; workspace bring-up in 5 days | 3,080 |
| 07 | [Tier 2: Linear Basic and the Separation of Powers](docs/chapters/07-tier-2-basic.md) | Lifting Free's ceilings and separating producer, commander, and witness | 2,320 |
| 08 | [Tier 3: Linear Business and the Seam Where Agents Enter](docs/chapters/08-tier-3-business.md) | Insights, SLAs, Triage Intelligence, and governing autonomous coding agents | 3,078 |
| 09 | [Tier 4: Linear Enterprise and Portfolio Governance at Scale](docs/chapters/09-tier-4-enterprise.md) | Multi-contract governance: SSO/SCIM, sub-teams, and workspace Dashboards | 2,682 |
| 10 | [Workflow Canon and the Validation Gate](docs/chapters/10-workflow-canon.md) | Why `Merged != Built != Running`; the 9-state machine and Validation gate (`P-6`) | 2,759 |
| 11 | [Cycles, Roadmaps & Cadence](docs/chapters/11-cycles-roadmaps-cadence.md) | Killing sprint velocity theater; 70% capacity rule and Plan-of-Record roadmaps | 2,737 |
| 12 | [Code Host Integration: GitHub Primary, GitLab & Forgejo Parallel](docs/chapters/12-code-host-integration.md) | Inline `RAV-<id>` PR guards, defeating the auto-close trap, and SemVer (`P-29`) | 3,249 |
| 13 | [Reporting Up: Project Updates, Initiative Health, and the Monthly Review](docs/chapters/13-reporting-up.md) | Why summaries are lossy transforms; separating measurement from conclusion | 3,406 |
| 14 | [The Assessment: Auditing Presence vs. Absence](docs/chapters/14-the-assessment.md) | Auditing what a workspace fails to report when a lane stalls | 2,324 |
| App. A | [Appendix A: The Operations-Team Variant](docs/chapters/appendix-a-operations-team.md) | Running non-code operations, vendor evaluations, and incident ledgers on the spine | 3,287 |

### Recommended Reading Paths

- **Install Monday (Linear Free):** Read [01](docs/chapters/01-what-this-is.md) -> [02](docs/chapters/02-seven-layers.md) -> [04](docs/chapters/04-operator-role.md) -> [05](docs/chapters/05-operating-surface.md) -> [06](docs/chapters/06-tier-1-free.md) -> [10](docs/chapters/10-workflow-canon.md) -> [13](docs/chapters/13-reporting-up.md). Skim [03](docs/chapters/03-numbered-principles.md).
- **Deepening Existing Practice:** Read [03](docs/chapters/03-numbered-principles.md) -> [10](docs/chapters/10-workflow-canon.md) -> [11](docs/chapters/11-cycles-roadmaps-cadence.md) -> [12](docs/chapters/12-code-host-integration.md) -> [13](docs/chapters/13-reporting-up.md).
- **Evaluating Plan Upgrades or AI Agents:** Read [08](docs/chapters/08-tier-3-business.md) and [09](docs/chapters/09-tier-4-enterprise.md).
- **Leadership / Executive:** Read [01](docs/chapters/01-what-this-is.md) -> [13](docs/chapters/13-reporting-up.md) -> [14](docs/chapters/14-the-assessment.md).

---

## Operating Model at a Glance

The Method is built around five foundational concepts:

1. **The Seven Layers:** Initiatives (objectives) roll up Projects (execution containers), which hold deliverable Issues (single outcome, single owner). Views filter the active graph, Intake captures external requests, Delivery Evidence connects git repositories, and Analytics surface hygiene trends.
2. **Validation Separates Implemented from Trusted (`P-6`):** PR merge moves an issue to *Validation*, never directly to *Done*. A human Operator or automated verification harness runs the validation command against the live system with attached evidence before the issue is closed.
3. **The 3-Person Team Scaffold:** Calibrated to the reality of one Operator and two engineers, ensuring the model never requires enterprise PM overhead to run effectively.
4. **Human Ownership of Priority and Judgment (`P-13`, `P-14`):** Tools, metrics, and AI agents deliver evidence and drafts; the human Operator clicks the accept/reject button, makes commitments, assesses risk, and owns accountability.
5. **Progressive Tiering:** Start on Free in a week. Upgrade to Basic only when outgrowing issue/team ceilings or requiring separation of powers; upgrade to Business only when requiring SLAs, Insights, or autonomous coding sessions.

---

## Repository Structure

```text
.
├── docs/
│   ├── chapters/          # The 14-chapter manuscript + Appendix A
│   ├── _shared/           # Authoring spec and canonical principle scaffold
│   │   ├── CONTEXT.md     # Voice rules, style mechanics, and rubric
│   │   └── PRINCIPLES.md  # Canonical P-1..P-29 scaffold
│   └── architecture/      # Decision records and repository structure
│       ├── decisions/     # ADRs for doctrine evolution (e.g. ADR-0001 SemVer)
│       └── repo-structure.md # Conformance to Tier-2 Repository Standard
├── scripts/
│   ├── compile.sh         # Generates the single-file Markdown edition
│   └── build-pdf.py       # Compiles Light and Dark PDF editions via Typst
├── .github/               # Issue templates, PR template, lint CI
├── AGENTS.md              # Authoritative agent guide and repository posture
├── CHANGELOG.md           # SemVer changelog
├── CITATION.cff           # Citation metadata
├── CONTRIBUTING.md        # Contribution guide and ADR process
├── CODE_OF_CONDUCT.md     # Community conduct guidelines
├── LICENSE                # License information
├── README.md              # Front door (this file)
├── SECURITY.md            # Private vulnerability reporting policy
└── SUPPORT.md             # Community support routes and commercial engagement
```

This repository conforms to **Tier 2** of the Ravenhelm Repository Structure Template. See [`docs/architecture/repo-structure.md`](docs/architecture/repo-structure.md) for the template and this repo's conformance choices.

### Compiling Single-File & PDF Editions

To build the full single-file Markdown manuscript or recompile the Light and Dark PDF editions:

```bash
./scripts/compile.sh > build/rlom.md
python3 scripts/build-pdf.py
```

---

## Commercial Implementation

The Method is published freely to be used and self-installed. For organizations requiring hands-on help, **[Ravenhelm](https://ravenhelm.co)** provides:

- **The Ravenhelm Operating Assessment:** A 2-to-4 week engagement covering discovery, a read-only workspace audit, gap classification, and a phased install plan (see [Chapter 14](docs/chapters/14-the-assessment.md)).
- **Custom Workspace Remediation:** Cleaning years of backlog rot and restructuring active initiatives without disrupting delivery.
- **Enterprise Multi-Team Rollouts & Integrations:** Code-host webhook bridging, cross-team dashboard wiring, and custom AI agent workflows.

Learn more at **[ravenhelm.co](https://ravenhelm.co)**.

---

## Community & Contributing

- **Discussions & Questions:** See [SUPPORT.md](SUPPORT.md) and join [GitHub Discussions](https://github.com/nwalker85/rlom-method/discussions).
- **Contributing:** Contributions are scoped. Editorial corrections and defect fixes are welcome via pull request. Changes to doctrine (the 29 numbered principles) require an Architecture Decision Record (ADR). See [CONTRIBUTING.md](CONTRIBUTING.md).
- **Citation:** See [CITATION.cff](CITATION.cff) to cite the Method in academic or industry publications.

---

## Authors & License

- **Author:** [Nathan Walker](https://nwalker.cc)
- **Publisher:** [Ravenhelm LLC](https://ravenhelm.co)
- **License:** RLOM Community License 1.0. RLOM is free to read and may be implemented internally by individuals and organizations. Redistribution of modified versions, commercial republication, third-party RLOM services, training, certification, and commercial incorporation require prior written permission from Ravenhelm LLC. See [LICENSE](LICENSE) for complete terms.
- **Commercial Licensing & Implementation:** [nate@ravenhelm.co](mailto:nate@ravenhelm.co)
