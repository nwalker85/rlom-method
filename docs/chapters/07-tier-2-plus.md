<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 7 — Tier 2: Linear Plus Upgrade

It is week seven. The Tier 1 install from Chapter 6 has held. The Operator has four active projects, a clean Triage queue most mornings, weekly updates that nobody has had to chase, and a GitHub link on roughly every issue that should have one. The two engineers know which view to open after standup. The system is real.

Then Monday arrives and Leadership asks, in a meeting that was not on the calendar, "What does the OKR rollup look like this quarter?"

The Operator pulls up Linear. There are four project pages, four sets of milestones, four colored health dots. There is no layer above them. There is no single sentence that says what the team is working toward — only four sentences that say what the team is working on. The Operator improvises a slide that night and decides on the train home that the Tier 1 install has outgrown itself.

This is what Tier 2 is for.

### What Plus is, and what it isn't

Linear Plus adds three things the Method asks for and one thing it merely tolerates. It adds the **objective layer** — initiatives, the durable container that sits above projects and answers "what are we working toward?" without forcing the reader to scan a list of in-flight work (P-2). It adds the **feedback-intake layer** — Customer Requests, the surface where voice-of-customer lands with attribution and impact data before it competes for engineering attention (P-22). And it adds the **trend layer** — Insights on shared views, which turns the Operator's spreadsheet wrangling into a panel that updates itself.

What Plus does not add: intelligent triage routing, structured Asks intake from Slack and email, SLA clocks on urgent production work, and the agent surfaces that make a team of three feel like a team of six. Those are Business-tier capabilities and belong to Chapter 8. The temptation when upgrading is to upgrade once, to the top. Resist it. A team that adopts initiatives, Customer Requests, and Insights well will get more out of the next four weeks than a team that adopts ten new surfaces and lands none of them. The overbuild test from Chapter 5 still applies (P-24).

The fourth thing Plus adds — richer project documents — is plumbing rather than doctrine. Use it where it lowers the cost of the right behavior. Don't let it become a wiki.

### Initiatives — the objective layer

An initiative in Linear is a manually curated rollup of projects with an owner, a status, a target date, an overview document, and an update cadence of its own. It is the artifact the Operator points at when Leadership asks the OKR question. It is the layer the monthly review compresses (P-21, P-27). Without it, every conversation about strategy has to be reconstructed from four to eight project pages every time.

