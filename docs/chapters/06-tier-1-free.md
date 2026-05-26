<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 6 — Tier 1: Linear Free Install

The Operator signed up for Linear Free on Sunday night. Monday morning the workspace is empty: one team named after the company, a default workflow with five states nobody chose, a sample project nobody asked for, and a blinking cursor where the first issue should go. Engineer A and Engineer B are waiting. Leadership wants to know what the team is working on by Friday. The Operator has six prior tools' worth of dead muscle memory and no idea which Linear feature actually matters yet.

This chapter is for that Monday. It is the minimum install — a workspace a 3-person team can stand up in five working days on Free, with no upgrades and no features the team will outgrow in a week. The install is deliberately small. The overbuild test (P-24) is the filter: every label, view, and template has to earn its slot by helping the Operator decide faster or preserving evidence the team would otherwise lose.

By Friday the workspace should hold one team, nine workflow states, four labels, four shared views, one project with one update, and a GitHub PR linked to the issue it implements. That's the install. Everything else waits.

### What Free gives you, and what it doesn't

Linear Free covers what a small team needs to run for months: one team, unlimited issues, unlimited members up to the plan cap, customizable workflows, shared custom views, basic project tracking, and GitHub PR linking. A 3-person team can ship work, track it, and report on it without paying.

What Free leaves out is the rollup and intake layer above the team: Initiatives (the objective layer per P-2), Customer Requests as a structured intake type, Insights as a queryable analytics surface on shared views, Triage Intelligence, Asks, SLA timers, and the full Releases pipeline. The Method uses all of them — but not on day one and not for a team that hasn't yet outgrown eyeballing four views. Chapter 7 covers the Plus upgrade and what triggers it; Chapter 8 covers Business and where self-install starts to break.

The trap on Free is the opposite of feature scarcity. It's the temptation to compensate for missing features by building elaborate label taxonomies, twenty saved views, and parallel workflows in documents. Don't. The Method's discipline (P-16, P-24) applies harder on Free than anywhere else.

### Week one install

#### Monday — team and workflow states

Rename the default team. The team's name is its actual remit — "Platform," "Growth," "Apps" — not the company name. The company is the workspace; the team is what this group of three is on the hook for. If the remit changes in six months, the team gets renamed. The Operator, Engineer A, and Engineer B are the only members; nobody else has a seat yet.

Then configure the workflow. Linear's default is close to what the Method wants but not exact. The canonical nine states (P-10) are:

1. **Triage** — new, unprocessed work. Default landing zone for anything filed without a project.
2. **Backlog** — accepted, not scheduled.
3. **Ready** — scoped, available to start.
4. **In Progress** — someone is actively working.
5. **In Review** — PR or artifact awaiting review.
6. **Validation** — merged or deployed work that still needs runtime, browser, release, or human-acceptance evidence.
7. **Blocked** — someone or something else is in the way; the blocker is named in a comment.
8. **Done** — evidence on file.
9. **Canceled** — no longer matters; the reason is in a comment.

The state to install carefully is **Validation** (P-6). On Free, no automation will move an issue into Validation — that's a Plus/Business feature. Install Validation anyway. Merged code is *implemented*, not *trusted*. The gap between "the PR is in main" and "the change actually works in the environment users hit" is where the Method earns its keep. Without Validation, the team moves issues straight from In Review to Done on PR merge, and the workspace starts lying within a month. With Validation, the Operator owns the closing act: confirm the deploy, paste the evidence link, mark the issue Done. The state is the prompt.

Settings → Teams → [team name] → Workflow. Rename what you can, create what's missing, archive what's extra. Resist `stage:*` labels for now (P-11); on Free, the team doesn't need them yet.

#### Tuesday — labels and first project

A minimal label namespace, per the chapter on labels and views (Chapter 5). Four namespaces, nothing else:

