<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 2 — The Seven Operating Layers

You installed Linear yesterday. You created a team, accepted Engineer A and Engineer B, and now you're looking at an empty workspace with at least ten primitives staring back at you: initiatives, projects, issues, cycles, milestones, views, Triage, Asks, Customer Requests, releases, labels, documents. The product is opinionated, but it doesn't tell you which primitives carry which weight. So you do what most operators do: you create a few projects, dump issues into them, and within a week you can't tell which view is the one you check on Mondays.

The Method's first job is to give you a structural map. Linear has many features; the Method uses seven layers. Everything else is supporting machinery that belongs to one of the seven.

### Why seven layers, not two

Jira gives you epics and tickets. Trello gives you cards on a board. Both leave the objective layer and the evidence layer to your imagination — you bolt OKRs onto a spreadsheet and your "done" definition onto a Slack channel. Linear ships both natively: initiatives sit above projects as a real objective container (P-2), and the integration surface with the code host ships evidence into the issue automatically (P-8). The Method's seven layers are not a methodology imposed on Linear; they are the layers Linear already exposes, named honestly so you can reason about them.

The payoff is scale without restructuring. A 3-person team can run all seven layers in a thin form on Monday morning. A 30-person team runs the same seven layers with more rows in each, more views slicing them, and more agents reading them — but no new layers and no rearrangement. The Method is meant to survive headcount growth without a re-platforming exercise.

### Initiatives — the objective layer

**Definition.** An initiative is a durable, quarter-or-longer outcome that groups projects under a single owner.

Initiatives are where the question "what are we trying to accomplish this quarter" gets a real, hyperlinked answer. They roll up projects (P-2), carry a target date, a health indicator, and an update cadence. They do not carry deadlines tighter than a quarter and they do not contain issues directly. The Method treats Linear as the active work graph (P-1), so an initiative without active projects under it is a smell — either revive it with a project or move the idea to a wiki.

For the 3-person team, the Operator's first initiative might be **Platform Reliability** — a durable objective that survives every individual release. It rolls up two projects: a CI/CD Backbone the engineers are building now, and a Production Stability project that's planned for next quarter. Health is "On Track." Updates run biweekly (P-21). The Leadership Team consumes the initiative update; it does not browse the projects underneath.

### Projects — the main execution container

**Definition.** A project is a bounded program of work with a single lead, a start and target date, milestones, and a weekly update.

Projects are the Method's main execution container (P-3). Active work without a project is the second-most-common smell in a Linear workspace; the first is doc-shaped issues (covered under Issues). A project answers five questions explicitly: what is being built, by when, by whom, with what milestones, blocked by what. The Operator owns project shape; the project lead — often an engineer at this scale — owns the weekly status update (P-19).

Engineer A's first project is **CI/CD Backbone**. Lead: Engineer A. Start: this week. Target: end of quarter. Milestones: Pipeline online → First service migrated → Documentation handed off. The project rolls up to the Platform Reliability initiative. It carries a Monday status update every week without exception (P-19), even when the update is "no movement, see last week."

### Issues — deliverable-sized work units

**Definition.** An issue is a single-outcome, single-owner work unit with exit criteria and an estimate measured in days, not weeks.

Issues are where execution actually happens. The Method's rule is strict: one outcome, one owner, exit criteria you could read aloud at standup, and verification possible within two weeks (P-4). An issue whose acceptance criteria list more than five items, or whose implementation spans more than two days or two files, gets split into a parent issue with sub-issues (P-12). The Method also enforces a locality rule (P-18): an issue's exit criteria override the project's defaults, which override workspace defaults. Closer-to-the-work guidance wins.

Issues are also where the Method's hardest discipline lives: documentation owns deep context (P-5). An issue is not the place for an ADR, a runbook, or a five-paragraph rationale. Link to the doc; keep the issue scoped to "what changed and how do we know."

Engineer B's first issue is **Add Linear-to-PR branch naming convention to the contributing guide**. Single outcome (the guide names the convention). Single owner (Engineer B). Exit criteria: PR merged, link posted to Engineer A and the Operator, two-line update in the parent project. Estimate: half a day.

### Views — the operator's daily control panel

**Definition.** A view is a saved filter over issues or projects that the Operator (and the team) checks on a recurring cadence.

Views are how the Method becomes operational. A workspace with no views is a workspace you can only navigate by clicking; a workspace with the right views is one where the Operator's morning takes ten minutes. The Method requires a small standard set: a "Now" view scoped to in-flight work, a "Waiting on Operator" view, a "Needs Validation" view, a "Stale Projects" view, and a "Blocked Critical Path" view. Each view is read at a defined cadence — daily, weekly, or before reporting.

Views also justify the entire label system. Labels exist to serve views (P-16). A label that no view cites is a candidate for deletion. The Operator does not add a `domain:security` label because security feels important; they add it because the security-domain view is a real surface someone reads on a real day.

The 3-person team shares one Now view that filters to all issues in Ready, In Progress, In Review, or Validation. The Operator looks at it Monday morning. Engineer A and Engineer B look at it before standup. It is the same view; the Method does not invent a separate operator view and a separate engineer view at this scale.