For the 3-person team, the install is small and concrete. The Operator creates two initiatives — **Platform Reliability** and **Operator Experience** — and wires the four active projects into them. Two projects (CI/CD Backbone, Production Stability) roll up to Platform Reliability. Two projects (Internal Tooling Integration, the Operator's own dashboard cleanup) roll up to Operator Experience. Each initiative gets an owner (the Operator, for now), a status (Active), a target date at quarter-end, and a one-paragraph summary that names the outcome — not the work, the outcome.

Three rules govern initiatives in the Method:

- **Few and durable.** A 3-person team should rarely run more than three initiatives at a time. Initiatives that change every cycle are projects in disguise.
- **Initiatives do not have issues.** Issues belong to projects; projects belong to initiatives (P-2, P-3). When an issue feels like it belongs directly to an initiative, the project layer is missing.
- **The owner posts updates on the initiative cadence, not the project cadence.** Project updates are weekly (P-19); initiative updates are biweekly (P-21). Don't conflate them.

> **Augmentation Surface — Initiative Drafting**
>
> Where an agent layer makes this work better: drafting the biweekly initiative update from the underlying project updates, surfacing which key results have moved since the last cycle and which have stalled, and naming the decision the Operator needs to make this cycle so it lands in front of Leadership rather than getting buried in narrative.
>
> What the PM keeps: the actual health call (green, yellow, red) and the narrative paragraph that frames the cycle for Leadership.

### Customer Requests — the feedback-intake layer

Customer Requests in Linear are a structured surface for capturing voice-of-customer feedback with requester attribution, customer attributes, and impact data. They link to issues and projects but do not become issues automatically. They are the answer to the question the Operator has been answering badly in Slack threads and inbox screenshots since week three: "We heard X from a customer — where does that live?"

The Method's posture on Customer Requests is strict: a request does not become scope (P-22). It becomes a captured artifact that the Operator triages on the daily pass. Conversion into an issue or a project is a deliberate decision. The Operator's first install is small. The team has one public-facing surface — the assistant demo from the Tier 1 install, now visible to a handful of beta customers — and the Operator turns on Customer Requests for that surface only. A web form on the demo page captures feedback. An Intercom or email channel, if the team has one, feeds the same queue. Important requests get the impact flag; the rest sit until Triage.

Engineer A, who built the demo, links their first PR to a Customer Request the following Wednesday. The PR fixes a bug a beta user reported on Monday. The request stays open, attached to the resolved issue, with the requester's context preserved. When Leadership asks two weeks later whether the beta is going well, the Operator can answer with counts and verbatim quotes pulled from a real surface — not from memory.

### Insights — the trend layer

Insights on shared views are how the Operator stops reconstructing the same chart every Friday. A view is a filter. An Insight is that filter over time, or sliced by a property, with a measure attached. Issue count by status over the last 30 days. Cycle time by project. Throughput per engineer. Triage time by source. Once an Insight is pinned to a view, it updates itself.

The Operator's first install is two Insights, both pinned to the Operator's Now view:

1. **Open issue count by status, last 30 days.** Shows the shape of work in flight — whether Triage is climbing, whether Validation is backing up, whether In Review is becoming a parking lot.
2. **Cycle time by project, last 60 days.** Shows whether the team is getting faster or slower at the same shape of work, project by project.

These two replace what the Operator was doing manually for the Friday summary. Leadership reads the Friday summary; they do not browse the workspace (P-27). The Insights live for the Operator's own decisions, and a screenshot of one lands in the Friday note when it is moving in a direction that needs explanation. Avoid reporting theater: an Insight that never changes the Operator's plan is a candidate for deletion.

### Richer project documents — the long-form bridge

On Plus, project descriptions get a companion: project documents, with embedded media, longer narratives, and collaborative editing. The temptation is to treat them as a wiki. Don't. Documentation owns deep context (P-5), and deep context lives in the team's documentation system — a wiki, a `docs/` directory in the relevant repo, an ADR folder. Project documents are the bridge between issue-sized content (a paragraph, an acceptance criteria list) and wiki-sized content (an architecture decision record, a multi-page runbook).

Two uses pay for the upgrade:

- **Project briefs.** A 300-to-800-word document attached to the project that names the outcome, the non-goals, the rough plan, the risks, and the open questions. Written once at project kickoff. Linked from the project description, never copied into it.
- **Post-launch retrospectives.** A document attached to the project after the launch milestone closes, naming what shipped, what slipped, what surprised, and what the team would do differently. Written once at project close. Feeds the next project's brief.

Neither replaces real documentation. Both replace the Slack thread the Operator was using to remember why a decision got made.

### The first initiative update Leadership actually reads

The point of all four upgrades is that something different lands in Leadership's inbox on Monday morning. Two weeks into the Plus install, the Operator posts the first initiative update on **Platform Reliability**. It is short. It is structured. It is the same shape every cycle, so Leadership learns to read it fast.

```text
Initiative: Platform Reliability
Cycle: 2 weeks ending YYYY-MM-DD
Health: Yellow (was Green)

Key results
  KR1 — p95 deploy latency under 10 minutes: 12m → 9m. On track.
  KR2 — zero unplanned production rollbacks per cycle: 1 rollback this cycle. At risk.
  KR3 — release pipeline coverage across active services: 3 of 4 services. On track.

Narrative
  The single rollback this cycle came from a config drift between staging and
  production that our current release pipeline does not catch. CI/CD Backbone
  picks up the gap next cycle; Production Stability owns the rollback runbook.
  Health is yellow until KR2 trends back to zero for two consecutive cycles.

Decision needed from Leadership
  None this cycle. Flag if KR2 is still red in two weeks.
```

Five lines of structure, one paragraph of narrative, one line that names what the Operator needs from Leadership — or names that nothing is needed. Leadership reads it Monday. The evidence chain holds: initiative health rolls up from project updates, project updates roll up from issue evidence, issue evidence rolls up from the code host (P-28). Break any link and the update collapses into theater.

### Ceiling signal — how to know Tier 2 is no longer enough

Tier 2 buys the team roughly two to four months of headroom over Tier 1. The signals that headroom is exhausted are concrete. When two of the following three land in the same quarter, plan the move to Chapter 8:

- **Intake volume outgrows the Operator's daily Triage pass.** Items routinely sit past the seven-day SLA (P-20). The Operator notices the "Stale Triage" view has more than a handful of items most mornings. Engineer B subscribes to the same view because the Operator has started missing things. Triage Intelligence (Business) starts paying for itself the day the Operator's daily pass takes longer than thirty minutes.
- **The team starts owning production work that needs SLA tracking.** Urgent bugs that need a clock, not a priority. Human decisions that need a deadline, not a label. The Operator finds themselves writing "respond by Thursday" in issue descriptions because Linear's due dates don't reflect urgency tiers. SLAs (Business) are the structured answer.
- **The Operator wants to install intake from channels they don't currently monitor in real-time.** Slack threads. Email aliases. Form submissions from non-customer-facing surfaces. The Operator wants the structure of Customer Requests for internal asks, and Customer Requests is the wrong tool. Linear Asks (Business) is the right one.

Two of three in one quarter is the threshold. One of three is normal Tier 2 operation — work around it. Three of three is overdue.

> **Where this gets hard**
>
> Tier 2 holds until Leadership's reporting taste diverges sharply from what Linear's initiative updates produce — they want pillar dashboards, KR scorecards, or quarterly business reviews that don't map cleanly to Linear's primitives, and the Operator finds themselves rebuilding the same numbers in a slide deck every cycle. At that point the question is no longer which tier of Linear to buy; it is which reporting layer sits on top of Linear and who owns it.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: 2059
  principle-citations: P-2, P-3, P-5, P-19, P-20, P-21, P-22, P-24, P-27, P-28
  flagged-principle-gaps: none
-->
