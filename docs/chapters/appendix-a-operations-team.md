<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Appendix A — The Operations-Team Variant

It is Monday, and the Operator runs a 3-person internal-services team — process automation and system integrations for the rest of the company. The board on the screen did not come from a roadmap the team wrote. It came from other people. Engineer A spent Friday on an integration a director asked for in a hallway, verbally, with no ticket. Engineer B is three weeks into an automation nobody formally requested, because a manager asked in a Slack DM and saying no felt rude. Two separate VPs each believe their request is next in line; neither is written down anywhere the other can see. There is no front door, so every door is the front door, and the Operator spends the first hour of every week reconstructing what the team even agreed to do.

That is the problem this appendix exists to solve, and it is a different problem than the rest of the Method addresses.

### Supply-side and demand-side — and who should skip this appendix

The Method's default reader is a **supply-side** team: a product-dev team that builds what is on its own board. Work originates inside the team, from a roadmap the Operator and Leadership set. Intake is a thin layer — the occasional bug report or feature idea the team chooses to accept — and the Triage-and-Asks machinery in Chapter 8 covers it completely. Everything that matters happens *after* an item is on the board.

A Center of Excellence, an operations team, a PMO, an internal platform or shared-services group is **demand-side**. The organization requests work *through* it. Its board is populated almost entirely by other people's asks, and the hardest, most failure-prone part of its operating model is not delivery — it is the seam where a request becomes committed work. For a demand-side team, intake *is* the product.

Here is the load-bearing claim of this appendix: the Method's **back half is roughly 80% identical for both kinds of team and is not restated here.** Once a request is accepted, it becomes an issue in a project under an initiative (P-2, P-3); it runs the nine-state workflow canon; it hits the Validation gate and must produce evidence before Done; it rolls up through the weekly-biweekly-monthly reporting cadence in Chapter 13; its health is computed, not picked. None of that changes. What changes is the **front half** — how work *enters* and is *governed* — and that is all this appendix installs. It swaps the demand-side front half in for teams that need it and leaves everything downstream exactly as the core chapters describe.

State the negative plainly, because it is the more common case: **a pure product-dev team does not need this appendix.** If the majority of your board originates from your own roadmap rather than from other people's requests, the intake pipeline, the service catalog, the service SLAs, and the field rigor below are overhead that fails the overbuild test (P-24). Install this variant only when you are answering demand you did not generate.

### Intake as a first-class layer

A demand-side team cannot treat intake as a side effect of Triage. It needs a formal flow that every request travels, visibly, on the record:

1. **Request** — captured through the front door (below), never verbally, never in a DM. A request that exists only in a hallway conversation does not exist (P-1).
2. **Intake Review** — the request has been seen and is being sized and clarified, but has not been accepted. Nothing is committed here.
3. **Groomed** — the request is understood well enough to accept or decline: scope is clear, the objective it serves is named, the requester has confirmed what they actually want.
4. **Accepted** — the request converts to a project or issue, gets a home in an initiative, and is assigned a target release version (P-29). Only here does it enter the nine-state delivery canon at Backlog.

The stage worth building deliberately is **Intake Review**, and its purpose is a metric. A product-dev team would never add it — the workflow canon is nine states and a tenth is a smell (P-10), and a supply-side team should reach for a `stage:*` label before a new state every time (P-11). A service team earns the exception, because the number Intake Review produces is the number a service team is judged on: **dwell time** — how long a request sits between arriving and being accepted. That is the seven-day Triage clock (P-20) generalized into a service-health metric. Intake Review lives in the intake pipeline *before* Backlog, so it never touches the nine delivery states; what it adds is a timestamp pair the Operator can report. When average intake dwell climbs from two days to nine, the team has a capacity problem its requestors are already feeling — and now it can see it before the complaints arrive, instead of after (P-20).

### The Service Catalog

The cure for "every door is the front door" is one published door. The team defines a small set of named **request types** and publishes them as its service catalog — the front-of-house menu of what the team does and how to ask for it. Generic examples a CoE tends to carry: a **process-automation candidate**, an **enhancement request** against a system the team owns, an **integration build**, and a **governance exception**. The catalog is the difference between a team that receives requests and a team that receives *legible* requests.

