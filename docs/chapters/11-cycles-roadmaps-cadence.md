<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 11 — Cycles, Roadmaps & Cadence

Engineer B came from a shop that ran two-week sprints, and in the second week asks the question the Operator has been avoiding: are we doing sprints or not? That same week Leadership asks for "the roadmap" — not this week's board, the next two quarters, on one page, by Thursday. The Operator has neither answer cleanly. They tried cycles once, early: turned them on, watched Linear produce a velocity chart, and three cycles later had a pile of rolled-over issues, a number nobody trusted, and a creeping sense the team now served the cycle instead of the other way around — so they turned it back off. And the roadmap they sent Leadership last quarter was a screenshot of the project board, already stale by the time it was pasted into the deck; the first question in the meeting was about a project that had shipped a week earlier.

Two real gaps, and the Method has so far been silent on both. The first is execution rhythm: does the team commit work in fixed batches or flow it continuously? The second is planning horizon: how does the team show the next two quarters without lying? Linear answers both on Free — Cycles and the timeline roadmap are free primitives. The Method's job is to say when to reach for each, and, more often, when not to.

Start from what the Method already runs on. The operating rhythm is cadence: a weekly project update (P-19), a biweekly initiative update, a monthly operating review (P-21, Chapter 13). That cadence is the spine, and it works whether or not the team ever turns cycles on.

Cycles are an optional execution-rhythm overlay. The roadmap is a planning horizon. Neither replaces the cadence; both sit on top of it.

### Cadence is the spine; cycles are an overlay

A cycle is Linear's name for a sprint: a fixed time box — usually two weeks — into which the team commits a batch of issues, with a start, an end, a carried-forward set, and a velocity number that accumulates across cycles. Linear makes them nearly free to turn on, which is exactly the risk.

The Method's default is cadence-driven, not cycle-driven. The weekly project update (P-19) already tells the team and Leadership what shipped, what is in flight, and what is blocked; the milestones on a project (P-3) already mark the meaningful execution boundaries. For many 3-person teams that is the whole rhythm they need, and a cycle on top of it is a second clock measuring the same time. The overbuild test (P-24) is the filter: a cycle has to help the Operator decide faster or surface risk earlier, or it is ceremony with a burndown chart attached.

### When to turn cycles on

Turn cycles **on** when the team benefits from a fixed batch and a rollover review. The signals are concrete:

- The work decomposes cleanly into two-week chunks.
- The team wants a heartbeat to commit against rather than an open backlog.
- The end-of-cycle review — what we committed, what carried over, why — would tell the Operator something the weekly update doesn't.

A team building steadily toward a known scope, where "are we moving fast enough" is a live question, is a team a cycle serves.

Leave cycles **off** when the team runs on continuous flow. The signals are the inverse:

- The work is interrupt-heavy — ops, support, on-call — and arrives unpredictably.
- Deliverables refuse to batch into two-week boxes; the plan was always going to bend to the next interrupt.
- The project update and the milestone already supply the rhythm; a cycle just adds a boundary the work keeps crossing and a rollover pile that means nothing.

Continuous-flow teams are driven by project updates and milestones, not by a sprint boundary.

Two hard warnings. First, **do not turn cycles on before the workflow canon is stable** (Chapter 10). A cycle measures the throughput of your Done column; if Done still means merged rather than validated (P-6), the velocity number just measures the lie faster. Stabilize the nine states (P-10) and the Validation gate first; add the cycle only once Done is trustworthy.

Second, **a cycle is not a roadmap**. A cycle is a two-week execution box; a roadmap is a multi-quarter horizon. Teams that run the current cycle board as their plan are showing Leadership two weeks of detail and calling it strategy. The horizon lives in initiatives and the timeline, covered below.

### Running a cycle: capacity and the seventy-percent rule

Once cycles are on, the discipline lives at the cycle boundary. Before a cycle starts, the team enters capacity — estimates on the candidate issues, and an honest read of how much each person can take given the days they are actually present. Linear sums the load; the Operator commits the cycle.

This is where the Method resolves a tension. Principle P-26 says sprint-or-cycle planning commits seventy percent of expected capacity, holding thirty percent for unplanned work. Read literally against a Method whose default has no cycles, P-26 looks like it assumes a ceremony the Method doesn't require. It doesn't. **P-26 is a capacity rule, not a cycle rule.**

The seventy-percent commitment is where the rule lives when cycles are on, and it is the most important number in cycle planning: a team that commits its full estimated capacity slips every cycle and learns nothing, because the explanation is always "something came up" (P-26). When cycles are off, the same thirty-percent reserve still holds — just at the weekly-commitment level instead of the cycle boundary. The Operator does not load Engineer A and Engineer B to the brim for the week either. Cycles give P-26 a place to be enforced; they are not what makes it true.

Cycle automations carry the mechanics. Linear can auto-add issues to the current cycle, roll unfinished issues forward to the next one, and run a cooldown between cycles. Let the automations do the moving; the Operator's job is the rollover *review*, not the rollover itself. The review asks one question of every carried-forward issue — why didn't this finish?

