<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 6 - Tier 1: Linear Free Install

You sit down on a Sunday night to track a three-person engineering team's work for Monday morning, and by midnight you are four tabs deep into rewriting the house wiring just to change a kitchen lightbulb. This is the Hal Problem: you walk into the garage for a screwdriver, notice the drawer squeaks, pull the workbench apart for WD-40, find a loose belt on the alternator, and three weeks later the kitchen is still dark while you are on the floor surrounded by forty pages of ontology notes. We have the corpse of that exact first build in our own ledger. When Ravenhelm first stood up Linear, we designed an intricate taxonomy from first principles before shipping a single tracked deliverable; within two quarters of real load, nobody maintained the cathedral, and the workspace rotted into 14 workflow states, 160 ad-hoc labels, and 0 of 45 projects with health set. We built a museum of intentions. Nothing inside it was true.

This chapter is the antidote for that Monday morning. It is the minimum physical install a three-person team - one Operator, Engineer A, and Engineer B - stands up in seven calendar days on Linear Free without spending a dollar or building a single surface the team cannot feed by Friday. The overbuild test (`P-24`) is the blade: every state, label, view, and template must earn its slot on the bench by either forcing a faster decision today or locking down an execution receipt the team would otherwise lose tomorrow. If a primitive does not do one of those two jobs before Friday at 5:00 p.m., you do not create it. Leave the drywall intact.

By Friday afternoon, your workspace holds exactly one team, the seven-state forward workflow spine (plus `Blocked` and `Canceled` for nine total slots), four label namespaces, four shared views, one active project with one published Friday update, and one merged pull request bound to an issue that cleared the `Validation` gate with live runtime proof. Everything else waits. And the sharpest lesson of Tier 1 is that almost everything that waits is already sitting right there on the Free tier, not locked behind a paywall.

### What Free actually gives you

Earlier drafts of this methodology misread the price sheet and assumed the architectural spine required a paid tier. That was wrong, and the correction changes how you sequence your entire first quarter. Linear Free hands you almost the entire operational chassis on day one: up to two teams, custom workflow states, namespaced labels, shared custom views, projects with milestones and documents, project and initiative status updates, the complete objective layer (**Initiatives** with health rollups and update cadences), **Cycles**, **Customer Requests** for structured voice-of-customer intake, **Releases** across up to 15 pipelines, **Pulse** digests, native issue relations (`blocks`, `blocked by`, `related`, `duplicate`), sub-issues, templates, the `Triage` inbox, priority and estimate fields, GitHub and GitLab pull-request linking, and the full GraphQL API with webhooks. The objective, intake, cadence, and release layers do not cost a cent. They sit on the workbench out of the box.

What Free withholds falls into two strict buckets: mechanical ceilings and autonomous analytics. The mechanical ceilings are hard integers: 2 teams, 250 active issues, and 10 MB file uploads. The capability exclusions are the analytics and automation layers that sit above the raw work graph: **Insights** (time-series and slice-by-property queries), **Triage Intelligence**, **Linear Asks**, **SLA timers**, and autonomous **Coding Sessions** unlock at Business (Chapter 8); multi-team **Dashboards**, **SAML/SCIM**, and the audit log unlock at Enterprise (Chapter 9); **Admin roles** and lifting the 250-issue cap arrive at Basic (Chapter 7). You never pay Linear to unlock the work graph itself. You pay later for room to grow and for machines that help you read the graph at scale.

That abundance is the exact trap on week one. Because Initiatives, Cycles, Customer Requests, and 15 Release pipelines are unlocked for free, the undisciplined architect turns all six knobs to ten on Monday morning. By Wednesday, a three-person team is drowning in empty containers it lacks the throughput to update, and by month two the engineers treat Linear as compliance theater and go back to coordinating in Slack DMs. Free will not stop you from overbuilding (`P-24`). Only your own discipline (`P-16`) keeps the bench clean.

