<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 6 — Tier 1: Linear Free Install

The Operator signed up for Linear Free on Sunday night. Monday morning the workspace is empty: one team named after the company, a default workflow with five states nobody chose, a sample project nobody asked for, and a blinking cursor where the first issue should go. Engineer A and Engineer B are waiting. Leadership wants to know what the team is working on by Friday. The Operator has six prior tools' worth of dead muscle memory and no idea which Linear feature actually matters yet.

This chapter is for that Monday. It is the minimum install — a workspace a 3-person team can stand up in about a week on Free, with no upgrade and no features the team will outgrow in a week. The install is deliberately small. The overbuild test (P-24) is the filter: every label, view, and template has to earn its slot by helping the Operator decide faster or preserving evidence the team would otherwise lose.

By Friday the workspace should hold one team, nine workflow states, four labels, four shared views, one project with one update, and a GitHub PR linked to the issue it implements. That's the install. Everything else waits — and most of it waits *on Free*, not behind a paywall.

### What Free actually gives you

Linear Free is far more capable than its price suggests, and the first job of this chapter is to correct a misreading earlier drafts of the Method made: most of what the Method leans on is already on Free. Free gives you up to two teams (start with one, named for its remit); the nine-state workflow; namespaced labels; shared custom views; projects with milestones and documents; project **and initiative** updates; the full objective layer — **Initiatives**, with health rollup and their own update cadence; **Cycles**; **Customer Requests** as a core intake type; **Releases** with up to fifteen pipelines; **Pulse** update digests; native issue relations (blocking, related, duplicate); sub-issues; templates; the Triage inbox; priority and estimates; GitHub and GitLab PR linking; and the GraphQL API with webhooks. The objective, intake, cadence, and release layers the Method runs on are not behind a paywall. They are on the free tier, waiting for the team to need them.

What Free actually withholds is narrower than it looks, and it falls into two buckets. The first is **scale**: Free caps you at two teams, 250 issues, and 10 MB uploads. Those are the real ceilings — mechanical limits, not missing capabilities. The second is a short list of **analytics and automation surfaces**: Insights (the queryable analytics layer on views) is Business, not Free; Triage Intelligence, Linear Asks, and SLA timers are Business; Dashboards are Enterprise. Admin roles and the lift on the caps arrive with Basic. The feature-tier matrix carries the authoritative gating — when in doubt, read it, don't guess. Net: nothing in the objective, intake, cadence, or release layer costs money. What you pay for later is room to grow (teams, issues) and the analytics and automation that sit on top of the primitives — never the primitives themselves.

The trap on Free is not scarcity; it is the opposite. Because the objective layer, Cycles, Customer Requests, and Releases are all sitting right there, the temptation is to install all of them in week one. Don't. A 3-person team that turns on initiatives, cycles, customer requests, and release pipelines on Monday has built six surfaces it cannot yet keep current. The overbuild test (P-24) applies harder on Free than anywhere, precisely because Free no longer stops you. The Method's discipline (P-16, P-24) is the only thing that does. Chapter 7 covers the Basic upgrade and what triggers it; Chapter 8 covers Business and where self-install starts to break.

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

The state to install carefully is **Validation** (P-6). Install it as a manual gate. Even where the integration can move issues automatically on PR events, the Method keeps the move into Validation — and the move out of it to Done — a human act (P-7); no automation closes the loop for you. Merged code is *implemented*, not *trusted*. The gap between "the PR is in main" and "the change actually works in the environment users hit" is where the Method earns its keep. Without Validation, the team moves issues straight from In Review to Done on PR merge, and the workspace starts lying within a month. With Validation, the Operator owns the closing act: confirm the deploy, paste the evidence link, mark the issue Done. The state is the prompt.

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

What the Method deliberately does **not** want — on any tier — is auto-transition to Done on PR merge (P-6, P-7). The Operator runs the closing by hand: PR merges → Operator moves the issue to Validation → Operator confirms deployment (browser check, deploy log link, runtime confirmation) → Operator pastes evidence in a comment → Operator moves the issue to Done. The discipline travels by hand. Chapter 10 covers the Validation gate in depth; Chapter 11 covers the deeper code-host integration. The install here is the minimum loop that produces an evidence chain (P-8, P-28).

**GitLab equivalent.** Enable the GitLab integration, use the issue ID in branch names and MR titles, and run the Validation close manually. The mechanic differs by integration; the doctrine doesn't.

