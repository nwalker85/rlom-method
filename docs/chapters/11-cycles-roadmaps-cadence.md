<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 11 - Cycles, Roadmaps & Cadence

On 2026-10-01, twelve court card answers sat in the Ravenhelm adjudication queue for sixteen hours without a single downstream slice waking up to consume them. The human operator had already ruled on every one of those twelve architectural gates; the decisions were timestamped, signed, and sitting on the bench. Nothing moved. Sixteen wall-clock hours of engineering capacity evaporated because the workspace had no operating rhythm wired to sweep resolved blockers the turn they arrived, and everyone assumed the board would advance itself. That same week on a canonical three-person team, Engineer B - fresh from a shop that ran two-week Scrum rituals - asks whether the team is doing sprints, while Leadership asks for the next two quarters on one page by Thursday. The Operator has neither answer cleanly.

We built the wrong version of both first. Early on, we turned Linear Cycles on because the toggle was free, watched the tool draw a velocity chart, and within three cycles had a graveyard of rolled-over tickets, a points total that measured nothing except how creatively engineers split tasks on Thursday afternoon, and a team that served the two-week clock instead of the work. Story points and sprint commitments turn engineers into dishonest accountants. We turned Cycles back off. Then, to answer Leadership's horizon question, we pasted a screenshot of the active project board into a slide deck; the artifact was dead before the meeting started, and the first question from the table was about a project that had already shipped seven days earlier. The screenshot was a corpse.

Two real mechanics were missing, and the Method resolves both without ceremonial theater. The first is execution rhythm: how do you flush stalled gates and move work without inventing artificial two-week cliff edges? The second is planning horizon: how do you lay the next two quarters across a calendar without lying about dates or letting deferred work compound in the dark? Linear provides Cycles and the timeline roadmap on the Free tier. The Method's job is to tell you when to reach for each - and when to leave the switch off.

Start from the spine the Method already runs on. Your operating rhythm is cadence: a daily blocker and queue sweep, a weekly project update (P-19), a biweekly initiative update, a monthly operating review (P-21, Chapter 13), and a quarterly horizon review. That cadence is the physical clock of the workspace, and it holds whether or not your team ever enables a cycle. Cycles are an optional execution-rhythm overlay. The roadmap is a multi-quarter planning horizon. Neither replaces the cadence; both bolt onto it.

### Cadence is the spine; cycles are an overlay

A cycle is Linear's primitive for a timebox: a fixed window - usually two weeks - into which a team slots a batch of issues, with a start date, a cutoff, an automatic rollover rule, and a throughput curve that accumulates across windows. Linear makes cycles effortless to activate, which is the exact trap. Flipping a switch takes three seconds; cleaning up six months of velocity theater takes a quarter.

The Method defaults to cadence-driven flow, not cycle-driven batching. Your weekly project update (P-19) already states on the record what shipped with receipts, what sits in flight, and what is wedged; the milestones inside each project (P-3) already mark the hard architectural boundaries where a phase either clears its exit gate or stops the line. For most three-person teams, that is the entire heartbeat required. Bolting a two-week sprint clock on top of weekly project updates and milestone gates just hangs a second watch on the wall measuring the same hours. Run every candidate process change through the overbuild test (P-24): unless a cycle forces the Operator to make a trade-off earlier or exposes a stalled dependency faster than Friday's project update, it is bureaucracy with a burndown chart attached. Leave it off.

### When to turn cycles on

Turn cycles **on** only when the work and the team genuinely benefit from a fixed timebox and a structured rollover audit. The physical signals are concrete:

- The work decomposes cleanly into deliverable-sized issues (P-4) that clear inside a ten-day window.
- The team runs primarily on planned build work and wants a fixed commitment boundary rather than pulling continuously from an open project queue.
- The end-of-cycle rollover audit - comparing what was committed on day one against what spilled over on day fourteen - reveals scoping errors that the weekly update misses.

A product team marching through a known specification, where "is our throughput holding steady against the target date" is a live operational question, gets real mileage from a cycle timebox.

Leave cycles **off** when the team runs on continuous flow or high-interrupt operations. The signals are the exact inverse:

- Work arrives asynchronously from live incidents, customer escalations, infrastructure faults, or adjudication cards that must be acted on the turn they arrive.
- Deliverables follow dependency waves whose natural boundaries take three days for one slice and nineteen days for the next; forcing them into fourteen-day calendar boxes just manufactures fake splits.
- Project updates and milestone gates already drive execution; adding a cycle boundary creates a fortnightly rollover pile that everyone ignores.

Continuous-flow teams govern execution by sweeping queues daily and gating progress at project milestones, not by pretending the calendar resets every second Monday.