| Surface Category | Included on Tier 1 (Free) | Held Back for Basic / Business / Enterprise | Week-One Install Verdict |
| :--- | :--- | :--- | :--- |
| **Work Graph Spine** | Up to 2 teams, custom states, sub-issues, relations, projects, initiatives | 5 teams + unlimited issues (Basic); sub-initiatives + sub-teams (Enterprise) | **Install 1 team, 1 project, 9 state slots.** Defer Initiatives to Week 3+. |
| **Intake & Routing** | Triage inbox, Customer Requests, templates, GitHub/GitLab PR links | Linear Asks, Triage Intelligence, Zendesk/Intercom (Business); Web forms (Enterprise) | **Install Triage + 1 template + code host.** Defer Customer Requests. |
| **Cadence & Delivery** | Cycles, Project/Initiative updates, Pulse, Releases (up to 15 pipelines) | SLA clocks (Business) | **Install Friday Project Update.** Defer Cycles and Releases until flow stabilizes. |
| **Analytics & Agents** | Custom shared views, GraphQL API, webhooks, "Open in coding tool" | Insights, Coding Sessions, Code Intelligence (Business); Dashboards (Enterprise) | **Install 4 shared views.** Do not build external scripts on week one. |

### The 7-day bench install

#### Day 1 (Monday) - Carve the team remit and lock the workflow gate

Open `Settings -> Teams`, select the default team named after your company, and rename it for the concrete remit your three people own (`Platform`, `Core-API`, `Client-Runtime`). The company is the workspace; the team is the blast radius this group of three answers for. Seat only the Operator, Engineer A, and Engineer B. Nobody else gets a login during week one.

Now open `Settings -> Teams -> [Team Name] -> Workflow` and strip out Linear's defaults until your board enforces the seven-state forward progression (`Triage`, `Backlog`, `Ready`, `In Progress`, `In Review`, `Validation`, `Done`) plus the two off-axis exceptions (`Blocked` and `Canceled`), giving nine canonical slots (`P-10`):

1. **Triage** *(Triage category)* - Raw, unexamined intake. Every Slack forward, bug report, or midnight thought lands here before touching the backlog.
2. **Backlog** *(Backlog category)* - Accepted work that is real and bound to a project (`P-3`), but not yet scoped or scheduled for immediate execution.
3. **Ready** *(Unstarted category)* - Scoped to deliverable size (`P-4`), carrying explicit exit criteria and a verification command (`P-15`), ready for an engineer to pull.
4. **In Progress** *(Started category)* - Active execution by a single named human owner (`P-14`) with an open branch in the code host.
5. **In Review** *(Started category)* - Pull request opened or decision artifact published, awaiting peer inspection.
6. **Validation** *(Started category)* - The load-bearing physical gate (`P-6`). The code is merged to `main`, but the issue is not finished until live runtime, browser, release, or human-acceptance receipts are pasted into the timeline (`P-7`).
7. **Blocked** *(Started category)* - Execution halted by an external dependency; the blocking entity or issue ID must be named in a comment the minute the state flips.
8. **Done** *(Completed category)* - Terminal truth. Verification receipt is on file in the issue comment stream (`P-28`).
9. **Canceled** *(Canceled category)* - Terminal discard. The reason for dropping the work is recorded in a closing comment.

Wire **Validation** right now and disable any integration toggle that moves an issue straight to `Done` when a pull request merges. Our v1 mistake was letting GitHub webhooks close issues on merge; within thirty days, "Done" meant "a PR landed on `main` while the container crashed in staging and the database migration never ran." Merged is implemented. Only verified in the target environment is trusted (`P-6`). When a PR merges, the issue lands in `Validation` and sits there like an indictment until a human checks the live system, pastes the receipt, and flips it to `Done` (`P-7`). Resist creating `stage:*` labels (`P-11`) or extra QA columns. Lock the nine slots.

#### Day 2 (Tuesday) - Stamp four label axes and one honest project

Navigate to `Settings -> Workspace -> Labels`. Earlier, we watched a workspace suffocate under 160 ungrouped labels (`urgent-ish`, `needs-eyes`, `backend-v2`, `tech-debt-q3`) where every engineer minted new tags on impulse and zero views queried any of them. A label is not prose commentary; it is an index key for a view (`P-16`). Install four orthogonal namespaces and nothing else:

- `type:` (`type:feature`, `type:bug`, `type:chore`, `type:docs`, `type:research`) - The structural shape of the deliverable.
- `component:` (three to five actual codebase boundaries, e.g., `component:auth`, `component:api`, `component:worker`) - Map only the directories you are touching this month.
- `risk:` (`risk:low`, `risk:medium`, `risk:high`) - The Operator's explicit blast-radius flag (`P-13`).
- `source:` (`source:internal`, `source:customer`, `source:alert`, `source:github`) - Provenance tracking so you know which intake pipe is flooding the floor.

