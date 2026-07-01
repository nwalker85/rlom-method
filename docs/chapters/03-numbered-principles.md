<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 3 — The Numbered Principles

You have been on three teams that all used Linear. One ran it like a public to-do list. One ran it like Jira, with seven custom states and a `Type` field nobody filled in. One ran it like a vibes-based Slack channel where Done meant somebody had stopped talking about it. None agreed on what a project was, what Done meant, or which artifact proved the work shipped — and none scaled past a dozen people without burning their PM out.

The Method does not solve that by adopting a tool harder. It writes down the decisions the Operator would otherwise re-derive every week and gives them numbers so they can be cited. The numbered principles are the spine — how the Method stays consistent across a 3-person team and a 30-person team, a Free workspace and a Business one, leadership that wants weekly slides and leadership that wants nothing.

The most load-bearing principle is **P-6 — Validation separates implemented from trusted**. If you apply one principle Monday, apply that one.

### How to use the principles

The principles only work if they are *cited*. A principle never named in a PR comment, issue comment, project description, or agent scope brief is dead weight. A principle cited weekly becomes load-bearing — the team learns to argue at the rule, not the case.

Cite as `P-#` in PR comments ("Holding in Validation per `P-7`"), issue comments ("Splitting — see `P-12`"), project descriptions, agent scope briefs ("Per `P-15`, validation command is `pnpm test:e2e`"), and triage rejections ("docs-only per `P-1`").

Cite frequently in the first month — the vocabulary calcifies fast, and once Engineer A writes `P-7` in a PR comment unprompted, the Method has installed itself. At six months, audit: a principle not cited and not visibly violated is either obvious enough to retire or so dormant the workspace is silently violating it.

> **Augmentation Surface — Principle Citation Detection**
>
> Where an agent layer makes this work better: scanning issue and PR comments for `P-#` citations, tallying which are cited, which are dormant, and which appear in violation reports, and surfacing the citation graph as a monthly hygiene signal. The agent also flags completion claims that lack the prescribed evidence — closing without `P-7`'s artifact, or Done without `P-9`'s release evidence.
>
> What the PM keeps: deciding whether a dormant principle should be retired, revived, or rewritten.

The 28 principles fall into nine groups (A–I). The counter-examples are diagnostic: when you see the failure in your workspace, you know which principle was quietly violated.

### Group A — The work graph (the shape)

#### P-1. Linear is the active work graph, not an archive.

**Rule.** Content that does not represent active or imminent execution belongs in a wiki, a `docs/` directory, or a project document — not in Linear.

**Rationale.** Linear is optimized for things that move. Static reference material corrodes the work graph by inflating lists, polluting search, and lowering signal; once a workspace tolerates archival content, every triage decision gets harder.

**Counter-example.** The Operator creates an "Onboarding checklist" issue with sixty items; it sits in Backlog nine months until archived, while three new hires print it from the team wiki.

#### P-2. Initiatives are the objective layer.

**Rule.** Initiatives express durable outcomes that roll up projects, with no deadline tighter than a quarter.

**Rationale.** Projects ship and end; initiatives express the *why* that persists across multiple projects. Tying objectives to projects forces re-derivation every quarter; tying them to initiatives gives Leadership stable headings to recognize across reviews.

**Counter-example.** A team without an initiative layer rewrites OKRs from scratch each quarter; Leadership reads four framings of the same goal across four quarters and concludes the team has no strategy.

#### P-3. Projects are the main execution container.

**Rule.** Issues belong to projects; a project answers what is being built, by when, by whom, with what milestones, and blocked by what — active work without a project is a smell.

**Rationale.** The project is the unit of accountability — where updates accrue, milestones gate progress, and Leadership reads health. An issue outside a project has no parent narrative and cannot be rolled up.

**Counter-example.** Engineer B on the 3-person team opens fifteen issues for "infrastructure cleanup" without a project; the monthly review shows zero progress because no status update captured any of it.

#### P-4. Issues are deliverable-sized.

