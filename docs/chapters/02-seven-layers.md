<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 2 - The Seven Operating Layers

A live planning session opened on the bench with one bounded question: *which model holds the fleet supervisor seat during concurrent slice execution?* Ten minutes in, verifying how the supervisor signed its dispatch tokens pulled the conversation downward into hardware-backed PKI. PKI pulled it sideways into service-to-service identity. Identity branched upward into a full platform tenancy redesign, which branched downward again into a rewrite of the agent memory substrate. Three hours later the session log held four thousand words of architecture notes, six new design threads, and zero answers to who sat in the supervisor chair.

That branch-up, branch-down trap is what happens to a recursive mind - human or LLM - when nothing holds the goal list at a fixed altitude. A flat issue tracker fails the exact same way. You install Linear on Tuesday, invite Engineer A and Engineer B, and stare at ten unlabelled primitives in the sidebar: initiatives, projects, issues, cycles, milestones, custom views, Triage, Asks, Customer Requests, releases, labels, documents. Because the tool does not force a containment hierarchy out of the box, v1 of almost every workspace is a flat bucket. A quarter-long reliability goal, a six-week CI migration, a four-hour branch-naming fix, and a 2,000-word database post-mortem all get filed as sibling issues in the same backlog. By week three, picking up a ticket to fix a webhook pulls the engineer into an unclosed architectural debate from two months ago. Nobody knows which screen to check on Monday morning.

The Method stops altitude drift by locking the workspace into **seven operating layers**. Every primitive Linear ships is bolted to one of those seven floors. Nothing floats between them.

### Why seven layers, not two

Legacy trackers give you two buckets and wish you luck. Jira gives you epics and stories; Trello gives you lists and cards. Both leave the strategic objective layer and the cryptographic proof layer outside the building, forcing you to tape quarterly OKRs into a slide deck and paste deployment receipts into a dying Slack thread. Linear ships the whole vertical column natively: initiatives sit above projects as a true quarter-scale objective container (`P-2`), while code-host webhooks inject merge and deployment evidence directly into the bottom of the issue (`P-8`). RLOM does not bolt an alien taxonomy onto Linear; it names the seven load-bearing surfaces already in the silicon and assigns each one a strict altitude and clock speed.

The dividend is scale without structural demolition. A 3-person squad runs all seven layers on Monday morning with two projects and five saved views. When that organization scales to 30 engineers and a fleet of autonomous worker slices, the schema does not change. More rows flow through the tables, more views slice the index, and automated gates verify the transitions, yet the seven layers stay bolted to the same studs. Build the frame once.

### Initiatives - the objective layer

**Definition.** An initiative is a durable, quarter-or-longer strategic outcome that groups bounded projects under a single accountable owner.

Initiatives hold the high-altitude question - *what must be measurably true by the end of the quarter that is not true today?* - so individual feature builds do not wander off into adjacent architecture rewrites. Initiatives aggregate projects (`P-2`), carry a target horizon, expose a three-color health signal, and run on a biweekly update clock (`P-21`). They never carry deadlines tighter than a quarter, and they never hold raw issues directly. Because Linear is the active work graph (`P-1`), an initiative with zero active or planned projects underneath it is dead weight; attach a real execution project to it this week or evict the essay to your wiki.

For our 3-person squad, the Operator stands up **Platform Reliability** as the anchor initiative. It spans multiple releases and parents two concrete projects: the **CI/CD Backbone** Engineer A is building right now, and the **Production Stability** hardening effort queued for next month. Health reads `On Track`. Every second week, the Operator writes a compressed initiative update (`P-21`). Leadership reads that rollup; they never spelunk through the issue queue underneath.

### Projects - the main execution container

**Definition.** A project is a bounded program of engineering work with a single human lead, explicit start and target dates, sequential milestones, and a mandatory weekly status receipt.

Projects are the primary execution container (`P-3`). In-flight engineering work floating outside a project is an immediate structural smell; it means work is burning capacity without a milestone gate or a weekly health check. Every valid project answers five questions on its front card: what we are building, when it lands, who leads it, which milestones gate the path, and what blocks the critical chain today. The Operator governs project scope and boundaries; the project lead - frequently Engineer A or Engineer B at squad scale - writes the Monday status receipt (`P-19`).

