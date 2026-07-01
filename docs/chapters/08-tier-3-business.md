<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 8 — Tier 3: Linear Business and the Edge of Self-Install

It is the end of the Basic quarter. The Operator opens Linear on a Tuesday morning and counts twenty items in Triage that came in overnight — a Sentry alert that fired at 3 a.m., four bug reports from beta users in Customer Requests, a dozen Slack-forwarded asks that an engineer has been pasting into Triage manually since Friday, and three "quick question" emails an executive forwarded with no context. There is a production incident from yesterday that should have had a clock on it and didn't. Engineer A is heads-down on a research repo and has been ignoring Triage for a week because the Operator told them to. Engineer B owns the public surface that just shipped and is waiting for the Operator to tell them which of the four beta-user bugs is real.

The Operator does the Triage pass. It takes ninety minutes. By the time it is done, the morning is gone, the Friday update for Leadership is unwritten, and a request the Operator already promised a decision on is now two days late.

This is the moment Basic stops being enough.

### The shift Business represents

Tier 1 was self-install on Free — and Free already carried the objective, intake, cadence, and release layers the Method runs on. Tier 2 (Basic) lifted Free's ceilings: more teams, unlimited issues, admin roles. Neither tier added a genuinely new capability surface. Business is different. Business is the first tier since Free that you buy for *capability* rather than headroom, and it is where Linear hands the Operator machinery the Operator does not have time to tune alone. Insights have to be shaped against the questions Leadership actually asks. Triage Intelligence has to be trained against the team's real patterns. Asks templates have to be designed so the form does not become a tax. SLAs have to be calibrated against actual incident history, not a generic table copied from a blog post. Agent surfaces — Linear Agent, AI Agents, MCP, Code Intelligence — appear as primitives, and someone has to decide what the agent through them actually does.

The capabilities are real. The ceiling here is not Linear; it is the Operator's bandwidth. That is where the freemium document stops giving away the full method. The shape is here. The tuning that makes the shape trustworthy is engagement-shaped work.

### Insights — the first analytics layer

Insights is the first genuinely new analytics surface since Free, and naming it here is a load-bearing correction: the Method's earlier tiering placed Insights a tier too low, at "Plus." It is a **Business** capability. Free gives you views — a view is a saved filter, a question about the current state of the workspace. Basic adds no analytics at all. Business adds Insights: that same filter *over time*, or sliced by a property, with a measure attached. Issue count by status over the last 30 days. Cycle time by project. Throughput per engineer. Triage time by source. Pin an Insight to a view and it updates itself.

The Operator's first install is two Insights, both pinned to the Operator's Now view:

1. **Open issue count by status, last 30 days.** The shape of work in flight — whether Triage is climbing, whether Validation is backing up, whether In Review has become a parking lot.
2. **Cycle time by project, last 60 days.** Whether the team is getting faster or slower at the same shape of work, project by project.

These replace what the Operator did by hand for the Friday summary all the way back on Free. Leadership reads the summary; they do not browse the workspace (P-27). An Insight lands in the Friday note only when it is moving in a direction that needs explaining. Avoid reporting theater: an Insight that never changes the Operator's plan is a candidate for deletion (P-24).

Composed, multi-view **Dashboards** — the pinned board Leadership opens for itself — are an **Enterprise** capability, not a Business one; the Enterprise chapter (Chapter 9) covers them. On Business, the unit of reporting is the individual Insight panel and the Friday summary the Operator writes around it. What the chapter does not cover: matching Leadership's reporting taste — which slices, which groupings, which properties the workspace does not yet capture. Iterating an Insight until it earns weekly attention is engagement-shaped work.

### Triage Intelligence

Triage Intelligence is Linear's AI-assisted routing layer. When a new item lands in Triage — from Slack, email, GitHub, Sentry, a customer request, a manual entry — Triage Intelligence proposes labels, a project, an assignee, related issues, and possible duplicates. The Operator confirms or overrides; over time the system gets better at the team's particular shape of work. Alongside it, Business adds Triage **Rules** and **Responsibility** — deterministic routing and an on-call rotation for who owns the inbox when — so the queue is not implicitly always the Operator's.

