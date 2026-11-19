<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 5 - The Operating Surface: Labels, Views, Templates

When we dumped the schema of our own v1 workspace onto the bench, the tag table returned **~160 ad-hoc labels alongside 14 custom workflow states**. Three engineers and a handful of early automation scripts had each invented their own dialect, leaving `bug`, `Bug`, `type:Bug`, and `defect` all live in the same drop-down menu and filtered by nothing. Nearly half of the 160 labels sat attached to a single forgotten issue. Over in the sidebar, nineteen private views and three shared views fought over what the word "active" meant. Every morning the Operator opened Linear, stared at a completely different slice of reality than Engineer A or Engineer B saw, and burned forty minutes clicking through tabs just to reconstruct what moved overnight. Nobody could point at one glass pane and say: *this is the floor right now.*

Principles written in a handbook live in people's heads; the operating surface lives in the silicon of the workspace. Chapter 2 established the seven containment layers, and Chapter 3 laid down the 29 numbered laws. This chapter wires the physical switches that enforce those laws every day: **orthogonal label namespaces, seven shared control-panel views, and friction-killing templates**.

This surface is where `P-25` (*Verify what you enforce*) gets teeth. A workflow rule that requires a human to remember five invisible conventions decays into folklore inside a month. When the label index feeds a saved view and the template pre-loads the required verification fields, compliance stops being a test of character. The board checks itself.

### Labels are an index, not an organizational scheme

Every broken workspace makes the same category error: treating labels like manila folders in a filing cabinet. Someone touches a frontend file, so they slap a `frontend` sticker on the ticket and feel organized. Six months later you have ~160 stickers and zero working queries. RLOM inverts the rule: **labels exist solely to power saved views, and any label cited by zero views gets deleted (`P-16`)**. Never mint a label because a topic *exists*. Mint a label only when an Operator or engineer needs a deterministic query axis to drive a recurring decision.

To prevent flat-namespace rot, RLOM partitions labels into **eight colon-namespaced axes**. A flat alphabetical list of 80 tags is cognitive noise; eight orthogonal prefixes act like a typed schema in the drop-down menu:

- `type:*` - `Feature`, `Bug`, `Chore`, `Documentation`, `Research`, `Gate`. Every issue carries exactly one `type:*` tag. The `type:Gate` value marks a milestone or dependency hold whose sole job is to block downstream waves until an approval, cutover, or external artifact lands.
- `component:*` - one value per bounded service, binary, or subsystem your squad owns (for example, `component:api`, `component:web`, `component:worker`). Keep this axis mapped one-to-one with your deployable boundaries; if you run a single monolith, skip `component:*` until you actually split a service out.
- `domain:*` - cross-cutting operational planes: `domain:security`, `domain:infrastructure`, `domain:product`, `domain:operations`. Use a light hand. Whereas `component:*` names *which code* changes, `domain:*` names *which discipline wakes up if this diff catches fire*.
- `risk:*` - `low`, `medium`, `high`. Stamped at `Triage`. Drives the **Blocked Critical Path** view and feeds the weekly risk table in Chapter 13.
- `source:*` - `asks`, `slack`, `support`, `github`, `sentry`. Records the intake pipe that spawned the ticket. When Triage analytics show that 80% of incoming bugs carry `source:slack`, you know you have an unbridled chat problem that needs Linear Asks (Chapter 8), not another standup meeting.
- `release:*` - `production`, `staging`, `internal`, `none`. Declares the blast-radius target so the `Validation` gate (Chapter 10) knows which receipt to demand. Any issue carrying `release:production` is mechanically barred from `Done` until runtime production proof is attached (`P-9`).
- `stage:*` - `design`, `qa`, `uat`, `soft-launch`. These are the sub-states that naive teams mistakenly add as workflow columns (`P-11`). Because the workflow canon is locked at exactly nine states (`P-10`), sub-phases ride as `stage:*` labels while the issue sits in `In Progress`, `In Review`, or `Validation`.
- `parking-reason:*` - `waiting-on-vendor`, `waiting-on-decision`, `waiting-on-budget`, `waiting-on-customer`. Applied exclusively to `Urgent` or `High` priority issues parked in `Backlog`. An `Urgent` issue sitting in `Backlog` without a `parking-reason:*` tag is a contradiction on its face: either the priority is inflated or a hidden blocker is going unreported.