> **Augmentation Surface — Layer Reconciliation**
>
> Where an agent layer makes this work better: scanning the workspace nightly for layer drift — an issue with three weeks of activity that should have been split into a project, a project whose only artifact is a long description and no issues that should have stayed a wiki page, a doc-shaped issue whose body would belong in a repo `docs/` directory. The agent surfaces candidates with proposed new homes.
>
> What the PM keeps: deciding the new home. Layer assignment is a judgment call about how the team will actually use the artifact next week, and that judgment stays with the Operator.

### Intake — the entry point for new work

**Definition.** Intake is the set of surfaces through which new work enters the workspace: Triage, Asks (Slack/email), Customer Requests, and ad-hoc creation by the Operator or an agent.

Intake is the layer that fails silently when it fails. A team without an intake discipline accumulates work in three places: a Slack channel nobody triages, a doc nobody re-reads, and a Linear backlog of un-prioritized issues. The Method's rule is that Triage is the single funnel: all new work enters Triage and gets classified within seven days (P-20) — accepted into a project, merged with a duplicate, canceled, converted to a Customer Request, escalated to the Operator, or moved to docs-only. Customer feedback does not bypass Triage on its way to scope (P-22); it becomes a Customer Request, and the Operator decides if and when it converts.

Intake also includes the Operator's own quick captures and any agent-created issues. The Method treats Linear as the system of record (P-23) — capture in Linear, not in a side channel that requires later re-entry.

For the 3-person team, intake is thin: the Operator creates most issues, Engineer A and Engineer B drop the occasional "this should be tracked" into Triage, and a Slack-to-Asks intake gets installed when the team grows past five people. The discipline still applies: nothing sits in Triage longer than seven days unclassified.

### Delivery evidence — the substrate for Validation

**Definition.** Delivery evidence is the set of artifacts produced outside Linear that prove an issue is implemented: PR URLs with merge status, CI results, deploy logs, screenshots, release notes, acceptance comments.

This is the layer that distinguishes the Method from teams that "use Linear." Code that is merged is implemented; code that has evidence of running in the target environment is trusted (P-6). The Method's Validation state (covered in detail in Chapter 10) is the gate between the two, and the gate is only as good as the evidence flowing into it. The code host produces that evidence (P-8): GitHub posts merge state, CI checks, and deploy outcomes; the GitLab equivalent posts merge request state, pipeline status, and deployment jobs. Linear links to those artifacts; Linear does not duplicate them.

For production-affecting work, no artifact means no Done (P-7). Engineer A's CI/CD Backbone issue stays in Validation until the pipeline has run a real deployment end-to-end and the log is linked in the issue. The Operator's job at that gate is to verify the link is real, not to take Engineer A's word for it.

### Analytics — the reporting substrate

**Definition.** Analytics is the layer of Insights, dashboards, and view-level metrics that converts the work graph into numbers the Operator and the Leadership Team can read.

Analytics is the last layer because it depends on every layer above it being clean. Throughput, cycle time, stale-project counts, Triage SLA health, agent throughput — all of these are derivable from a workspace where projects have updates, issues have evidence, and views are real. In a workspace where projects are stale and issues close without evidence, the same metrics measure theater.

The Method uses analytics sparingly at the 3-person stage: one Insights panel showing issue count by status on the Now view, one showing project age on the Stale view. As the team grows, dashboards consolidate the metrics the Operator hands upward — and the monthly review (Chapter 12) rolls initiative health up to the Leadership Team. The chain holds only because each lower layer carries its own evidence (P-28).

### Layer-to-capability map

| Layer | Primary Linear capability | Deep-dive chapter |
|---|---|---|
| Initiatives | Initiatives + initiative updates | Chapter 12 (Reporting Up) |
| Projects | Projects, milestones, project updates, dependencies | Chapter 10 (Workflow Canon), Chapter 12 |
| Issues | Issues, parent/sub-issues, exit criteria, labels | Chapter 5 (Operating Surface), Chapter 10 |
| Views | Custom views, label filters, Insights panels | Chapter 5 |
| Intake | Triage, Triage Intelligence, Asks, Customer Requests | Chapter 8 (Tier 3) |
| Delivery evidence | GitHub/GitLab integration, Releases, SLAs | Chapter 11 (Code Host Integration) |
| Analytics | Insights, dashboards | Chapter 12 |

### Closing

The seven layers are necessary; you cannot drop one without weakening the work graph. The operating surface — labels, views, templates — covered in Chapter 5 is how those layers actually show up in the workspace day to day. The workflow canon and the Validation gate in Chapter 10 are the most opinionated part of the Method, and they sit on top of these seven layers. Everything that follows in this document assumes the layers are named, owned, and used as defined here.

> **Where this gets hard**
>
> Layer assignment becomes archeology when a team has historical work scattered across three shapes — some in tickets nobody updated, some in docs nobody linked, some in chat threads nobody can search — and the question "is this an issue, a project, or a wiki page" can't be answered without reading a quarter of context for each item.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: ~1750
  principle-citations: P-1, P-2, P-3, P-4, P-5, P-6, P-7, P-8, P-12, P-16, P-18, P-19, P-20, P-21, P-22, P-23, P-28
  flagged-principle-gaps: none
-->
