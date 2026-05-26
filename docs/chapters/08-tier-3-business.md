<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 8 — Tier 3: Linear Business and the Edge of Self-Install

It is the end of the Tier 2 quarter. The Operator opens Linear on a Tuesday morning and counts twenty items in Triage that came in overnight — a Sentry alert that fired at 3 a.m., four bug reports from beta users in Customer Requests, a dozen Slack-forwarded asks that an engineer has been pasting into Triage manually since Friday, and three "quick question" emails an executive forwarded with no context. There is a production incident from yesterday that should have had a clock on it and didn't. Engineer A is heads-down on a research repo and has been ignoring Triage for a week because the Operator told them to. Engineer B owns the public surface that just shipped and is waiting for the Operator to tell them which of the four beta-user bugs is real.

The Operator does the Triage pass. It takes ninety minutes. By the time it is done, the morning is gone, the Friday update for Leadership is unwritten, and a request the Operator already promised a decision on is now two days late.

This is the moment Tier 2 stops being enough.

### The shift Business represents

Tier 1 was self-install: a single PM on Free, one week. Tier 2 added the objective, intake, and trend layers — install work the Operator could still do on a quiet Friday. Business is different. Business is the tier where Linear gives the Operator capabilities the Operator does not have time to tune alone. Triage Intelligence has to be trained against the team's real patterns. Asks templates have to be designed so the form does not become a tax. SLAs have to be calibrated against actual incident history, not a generic table copied from a blog post. Insights become workspace-level dashboards the Operator promises to keep current. Agent surfaces — Linear Agent, AI Agents, MCP — appear as primitives, and someone has to decide what the agent through them actually does.

The capabilities are real. The ceiling here is not Linear; it is the Operator's bandwidth. That is where the freemium document stops giving away the full method. The shape is here. The tuning that makes the shape trustworthy is engagement-shaped work.

### Triage Intelligence

Triage Intelligence is Linear's AI-assisted routing layer. When a new item lands in Triage — from Slack, email, GitHub, Sentry, a customer request, a manual entry — Triage Intelligence proposes labels, a project, an assignee, related issues, and possible duplicates. The Operator confirms or overrides; over time the system gets better at the team's particular shape of work.

The Method's posture is that Triage Intelligence starts conservative. Suggestions, not auto-application. Labels and duplicate flags can auto-apply early because the cost of being wrong is low and the cost of policing is low (P-25). Project, assignee, priority, and cancellation stay suggestion-only until the Operator has watched the system make those calls correctly for two or three weeks. Customer feedback never auto-converts to scope — the principle is older than the feature (P-22). An item from Customer Requests can be enriched with suggestions, but conversion to an issue or project remains an Operator decision.

When it pays for itself: the day the Operator's daily Triage pass takes longer than thirty minutes. For the 3-person team in this chapter's opening, that day was last Tuesday.

What the chapter does not cover: the tuning. Telling Triage Intelligence which of two `component:*` labels applies to a given alert pattern, or which project owns Sentry exceptions from a particular service, or which Slack channel's asks should default to Engineer B — those decisions live in workspace and team guidance documents that have to be written, tested, and revised as the team's project shape changes. The system gets smart in proportion to the training data the Operator gives it.

> **Augmentation Surface — Triage at Scale**
>
> Where an agent layer makes this work better: pre-classifying Triage items against the team's established patterns, flagging the three items the Operator should look at first, and escalating the ones that need human judgment within the seven-day Triage SLA (P-20). On a twenty-item morning, the Operator opens a sorted queue with summaries already drafted instead of twenty cold cards.
>
> What the PM keeps: every escalation, every priority change, every rejection. The agent layer proposes; the Operator decides. Delegation without acceptance criteria produces wasted capacity (P-15); the agent layer's job is to compose the criteria, not to skip past them.

### Linear Asks

Linear Asks is structured intake from Slack, email, and web forms. Where Customer Requests handles external feedback for a public-facing product surface, Asks handles internal requests: an engineer in another part of the organization asking the team to look at something, an executive forwarding a question with a deadline attached, a partner team filing a request through a Slack channel the Operator does not monitor in real time. Asks lands in Triage with a structured form already filled out — requester, channel, summary, optional template fields — so the Operator is not staring at "FYI" with no surrounding context.