**Rule.** An issue has a single outcome, defined scope, exit criteria, and one owner; an issue that takes more than two weeks to verify should be split.

**Rationale.** Issues are the smallest unit the Operator and Leadership both reason about. Past two weeks they stop being deliverables and become workstreams — and workstreams are projects, with their own machinery.

**Counter-example.** A "Migrate the auth service" issue stays open three months; no update can say "60% done" because nothing in the work graph represents the 60%.

#### P-5. Documentation owns deep context.

**Rule.** ADRs, design docs, runbooks, and decision narratives live outside Linear, and Linear issues link to them rather than embed them.

**Rationale.** Linear's issue descriptions are not version-controlled, diffable, or discoverable from outside the workspace. Long-form context written into an issue rots and cannot be cited by anyone without the URL.

**Counter-example.** Six months after launch the team cannot reconstruct why a service was built on Postgres instead of DynamoDB; the rationale lived in an issue description archived when the project closed.

### Group B — Evidence and validation

#### P-6. Validation separates implemented from trusted.

**Rule.** Code that is merged is *implemented*; code that has passed runtime, browser, release, infrastructure, or human-acceptance evidence is *trusted* — only trusted code becomes Done.

**Rationale.** The single most load-bearing principle in the Method. Without it, the workspace collapses into a binary — merged or not — and every other principle is reduced to ceremony. Validation is where the Operator catches the gap between "the diff landed" and "the thing works in front of a user"; it is where production incidents are prevented and browser regressions get caught before Leadership notices. Teams that skip Validation discover within a quarter that their Done column is a lie. Validation costs throughput on the leaderboard and buys credibility everywhere else — that trade is the entire game.

**Counter-example.** Engineer A on the 3-person team merges a PR that "fixes the upload bug" and moves it straight to Done; at the weekly review Leadership asks if it was tested on Safari, the issue reopens Monday, and the team starts to fear status meetings.

#### P-7. Evidence beats assertion.

**Rule.** Every claim of completion must point to an artifact — merged PR URL, deploy log, screenshot, document, or acceptance comment from someone other than the assignee.

**Rationale.** "I closed it" is not evidence. Once the team accepts the artifact discipline, Validation becomes self-enforcing — empty Done is Done that will be reopened.

**Counter-example.** Engineer A on the 3-person team closes seventeen issues Friday with no PR links; Monday the Operator cannot tell which shipped, and forensics confirms two did not.

#### P-8. The code host proves implementation.

**Rule.** Merge state, CI results, deploy logs, and runtime evidence live in the code host (GitHub, or the GitLab equivalent) — Linear links to them rather than duplicating them.

**Rationale.** Two sources of truth for implementation status drift instantly. Linear's role is to reference what the code host says, not re-state it — re-statement is where lies enter (the issue says shipped, the deploy log says rolled back).

**Counter-example.** An Operator marks ten issues "deployed" from a Friday status meeting; the deploy rolled back overnight, but Linear still says shipped Monday when Leadership reads the update.

#### P-9. Production work does not go Done before release evidence.

**Rule.** For customer-shipping issues, the Validation → Done transition requires release evidence — runtime smoke plus browser proof, or a deploy log plus an acceptance comment.

**Rationale.** Production-specific corollary of `P-6`. Internal-tool blast radius is the team; customer-facing blast radius is the brand, so the evidence bar is higher.

**Counter-example.** The team marks a customer-facing pricing change Done when the PR merges; three hours later a customer reports the price is wrong because nobody loaded the page after deploy.

### Group C — Workflow canon

#### P-10. The workflow canon is nine states.

**Rule.** The Method's workflow is exactly nine states — Triage, Backlog, Ready, In Progress, In Review, Validation, Blocked, Done, Canceled — and adding states is a smell.

**Rationale.** Every additional state is a decision the Operator makes on every issue, every day. The 9-state canon is the smallest set that preserves the Validation distinction (`P-6`), the queue (Backlog vs Ready), and the obstruction (Blocked); workspaces with thirteen states are workspaces where the Operator has stopped reading the column.