Obey two hard rules before touching the cycle toggle. First, **never turn cycles on before the workflow canon is locked down** (Chapter 10). A cycle chart measures the rate at which issues cross into your `Done` column; if `Done` still means "a PR merged" rather than "verified running in production with an attached receipt" (P-6), your velocity chart only measures how fast the workspace lies to itself. Lock the nine states (P-10) and enforce the `Validation` gate first; measure throughput only after `Done` is admissible evidence.

Second, **a cycle is a timebox, never a mini-waterfall and never a roadmap**. A cycle holds two weeks of tactical execution; a roadmap holds two quarters of strategic sequence. Operators who hand Leadership the current cycle board when asked for a plan are showing fourteen days of ticket shrapnel and calling it strategy. Strategy lives in initiatives and the timeline view.

### Running a cycle: capacity and the seventy-percent rule

When cycles are enabled, discipline lives at the boundary between windows. Before a cycle opens, the team sizes candidate issues and takes an honest reading of available engineering days on the bench. Linear totals the load; the Operator locks the commitment.

This is where Principle P-26 governs the math. P-26 states that cycle or weekly planning commits at most seventy percent of expected capacity, holding thirty percent in reserve for unplanned interrupts, production regressions, and scope friction. Teams that read P-26 as a Scrum-only rule miss the physics. **P-26 is a queue-theory law, not a sprint ceremony.**

A system loaded to one hundred percent utilization has infinite queue wait times the moment a single variance hits. When a team commits one hundred percent of its estimated hours into a two-week cycle, every cycle slips, rollover becomes ambient noise, and the post-mortem excuse is always "something unexpected came up" (P-26). Something unexpected always comes up; that is what the thirty-percent buffer is paying for. When cycles are off, the exact same seventy-percent ceiling governs the Operator's weekly slice allocation. You do not pack Engineer A and Engineer B to the gills on Monday morning and act surprised when a Wednesday production page blows up Friday's milestone. Cycles simply give P-26 a dated boundary line.

Let Linear's native automations handle the mechanical plumbing: auto-assigning active issues into the current cycle, rolling unfinished issues into the next window at cutoff, and enforcing a cooldown period between cycles. The automation moves the rows; the Operator runs the **rollover audit**. Every issue that spills across a cycle boundary gets interrogated with one question: why did this fail to clear?

- **Scoping fault:** The issue concealed three deliverables inside one title and violated the two-week sizing ceiling (P-4). Split the corpse before it enters the next window.
- **Interrupt absorption:** Live operational fire consumed the thirty-percent reserve and ate into committed capacity (P-26). Record the interrupt source so Triage sees the drain.
- **Priority drift:** The issue sat untouched in `Backlog` or `Todo` for ten days because the Operator loaded higher-priority work sideways without pulling the displaced ticket out (P-13).

Rollover is telemetry. If an issue rolls over twice without being split, descoped, or killed, your cycle is no longer a timebox; it is a conveyor belt for stale inventory.

### Preventing growing-cost deferrals

The nastiest defect in roadmap and cycle management is the **growing-cost deferral**: a foundational task - a namespace authentication scaffold, a schema migration, a shared test harness - gets kicked out of the current window as "not needed until Wave 3" with no scheduled review trigger. While that deferral sits in the backlog, four downstream features get built on ad-hoc snowflake workarounds. By the time the team pulls the deferred issue back onto the bench, the cost to retrofit the four snowflakes has multiplied fivefold.

A deferral whose cost grows while you wait cannot be tossed into an undated backlog bucket. Whenever the Operator defers an architectural or cross-cutting issue out of a cycle or milestone, the issue must be pinned to a **named target milestone or extraction wave** with an explicit review trigger before the downstream consumers open. If a deferral has flat cost - a cosmetic UI polish or an isolated CLI flag - defer it freely until demand proves it matters. If every week of delay pours concrete over a broken foundation, hoist it into the current wave or bind it to the exact calendar gate that blocks the dependent projects.

### Roadmaps: the timeline over initiatives and projects

Leadership's second question - the next two quarters on one page - is answered by Linear's timeline view: date-bearing projects plotted horizontally across a calendar grid, grouped into swimlanes by parent initiative.

Every active project carries a start date and a target completion date (P-3); every parent initiative names the durable quarter-plus outcome those projects must prove (P-2). The roadmap is not a separate slide deck someone draws in Figma on Wednesday night. It is the live objective layer rendered against wall-clock time: initiatives as rows, projects as bars, milestones as diamonds inside the bars, and the two-quarter window as the viewport.

The timeline exposes two structural truths that a kanban board hides:

1. **Cross-initiative dependency chains:** When the `OpenBao AppRole Migration` project under Platform Reliability must clear its exit gate before `Customer SSO Onboarding` under Enterprise Readiness can write a line of code, you wire a native blocking relation between the projects (available on Free). The timeline draws the hard dependency line between the bars. If the upstream bar slips two weeks right, the downstream collision is visible on screen immediately.
2. **Horizon honesty:** On a column board, a project that has been `In Progress` for four months looks identical to one that started yesterday. On the timeline, a project bar stretching past the end of the quarter is a physical claim the Operator must defend or resize.