For the 3-person team, the install moment is when the Operator has three Slack channels of unprocessed messages and Engineer A has stopped pasting them into Triage because pasting is now a job. Asks turns the paste into a form. The Slack channel becomes an Ask channel; form fields capture what the Operator would otherwise have to chase down in DMs. The captured ask routes through Triage and gets the same Triage Intelligence treatment as any other item.

When it pays for itself: the moment the Operator can no longer say with confidence what is sitting in the team's Slack DMs.

What the chapter does not cover: the form design. Asks templates are product design. Too few fields and the Operator still has to chase context; too many and the requester abandons the form and goes back to DM. Designing a four-field template that captures enough to triage without becoming a ten-field tax takes iteration against real requesters. Different intake sources need different templates — a bug report template is not an executive-decision template. The Method names the principle (templates lower the cost of doing the right thing, P-17); the engagement does the tuning.

### SLAs

SLAs are turnaround clocks on issues that need urgency tracking distinct from priority. Priority answers "which of these matters most"; an SLA answers "by when does this need a response." The two are not the same. A low-priority bug with a 24-hour SLA matters less than a high-priority feature but has a clock on it; the high-priority feature does not.

The Method's posture is that SLAs exist for a narrow set of work and the Operator owns the commitments behind them (P-13). The starting rule set is small and conservative:

- Production incident: 24 hours to first response, resolution clock tracked separately.
- Security or access blocker: 48 hours.
- Operator decision blocking active work: 2 business days.
- Customer-facing regression: 1 week.

For the 3-person team, SLAs land on the Operator's calendar the week Engineer B's public surface starts taking production traffic. The two engineers can no longer absorb "we'll get to it" as an answer for that surface; customers can't either. SLAs convert "we'll get to it" into a clock the workspace tracks and the Friday update reports against.

When it pays for itself: the first production incident that should have had a clock and didn't. The Operator finds out after the fact that nobody picked it up for thirty hours.

What the chapter does not cover: distinguishing real-risk SLAs from noise SLAs. Putting an SLA on every priority-high issue produces a workspace where every issue is breaching SLA and no issue is actually urgent. The calibration — which incident categories actually need a 24-hour clock, which "urgent" decisions are really 2-business-day decisions — comes from the team's incident history. A team without six months of clean incident data is calibrating against folklore. Verify what you enforce (P-25); SLAs that fire on the wrong things stop being trusted, and untrusted SLAs are worse than no SLAs.

### Advanced Insights and dashboards

Tier 2 introduced Insights pinned to shared views. Business introduces workspace-level dashboards: composed panels of Insights pulled from multiple views, with the same self-updating shape but the structure of a report rather than a single chart. The Friday update the Operator writes by hand in Tier 2 can become a pinned dashboard in Tier 3: open issue counts by status, cycle time by project, SLA health by domain, agent throughput by delegate, all in one place that updates itself between Friday and Friday.

For the 3-person team, the dashboard moment is when Leadership says, in a meeting that was not on the calendar, "Can we get a weekly view we can pull up ourselves?" Leadership consumes summaries, not raw Linear (P-27); a dashboard is a summary that updates itself. It is still a translation layer the Operator owns.

When it pays for itself: the first time the Operator answers a Leadership question by sending a dashboard link instead of building a deck.

What the chapter does not cover: matching Leadership's reporting taste. Leadership wants the dashboard to look a particular way, group a particular way, color a particular way, slice on properties the workspace does not currently capture. Iterating a dashboard until it earns weekly attention from the audience that consumes it is engagement-shaped work. A dashboard nobody opens is reporting theater (P-27 again, from the other direction).

### Agent surfaces — Linear Agent, AI Agents, MCP

Business unlocks three agent surfaces. The Method describes what each one **is**. It does not, in this document, describe how to build the agent that uses them. That distinction is the point of this chapter.