**Counter-example.** A workspace adds "In QA," "Pending Approval," "Soft Launch," and "Awaiting Release" over six months; no two engineers agree on In Review, and Validation sits empty because work routes around it.

#### P-11. Stage labels carry the things that look like states but aren't.

**Rule.** "In QA," "Pending Approval," "Design Review," and similar are not workflow states — they are `stage:*` labels applied during In Progress, In Review, or Validation.

**Rationale.** Sub-stages matter for filtering; the answer is a label, not a state. Labels can be added without breaking the workflow contract, view-filtered without breaking analytics, and team-specific without fragmenting the workspace.

**Counter-example.** A team adds "In Design Review" as a state, then has to redefine cycle-time analytics, retrain every Insights view, and write a migration script — a `stage:design-review` label would have done the same in five minutes.

#### P-12. Prefer parent issues with sub-issues over giant single issues.

**Rule.** If acceptance criteria exceed five items, or implementation spans more than two files or two days, split into a parent issue with sub-issues.

**Rationale.** Giant issues defeat estimation, parallelization, and the evidence chain. A parent-and-children structure preserves the narrative while making each unit independently reviewable, assignable, and verifiable.

**Counter-example.** Engineer B on the 3-person team takes a single issue titled "Implement billing v2"; three weeks later the Operator cannot answer "what's left?" because nine acceptance criteria are not discrete units.

### Group D — The Operator

#### P-13. The Operator owns priority, taste, risk, and real-world commitments.

**Rule.** Priority, taste, risk judgment, and real-world commitments do not delegate — an agent or an Engineer can propose, surface, or draft them, but the Operator decides.

**Rationale.** These four are where being wrong costs trust, money, or outside relationships. An agent can *surface* a drift or *draft* a commitment, but the moment those decisions happen without the Operator's acknowledgment, the team loses the human accountability that makes the structure legible upward.

**Counter-example.** The Operator on the 3-person team lets an agent auto-promote issues from Low to Urgent on customer-mention frequency; by Friday Engineer A has been reassigned to four "urgent" tickets nobody committed to, and a leadership-promised demo slips two days.

#### P-14. Agents are executors, not owners.

**Rule.** Specialist agents can be delegated work, but human ownership stays explicit on every issue via the assignee field — even when a `delegate` field is set to a bot.

**Rationale.** The assignee is the throat to choke; setting the assignee to a bot makes the issue ownerless in any meaningful human sense. The split — assignee=human, delegate=bot — keeps agent productivity while preserving accountability. As agents move from drafting comments to running coding sessions that open pull requests, the delegate can now change the codebase directly — which raises the cost of an ownerless issue, not lowers it. The human assignee owns what the agent ships.

**Counter-example.** A workspace assigns issues to an AI bot user; six weeks later the bot has "owned" thirty issues, two regressed silently, with no human to ask why.

#### P-15. Agent delegation requires acceptance criteria and a validation command.

**Rule.** Setting a delegate on an issue requires a scope comment naming outcome, scope, validation command(s), expected artifact, and repo or file paths.

**Rationale.** Agents fail on under-specified inputs in ways that look superficially fine. Without a validation command, the Operator can only audit by reading the diff line by line — exactly the work delegation was supposed to save. This is sharper for coding-session agents that open pull requests: the validation command is the acceptance test the Operator runs instead of re-reading generated code.

**Counter-example.** The Operator delegates "fix the flaky tests" with no validation command; the agent disables three of them, and the Operator does not notice until a regression ships two weeks later.

### Group E — The operating surface

#### P-16. Labels exist to serve views.

**Rule.** A label not cited by any view is a candidate for deletion — labels are an index, not an organizational scheme.

**Rationale.** Every label is a small tax on every issue creation. The "serves views" test keeps the namespace lean and the Operator's filter vocabulary small enough to remember.

**Counter-example.** A workspace has 240 labels; an audit finds 180 referenced by zero views, created during a single project four quarters ago.

#### P-17. Templates lower the cost of doing the right thing.