Notice how every single namespace above unlocks a concrete operational query. Combining `type:Bug` + `risk:high` + `release:production` gives the Operator a zero-noise morning incident radar. Filtering on `stage:uat` isolates the user-acceptance queue without polluting cycle-time charts. Querying `Priority in (Urgent, High)` + `State = Backlog` + `Label != parking-reason:*` exposes priority theater in five seconds before Monday standup. No view, no label (`P-16`). If you just want to find a topic six months from now, use full-text search.

One hard schema guard before moving to views: **never use a label to shadow a native Linear typed field**. Priority, Estimate, Workflow State, Assignee, and Project Health are single-valued database columns enforced by Linear's state engine. Creating a `priority:high` label, a `health:red` label, or a `status:done` label guarantees split-brain drift because labels allow set membership (an issue can accidentally carry both `priority:low` and `priority:high`) while native fields enforce a single value. That exact collision is how `bug`, `Bug`, and `defect` poisoned our v1 workspace. Use native columns for state; reserve labels for orthogonal query axes.

> **Augmentation Surface - Surface Maintenance**
>
> Where an agent layer makes this work better: running a monthly schema audit across the workspace API - listing every label referenced by zero saved views (`P-16`), identifying near-duplicate tag strings (`bug` vs `type:Bug`), flagging `stage:*` labels still stuck on issues that already crossed into `Done`, and reporting saved views with zero opens in the last 90 days. The agent hands the Operator a crisp deletion manifest.
>
> What the PM keeps: approving the purge. Deleting a dormant label or consolidating two component tags is a schema decision that stays in the Operator's chair.

### Views are the daily control panel

A saved view is an operational question compiled into a permanent filter. RLOM installs **seven shared views** as the squad's common glass. They are shared across the workspace so the Operator, Engineer A, and Engineer B never argue from different screens. Keep personal scratch views in your private sidebar if you must, but run the floor off the seven shared boards.

**1. Operator's Now.** Filter: `Priority in (Urgent, High)` AND `State in (Ready, In Progress, In Review)`, grouped by `Assignee`. This is the live execution floor. The Operator scans it first thing every morning; Engineer A and Engineer B check it before pulling their next unit of work. By displaying parent projects inline, this view immediately exposes orphan tickets violating `P-3` (active work without a project) and bloated monoliths violating `P-4` (deliverable sizing).

**2. Waiting on the Operator.** Filter: `State != Done/Canceled` AND (`Label = stage:decision` OR blocker/delegate relation pointing to the Operator seat). This is the human accountability queue required by `P-13`. Priority rulings, taste calls, risk acceptances, and external commitments queue here. If this board ever holds more than five rows at the end of the day, the squad is not failing; the Operator's calendar is broken. Clear your own queue first.

**3. Blocked Critical Path.** Filter: `State = Blocked` AND `Priority in (Urgent, High)`. Owned day-to-day by the engineer sitting deepest in the platform dependency chain (Engineer B in our 3-person squad) and reviewed first at standup. Under `P-10`, moving a ticket into `Blocked` requires naming the exact blocking issue or external vendor in a relation or comment. A `Blocked` ticket with no named obstruction is a triage defect; fix the link or put it back in `In Progress`.

**4. In Review.** Filter: `State = In Review` with linked code-host pull request metadata displayed (`CI status`, `reviewers`, `mergeability`). Both engineers subscribe; the Operator sweeps it once daily to catch review starvation before a PR rots on the branch. This view bridges Linear to `P-8` (*The code host proves implementation*).

**5. Needs Validation / Evidence.** Filter: `State = Validation` AND `Time in state > 24h`. Watched jointly by the Operator and the lead engineer. Chapter 10 details the Validation doctrine; this view is the physical turnstile where `P-6` (*Validation separates implemented from trusted*) and `P-7` (*Evidence beats assertion*) execute. Merged tickets park here until the staging log, container `:b<N>` digest, screenshot, or production probe (`P-9`) lands in the comments. Nothing leaves this view without a receipt.