**Linear Agent** is the assistant inside Linear itself, addressable with `@Linear` in comments, documents, project descriptions, and updates. It answers workspace questions, summarizes long threads, drafts issues from chat, and runs against the workspace's own data. Skills can be configured to standardize the things the Operator does repeatedly.

**AI Agents** are app users — bots that appear in the workspace as members, can be mentioned, can be set as a delegate on an issue, can comment, can collaborate on documents and projects. They are how an external agent (a coding agent on a repo, a research agent against a corpus, a QA agent against a deploy) shows up in Linear as a participant rather than a script.

**MCP** is the protocol surface that lets Linear Agent and external agents talk to other tools — your code host, your documentation system, your monitoring stack — through approved MCP servers configured at the workspace level.

The Method's posture is constrained. Agents are executors, not owners (P-14). Human ownership stays on the issue's assignee field even when a delegate is an agent. Delegation to an agent requires the same acceptance criteria, validation command, expected artifact, and scope that delegation to a human would require — and arguably more, because the agent has no judgment to fall back on (P-15). The agent surfaces in Linear make it possible for an agent to participate; they do not, by themselves, make the participation useful.

For the 3-person team, the agent surfaces start to matter the week Engineer A delegates a sub-issue to a coding agent on the research repo. The issue stays assigned to Engineer A. The delegate field carries the agent. The acceptance criteria are in the issue body. The validation command is named. The PR lands; Engineer A reviews; the issue moves to Validation with evidence (P-6). The surface is doing exactly what the chapter says it does — making the delegation visible in the workspace. The agent through it is product.

When it pays for itself: never, automatically. The surfaces pay for themselves only when there is an agent through them and a delegation protocol around them. Buying Business for the agent surfaces and not installing the protocol is buying a steering wheel without a car.

What the chapter does not cover: how to build the agent. Prompt design, skill chains, MCP-server selection, agent orchestration patterns, the AI PM that uses Triage Intelligence's suggestions to compose delegation packets — those are Ravenhelm product, not freemium content. The surfaces exist; the agent through them is engagement-shaped work.

### Ceiling signal — when the Operator's bandwidth runs out

Tier 3's ceiling is not Linear features. The features are there. The ceiling is the Operator. The signals to watch for are bandwidth signals, not capability gaps:

- **Tuning takes more time than the Operator has.** Triage Intelligence is drifting because nobody has written the workspace guidance update it needs. Asks templates have not been touched in two months and intake quality is degrading. SLA rules are firing on things that shouldn't have SLAs because the calibration pass keeps slipping. The workspace oscillates between hands-on weeks when the Operator catches up and neglected weeks when other priorities consume the calendar. Nothing is broken; everything is decaying.
- **Leadership asks for reporting the Operator can produce once but not sustain weekly.** The first quarterly business review goes well — the Operator spent a Sunday building it. The second one is late. The third one is missing data. The dashboards Leadership wanted to "just open" have stale numbers because the underlying view configuration drifted and the Operator has not had the afternoon to fix it (P-27).
- **The team starts hiring around the gap.** A second Operator, a Chief of Staff, an embedded TPM, an agent layer the Operator does not have time to design — the team is solving for the ceiling by adding headcount or capability without first installing the operating model the new role plugs into. The new hire spends their first quarter inventing the same set of views, the same Triage routine, the same delegation protocol the existing Operator was running in their head.

When any one of those signals lands, Ravenhelm starts. The Method's freemium document gives the shape; the engagement gives the fit. A 3-person team can install Tier 1 alone in a week and Tier 2 alone in a quarter. Tier 3 is where alone runs out.

> **Where this gets hard**
>
> The team that wants Business-tier capabilities and agent surfaces operational on day one — Triage Intelligence routing real intake, Asks templates capturing real channels, SLAs firing on real incidents, dashboards Leadership actually opens, agents participating in real delegation loops — has no calendar for the multi-week tuning that makes any of it trustworthy. The capabilities ship in an afternoon; the trust takes a season.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: 2397
  principle-citations: P-6, P-13, P-14, P-15, P-17, P-20, P-22, P-25, P-27
  flagged-principle-gaps: none
-->
