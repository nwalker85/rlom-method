<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 13 — Reporting Up: Project Updates, Initiative Health, and the Monthly Review

It is Thursday at 4:15 p.m. You have not started the leadership status note yet. Your engineering Slack channel needs a "this week so far" pin by end of day. The all-hands deck — the one Leadership wants Friday morning — has a slide titled "Platform Reliability — status?" and the slide is blank. The leadership Notion page wants a bulleted update by Monday and the bullets are supposed to follow last quarter's format, which nobody remembers. You open three tabs, three editors, three different sets of headings, and you write what is functionally the same paragraph three times in three voices. The first version is too operational, the second is too vague, the third sounds like a press release. By Friday at noon you have produced three reports, none of which Leadership reads end-to-end, and none of which you can quote on Monday when someone asks you what changed last week. You did the work. The work did not compound.

The Method's reporting layer exists to make that compounding happen. The Operator writes once, at the right altitude, in a fixed template, and the same content rolls up. Leadership reads summaries, not raw Linear (P-27). Your job is translation — from issues to project updates, from project updates to initiative updates, from initiative updates to the monthly review. Each layer compresses the one below it. The compression only works if the format below is stable enough to compress mechanically.

### The three cadences and the nesting

Three rhythms hold the stack together. Weekly, every active project gets a project update (P-19). Biweekly, every active initiative gets an initiative update. Monthly, the initiative updates feed a 30-minute (or 5-minute-read) operating review for Leadership (P-21). Project → initiative → review. The Operator writes upward; Leadership reads downward and almost never reaches past the top.

The evidence chain (P-28) is what makes the rollup honest. Initiative health rolls up from project updates. Project updates roll up from issue evidence. Issue evidence rolls up from the code host — merged PRs, deploy logs, acceptance comments (P-7, P-8). Break any link and the chain collapses into theater: green initiative status that nobody can defend, monthly reviews that recite intentions, all-hands updates assembled from memory. The templates that follow are what keep the chain unbroken. They are not aesthetic choices. Each section forces the Operator to either point at evidence or admit there isn't any yet.

### The weekly project update

Every active project gets an update every week. No exceptions for "nothing happened" weeks — write the update anyway, mark the items as carried over, and keep the cadence. A project without an update for seven days surfaces in the stale-projects view; that view is what makes the cadence enforceable rather than aspirational (P-19).

The Operator posts the update on Friday afternoon as a project update in Linear. The team is also a reader. Engineer A and Engineer B should glance at it before logging off Friday; the update tells them what shipped, what is in flight, and what is blocked going into Monday. It is not a Leadership-only artifact.

```markdown
# [Project Name] — Week of [YYYY-MM-DD]

## Shipped this week
- [Issue title] — [one-line outcome]. [PR link or evidence link]
- [Issue title] — [one-line outcome]. [PR link or evidence link]

## In flight
- [Issue title] — In Progress. Owner: [name]. Expected: [date or milestone].
- [Issue title] — In Review. PR: [link]. Awaiting: [reviewer or check].
- [Issue title] — Validation. Evidence needed: [runtime smoke / browser proof / acceptance].

## Blocked
- [Issue title] — blocked on [specific blocker]. Unblocker: [name or system]. Age: [N days].

## Decisions needed
- [Question, one sentence]. Owner of the decision: [Operator or Leadership]. Decide by: [date].

## Next week
1. [Top priority]
2. [Second priority]
3. [Third priority, if any]
```

Three failures the template prevents. First, the "everything is fine" update — the one that says "good progress, no blockers" and elides the two issues quietly stuck in Blocked for nine days; the template forces a Blocked section, and an empty section is a claim the Operator has to be able to defend. Second, the wall-of-text update — five paragraphs of context with no actionable items; the template's bullet structure makes that physically awkward to write. Third, the buried decision request — an Operator-needs-a-Leadership-call hidden in the middle of paragraph three; the Decisions section makes it the part Leadership can scan in 10 seconds.