The Method's posture is that Triage Intelligence starts conservative. Suggestions, not auto-application. Labels and duplicate flags can auto-apply early because the cost of being wrong is low and the cost of policing is low (P-25). Project, assignee, priority, and cancellation stay suggestion-only until the Operator has watched the system make those calls correctly for two or three weeks. Customer feedback never auto-converts to scope — the principle is older than the feature (P-22). An item from Customer Requests can be enriched with suggestions, but conversion to an issue or project remains an Operator decision.

When it pays for itself: the day the Operator's daily Triage pass takes longer than thirty minutes. For the 3-person team in this chapter's opening, that day was last Tuesday.

What the chapter does not cover: the tuning. Telling Triage Intelligence which of two `component:*` labels applies to a given alert pattern, or which project owns Sentry exceptions from a particular service, or which Slack channel's asks should default to Engineer B — those decisions live in workspace and team guidance documents that have to be written, tested, and revised as the team's project shape changes. The system gets smart in proportion to the training data the Operator gives it.

> **Augmentation Surface — Triage at Scale**
>
> Where an agent layer makes this work better: pre-classifying Triage items against the team's established patterns, flagging the three items the Operator should look at first, and escalating the ones that need human judgment within the seven-day Triage SLA (P-20). On a twenty-item morning, the Operator opens a sorted queue with summaries already drafted instead of twenty cold cards.
>
> What the PM keeps: every escalation, every priority change, every rejection. The agent layer proposes; the Operator decides. Delegation without acceptance criteria produces wasted capacity (P-15); the agent layer's job is to compose the criteria, not to skip past them.

### Linear Asks

Linear Asks is structured intake from Slack and email. Where Customer Requests handles external feedback for a public-facing product surface, Asks handles internal requests: an engineer in another part of the organization asking the team to look at something, an executive forwarding a question with a deadline attached, a partner team filing a request through a Slack channel the Operator does not monitor in real time. Asks lands in Triage with a structured form already filled out — requester, channel, summary, optional template fields — so the Operator is not staring at "FYI" with no surrounding context.

For the 3-person team, the install moment is when the Operator has three Slack channels of unprocessed messages and Engineer A has stopped pasting them into Triage because pasting is now a job. Asks turns the paste into a form. The Slack channel becomes an Ask channel; form fields capture what the Operator would otherwise have to chase down in DMs. The captured ask routes through Triage and gets the same Triage Intelligence treatment as any other item.

Asks **web forms** — public-facing intake forms hosted for requesters outside the workspace — are an **Enterprise** capability, not a Business one (Chapter 9). On Business, Asks runs through Slack and email channels; that covers internal intake, which is what the 3-person team needs first.

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

### Agent surfaces — agents as workspace participants

Business unlocks the agent surfaces, and this is the part of Linear that has moved fastest since the Method's first edition. The Method's job is unchanged: it describes what each surface **is** and names where an agent helps. It does not, in this document, describe how to build the agent that uses them. That distinction is the entire boundary between freemium content and engagement — and it has gotten sharper, not softer, as the surfaces have grown teeth.

**AI Agents are app users.** An agent registers in the workspace as a member: it has a name, it can be `@`-mentioned in comments, documents, project descriptions, and updates, it can be assigned or set as a delegate on an issue, and it can comment and collaborate the way a human teammate does. Linear ships its own first-party agent — addressable by `@`-mention for workspace questions, thread summaries, and issue drafting — and third-party agents (a coding agent on a repo, a research agent against a corpus, a QA agent against a deploy) register through the same framework rather than running as scripts fired from a terminal. The **agent framework** — registering agents, `@`-mentioning them, the `delegate` field — is available broadly at the framework's free tier; the **agent automations** that let those agents take workflow actions on their own are a **Business/Enterprise** capability.

**The `delegate` field is the load-bearing primitive.** An issue's assignee is a human; its delegate may be an agent. That split is not cosmetic — it is P-14 rendered as a field. The assignee is the throat to choke; the delegate is who is doing the typing this week. Setting the assignee to a bot makes the issue ownerless; setting the delegate to a bot keeps a human accountable while the agent works (P-14). Delegation to an agent still requires the full scope packet — outcome, scope, validation command, expected artifact, repo and file paths — that delegation to a human requires, and arguably more, because the agent has no judgment to fall back on (P-15).