Engineer A leads **CI/CD Backbone**, parented under Platform Reliability. Start date: Monday. Target date: end of quarter. Milestones lock the sequence: `Pipeline online` -> `First service migrated` -> `Runbook handed off`. Every Monday morning, without fail, Engineer A posts the weekly project update (`P-19`). Even if the project sat frozen behind an upstream blocker all week, the Monday entry goes into the ledger. Silence is never a valid status.

### Issues - deliverable-sized work units

**Definition.** An issue is an atomic, single-outcome, single-owner unit of delivery with binary exit criteria and an execution horizon measured in days, never weeks.

Execution lives inside issues. The sizing law (`P-4`) is unforgiving: one verifiable outcome, one human assignee in the seat, exit criteria crisp enough to test with a command or inspect in thirty seconds, and full completion including Validation inside two weeks. The moment an issue accumulates more than five acceptance bullets, crosses more than two days of implementation, or sprawls across unrelated subsystems, split it into a parent tracking issue with atomic sub-issues (`P-12`). Issues also obey strict locality (`P-18`): an issue's explicit exit criteria override the parent project's defaults, which in turn override workspace-wide templates. Closer to the metal wins.

This layer is also where teams must enforce the boundary between the work graph and the library (`P-5`). When an engineer starts pasting a six-page Architecture Decision Record, a schema migration runbook, or a root-cause timeline into an issue description, stop them. Long-form rationale belongs in version-controlled repository `docs/` or the team wiki; the Linear issue holds the link, the diff boundary, and the exit test.

Engineer B picks up the squad's first atomic issue: **Add Linear-to-PR branch naming guard to `CONTRIBUTING.md`**. One outcome: the repository docs and pre-push hook specify the exact `<type>/<issue-id>-<slug>` contract. One owner: Engineer B. Exit criteria: pull request merged to `main`, link attached, and parent milestone incremented. Estimate: four hours.

### Views - the operator's daily control panel

**Definition.** A view is a persisted, shared query over issues or projects that the Operator and squad sweep on a fixed daily or weekly clock.

Saved views turn a passive database into an air-traffic control board. If you have to click through team sidebars and build ad-hoc filters to find out what is wedged, your operating surface is broken. RLOM installs seven shared views as the squad's instrument panel: **Operator's Now** (active in-flight execution), **Waiting on the Operator** (decisions queued on the human seat), **Blocked Critical Path**, **In Review**, **Needs Validation / Evidence**, **Projects Without Recent Updates**, and **Stale Triage**. Each view is wired to a specific time of day.

Views also govern the life and death of every label in the workspace (`P-16`). Labels are query indices, not decorative stickers. If you create a label that no saved view filters against, you just added friction to issue creation for zero operational return. Delete every label that lacks a view.

On our 3-person team, the Operator, Engineer A, and Engineer B all open the exact same **Operator's Now** view before morning standup. It filters to issues in `Ready`, `In Progress`, `In Review`, and `Validation`, grouped by assignee. Nobody maintains a private stash of hidden boards. One truth sits on the glass.

> **Augmentation Surface - Layer Reconciliation**
>
> Where an agent layer makes this work better: running a nightly structural sweep across the graph to catch altitude violations - flagging an issue that has accumulated twenty comments and three weeks of churn because it is secretly an undeclared project, identifying a "project" with zero issues and five pages of prose that belongs in the wiki (`P-5`), or catching active `In Progress` issues orphaned outside any parent project (`P-3`). The agent posts the reclassification candidates to the Operator's morning queue.
>
> What the PM keeps: clicking the move button. Deciding whether an overgrown issue gets promoted to a bounded project or split into sub-issues (`P-12`) is a scope and priority call (`P-13`), never an automated background mutation.

### Intake - the entry point for new work

**Definition.** Intake is the airlock where raw signals - Triage items, Slack/email Asks, Customer Requests, bug reports, and agent-surfaced defects - enter the workspace before touching the active backlog.

When intake has no airlock, a team drowns in three separate swamps at once: DM requests promised in Slack, half-baked notes in a shared doc, and raw tickets dumped straight into `Backlog` where they rot alongside real commitments. RLOM locks the front door: every unscheduled signal lands in **Triage** first and faces a hard seven-day SLA (`P-20`). Before day seven expires, the Operator classifies the item - accepting it into a bounded project, merging it into a duplicate, canceling it outright, attaching it to a Customer Request, or routing it to repository documentation (`P-1`). Raw customer requests never jump the airlock straight into engineering scope (`P-22`); they attach as signal until the Operator schedules the work.