> **Augmentation Surface — Update Drafting**
>
> Where an agent layer makes this work better: pulling the project's shipped issues (Done in the last 7 days), in-flight issues (In Progress, In Review, Validation), Blocked items with their blocker comments, and Waiting-on-Operator items with their decision deadlines into a first-draft project update every Friday morning — every section of the template pre-populated, every link in place, ready for the Operator to edit by lunch. The same pattern compounds upward: biweekly initiative drafts assembled from the project updates underneath them, monthly review drafts assembled from the most recent initiative updates. The drafting is the high-leverage part. Most of the Operator's translation work becomes review and edit, not authorship.
>
> What the PM keeps: the framing call ("this is the bet next cycle, here is why"), the risk call (what to flag to Leadership now and what to hold a week), and every decision request — the precise wording, the deadline, and who owns the decision.

### The biweekly initiative update

Every two weeks, every active initiative gets an update. Initiatives are the objective layer (P-2) — durable outcomes that roll up projects, with target horizons no tighter than a quarter. The biweekly cadence is the compression step between weekly project chatter and the monthly Leadership rollup. The Operator should not be writing initiative updates more often than biweekly; the underlying work does not move fast enough to justify weekly initiative-level prose, and writing it weekly produces noise that drowns the signal Leadership is supposed to see.

Use the generic initiative archetypes any 3-person team can adopt: Platform Reliability, Operator Experience, New Product Bring-Up, Compliance Readiness, First Revenue. Substitute whatever names your own initiatives carry; the template is identical.

```markdown
# Initiative: [Initiative Name] — Update [YYYY-MM-DD]

## Objective health
**[Green | Yellow | Red]** — [one-line reason if not green]

## Key result status
| KR | Current | Target | Trend |
|---|---|---|---|
| [Metric or outcome] | [value] | [target] | [up / flat / down] |
| [Metric or outcome] | [value] | [target] | [up / flat / down] |
| [Metric or outcome] | [value] | [target] | [up / flat / down] |

## Narrative
[One paragraph. What changed this cycle. What is the bet for the next cycle. What is the one risk Leadership should know about — the one the Operator would otherwise want to hide.]

## Linked projects and current status
- [Project Name] — [On Track / At Risk / Blocked]. Latest update: [link]. One line: [what is happening].
- [Project Name] — [On Track / At Risk / Blocked]. Latest update: [link]. One line: [what is happening].
```

Failures the template prevents. First, the perpetually-green initiative — the one whose status has been green for nine biweeks because nobody wants to be the one to flip it; the Trend column on every KR forces a directional claim, and three flats in a row is itself a yellow signal. Second, the narrative as press release — the paragraph that lists accomplishments and omits the bet and the risk; the prompt explicitly asks for what the Operator would otherwise want to hide. Third, the initiative untethered from projects — health asserted without project evidence underneath; the Linked Projects section makes the rollup chain visible, and an initiative with no recent project updates beneath it is not actually being run.

### The monthly operating review

At the end of each month, the Operator publishes a single document that consumes the most recent initiative updates and presents the state of the portfolio to Leadership. It is consumed in one of two ways: a 30-minute meeting where the Operator walks Leadership through the rollup, or a 5-minute read in advance with a 15-minute decision conversation after. Both should work from the same document. Leadership does not browse the workspace; this document is the workspace from their perspective (P-27).

```markdown
# Monthly Operating Review — [Month YYYY]

## Initiative rollup
| Initiative | Health | KR summary | Trend |
|---|---|---|---|
| [Initiative Name] | [G/Y/R] | [1-line KR state] | [up / flat / down] |
| [Initiative Name] | [G/Y/R] | [1-line KR state] | [up / flat / down] |
| [Initiative Name] | [G/Y/R] | [1-line KR state] | [up / flat / down] |

## What shipped this month
[5–10 lines. The completed work that mattered, not every closed issue. Each line names the outcome and links to the evidence — PR, release, acceptance artifact (P-7).]

## Stale work
- **Projects without recent updates:** [list, with last-update date]. (P-19)
- **Triage items past SLA:** [count and oldest age]. (P-20)
- **Initiatives without movement:** [list, with last initiative update date].

## Decisions ahead
- [Decision Leadership will need to make]. Expected by: [date]. Why now: [one line].
- [Decision Leadership will need to make]. Expected by: [date]. Why now: [one line].
```