**6. Projects Without Recent Updates.** Filter: `Project Status = Active` AND `Last Project Update > 7 days ago`. Checked by the Operator every Monday at 8:30 a.m. This view mechanizes `P-19` (*Active projects get a status update every week*). If an active project lights up this board on Monday morning, the project lead writes the update before standup or the Operator downgrades the project status to `Planned` or `Paused`. Zero silent projects.

**7. Stale Triage.** Filter: `State = Triage` AND `Created > 5 days ago`. Gives the Operator a 48-hour early warning before an incoming item breaches the hard seven-day Triage SLA (`P-20`).

Seven views. Seven exact questions. Guard the count ruthlessly. The day a workspace accumulates eighteen shared views in the sidebar is the day everyone stops looking at all of them.

### Templates lower the cost of doing the right thing

During an audit of agent tool-routing failures (`WALKER-004J` / `RAV-1962`), we watched an autonomous coding slice inside the `yager` repository read dozens of source files, write a patch, run zero unit tests, and ship a fatal module-level `NameError`. Why? In that harness configuration, calling `read_file` was frictionless and free, whereas invoking `bash` to run `pytest` popped an interactive human approval prompt. The agent was not malicious; it was an optimizer following the cost gradient of its environment. When we priced the verification command higher than guessing, the actor guessed.

The law we wrote on the wall that afternoon governs every human and agent interface in the estate: **never price the oversight path above the unsafe one.**

An issue template is a pricing mechanism (`P-17`). If opening a blank, unstructured ticket takes two seconds and writing a properly scoped deliverable with exit criteria and validation commands requires remembering six Markdown headings from scratch, tired humans and rushed agents will file blank tickets every time. By pre-loading the exact headings into Linear's default templates, you make the disciplined path the lowest-effort path on the bench. RLOM installs four issue templates, one project template, and one delegation comment template:

**Feature template.** Pre-populates six mandatory fields:
- **Outcome:** One declarative sentence stating what works after this lands and for whom.
- **Scope Boundary:** Explicit `In Scope`, `Out of Scope`, and `Deferred` bullets so the executor does not branch-drift into adjacent refactors.
- **Acceptance Criteria:** Five or fewer binary, testable statements (`P-4`, `P-12`).
- **Expected Validation Receipt:** The exact artifact required to clear `Validation` into `Done` (`P-6`, `P-7`) - e.g., Harbor `:b<N>` digest, staging curl readout, or browser screenshot.
- **Target Repository & Paths:** Canonical repo and directory boundary.
- **Design / ADR Link:** Pointer to the external specification (`P-5`).

**Bug template.** Forces diagnostic facts before anyone touches code:
- **Reproduction Receipt:** Exact command, URL, payload, environment, and commit/version tag.
- **Blast Radius:** Who is impacted right now, how many tenants/requests are failing, and whether data custody is at risk.
- **Severity:** `P0` through `P3` with the one-line criteria printed inline inside the template comment so the filer never guesses.
- **Verification Proof Required:** Regression test name, live log query, or synthetic check required at the `Validation` gate (`P-7`, `P-9`).

**Research Spike template.** Stops open-ended exploration from turning into a shadow project:
- **Hard Timebox:** Exact hours or days allocated (a spike without a kill clock is an untracked project).
- **Root Question:** The single architectural or vendor question this spike must answer in the affirmative or negative.
- **Required Decision Artifact:** An committed ADR, benchmark table, or throwaway proof-of-concept branch (`P-5`).
- **Decision Deadline:** The calendar date when the spike either spawns a bounded project (`P-3`) or closes to `Canceled`.