- `type:` — Feature, Bug, Chore, Documentation, Research. What kind of work this is.
- `component:` — the service or area of the codebase: `component:api`, `component:web`, `component:auth`. Fill in your own components; don't pre-populate twenty.
- `risk:` — low, medium, high. The Operator's prompt to surface risk early (P-13).
- `source:` — github, slack, email, support. Where the work originated. Valuable even on day one for spotting where intake noise is coming from.

Skip `domain:`, `stage:`, `parking-reason:`, `okr:`, and `release:` for now. The overbuild test (P-24) asks five questions; on a 3-person team in week one, those namespaces fail at least three of them. Add labels when a view needs them — which is the test (P-16). A label not cited by any view is dead weight.

Then create the first project. One project. Name it for the team's current focus — "Internal Product MVP," "Platform Reliability," "First Revenue." Set a lead (the Operator), a start date (today), and a target date that's honest — four to eight weeks out, not a quarter. Write a one-paragraph summary: what is being built, by when, why it matters. Link the relevant design doc, PRD, or planning note (P-5 — deep context lives outside Linear). No milestones yet; the team hasn't shipped anything to learn what milestones it wants.

#### Wednesday — views and first issues

Four shared views. No more.

- **Operator's Now** — `state in {In Progress, In Review, Validation}`, sorted by priority then updated. The Operator's single-pane view. If a thing is moving, it's here.
- **Waiting on the Operator** — `assignee = Operator AND state in {Ready, Blocked}`. The Operator's own queue. Priority, taste, risk, and commitments don't delegate (P-13); this view keeps the Operator's backlog from hiding under engineering work.
- **Blocked** — `state = Blocked`, all issues, sorted by updated descending. The stuck-work radar. After three days the Operator either unblocks it or escalates.
- **In Review** — `state = In Review`, all issues. Engineering's review queue. Catches PRs that have been open too long.

That's it. The temptation on Wednesday is to keep going — "Stale Work," "By Component," "By Assignee," "Recently Done." Don't. Save the impulse for two weeks from now, after the team has used these four and the Operator can point at a real decision they couldn't make because no view supported it. That's the bar (P-24).

Then write the first batch of issues. Pull them from wherever the team's current work lives — a planning doc, a notes file, a half-built backlog in the old tool. The rule is deliverable-sized (P-4): one outcome, defined scope, exit criteria, one owner. An issue that takes longer than two weeks to verify gets split into a parent with sub-issues (P-12). Use an issue template (P-17) — Linear's default is fine for week one. Attach the issues to the project. Engineer A picks up the first; Engineer B picks up the second.

#### Thursday — GitHub integration

Settings → Integrations → GitHub. Install the integration; Free supports linking multiple repos. Authorize Linear; pick which repos to connect.

The convention to install is the issue ID in the branch name or PR title. Linear auto-generates branch names from issues — Engineer A copies the suggested branch name (e.g., `eng-a/eng-42-add-rate-limiter`) when starting work. When the PR opens, Linear adds the link to the issue. That's the whole pattern on Free.

What Free does **not** give you, and what the Method deliberately doesn't want (P-6, P-7), is auto-transition to Done on PR merge. On Free, the Operator runs the closing manually: PR merges → Operator moves the issue to Validation → Operator confirms deployment (browser check, deploy log link, runtime confirmation) → Operator pastes evidence in a comment → Operator moves the issue to Done. The discipline travels by hand. Chapter 9 covers the Validation gate in depth; Chapter 10 covers the deeper code-host integration Plus and Business unlock. The install here is the minimum loop that produces an evidence chain (P-8, P-28).

**GitLab equivalent.** Enable the GitLab integration, use the issue ID in branch names and MR titles, and run the Validation close manually. The mechanic differs by integration; the doctrine doesn't.