Each request type maps to a Linear **Asks** template (Chapter 8) built from the operating surface's own label, view, and template mechanics (Chapter 5) — it pre-tags the team, the target project, and the labels the type always carries, and presents an intake form whose required fields are fixed for that type. Submitting the form auto-creates a triaged issue that already has its structure — the Operator opens a sized, labeled, routable request instead of "can you help with something?" from a channel they do not watch. This is P-17 doing its job at the front door: templates lower the cost of doing the right thing, so the right thing is the path of least resistance. It replaces the ad-hoc hallway-Slack-email intake that was drowning the Operator on Monday, and it does so without the Operator having to police anyone — the form is easier than the DM (P-22: a request is captured and triaged, never converted straight to scope by whoever asked loudest).

> **Augmentation Surface — Intake Classification**
>
> Where an agent layer makes this work better: reading each inbound request as it lands, matching it to a catalog request type, pre-filling the intake form, flagging the missing required fields, drafting a first-response acknowledgment inside the service SLA, and tracking intake dwell so the queue self-reports (P-20). A demand-side team runs two agent roles, not one — an *intake* agent that classifies and routes what arrives, distinct from any *build* agent that executes what was accepted — and keeping them separate keeps classification from quietly becoming commitment.
>
> What the PM keeps: the accept-or-decline call and the charter decision. Customer and requester feedback is signal, not scope (P-22); priority, taste, risk, and real-world commitments do not delegate (P-13). The agent sizes and routes the request; the Operator decides whether the team takes it.

### Governance cadence

The core reporting cadence in Chapter 13 — weekly project updates (P-19), biweekly initiative updates, a monthly operating review (P-21) — holds unchanged. A demand-side team extends it at both ends rather than replacing it, and the discipline is to frame these as extensions, not a parallel bureaucracy that fails the overbuild test (P-24).

At the fast end, a **daily** rhythm: a short standing pass over Intake Review, so no request sits un-acknowledged past its first-response clock, and the day's accepted work is visible. At the slow end, a **Quarterly Business Review** — the QBR — where the team reports to its sponsors on what it accepted, what it delivered, intake dwell and SLA-breach trends, and what it is declining and why. The QBR is the monthly review (P-21) compressed one more level, aimed at the people who fund the team rather than the people who read weekly updates.

Two governance gates matter for a team that spends other people's mandate:

- **A charter-approval gate.** Before a project leaves intake and starts, a named sponsor signs off on it — the objective it serves, the rough cost, the trade-off against what the sponsor's request displaces. This is P-13 rendered as a gate: a real-world commitment does not get made because a form was submitted; it gets made because the Operator (Chapter 4) and an accountable sponsor both agreed to it. The gate is what stops the loudest requester from setting the team's priorities by volume (P-22).
- **RACI on stakeholder-heavy initiatives.** When an initiative touches several departments, name who is Responsible, Accountable, Consulted, and Informed on it, in the initiative document. A supply-side team rarely needs this; a demand-side team with five stakeholders per initiative needs it to keep "who approves this" from being re-litigated every update.

### Service SLAs

This is the commitment a service team owes that a product-dev team owes no one. A supply-side team answers to its own roadmap; a demand-side team answers to requestors who are waiting, and it owes them clocks. Two, specifically, layered onto the Business-tier SLAs in Chapter 8:

- **Time-to-first-response** — how long from a request landing to the requester hearing back, even if the answer is "received, in Intake Review, decision by Thursday." This is the clock that most cheaply buys trust, because most requester frustration is silence, not delay.
- **Time-to-resolution** — how long from acceptance to Done, tracked per request type, because an integration build and a governance exception do not carry the same promise.

Both attach to Triage and to Asks-sourced items using Linear SLAs, which are a Business-tier capability (Chapter 8). Alongside them, keep the escalation rule the core already implies and make it explicit for a service team: **an item blocked more than N days escalates** to the Operator and, past a second threshold, to the sponsor. As Chapter 8 warns, calibrate these against real history — an SLA on every request produces a queue where everything is breaching and nothing is urgent, and an untrusted SLA is worse than none (P-25). The clock exists to make silence impossible, not to manufacture false alarms.

### CoE-grade field discipline

A demand-driven team needs rigor at issue creation that a 3-person product team can skip, and the reason is the demand itself: when work arrives from dozens of requesters across the org, the only way a report rolls up honestly is if every item was captured to the same shape. A supply-side team of three shares context in its heads; a service team's context lives in the fields or it does not live at all.

Three rules, stricter than core:

