# Ravenhelm Linear Operating Method (RLOM)

> A tiered, human-centric operating model for running a software team on Linear — installable by a single PM in a week, scalable across plan tiers as the team grows, and grounded in twenty-nine numbered principles.

Authored by **[Nathan Walker](https://nwalker.cc)** · Published by **[Ravenhelm LLC](https://ravenhelm.co)**  
Current Release: **v1.0.3** · [PDF (Light)](RLOM-v1.0.3.pdf) · [PDF (Dark)](RLOM-v1.0.3-dark.pdf) · [Changelog](CHANGELOG.md) · [Start Reading →](docs/chapters/01-what-this-is.md)

---

## What Problem This Solves

You opened Linear this morning and the backlog had 200+ issues. No project rollup means anything. Done means someone stopped talking about it in Slack, and when leadership asks for the status of platform work, your answer is a guess.

The Method fixes this without a multi-month transformation. It gives you:

- An **active work graph** where issues belong to deliverable projects (P-1, P-3, P-4);
- A **validation gate** separating implemented code from trusted code (P-6, P-7);
- A **three-tier upward reporting cadence** that turns leadership updates into a system rather than a Sunday evening chore (P-27);
- An **honest tiering ladder** that runs mostly on Linear Free and upgrades only when concrete operational ceilings are hit.

## Who This Is For

The primary reader is a single **Operator (PM or technical lead)** running a 3-person team (the Operator, Engineer A, and Engineer B) who reports to a leadership audience wanting trustworthy status without logging into the tracker. It scales cleanly up to 12+ engineers and across multi-team enterprises.

*Running an operations, PMO, or internal Center-of-Excellence team?* See [Appendix A](docs/chapters/appendix-a-operations-team.md) for the demand-side intake variant.

---

## Start Reading

The book is organized into **14 chapters plus an Operations-Team appendix** (~38,500 words). Ten chapters are usable on Linear Free immediately.

| # | Chapter | Key Focus | Words |
|---|---|---|---|
| 01 | [What This Is and Who It's For](docs/chapters/01-what-this-is.md) | The premise, canonical team, and the contract | 1,633 |
| 02 | [The Seven Operating Layers](docs/chapters/02-seven-layers.md) | Initiatives, projects, issues, views, intake, delivery evidence, analytics | 2,098 |
| 03 | [The Numbered Principles](docs/chapters/03-numbered-principles.md) | The 29 canonical principles (`P-1`..`P-29`) with rationales and failure modes | 3,884 |
| 04 | [The PM Operator Role](docs/chapters/04-operator-role.md) | The 5-level practice ladder from backlog hygiene to executive partner | 1,993 |
| 05 | [The Operating Surface: Labels, Views, Templates](docs/chapters/05-operating-surface.md) | Strict label namespaces, the 6 core views, and issue templates | 2,559 |
| 06 | [Tier 1: Linear Free Install](docs/chapters/06-tier-1-free.md) | **Start here to install.** Complete workspace bring-up in 5 days | 2,814 |
| 07 | [Tier 2: Linear Basic Upgrade](docs/chapters/07-tier-2-basic.md) | Lifting Free's ceilings when team count and issue limits require it | 1,641 |
| 08 | [Tier 3: Linear Business & Edge of Self-Install](docs/chapters/08-tier-3-business.md) | Insights, SLAs, Triage Intelligence, and modern AI coding agent surfaces | 3,803 |
| 09 | [Tier 4: Linear Enterprise & Operating System](docs/chapters/09-tier-4-enterprise.md) | Multi-team scale: SSO/SCIM, sub-teams, and workspace Dashboards | 2,624 |
| 10 | [Workflow Canon & The Validation Gate](docs/chapters/10-workflow-canon.md) | The 9-state machine and the load-bearing Validation gate (P-6) | 2,403 |
| 11 | [Cycles, Roadmaps & Cadence](docs/chapters/11-cycles-roadmaps-cadence.md) | Execution rhythm overlay and Plan-of-Record roadmaps | 2,072 |
| 12 | [Code Host Integration](docs/chapters/12-code-host-integration.md) | GitHub primary, GitLab parallel, self-hosted webhooks, and SemVer (P-29) | 3,265 |
| 13 | [Reporting Up](docs/chapters/13-reporting-up.md) | Weekly project updates, biweekly health rollups, and the monthly review | 3,259 |
| 14 | [The Assessment](docs/chapters/14-the-assessment.md) | What this book doesn't cover and when to bring in Ravenhelm | 1,572 |
| App. A | [Appendix A — Operations-Team Variant](docs/chapters/appendix-a-operations-team.md) | The intake, service-catalog, and governance front-half for CoE teams | 2,767 |

### Recommended Reading Paths

- **Install Monday (Linear Free):** Read [01](docs/chapters/01-what-this-is.md) → [02](docs/chapters/02-seven-layers.md) → [04](docs/chapters/04-operator-role.md) → [05](docs/chapters/05-operating-surface.md) → [06](docs/chapters/06-tier-1-free.md) → [10](docs/chapters/10-workflow-canon.md) → [13](docs/chapters/13-reporting-up.md). Skim [03](docs/chapters/03-numbered-principles.md).
- **Deepening Existing Practice:** Read [03](docs/chapters/03-numbered-principles.md) → [10](docs/chapters/10-workflow-canon.md) → [11](docs/chapters/11-cycles-roadmaps-cadence.md) → [12](docs/chapters/12-code-host-integration.md) → [13](docs/chapters/13-reporting-up.md).
- **Evaluating Plan Upgrades or AI Agents:** Read [08](docs/chapters/08-tier-3-business.md) and [09](docs/chapters/09-tier-4-enterprise.md).
- **Leadership / Executive:** Read [01](docs/chapters/01-what-this-is.md) → [13](docs/chapters/13-reporting-up.md) → [14](docs/chapters/14-the-assessment.md).

---

## Operating Model at a Glance

The Method is built around five foundational concepts:

1. **The Seven Layers:** Initiatives (objectives) roll up Projects (execution containers), which hold deliverable Issues (single outcome, single owner). Views filter the active graph, Intake captures external requests, Delivery Evidence connects git repositories, and Analytics surface hygiene trends.
2. **Validation Separates Implemented from Trusted (P-6):** PR merge moves an issue to *Validation*, never directly to *Done*. A human Operator or automated test runs the validation command with evidence before the issue is closed.
3. **The 3-Person Team Scaffold:** Calibrated to the reality of one Operator and two engineers, ensuring the model never requires enterprise PM overhead to run effectively.
4. **Human Ownership of Priority (P-13):** Tools, metrics, and AI agents surface candidates and drafts; the human Operator makes commitments, assesses risk, and exercises taste.
5. **Progressive Tiering:** Start on Free in a week. Upgrade to Basic only when outgrowing issue/team ceilings; upgrade to Business only when requiring SLAs, Insights, or autonomous coding sessions.

---

## Repository Structure

```
.
├── docs/
│   ├── chapters/          # The 14-chapter manuscript + Appendix A
│   ├── _shared/           # Authoring spec and canonical principle scaffold
│   │   ├── CONTEXT.md     # Voice rules, neutralization, and rubric
│   │   └── PRINCIPLES.md  # Canonical P-1..P-29 scaffold
│   └── architecture/      # Decision records and repository structure
│       ├── decisions/     # ADRs for doctrine evolution (e.g. ADR-0001 SemVer)
│       └── repo-structure.md # Conformance to Tier-2 Repository Standard
├── scripts/
│   └── compile.sh         # Generates the single-file edition
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

### Compiling Single-File Edition

To build the full single-file manuscript with a generated table of contents:

```bash
./scripts/compile.sh > build/rlom.md
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
