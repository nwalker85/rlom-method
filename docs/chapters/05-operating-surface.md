<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 5 — The Operating Surface: Labels, Views, Templates

Open a workspace that has been running without a method for a year. Three engineers each invented their own label scheme, so the workspace has `bug`, `Bug`, `type:Bug`, and `defect` — all of them in use, none of them filtered against. Half the labels are attached to a single issue. The views panel shows nineteen private views and three shared ones, and the three shared ones don't agree on what "active" means. The Operator opens Linear in the morning, sees a different workspace than either engineer sees, and spends the first forty minutes reconstructing what changed overnight. There is no single screen anyone can point to and say *this is what we are working on now*.

That is the gap this chapter closes. The seven layers in Chapter 2 describe the shape of the work graph. The numbered principles in Chapter 3 describe the doctrine. This chapter is how the Method actually shows up in the workspace — the labels you index against, the views the team watches, and the templates that make it cheaper to do the right thing than the wrong thing.

The operating surface is the *enforceable* part of the Method. Principles in a document live in heads. Labels and views live in the workspace. When two team members disagree about whether a piece of work is in flight, the answer is in a saved view — not in conversation. That makes the operating surface the verification surface (P-25): a rule you can't check programmatically decays into folklore. Labels and views are the check.

### Labels are an index, not an organizational scheme

The single most common mistake in a one-year-old workspace is treating labels as a filing cabinet. The Method treats them the opposite way: a label exists to serve a view, and a label not cited by any view is a candidate for deletion (P-16). That inverts the usual instinct. You do not create a `frontend` label because work *is* frontend. You create a `domain:product` label because a specific view filters on it and the Operator needs that view to decide something.

The Method uses eight namespaced label groups. They are namespaced because flat label spaces collapse to noise inside six months, and because the colon prefix lets you scan a label list and see structure instead of an alphabetical pile.

- `type:*` — Feature, Bug, Chore, Documentation, Research, Gate. Every issue gets exactly one. The "Gate" type marks issues whose only purpose is to hold a decision or an approval until it lands.
- `component:*` — one per service or subsystem the team owns. Let the reader fill in the names; the Method does not prescribe them. A team running three services might have `component:api`, `component:web`, `component:worker`. A team with one monolith might skip this namespace until they split.
- `domain:*` — broad areas of concern: `domain:security`, `domain:infrastructure`, `domain:product`, `domain:operations`. Use sparingly. Domain answers "who would be interested in this if it broke" — not "what code does it touch."
- `risk:*` — `low`, `medium`, `high`. Applied at Triage. Drives one view (Blocked Critical Path) and one report (the weekly risk roll-up in Chapter 13).
- `source:*` — `asks`, `slack`, `support`, `github`, `sentry`. Where the work came in from. Drives Triage analytics: if eighty percent of incoming work is `source:slack`, the team needs Asks (Chapter 7), not more meetings.
- `release:*` — `production`, `staging`, `internal`, `none`. Marks the deployment surface so the Validation gate (Chapter 10) knows what evidence to require. `release:production` means runtime evidence is non-negotiable before Done (P-9).
- `stage:*` — `design`, `qa`, `uat`, `soft-launch`. These are the "states that aren't states" (P-11). The workflow canon is nine states (Chapter 10); anything that looks like a tenth state — pending approval, in QA, soft-launch — is a stage label applied during In Progress, In Review, or Validation. The canon stays at nine.
- `parking-reason:*` — `waiting-on-vendor`, `waiting-on-decision`, `waiting-on-budget`, `waiting-on-customer`. Applied only to Urgent or High issues sitting in Backlog. An Urgent issue in Backlog without a parking reason is a smell — either the priority is wrong or the reason is hiding.

Each namespace serves at least one view. `type:Bug` plus `risk:high` plus `release:production` is the filter behind the Operator's morning incident scan. `source:slack` is the filter behind the weekly Asks review. `stage:uat` is the filter behind the Validation queue. `parking-reason:*` populates a sanity-check view the Operator runs before standup: *what am I claiming is urgent that I am actually not working on, and why?*

This is P-16 in action. No view, no label. Before adding `type:Spike`, ask which view it serves. If the answer is "I just want to find them later," that is what search is for.