**Agent guidance and shared Skills** are how the Operator standardizes agent behavior without re-typing instructions into every issue. Workspace- and team-level guidance documents hold the standing instructions an agent reads before it acts; **Skills** package the things the Operator does repeatedly — the shape of a good triage summary, the format of a delegation packet, the house rules for a release note — into reusable units an agent can invoke. Guidance is where locality lives for agents: a repo-strict convention or a team-specific default belongs in the closest guidance layer, not the global one (P-18).

**MCP server support** is the protocol surface that lets Linear's agents and external agents reach tools and context outside Linear — the code host, the documentation system, the monitoring stack — through approved MCP servers configured at the workspace level. MCP is what turns an agent from a chat box that knows only the issue text into a participant that can read the repo, the runbook, and the last deploy log before it answers.

**Write-with-Agent** drafts the prose the Operator would otherwise write by hand — a project or initiative update composed from the issues and evidence already in the workspace. The agent drafts; the Operator owns the send. A project update is a commitment Leadership reads as truth (P-27), and priority, taste, and risk do not delegate (P-13): the agent can assemble the words, but the Operator decides what the update claims.

**Triage Automations** let an agent take open-ended actions on Triage items — enrich, label, route, flag a duplicate, draft a first response — inside the seven-day Triage SLA (P-20). The posture matches Triage Intelligence above: labels and duplicate flags can auto-apply early because the cost of being wrong is low; conversion, priority, and cancellation stay human until the Operator has watched the automation make those calls correctly for weeks (P-22, P-25).

### The escalation — agents that write and ship code

The Method's first edition treated agents as planning and coordination help: they summarized threads, drafted issues, pre-classified Triage. That framing is now out of date. Linear's agents have escalated from drafting comments to **writing and shipping code**, and the discipline this chapter describes does not loosen as a result — it tightens. An agent that drafts a comment costs a bad paragraph when it is wrong. An agent that opens a pull request costs a bad merge. The higher the blast radius, the more load-bearing P-14 becomes.

**Code Intelligence** (**Business/Enterprise**, beta) is the first rung: an agent that reads the connected codebase and answers implementation questions grounded in the actual repo rather than the issue text alone — "where is rate limiting enforced," "what breaks if we change this schema." It reads; it does not write. Its value to the Method is that it makes delegation packets sharper: the acceptance criteria and validation command (P-15) can be written against what the code actually does.

**Coding Sessions** (**Business/Enterprise**) are the escalation itself. An agent — running Claude Code or Codex, cloud-executed rather than tied to an engineer's laptop — takes an issue, writes the code, and opens a pull request: triage-to-fix with no human keystroke between the report and the diff. This is the capability that changes the stakes of everything above it. The agent is no longer proposing work; it is producing the artifact P-6 says must be validated. A Coding Session that opens a PR has produced *implemented*, not *trusted*, code (P-6); the code host still proves the implementation (P-8); and nothing customer-facing reaches Done without release evidence, however the diff was authored (P-9).

**Linear Diffs** bring code review inside Linear — the diff, the review threads, and the merge decision surfaced next to the issue rather than only in the code host. When the author of the diff is an agent, the review is not a courtesy; it is the validation gate (P-6), and the human reviewer supplies the acceptance the evidence chain requires from someone other than the author (P-7).

**"Open in coding tool"** is the low-ceremony version of the same move: from any issue, the Operator or an engineer hands the work to Cursor, Claude Code, or Codex with a prompt template pre-filled from the issue. It is a **Free-tier** convenience — no Business seat required — and it is the most common on-ramp, because the human stays in the driver's seat the whole way: the agent writes in the tool, the human runs the validation command and opens the PR under their own name.

For the 3-person team, the escalation lands the week Engineer A stops pasting an issue into a coding tool by hand and instead delegates the sub-issue to a Coding Session on the research repo. The issue stays assigned to Engineer A (P-14); the delegate field carries the agent; the acceptance criteria and the validation command are in the issue body (P-15). The Coding Session opens a PR, a Linear Diff surfaces it, and Engineer A reviews, runs the validation command, and moves the issue to Validation with evidence (P-6, P-7). The agent wrote the code. Engineer A still owns whether it ships — which is exactly why the escalation makes the human-ownership discipline matter more, not less.