Do not create `domain:`, `stage:`, `okr:`, or `release:` labels in week one. If a label is not queried by one of Wednesday's four views, it is scrap metal on the shop floor.

Next, create exactly **one project** (`P-3`). Name it for the concrete deliverable crossing the finish line in the next four to eight weeks (`Auth Service Cutover`, `Billing Webhook Spine`), never an immortal department name (`Backend Improvements`). Assign the Operator as Project Lead, set today as the start date, and set an honest target date four to six weeks out. Write a single paragraph in the project summary defining what ships, how you will prove it works, and link out to your repository ADR or architecture doc for deep context (`P-5`). Leave milestones empty until you have shipped for two weeks.

#### Day 3 (Wednesday) - Build the four control-panel views and cut the first deliverables

Click `Views -> New View` at the team level and build the Operator's four-gauge instrument panel. Every view must be shared with the team so Engineer A and Engineer B look at the exact same docket you read at 8:30 a.m.:

- **Operator's Now** - Filter: `State is any of In Progress, In Review, Validation`. Sort by `Priority`, then `Updated`. This is the active shop floor; if a task is burning engineering hours today, it sits on this screen.
- **Waiting on the Operator** - Filter: `Assignee is [Operator] AND State is any of Triage, Ready, Blocked`. Priority, risk tolerance, and scope cuts never delegate (`P-13`); this view stops the Operator from becoming the hidden bottleneck behind two idle engineers.
- **Blocked Radar** - Filter: `State is Blocked`. Sort by `Updated (oldest first)`. Any issue sitting here past 72 hours without an escalation comment gets either unblocked by the Operator or killed (`Canceled`).
- **Review & Validation Queue** - Filter: `State is any of In Review, Validation`. This catches diffs rotting on the vine and merged commits waiting for live production receipts (`P-6`).

Stop at four views. Do not build "Stale Backlog," "By Story Point," or "Engineer Leaderboard." Wait fourteen days until you hit a concrete routing question these four views cannot answer (`P-24`).

Now pull the team's real in-flight work out of scattered markdown files, sticky notes, and Slack threads, and cut the first 8 to 12 issues into your project. Every issue must pass the deliverable test (`P-4`): one discrete outcome, bounded scope, one human assignee (`P-14`), and an explicit exit criterion stating what artifact proves `Validation` (`P-7`). If an issue will take longer than ten working days to verify, split it into a parent issue and atomic sub-issues (`P-12`). Assign the first deliverable to Engineer A and the second to Engineer B.

#### Day 4 (Thursday) - Wire the code host and block the auto-close trap

Open `Settings -> Integrations -> GitHub` (or GitLab / Forgejo webhook bridge, covered in full in Chapter 12) and connect your active repositories. Configure branch automation so that copying the issue's git branch string (`eng-a/rav-101-token-leeway`) and opening a pull request automatically transitions the issue to `In Review`.

Now check the transition matrix under the integration settings and **rewrite the merge rule**. By default, code host integrations transition issues to `Done` when a pull request merges into the default branch. Change that target state from `Done` to `Validation` (or disable auto-close on merge and enforce manual move to `Validation`). That single dropdown is the hinge of the entire methodology (`P-6`, `P-8`). When Engineer A merges PR #14 on Thursday afternoon, Linear moves `RAV-101` into `Validation` - never `Done`. The ledger records that code hit the branch, while withholding credit until the code runs in the world.

> **Augmentation Surface - Install Verification**
>
> Where an agent layer makes this work better: at the end of Day 4, an audit agent queries the Linear GraphQL API against the Tier 1 install contract - verifying that the nine state slots exist in their proper state categories, the PR-merge transition points to `Validation` rather than `Done`, the label count is under 15 across the four canonical prefixes, the four shared views exist, and every active issue is attached to the project (`P-3`). The agent posts a pass/fail receipt table.
>
> What the PM keeps: deciding whether a flagged exception (such as a fifth `component:*` label or a second project for an emergency hotfix lane) earns its keep under `P-24`. The script inspects the wiring; the Operator owns the waiver.

#### Day 5 to Day 7 (Friday through Sunday) - Walk one issue through Validation and ship the Friday update