Failures the template prevents. First, the highlight reel — the monthly review that lists shipped work and skips stale work; the explicit Stale Work section is non-negotiable, and the Operator who leaves it blank should be asked to defend the claim. Second, the surprise decision — the architectural call or budget ask that lands in front of Leadership with no warning; the Decisions Ahead section is the pipeline that prevents this, and items that appear here this month often become Decisions Needed in next month's project updates. Third, the reverse-engineered status — a monthly review written from scratch in the last week of the month, disconnected from the initiative and project updates that fed it; if the templates above were used on cadence, this document assembles itself in under an hour.

### Computed health (the RAG operating model)

Every one of the three templates carries a health field, and so far the Method has told you to *pick* it — On Track / At Risk / Off Track on a project, Green / Yellow / Red on an initiative. A pick made at 4 p.m. Friday by a tired Operator is a vibe; the perpetually-green initiative and the everything-is-fine project update are one failure in two costumes — a health signal nobody computed and nobody can defend.

Health should be computed, not picked. The Method's rule is a deterministic Red / Amber / Green ladder, evaluated top to bottom — the first matching rung sets the color:

1. **Red** — the project is Blocked (a hard blocker sits on the critical path), *or* it is past its target date with under ~25% of its issues Done.
2. **Amber** — it is past its target date with ~25–74% of issues Done, *or* any single issue has been stuck in Blocked for more than seven days.
3. **Green** — none of the above (a project that is 100% Done is Green by definition).

Three counts and a date decide the color, so two Operators looking at the same project get the same answer — a status you can recompute is one the team argues at the rule, not the case. Map the rungs onto the field Linear already gives you — Green is On Track, Amber is At Risk, Red is Off Track — and the result writes straight into the native Project Health field. This is the line to memorize: **Linear gives you the health *field*; the Method gives you the *computation rules*.** Project Health ships on every tier; the rules are yours, and without them the field is a dropdown three people fill three different ways.

Wire the rules as a small automation, not a habit. A scheduled job — or a webhook on the relevant Linear events — runs the ladder against the API once a week, the morning the weekly project updates are due (P-19), and writes each active project's color before the Operator sits down. Between runs, two events escalate in real time: a target date passing flips the project to at least Amber, and a blocker landing on the critical path flips it to Red. The Operator never has to remember to downgrade a project; the system does, which makes this P-25 in its purest form — a convention you can check programmatically holds where one enforced by Friday willpower erodes by week four. The computed color is the default; the Operator overrides it only on a risk the rule cannot see, and writes down why.

Computed color is necessary but not sufficient, and the gap is evidence: a project can be 100% Done and still not honestly be Green if its Done issues are empty — closed with no merged PR, no deploy log, no acceptance comment (P-6, P-7). The ladder measures whether the work *moved*; Validation measures whether it is *real*, so a mature automation checks both — issues marked Done with no evidence link leave the project not Green but unproven, which reads as Amber with a one-line reason ("3 Done issues lack release evidence"). Green that outruns its evidence is the theater P-28 warns about; the chain holds from the color down to the merge commit in the code host (Chapter 12).

The ladder rolls up the same way. An initiative's health is the worst color among its linked projects, escalated when those projects go quiet — an initiative riding three projects that have not posted an update in three weeks is not Green whatever their last-known colors, because the rollup has gone blind (P-21, P-28). That turns the biweekly initiative update's Objective Health from a feeling into a function of the project layer beneath it, and keeps the monthly review's rollup table defensible when Leadership reads it (P-27).

Where the colors are *surfaced* scales with tier; the computation does not. The per-project Project Health field is Free; trends across the portfolio — how long it sat Amber last quarter, which initiatives flip color most often — are an Insights question, and Insights is Business-tier. The org-level RAG board, where Leadership watches every initiative's color on one screen, is a Dashboard, and Dashboards are Enterprise (Chapter 9). The rules are identical at every tier; only the reach of the result changes.