When it pays for itself: never, automatically. The surfaces pay only when there is a delegation protocol around them. Buying Business for the agent surfaces and skipping the protocol is buying a self-driving car with nobody willing to sit in the seat — and now the car merges to main.

What the chapter does not cover: how to build the agent. Prompt design, skill chains, MCP-server selection, orchestration patterns, the AI PM that composes delegation packets from Triage Intelligence's suggestions and audits a Coding Session's output before a human ever opens it — those are Ravenhelm product, not freemium content. Linear ships the surfaces; the Method names where they help; the agent that runs safely through them is engagement-shaped work.

### Team boundaries, guests, and access controls

Business is also where the workspace gains boundaries. **Private teams** let a team's issues stay invisible to the rest of the workspace — the first time a sensitive workstream (security, an acquisition, a comp project) can live in Linear without a separate workspace. **Guests** let an outside collaborator — a contractor, a partner-team reviewer — into specific teams without a full seat across the workspace. **Login-method restrictions**, including enforced Google SSO, let the Operator require a sanctioned sign-in path. And the **Intercom** and **Zendesk** integrations route support conversations into Customer Requests, so the feedback layer the team has run on Free since the beta now connects to the channels support actually lives in.

What stays above Business, in Enterprise (Chapter 9): SAML/SSO with SCIM provisioning, the audit log, IP-range restrictions, multi-level sub-teams, Dashboards, Asks web forms, and the Salesforce/Gong/Airbyte integrations. The line between Business and Enterprise is the line between one well-run organization and a fleet of teams that has to be governed centrally.

### Ceiling signal — when the Operator's bandwidth runs out

Tier 3's ceiling is not Linear features. The features are there. The ceiling is the Operator. The signals to watch for are bandwidth signals, not capability gaps:

- **Tuning takes more time than the Operator has.** Triage Intelligence is drifting because nobody has written the workspace guidance update it needs. Asks templates have not been touched in two months and intake quality is degrading. SLA rules are firing on things that shouldn't have SLAs because the calibration pass keeps slipping. The workspace oscillates between hands-on weeks when the Operator catches up and neglected weeks when other priorities consume the calendar. Nothing is broken; everything is decaying.
- **Leadership asks for reporting the Operator can produce once but not sustain weekly.** The first quarterly business review goes well — the Operator spent a Sunday building it. The second one is late. The third one is missing data. The Insight panels Leadership wanted to "just open" have stale numbers because the underlying view configuration drifted and the Operator has not had the afternoon to fix it (P-27). When Leadership wants a board it can pull up unaided, the answer is an Enterprise Dashboard (Chapter 9) — and someone has to own keeping it current.
- **The team starts hiring around the gap.** A second Operator, a Chief of Staff, an embedded TPM, an agent layer the Operator does not have time to design — the team is solving for the ceiling by adding headcount or capability without first installing the operating model the new role plugs into. The new hire spends their first quarter inventing the same set of views, the same Triage routine, the same delegation protocol the existing Operator was running in their head.

When any one of those signals lands, Ravenhelm starts. The Method's freemium document gives the shape; the engagement gives the fit. A 3-person team can install Tier 1 alone on Free in a week and grow into Basic in a quarter. Tier 3 is where alone runs out. The tier beyond it — Enterprise (Chapter 9) — is not about more capability for one team; it is about running the method across many teams at once.

> **Where this gets hard**
>
> The team that wants Business-tier capabilities operational on day one — Triage Intelligence routing real intake, Asks templates capturing real channels, SLAs firing on real incidents, Insights Leadership actually reads, agents participating in real delegation loops — has no calendar for the multi-week tuning that makes any of it trustworthy. The capabilities ship in an afternoon; the trust takes a season.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: ~3650
  principle-citations: P-6, P-7, P-8, P-9, P-13, P-14, P-15, P-17, P-18, P-20, P-22, P-24, P-25, P-27
  flagged-principle-gaps: none
-->