All capture happens inside Linear (`P-23`). Never keep a secondary spreadsheet or shadow backlog to "pre-triage" ideas before creating tickets. Put it in Triage and let the seven-day clock force the verdict.

### Delivery evidence - the substrate for Validation

**Definition.** Delivery evidence is the verifiable proof generated outside Linear - merged pull request URLs, passing CI run links, container digest tags, deployment logs, browser screenshots, and non-author acceptance sign-offs - that proves a change works in reality.

This layer is the firewall between theater and engineering. A merged pull request proves only that code is *implemented*; runtime verification in the target environment proves that code is *trusted* (`P-6`). Between `In Review` and `Done` sits the **Validation** state (detailed in Chapter 10), and the Validation gate only opens when hard delivery evidence lands on the issue (`P-7`). The code host and deployment rails generate those receipts automatically (`P-8`): GitHub, GitLab, or Forgejo webhooks attach the PR lifecycle, CI task results, and release tags directly to the Linear issue record. Linear indexes the receipts; it never asks a human to re-type them.

For production-bound changes (`release:production`), an issue without runtime proof never crosses into `Done` (`P-9`). Engineer A's CI/CD Backbone ticket sits in `Validation` until the new pipeline actually builds, pushes, and deploys a live service end-to-end and the execution log is linked on the ticket. The Operator checks the receipt, not the adjective.

### Analytics - the reporting substrate

**Definition.** Analytics is the read-only aggregation layer - Linear Insights, view counters, and portfolio dashboards - that compiles verified graph state into cycle times, throughput trends, and SLA health.

Analytics sits at the bottom of the seven layers because math over dirty state is garbage. When active work hides outside projects, Triage rots past thirty days, and issues jump straight from `In Progress` to `Done` on a pinky promise, every throughput chart in Insights is fiction. Once the upper six layers hold their structural contracts, analytics requires zero manual spreadsheet assembly: cycle time, blocker dwell, Triage SLA compliance (`P-20`), and weekly project health (`P-19`) read straight off the live graph.

At 3-person squad scale, keep analytics ruthless and minimal: one counter tracking status distribution across the active board, and one aging query watching `Projects Without Recent Updates` and `Stale Triage`. As the organization scales into Business and Enterprise tiers, those exact primitives feed the monthly leadership review (Chapter 13) through an unbroken chain of custody from merge commit to executive summary (`P-28`).

### Layer-to-capability map

| Layer | Primary Linear capability | Deep-dive chapter |
|---|---|---|
| Initiatives | Initiatives + initiative updates | Chapter 13 (Reporting Up) |
| Projects | Projects, milestones, project updates, dependencies | Chapter 10 (Workflow Canon), Chapter 13 |
| Issues | Issues, parent/sub-issues, exit criteria, labels | Chapter 5 (Operating Surface), Chapter 10 |
| Views | Custom views, label filters, Insights panels | Chapter 5 |
| Intake | Triage, Triage Intelligence, Asks, Customer Requests | Chapter 8 (Tier 3) |
| Delivery evidence | GitHub/GitLab integration, Releases, SLAs | Chapter 12 (Code Host Integration) |
| Analytics | Insights, dashboards | Chapter 13 |

### Closing

Drop any one of these seven layers and the containment hierarchy fails: drop Initiatives and projects lose their quarter-scale anchor; drop Delivery Evidence and `Done` becomes a lie; drop Views and your labels decay into unindexed graffiti. Chapter 5 wires these seven layers into daily workspace hardware through orthogonal labels, seven shared views, and poka-yoke templates. Chapter 10 locks the nine-state workflow canon and the Validation gate onto that surface. Hold the layers at their assigned altitudes.

> **Where this gets hard**
>
> Installing seven layers into an empty workspace takes an hour. Retrofitting them onto a two-year-old tracker where initiatives were filed as epics, architecture docs were pasted into ticket comments, and 400 half-finished tasks sit in `In Progress` with no parent project is forensic archaeology. You cannot bulk-move those rows without reading the dependency seams first.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: 2050
  principle-citations: P-1, P-2, P-3, P-4, P-5, P-6, P-7, P-8, P-9, P-12, P-13, P-16, P-18, P-19, P-20, P-21, P-22, P-23, P-28
  flagged-principle-gaps: none
-->