**Rule.** Every recurring work type — bug, feature, research spike, production incident, agent delegation — gets an issue template.

**Rationale.** A blank issue invites skipping the structure. A templated issue nudges the creator toward the format the Operator and the validation gate both expect, encoding the Method without anyone having to remember it.

**Counter-example.** The team has no production-incident template; the next outage is recorded as a free-form issue with no severity, no commander, no runtime-evidence link, and the post-mortem takes three times as long.

#### P-18. Locality wins.

**Rule.** Closer-to-the-work guidance is more authoritative — a repo-level convention overrides workspace defaults for that repo, a project description overrides workspace defaults for that project, and an issue's acceptance criteria override project defaults for that issue.

**Rationale.** Global rules are baselines and are wrong in any sufficiently specific context. Locality lets the Method scale across many projects without forcing every project into the same shape — the auth repo can be stricter than the workspace default, and a one-off migration can override the project's normal Done.

**Counter-example.** A workspace globally mandates "every PR must include a benchmark"; a one-line CSS bugfix sits open three days because the engineer is inventing a benchmark for a color change.

### Group F — Cadence

#### P-19. Active projects get a status update every week.

**Rule.** A project with no update for seven days surfaces in a stale-projects view; the cadence is non-negotiable, though the format compresses when there's nothing to say.

**Rationale.** Project updates are the rolling truth-telling that prevents the monthly review from becoming a surprise. The compressible format ("Still in progress, no risks") is the release valve.

**Counter-example.** A project goes four weeks without an update during a steady stretch; in week five it goes At Risk and Leadership is blindsided because the last status they have is from a month ago.

#### P-20. Triage has a seven-day SLA.

**Rule.** By day seven, an item in Triage is classified — accepted, merged, canceled, converted to a customer request, escalated to the Operator, or moved to docs-only.

**Rationale.** Triage is a queue, not a holding pen. Items that sit there become the workspace's unread inbox; the seven-day clock forces a decision even if it's "this is documentation."

**Counter-example.** Triage swells to ninety items over a quarter; the Operator stops opening it, and a P0 customer report sits nine days before anyone notices.

#### P-21. Initiative updates run biweekly; the monthly review rolls initiatives up to Leadership.

**Rule.** Project updates feed initiative updates; initiative updates feed the monthly review; each layer compresses the one below it, and Leadership consumes the top of the stack.

**Rationale.** The cadence pyramid is the Method's reporting structure. Weekly suits the team; biweekly compresses enough to write without re-doing work; monthly fits an executive audience.

**Counter-example.** A team writes weekly updates but never compresses them; Leadership receives forty-seven raw updates in a month and either reads none or reads them all badly.

### Group G — Intake and feedback

#### P-22. Customer feedback does not directly become scope.

**Rule.** A customer request is captured and triaged; conversion to a project or issue is an Operator decision (or, once trust is established, an agent-layer decision routed through a Waiting-on-Operator view).

**Rationale.** Customer feedback is signal, not commitment. Direct conversion is how roadmaps get hijacked by the loudest customer; Triage is where the Operator weighs the request and accepts, parks, or declines.

**Counter-example.** The team installs a feedback widget that opens issues directly into Backlog; six weeks later the backlog is half customer suggestions and the Operator has stopped reading it.

#### P-23. The system of record is Linear.

**Rule.** Two-way sync with external trackers is debt — webhooks in are fine, but bidirectional sync is not.

**Rationale.** Every two-way sync has drift: updates that did not propagate, statuses that overwrote deliberate edits, deletions that left orphans. Single-source-of-truth is harder upfront, dramatically easier downstream.

**Counter-example.** A team installs bidirectional sync between Linear and another ticket system; three months in, the Operator spends a Friday figuring out why an issue is Done in one and Open in the other, and concludes neither can be trusted.

### Group H — System hygiene

#### P-24. The overbuild test.

**Rule.** Before adopting any new feature, label, view, or template, answer five yes/no questions: does it help the Operator decide faster, does it help an executor execute faster, does it preserve evidence we'd otherwise lose, does it reduce repeated PM work, does it make risk visible earlier — four or more yes, adopt; three or fewer, skip.