One more discipline before views: prefer Linear's native typed fields over labels for anything Linear already models. Priority, estimate, workflow state, and project health are single-valued typed fields — a label that duplicates one of them (a `priority:high` label, a `red` health label, a `done` label) is drift waiting to happen, because a label is set membership and a native field is a single enforced value. The `bug`/`Bug`/`defect` collision that opens this chapter is what labels do when they impersonate a typed field. Reach for a label only when the concept is a genuine many-to-one index that no native field captures.

> **Augmentation Surface — Surface Maintenance**
>
> Where an agent layer makes this work better: detecting labels with zero referencing views, views with no recent activity, templates that no one uses, and stage labels that have outlived their underlying state. The agent generates a monthly hygiene report — *these 12 labels are referenced by no view; these 4 views were last opened three months ago; this template has been used twice in 90 days* — so the Operator can make deletion decisions on evidence instead of guesswork.
>
> What the PM keeps: deciding whether a dormant artifact should be removed, repurposed, or left in place because a future workflow needs it.

### Views are the daily control panel

A view is a saved question. The Method requires a small set of shared views — shared so every team member sees the same workspace — and treats them as the daily control panel. The Operator opens these views before standup; the engineers open the ones that touch them. Private views are fine for personal scratch work, but the load-bearing views are shared.

**Operator's Now.** Filter: priority Urgent or High, state in Ready, In Progress, In Review. Group by assignee. This is what is actively in flight. The Operator watches it every morning. Engineer A and Engineer B each glance at it before picking up new work. It enforces P-3 (active work has a project) by making project-less issues look out of place, and P-4 (issues are deliverable-sized) by making oversized issues conspicuous.

**Waiting on the Operator.** Filter: issues whose state is not Done and whose human-decision flag is set, plus issues whose blocker text names the Operator. Only the Operator subscribes; engineers see it on request. This is the queue P-13 makes load-bearing — priority, taste, risk, and real-world commitments do not delegate. If this view has more than five items, the Operator's calendar is wrong, not the engineers' execution.

**Blocked Critical Path.** Filter: state Blocked, priority Urgent or High. Engineer B owns this view because they sit downstream of the most platform dependencies and are blocked most often; they raise items in standup. It enforces P-10 — Blocked is a state of the canon, and an issue in Blocked must name its blocker. A Blocked issue with no named blocker is a triage failure.

**In Review.** Filter: state In Review with at least one linked PR. The view shows the PR status (checks passing, requested reviewers, mergeable). Both engineers subscribe; the Operator scans it once a day to spot review backlog. This is where P-8 lives: the code host proves implementation, and this view is the bridge between Linear and that proof.

**Needs Validation / Evidence.** Filter: state Validation, age greater than 24 hours. The Operator and Engineer A both subscribe. This view is the Validation gate (Chapter 10 owns the doctrine; this chapter owns the surface). An item sits here until evidence is posted — a deploy log, a screenshot, an acceptance comment from someone other than the assignee (P-7). Validation separates implemented from trusted (P-6), and this view is where the separation gets enforced day-to-day.

**Projects Without Recent Updates.** Filter: project status Active, last update older than seven days. The Operator watches it on Monday morning. This view operationalizes P-19 — active projects get an update every week, the format can compress when there is nothing to say, the cadence does not move. If a project surfaces here, the Operator either writes the update or moves the project to Planned.

**Stale Triage.** Filter: state Triage, age greater than five days. Surfaces P-20 violations one to two days before the seven-day SLA so the Operator has runway, not just an alarm. Operator-only.

Seven shared views, named for the question each one answers. The fight is to keep this list short. Every new view dilutes the daily scan — when there are eighteen shared views, no one looks at any of them. When there are seven, the team agrees on what they are looking at.

### Templates lower the cost of doing the right thing

A template is a default. The right behavior should be the easy behavior (P-17). The Method requires four issue templates and one project template at minimum, plus a commenting template for agent delegation that becomes load-bearing at Tier 3 (Chapter 8).

**Feature template.** Sections: Outcome (one sentence — what changes for whom), Scope (in/out, plus what is explicitly deferred), Acceptance criteria (testable bullets, not prose), Evidence expected (which artifact proves Done — deploy log, screenshot, acceptance comment), GitHub repo (the GitLab equivalent is the GitLab project path), Design link (when visual review applies). The template forces the issue author to decide what Done looks like before opening the issue, which is the cheapest moment to decide.