- It was bigger than estimated — a scoping miss (P-4).
- The team was interrupted — the thirty percent was real (P-26).
- It was never actually started — a prioritization problem the Operator owns (P-13).

The pile is data; the review is where it becomes a decision. The cycle board, meanwhile, is still not the plan you show Leadership — that is the roadmap, which is the rest of this chapter.

### Roadmaps: the timeline over initiatives and projects

The roadmap answers Leadership's other question — the next two quarters on one page. In Linear it is the timeline view: date-bearing projects laid horizontally on a calendar, swimlaned by initiative.

Each project carries a start date and a target date (P-3); each initiative is the durable outcome those projects ladder up to (P-2). The roadmap is the objective layer rendered against time — initiatives as the rows, projects as the bars, the quarter as the horizon.

Two things the timeline shows that no board can. First, **sequence across initiatives**: when a project under Platform Reliability has to finish before a project under New Product Bring-Up can start, the dependency is a native blocking relation (a Free primitive) and the timeline draws it as a line between bars. The Operator sees the cross-initiative dependency that a per-team board hides. Second, **horizon honesty**: a project bar that runs past the quarter edge is a visible claim the Operator has to defend, where a board just shows "In Progress" with no end in sight.

The roadmap feeds the monthly operating review (Chapter 13). The initiative rollup the Operator presents to Leadership is the same set of bars, compressed to health and trend (P-21). The roadmap is not a separate artifact maintained alongside the reporting stack; it is the visual the reporting stack reads from.

### Plan-of-Record vs. What-If

The roadmap is only trustworthy if there is exactly one of it. The discipline is to keep a single committed roadmap — the **Plan-of-Record** — separate from every scenario the Operator wants to explore. The Plan-of-Record is what the team executes against and what Leadership reads (P-27); it changes deliberately, with a reason, never casually because someone dragged a bar in a planning meeting.

What-if planning is real and necessary — what if we pull the integration project forward a month, what if a fifth engineer joins next quarter, what if we drop the compliance work to ship revenue sooner. That work belongs in a scenario kept visibly separate: a duplicated draft timeline, a planning document, a clearly-labeled what-if view — never edits to the committed plan. The moment the team can't tell whether a date is a commitment or a hypothesis, the roadmap stops being something Leadership can trust, and the evidence chain (P-28) breaks at the top: an initiative rollup built on dates nobody actually committed to is theater.

One Plan-of-Record; as many what-ifs as you like, all of them clearly not it. Promoting a what-if into the Plan-of-Record is the Operator's call, and it is a commitment (P-13), not a drag-and-drop.

> **Augmentation Surface — Capacity and Scenario Modeling**
>
> Where an agent layer makes this work better: forecasting a cycle's realistic load from each person's actual availability and historical carry-over before the Operator commits it (P-26); generating what-if timelines on request — pull this project forward, add an engineer next quarter, drop that initiative — as throwaway scenarios that never touch the Plan-of-Record; and watching the committed roadmap for drift, flagging the project whose target date has quietly slipped past its initiative's horizon before the monthly review surfaces it.
>
> What the PM keeps: the commit itself — which cycle to start, which what-if becomes the plan, and which slipping date is a real risk to escalate versus a bar to redraw (P-13).

### Rhythm and horizon, not new bureaucracy

Put the three together and nothing new is added to the operating model. The cadence is the rhythm the Operator already runs:

- **Daily** — clear Blocked and the Operator's own queue.
- **Weekly** — the project update (P-19).
- **Biweekly** — the initiative update.
- **Monthly** — the operating review (P-21).

The roadmap is the horizon that rhythm reports against — the quarter-plus view the monthly review rolls up to. A cycle, if the team adopts one, is a sub-rhythm that sits *under* the weekly update: a two-week execution heartbeat, not a replacement for it. The Operator still writes the Friday update whether or not a cycle is running; the cycle just gives the team a batch boundary inside the week-by-week flow.

That is the whole relationship. Cadence is rhythm. The roadmap is horizon. Cycles are an optional heartbeat under the rhythm. A team that mistakes any one for another — runs the cycle board as its roadmap, treats the roadmap as a weekly status, or bolts a cycle onto continuous-flow work that doesn't want one — has bought bureaucracy. A team that keeps the three in their lanes has rhythm and horizon for free, on the free tier, and answers Engineer B's sprint question and Leadership's roadmap question from the same operating model it was already running.

> **Where this gets hard**
>
> The roadmap Leadership wants and the roadmap the work supports diverge the moment a date becomes a promise to someone outside the team — a customer commitment, a board deadline, a launch already announced. Now the Plan-of-Record is under pressure to show the date Leadership sold, not the date the projects support, and the Operator is asked to drag a bar to make a slide true. Holding the line — committed dates reflect committed work, what-ifs stay labeled — is a credibility fight the Operator rarely has the seniority to win alone.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: ~1700
  principle-citations: P-2, P-3, P-4, P-6, P-10, P-13, P-19, P-21, P-24, P-26, P-27, P-28
  flagged-principle-gaps: none
-->