**Rationale.** Workspace bloat is the failure mode of every PM who likes their tool. The five questions force the Operator to articulate what the new thing buys.

**Counter-example.** The Operator on the 3-person team adds a view "Issues Tagged Frontend" because it seemed useful; six months later it has been opened twice and nobody remembers it.

#### P-25. Verify what you enforce.

**Rule.** Don't enforce a convention you can't check programmatically.

**Rationale.** Manual enforcement scales to one person on one day; programmatic enforcement scales to every PR and every issue without the Operator being the bad cop. If the rule cannot be automated, find a cheaper enforcement point or accept the rule will erode.

**Counter-example.** A workspace adopts "every commit message must include the Linear issue ID"; with no pre-commit hook, compliance drifts from 80% in month one to 30% by month four, and the dependent integration rots.

#### P-26. Capacity commits to seventy percent.

**Rule.** Sprint or cycle planning commits seventy percent of expected capacity; the remaining thirty percent is reserved for unplanned work. Cycles are optional in the Method (Chapter 11); the seventy-percent rule applies to whatever planning horizon the team commits against, whether a cycle, a milestone, or a week.

**Rationale.** Unplanned work is recurring, not a special case. Teams that commit to 100% slip every cycle and learn nothing because the explanation is always "something came up"; teams at 70% finish on time and surface real overcapacity when they finish early.

**Counter-example.** Engineer A and Engineer B each commit to ten points; an incident takes a day and an urgent customer call takes a half-day, and by Friday both have shipped six and the Operator apologizes to Leadership for the third week running.

### Group I — Reporting

#### P-27. Leadership consumes summaries, not raw Linear.

**Rule.** Leadership reads project updates and initiative health — they do not browse the workspace.

**Rationale.** Raw Linear is an engineering surface. Leadership reads it the way an executive reads a database schema: technically possible, practically wrong. The Operator's translation is the value-add.

**Counter-example.** The Leadership Team on the 3-person team asks for "real-time visibility" and gets a board link; they log in once, find it overwhelming, and at the next standup ask the Operator a question any project update would have answered — but the Operator stopped writing them because Leadership "had the board now."

#### P-28. The evidence chain holds.

**Rule.** Initiative health rolls up from project updates, project updates roll up from issue evidence, and issue evidence rolls up from the code host — break any link and the chain collapses into theater.

**Rationale.** Every rollup is only as honest as the layer underneath. Initiative health that ignores project updates is a vibe; project updates that ignore issue evidence are a guess; issue evidence that ignores the code host is a story. With the chain intact, the monthly review is defensible all the way to the merge commit.

**Counter-example.** A monthly initiative report says On Track; project updates have not been written in three weeks, issues have no evidence links, and the Operator cannot trace a single claim to an artifact.

### Closing

Principles are not laws. They are decisions made in advance, written down with numbers, so the Operator does not have to decide them again at 4pm Friday when an issue sits in Validation and Leadership asks why it isn't shipped. The Friday answer is already written. The Operator remembers the number and cites it; the Method makes the number worth remembering.

> **Where this gets hard**
>
> The moment Leadership disagrees with a load-bearing principle — most commonly `P-6`, because they want Done to mean merged, not validated — the Method has to be defended in a calendar meeting against a stakeholder who outranks the Operator. The defense is not technical; it is about which incidents the team is willing to ship into next quarter, and most Operators do not have the seniority or the artifact library to make that argument alone.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: 3524 (slightly over 3500 ceiling; structural floor from 28 principles each with Rule/Rationale/Counter-example labels)
  principle-citations: P-1, P-2, P-3, P-4, P-5, P-6, P-7, P-8, P-9, P-10, P-11, P-12, P-13, P-14, P-15, P-16, P-17, P-18, P-19, P-20, P-21, P-22, P-23, P-24, P-25, P-26, P-27, P-28
  flagged-principle-gaps: none
-->