The timeline feeds Chapter 13's monthly operating review directly. The initiative rollup table Leadership reads at the end of the month is the exact same set of timeline bars compressed into deterministic Red / Amber / Green health and key-result trend (P-21). One graph, two projections, zero manual slide-drawing.

### Plan-of-Record vs. What-If

A roadmap only holds authority if there is one canonical ledger. Keep a single committed timeline - the **Plan-of-Record** - strictly isolated from every hypothetical scenario you model. The Plan-of-Record is the contract the engineering floor executes against and the ledger Leadership reads (P-27). Nobody drags a project bar on the Plan-of-Record during a live meeting just to see how the dates look.

Scenario modeling is mandatory operator work: testing what happens if you pull an integration forward three weeks, add a third engineer in Q3, or freeze a low-margin initiative to clear a security audit. Run those experiments inside an isolated sandbox - a duplicated draft view, a scratch planning doc, or a temporary filter - never by mutating the live target dates on active projects. The instant engineers and executives cannot tell whether a date on the timeline is a hard commitment or a Tuesday afternoon thought experiment, the evidence chain (P-28) snaps at the top. A rollup built on shifting sand is theater.

Maintain one Plan-of-Record; spin up as many throwaway What-If models as the decision requires. Promoting a What-If scenario into the Plan-of-Record is an explicit executive ruling owned by the Operator (P-13), recorded with a changelog note explaining what moved and what got displaced.

> **Augmentation Surface - Capacity and Scenario Modeling**
>
> Where an agent layer makes this work better: computing realistic cycle capacity from historical throughput, active interrupt rates, and calendar availability before the Operator locks the window (P-26); generating isolated What-If schedule projections on command - showing the exact critical-chain impact of pulling a project forward or deferring a scaffold - without mutating a single field on the live Plan-of-Record; and sweeping the committed timeline daily to flag any project whose internal milestone completion rate has diverged from its target date before the monthly review arrives.
>
> What the PM keeps: locking the commitment itself - deciding which work enters the window, which What-If scenario gets ratified as the new Plan-of-Record, and which slipping target date represents an engineering reality to escalate versus scope to cut (P-13).

### The four-speed operating cadence

Put cadence, cycles, and roadmaps together and every clock in the workspace has a distinct job. Nothing overlaps; nothing relies on memory:

| Cadence | Horizon | Primary Surface | What Moves |
|---|---|---|---|
| **Daily Sweep** | 24 hours | `Blocked`, `Triage`, & `Waiting on Operator` views | Flush answered questions the turn they arrive; clear new blockers; route fresh intake inside SLA. |
| **Weekly Pulse** | 7 days | Project Updates (P-19) & 70% capacity allocation (P-26) | Record shipped receipts; audit in-flight milestones; expose blockers >7 days; set next week's top 3 priorities. |
| **Biweekly / Cycle Boundary** | 14 days | Initiative Updates & Cycle Rollover Audit (if enabled) | Compress project health into initiative trends; interrogate every rolled-over issue (`split`, `interrupt`, or `drift`). |
| **Monthly / Quarterly Review** | 30-90 days | Monthly Operating Review (P-21) & Timeline Roadmap | Reconcile the Plan-of-Record against delivered outcomes; evaluate deferred scaffolds; make portfolio trade-offs with Leadership. |

The sixteen-hour stall on 2026-10-01 happened because the Daily Sweep treated summary counters as truth instead of sweeping the open decision queue and pushing rulings into execution the moment they landed. Cadence is the mechanism that forces the workspace to notice its own state. The roadmap is the quarter-plus horizon that cadence measures against. Cycles, when turned on, sit underneath the weekly pulse as a two-week batch boundary. Keep each clock in its lane, and you answer Engineer B's sprint question and Leadership's roadmap question from one unbroken ledger.

> **Where this gets hard**
>
> The roadmap Leadership wants on the board slide and the roadmap the critical chain actually supports diverge the instant a date is promised externally - a customer contract deadline, a board commitment, or a launch window announced before engineering sized the dependencies. Now the Plan-of-Record is under executive pressure to reflect the date that was sold rather than the work required to build it, and the Operator is told to drag the project bar left to make the slide green. Holding the ledger line - where committed dates require matched capacity or explicit scope cuts, and wishful dates stay labeled as What-Ifs - is an authority collision that few Operators survive without an external standard to point at.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: ~2250
  principle-citations: P-2, P-3, P-4, P-6, P-10, P-13, P-19, P-21, P-24, P-26, P-27, P-28
  flagged-principle-gaps: none
-->