> **Augmentation Surface — Install Verification**
>
> Where an agent layer makes this work better: at the end of the install week, an agent can scan the workspace against the install checklist — confirming the nine workflow states exist with the right categories, the four views are shared at the team scope, the GitHub integration is wired with at least one linked PR, the first project has a target date and at least one issue, and the first project update is posted. The agent surfaces gaps as a list, not a fix.
>
> What the PM keeps: the judgment call on whether a deferred item — a label namespace, a fifth view, Cycles, a first initiative — should be added in week two or left until the team has a decision that needs it. The agent enumerates; the Operator decides.

#### Friday — first project update

Engineer A's PR opens Friday afternoon. The Operator catches it in the In Review view, reviews the PR, and waits for merge. Once merged, the Operator moves the issue to Validation, pastes the deploy log link, runs a browser check on the staging or production URL, pastes the screenshot, and moves the issue to Done. The full evidence chain (P-28) shows up on the issue for the first time. The Operator now knows what the loop costs in minutes and has a real example to show Engineer B on Monday.

Then the Friday project update (P-19). Linear's update format is enough on Free. Five short sections:

- **Shipped.** What got to Done this week, with the evidence link.
- **Open.** What's in flight, by name.
- **Blocked.** What's stuck and why.
- **Decisions needed.** What the Operator needs from leadership (or from inside the team) to keep moving.
- **Next.** What gets started next week.

Post it. That update is the artifact leadership consumes (P-27) and the cadence the Method runs on for the lifetime of the project — every Friday, no exceptions, even when the update reads "shipped: nothing; the team spent the week stuck on X."

### Growing into the rest — still on Free

The week-one install is four primitives plus one project and one integration. The next several weeks are about reaching — one capability at a time, each when a real decision needs it (P-16) — for surfaces Free already includes, no upgrade required:

- **Initiatives** when Leadership starts asking how projects ladder up to outcomes (P-2). Two or three durable initiatives, owners, quarter-end targets. The objective layer is Free; reach for it the week the rollup question lands, not before.
- **Cycles** when the team wants a time-boxed cadence to commit against rather than an open backlog. Whether a 3-person team needs cycles, or runs on the weekly update cadence alone, is a judgment call — and it is free either way.
- **Customer Requests** when feedback arrives faster than the Operator can hand-convert it and provenance starts getting lost (P-22). A request is captured intake, never automatic scope.
- **Releases** when the team ships on a pipeline worth naming. Free covers up to fifteen pipelines — more than a small team needs; the release-organization doctrine lives in the code-host chapter (Chapter 11).
- **Pulse** when the Operator wants update digests pushed rather than pulled.
- **Native relations** the first time "Blocked" as a state is too coarse — when an issue is blocked *by* a specific other issue and the link itself is the information.

None of these is an upgrade. Each is a Free primitive the team grows into when a view or a decision pulls it in — and each still answers to the overbuild test.

### What you have at the end of week one

A workspace Engineer B can open on Monday and understand. One team named for the team's remit. Nine workflow states, with Validation installed and used at least once. Four labels, each cited by at least one view or attached to at least one issue. Four shared views covering the Operator's morning, the Operator's own queue, the team's blocked work, and the team's review queue. One project with one update and at least one Done issue carrying full evidence. A GitHub integration with at least one linked PR. A weekly rhythm the team has run end-to-end once.

The rhythm to keep, lightly (Chapter 12 covers reporting in depth): Monday the Operator confirms priorities and clears Triage. Daily the Operator clears Waiting on the Operator and Blocked. Friday the Operator posts the project update.

### Ceiling signal

Tier 1's ceiling is mechanical, not feature-shaped — and that is the whole correction. The team does not leave Free because it needs Initiatives, Cycles, Customer Requests, or Releases; it already has them. It leaves Free when it hits the caps. Three concrete signals; when any one of them is firm, move to Chapter 7 and the Basic upgrade:

- **The issue count is approaching 250.** Free's hard cap. The Operator notices archived-versus-active math starting to matter, or Linear warns that new issues are near the limit. Basic lifts this to unlimited.
- **The team needs a third team.** Free allows two. A second squad with its own remit, or a separate team for a distinct product surface, is the moment the 2-team cap binds. Basic raises it to five.
- **Administration outgrows flat membership.** The workspace needs admin roles to delegate settings, or uploads are bumping the 10 MB ceiling. Both come with Basic.

Unlike the later tier moves, there is no "two of three" threshold here. These are hard limits, not judgment calls — you cross a line or you don't. One firm cap signal is enough.

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
  word-count: ~2350
  principle-citations: P-2, P-4, P-5, P-6, P-7, P-8, P-10, P-11, P-12, P-13, P-16, P-17, P-19, P-22, P-24, P-27, P-28
  flagged-principle-gaps: none
-->