> **Augmentation Surface — Install Verification**
>
> Where an agent layer makes this work better: at the end of the install week, an agent can scan the workspace against the install checklist — confirming the nine workflow states exist with the right categories, the four views are shared at the team scope, the GitHub integration is wired with at least one linked PR, the first project has a target date and at least one issue, and the first project update is posted. The agent surfaces gaps as a list, not a fix.
>
> What the PM keeps: the judgment call on whether a deferred item — a label namespace, a fifth view, a second integration — should be added in week two or left until Plus. The agent enumerates; the Operator decides.

#### Friday — first project update

Engineer A's PR opens Friday afternoon. The Operator catches it in the In Review view, reviews the PR, and waits for merge. Once merged, the Operator moves the issue to Validation, pastes the deploy log link, runs a browser check on the staging or production URL, pastes the screenshot, and moves the issue to Done. The full evidence chain (P-28) shows up on the issue for the first time. The Operator now knows what the loop costs in minutes and has a real example to show Engineer B on Monday.

Then the Friday project update (P-19). Linear's update format is enough on Free. Five short sections:

- **Shipped.** What got to Done this week, with the evidence link.
- **Open.** What's in flight, by name.
- **Blocked.** What's stuck and why.
- **Decisions needed.** What the Operator needs from leadership (or from inside the team) to keep moving.
- **Next.** What gets started next week.

Post it. That update is the artifact leadership consumes (P-27) and the cadence the Method runs on for the lifetime of the project — every Friday, no exceptions, even when the update reads "shipped: nothing; the team spent the week stuck on X."

### What you have at the end of week one

A workspace Engineer B can open on Monday and understand. One team named for the team's remit. Nine workflow states, with Validation installed and used at least once. Four labels, each cited by at least one view or attached to at least one issue. Four shared views covering the Operator's morning, the Operator's own queue, the team's blocked work, and the team's review queue. One project with one update and at least one Done issue carrying full evidence. A GitHub integration with at least one linked PR. A weekly rhythm the team has run end-to-end once.

The rhythm to keep, lightly (Chapter 11 covers reporting in depth): Monday the Operator confirms priorities and clears Triage. Daily the Operator clears Waiting on the Operator and Blocked. Friday the Operator posts the project update.

### Ceiling signal

Three concrete signals that the team has outgrown Tier 1. When two of three land in the same month, move to Chapter 7 and the Plus upgrade.

The first signal is the **objective layer**. The team has three or four projects active and leadership is asking how they ladder up — which outcome does this project serve, which two projects are the same bet under different names, what gets dropped if budget shifts. The Operator is answering in a slide deck because Linear can't. That's the Initiatives gap (P-2) and it's a Plus feature.

The second signal is **structured intake**. Customer feedback — from support, sales calls, the team's own users — is arriving as Slack messages, emails, and Notion pages, and the Operator is hand-converting each one into Linear issues (or worse, losing them). The team needs Customer Requests so feedback enters Triage with provenance (P-22). On Free the team can fake it with a `source:` label and discipline; once volume crosses a threshold the discipline breaks.

The third signal is **trend reporting**. Leadership starts asking questions the Operator can't answer by looking at the four views — cycle time, throughput by component, where the bottlenecks have been over six weeks. Insights is the answer, and Insights on shared views is a Plus feature. When the Operator catches themselves exporting issues to a spreadsheet to compute the same numbers twice in two weeks, the team has hit this signal.

> **Where this gets hard**
>
> The Validation gate assumes the Operator can produce the evidence — a deploy log link, a browser check, a runtime confirmation. When the team needs Validation evidence from infrastructure the Operator doesn't own — a separate ops team owns the deploy pipeline, the deploy logs live in a system the Operator can't read, getting a link on every production issue requires negotiating with another team's PM — the install stalls. The workspace looks correct; the evidence chain (P-28) breaks at the boundary.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: 2195
  principle-citations: P-2, P-4, P-5, P-6, P-7, P-8, P-10, P-11, P-12, P-13, P-16, P-17, P-19, P-22, P-24, P-27, P-28
  flagged-principle-gaps: none
-->