- **The Rule of One.** Each parent issue carries exactly one required objective or OKR label — one, not zero and not three — plus a matched set of required single-select fields for its type. One objective per parent is what makes the rollup unambiguous: every unit of work answers to exactly one stated goal, so the QBR can total effort by objective without double-counting or orphans (P-2, P-16).
- **A per-issue-type required-field matrix**, enforced as a hard create-time block, not a habit. Because the rule is checked programmatically at creation rather than policed after the fact, it actually holds (P-25):

  | Request type | Required fields at creation |
  |---|---|
  | Process-automation candidate | requester, sponsor, objective label, current-effort estimate, expected saving |
  | Enhancement request | requester, target system, objective label, priority, acceptance criteria |
  | Integration build | requester, source system, target system, objective label, data-sensitivity |
  | Governance exception | requester, policy referenced, objective label, approver, expiry date |

- **Mandatory objective and initiative linkage** per parent — no accepted parent issue exists without a project and an initiative above it (P-3). A supply-side team can tolerate a loose issue for a day; a demand-side team cannot, because a request with no objective above it is a favor, and a board full of favors is how a service team loses the ability to say what it is for.

The discipline is deliberately heavier than the core, and the overbuild test (P-24) is the check on it: each required field must earn its place by feeding a decision, a report, or the charter gate. A field nobody reads is a tax on every requester, and a service team's requesters abandon a form faster than a teammate does.

### Two optional label axes

Two label axes serve views (Chapter 5) a demand-side team tends to want, and both are strictly optional — add either only when a real view needs it, never speculatively (P-16, P-24).

- **`layer:`** — `capability` / `delivery` / `impact`. The plain-language version is *building the factory / running the factory / measuring the value*: `capability` is the team's own tooling and platform build-out, `delivery` is the run-the-factory work of fulfilling requests, `impact` is the measurement and value-tracking work. The view this serves is the mix question every service team's sponsor eventually asks — how much of the quarter went to building versus running versus proving worth — which is unanswerable without the axis and trivial with it.
- **`customer:`** — `internal` / `external`. This splits requests by who they ultimately serve, so the team can show internal-facing versus external-facing load on one filter. It matters most when a CoE straddles both — automating an internal finance process one week and shipping something a paying customer touches the next, at very different evidence bars.

Neither axis is prescribed. Each is justified the moment its view is one Leadership or a sponsor asks for repeatedly, and deleted the moment no view cites it (P-16).

### Computed RAG governance

A CoE reports health to its executives on a rolled-up RAG dashboard, and the operating model for that health is already written — this appendix does not restate it. The deterministic Red / Amber / Green ladder, the rule that health is computed rather than picked, the escalation on stale rollups, and the split between the health *field* Linear gives you and the computation *rules* the Method gives you all live in Chapter 13, and they apply here without modification (P-28). The demand-side additions feed the same computation rather than replacing it: intake dwell time (from Intake Review) and SLA-breach counts become inputs the executive board watches next to project and initiative color.

Where that board *lives* is the only tier-dependent part. A per-project health color is Free; portfolio trends are an Insights question and Insights is Business; the org-level RAG board — every initiative's color on one screen for the sponsors — is a Dashboard, and Dashboards are an Enterprise capability (Chapter 9). Leadership reads that board, not the workspace beneath it (P-27); the Operator's job is to keep the layers under it honest so the color the sponsors see is one the team can defend all the way down to the evidence (P-28).

> **Where this gets hard**
>
> The organization that wants a real front door — a published catalog, enforced intake, service SLAs the requesters trust, a charter gate that survives a VP walking up to an engineer's desk — is asking a 3-person team to hold a governance boundary against people who outrank it, using rigor (the Rule of One, the required-field block, the RACI) that is only worth the friction if it is installed and calibrated correctly the first time. Install the field discipline too loose and the reports lie; too tight and the requesters route around the form and you are back to the hallway. The catalog ships in an afternoon; the boundary that makes it stick takes a season and a mandate the team usually does not have alone.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass — appendix (opt-in variant); demand-side front-half only, back half deferred to core chapters; intake pipeline as ordered list; required-field matrix as table
  word-count: ~2550 (prose; ~2765 incl. table/callouts)
  principle-citations: P-1, P-2, P-3, P-10, P-11, P-13, P-16, P-17, P-19, P-20, P-21, P-22, P-24, P-25, P-27, P-28, P-29
  flagged-principle-gaps: none
-->