### Pulse (the consumption layer)

Everything above is the *authoring* side of reporting — the Operator writing once, at altitude, on cadence. Pulse is the *delivery* side: how the people downstream receive it without opening Linear. Pulse is a Free feature, and it is what makes P-27 — Leadership consumes summaries, not raw Linear — physically true rather than aspirational.

Pulse is three things: a digest feed of project and initiative updates — every status update and health change as a readable stream instead of buried in a workspace nobody on the Leadership Team logs into; an Inbox digest, daily or weekly, that lands new updates in front of each reader on a schedule they choose; and Pulse audio — read-aloud summaries Leadership can hear on a commute instead of read at a desk. The channel meets the reader where they are; the cadence stays exactly as authored.

The distinction that keeps Pulse from becoming noise: **Pulse is the firehose; the authored summary is the signal.** The digest carries every update as written, but it does not replace the weekly project update or the monthly operating review, because those are curated — the Operator chose what mattered, named the risk, and asked for the decision (P-21). A Leadership Team that reads only the firehose and never the authored rollup has un-hired the Operator's translation and gone back to browsing raw Linear with extra steps — the exact failure P-27 exists to prevent. Used well, Pulse keeps Leadership current between monthly reviews without their ever opening the workspace, and lets the Operator confirm an update landed without chasing a read receipt.

### Friday afternoon, in practice

It is Friday at 3:40 p.m. The Operator has two active projects — call them CI/CD Backbone and Internal Tooling Integration — and three active initiatives: Platform Reliability, Operator Experience, and New Product Bring-Up. The Operator posts a project update on each project in Linear: shipped, in flight, blocked, decisions needed, next week. Each update takes eight minutes because the agent layer has pre-populated the structure from the week's Linear and code-host activity. The Operator pins a four-line summary into the team Slack channel — what shipped, one blocker, the decision now waiting on Leadership — and queues the biweekly Platform Reliability initiative update as a Monday-morning draft, because today is the second Friday of the cycle and that initiative is due. Engineer A and Engineer B each open the project updates from their phones around 5 p.m., see that the staging deploy fix shipped and that the schema migration is blocked on a Leadership decision, close the tab, and start their weekends. The Operator's Friday afternoon, before the Method: two hours. The Operator's Friday afternoon, with the Method: thirty-five minutes. The leadership note for Monday writes itself from the Friday updates because the headings match.

### What reporting is for

The goal of reporting is not to perform progress; it is to surface the decisions Leadership owns. A project update that produces no decision request is fine on a green week — most weeks are green weeks and the absence of a decision is itself information. A string of green weeks with no decision requests is a smell. The Operator is either running a project that genuinely needs nothing from Leadership for a quarter (rare), or hiding the hard parts behind tidy bullets (common). The Decisions Needed section in the project update, the risk sentence in the initiative narrative, and the Decisions Ahead section in the monthly review are the three places the system asks the Operator to be honest. The cadence — weekly, biweekly, monthly — is the part that makes the honesty habitual rather than heroic.

> **Where this gets hard**
>
> When Leadership's reporting taste has its own format — quarterly pillar dashboards, BSC-style scorecards, board narratives, OKR check-ins in a slide template the Chief of Staff inherited four years ago — and that format does not map cleanly to Linear's project and initiative primitives, the Operator ends up maintaining two reporting stacks: the Method's (for operational truth) and Leadership's (for the format they want). The translation either consumes a day a month or decays into a copy-paste that loses fidelity at the seams.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass — three templates (project update, initiative update, monthly review) each present as a markdown code block in cadence order; computed-RAG ladder presented as an ordered (evaluate-in-order) list
  word-count: ~3060 (added ~990: computed-health RAG operating model + Pulse consumption layer)
  principle-citations: P-2, P-6, P-7, P-8, P-19, P-20, P-21, P-25, P-27, P-28
  flagged-principle-gaps: none
-->