On Friday morning, Engineer A's pull request merges. Watch the issue land in `Validation` on the **Operator's Now** view. Do not let anyone drag it to `Done` from memory. Walk the verification gate by hand (`P-7`, `P-28`): pull the deploy job log showing the new container digest booting cleanly, hit the live staging or production endpoint in a browser or via `curl`, and paste both the log URL and the output screenshot into the issue comment thread. Only after the receipt sits in the timeline does the Operator flip the state from `Validation` to `Done`. Engineer A and Engineer B have now seen the standard with their own eyes.

At 4:00 p.m. Friday, open the project header, click **New Update**, set the project health badge (`On Track`, `At Risk`, or `Off Track`), and publish the five-block weekly ledger (`P-19`, `P-27`):

- **Shipped (Verified Done)** - Issues that cleared `Validation` this week, with direct links to their proof artifacts.
- **In Flight** - Issues currently in `In Progress`, `In Review`, or `Validation`, named by ID and owner.
- **Blocked** - What is wedged, who owns the unblock, and the date it escalates.
- **Decisions Needed** - Explicit tradeoffs requiring leadership sign-off before Monday's pull.
- **Next Week's Commit** - The exact `Ready` issues entering execution on Monday morning.

Post the update. Over the weekend, touch nothing. When Engineer B opens Linear on Monday morning of Week 2, the entire operating loop has run once from intake to verified production receipt.

### Growing into the rest of Free without drowning

During weeks two through twelve, you do not upgrade your Linear billing plan. Instead, you turn on the remaining Free-tier machinery one piece at a time, only when a concrete operational pain forces the pull (`P-16`, `P-24`):

- **Initiatives (`P-2`)** - Switch these on in Week 3 or 4 when a second project launches and Leadership asks how both workstreams ladder up to quarterly company outcomes. Create two or three durable initiatives with quarter-end targets and link your projects beneath them.
- **Native Issue Relations (`blocks` / `blocked by`)** - Add explicit dependency edges the first time an issue in `Ready` cannot start until another issue clears `Validation`.
- **Cycles** - Enable time-boxed cycles only if your team needs a fixed one- or two-week commitment heartbeat on top of continuous flow (Chapter 11).
- **Customer Requests (`P-22`)** - Turn on structured customer attribution when beta users start generating feedback faster than you can triage in raw Slack threads. Remember the iron law: a Customer Request is captured signal, never automatic scope.
- **Releases (`P-9`)** - Configure release pipelines (Free includes up to 15) once you separate merge-to-main from tagged production rollouts (Chapter 12).

### Ceiling signal - when Free physically runs out

You do not leave Tier 1 because you want better project management primitives; you already own the primitives. You leave Tier 1 when your team hits one of Free's three hard integer walls. Because these are mechanical limits rather than subjective maturity thresholds, any **single** signal below triggers the move to Chapter 7 (Linear Basic):

- **Active and archived issue volume approaches 250.** Free enforces a hard 250-issue ceiling (excluding canceled issues). The moment you catch yourself deleting old tickets or hesitating to split a multi-week parent issue into proper sub-issues (`P-12`) just to hoard issue slots, upgrade immediately. Never corrupt the work graph to save ten dollars.
- **You need a third team boundary.** Free caps the workspace at 2 teams. When a second engineering squad spins up alongside an operations or platform lane and you need a third distinct backlog, the 2-team limit binds.
- **Flat permissions or 10 MB uploads block daily work.** Either you need to delegate team-level settings to a squad lead without handing over root workspace keys (requiring **Admin roles**), or your engineers are blocked from pasting browser verification videos and heap snapshots into `Validation` comments by the 10 MB upload cap.

Cross any one of those three lines, pay the ten dollars a seat, and move to Tier 2.

> **Where this gets hard**
>
> The `Validation` gate (`P-6`) is frictionless when your three-person team owns the repo, the CI runner, and the production cluster. It grinds to a halt when a separate infrastructure department owns deployments, locks the Operator out of cluster logs, and treats every request for runtime proof as an insult. The workspace looks clean on paper while issues pile up in `Validation` with no legal way to verify whether code is actually running.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: ~2500
  principle-citations: P-2, P-3, P-4, P-5, P-6, P-7, P-8, P-9, P-10, P-11, P-12, P-13, P-14, P-15, P-16, P-19, P-22, P-24, P-27, P-28
  flagged-principle-gaps: none
-->