**Standard Project template.** Governs every execution container (`P-3`):
- **Durable Goal:** The outcome delivered to the parent Initiative (`P-2`).
- **Canonical Milestones:** Pre-populated as `1. Scope & DAG Accepted` -> `2. Implementation` -> `3. Validation & Receipts` -> `4. Production Rollout` -> `5. Runbook & Handoff`.
- **Upstream / Downstream Dependencies:** Linked projects or external gates.
- **Kickoff Update Slot:** Must be posted within 48 hours of creation so the project never hits `Projects Without Recent Updates` (`P-19`).
- **Exit Criteria:** What must be running in production to mark the project `Completed`.

**Agent Delegation Comment template.** Saved as a reusable Linear template snippet and stamped whenever the Operator or lead engineer assigns a task to a coding or triage agent (`P-14`, `P-15`). Fields: **Target Outcome**, **Strict File/Module Boundary**, **Exact Validation Command** (e.g., `cargo test --workspace` or `./scripts/compile.sh`), and **Required Return Artifact** (PR URL + test output). Handing an agent this template makes running the test suite cheaper than hallucinating success.

All six templates obey **Locality wins (`P-18`)**. The workspace template sets the floor; a project spec can tighten the rules for a high-risk migration; an individual issue's exit criteria override both for that specific diff.

### Relations and recurring issues

Two native Linear mechanics finish the surface wiring when used with discipline.

**Issue relations (`blocks` / `blocked by`, `duplicate`, `related`).** Treat `blocks` and `blocked by` as hard structural edges in your execution DAG. Whenever an issue moves into the `Blocked` workflow state (`P-10`), bind it with a native `blocked by` relation to the upstream issue holding the gate, in addition to naming the blocker in the comment thread. That bidirectional pointer makes the dependency visible on both tickets so Engineer A knows that merging their schema PR immediately unblocks Engineer B's API ticket. Use `duplicate` at `Triage` to collapse redundant bug reports while preserving customer signal links. Use `related` sparingly; if you find yourself chaining six issues together with `related` links, stop and group them under a parent issue with sub-issues (`P-12`) or a bounded project (`P-3`).

**Recurring issues (mechanizing maintenance).** Remember the corpse that opened Chapter 1: we designed a clean system, got bored of manual upkeep, and watched the workspace rot to 14 states, ~160 labels, and 0 of 45 projects with health set. You cure maintenance boredom by turning workspace upkeep into scheduled, recurring issues inside the work graph itself:
- A weekly recurring Monday issue for the **Triage & Stale Project Sweep** (`P-19`, `P-20`).
- A monthly recurring issue for the **Orphan Label & Zombie View Purge** (`P-16`).
- A quarterly recurring issue for the **Overbuild Audit** (`P-24`).

Because recurring issues spawn straight into the active board, they show up on `Operator's Now`, require a completion receipt (`P-7`) to close, and trigger alarm views if ignored. The operating model maintains itself on the exact same rails it uses to ship code.

### The overbuild test

Every month somebody on the team will propose a ninth label namespace, an eighth shared view, or a custom workflow column for a special project. Before creating it, run the proposal through the five-question **Overbuild Test (`P-24`)**:

1. Does it help the Operator make a priority, taste, or risk decision faster?
2. Does it help an engineer or agent slice execute and verify work faster?
3. Does it capture delivery evidence we would otherwise lose at the `Validation` gate?
4. Does it eliminate recurring manual translation work for the PM?
5. Does it expose blast-radius or schedule risk earlier in the week?

Count the `yes` answers. **Four or five:** build it and wire it to a view. **Three or fewer:** reject it on the spot. A workbench stays fast because of what you refuse to bolt onto it. Keep the surface clean.

> **Where this gets hard**
>
> Cutting ~160 legacy labels down to 25 orthogonal tags and collapsing 19 private boards into 7 shared views is a five-minute API script wrapped inside a two-week political fight. Every zombie label and private dashboard has an author who swears their workflow will collapse without it. Pulling them onto a shared control panel requires replacing their private workarounds with shared views that answer their real questions faster.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: 2560
  principle-citations: P-2, P-3, P-4, P-5, P-6, P-7, P-8, P-9, P-10, P-11, P-12, P-13, P-14, P-15, P-16, P-17, P-18, P-19, P-20, P-24, P-25
  flagged-principle-gaps: none
-->