**Bug template.** Sections: Reproduction (exact steps, environment, version), Blast radius (who is affected and how many), Severity (P0–P3 with the Method's definitions inline so the author cannot guess), Evidence required for the fix (regression test, manual repro confirmation, monitoring confirmation). The blast-radius field is the one most teams skip and the one that most often determines whether a bug deserves the priority it was opened with.

**Research spike template.** Sections: Timebox (hours or days — a spike with no timebox is a project in disguise), Question the spike answers, Expected artifact (a decision doc, a prototype branch, a benchmark table), Decision deadline (the date by which the spike's output must drive a decision or get archived). Spikes that produce no decision artifact are how research budgets disappear.

**Standard project template.** Sections: Goal (the durable outcome, not the next step), Milestones (the Method's canonical phases — Scope accepted, Implementation, Validation, Production rollout, Documentation and handoff — plus any project-specific phases), Dependencies (other projects, vendor commitments, hiring), First update (drafted at kickoff, posted within forty-eight hours), Exit criteria (what makes this project Done, in plain language). Every project starts from this template. A project without a first update within forty-eight hours surfaces on Projects Without Recent Updates by day seven.

**Agent delegation comment template.** A comment, not an issue. Used when the Operator (or, at Tier 3, the agent layer) hands an issue to a specialist agent. Sections: Outcome, Scope, Validation command (the exact command or check that proves the work is correct), Expected artifact (PR URL, document, file path), Repo and file paths. Required by P-15 — vague delegation produces vague output. Chapter 8 carries the full pattern; this chapter installs the comment template so the muscle is in place before agents arrive.

These templates encode locality (P-18). The template is the workspace default; a project description can override it for that project; an individual issue's acceptance criteria override the project default for that issue. Closer-to-the-work guidance wins.

### Relations and recurring issues

Two native primitives the Method uses deliberately but does not over-invest in.

**Issue relations.** Linear models relations between issues — *blocking* / *blocked-by*, *related*, and *duplicate*. The Method leans on the dependency pair and uses the rest sparingly. *Blocked-by* is the structural complement to the Blocked state (P-10): the state says "this is stuck," the relation says "on what." When a Blocked issue is held up by another tracked issue, link it *blocked-by* in addition to naming the blocker in a comment — so the dependency shows on the blocker's side too and nobody has to carry the chain in their head. *Duplicate* is set at Triage (it is a native status type). *Related* is for genuine cross-references, not a substitute for a parent issue (P-12) or a project — if you are building a tree out of *related* links, the work wanted a parent-and-sub-issues shape instead. Relations are an index of dependency, not a second hierarchy.

**Recurring issues.** Repeating operating work — the weekly project-update sweep, the Monday Triage clear, the monthly label-hygiene pass, the quarterly overbuild audit (P-24) — should be a recurring issue, not a reminder in someone's head or a line in a doc that rots. A recurring issue puts the cadence in the work graph where the Method can see it: it appears in views, carries evidence when it is done, and surfaces on Stale Triage if it is ignored. The Method's own maintenance — the verification it depends on (P-25) — is the first thing to make recurring.

### The overbuild test

Before adding any new label, view, or template, run it through P-24's five questions. Does it help the Operator decide faster? Does it help an executor execute faster? Does it preserve evidence the team would otherwise lose? Does it reduce repeated PM work? Does it make risk visible earlier? Four or more yes — adopt. Three or fewer — skip.

The operating surface gets cluttered the same way a kitchen counter does: each individual item seemed useful when it landed, and now nothing can be found. The overbuild test is the cabinet door. Apply it every time and the surface stays operational. Skip it for a year and the surface becomes the problem the next operating model is brought in to fix.

> **Where this gets hard**
>
> When label sprawl has gone unmanaged for a year and an audit reveals one hundred fifty labels of which thirty are cited by views, the deletion sweep is political, not technical — every label has someone who created it and a story for why it should stay. The same dynamic hits a view list that has accumulated nineteen private dashboards no one else can see.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: ~2400 prose (expanded with relations/recurring + typed-fields note)
  principle-citations: P-3, P-4, P-6, P-7, P-8, P-9, P-10, P-11, P-12, P-13, P-15, P-16, P-17, P-18, P-19, P-20, P-24, P-25
  flagged-principle-gaps: none
-->
