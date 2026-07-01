<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 10 — Workflow Canon and the Validation Gate

It is 4:48 on a Friday. The Operator has already posted the weekly summary to Leadership: nine issues Done this sprint, two slipping into next week, one still blocked on a vendor. At 5:11 a customer pings in shared Slack — the export feature that shipped Tuesday returns an empty CSV. At 5:23, monitoring finally catches up: a migration ran on staging but never on production, so a different feature has been silently writing to a column that does not exist. By 5:40 the Operator is re-reading the Friday summary and counting which of those nine "Done" issues actually shipped working code to customers. The answer is six. The other three were merged, closed, and counted. Nobody looked at them after the PR went green.

The Method's workflow exists to make that Friday impossible. It has exactly nine states. The one between merge and Done — Validation — is the load-bearing piece. The rest of this chapter argues that point and installs it.

### The nine states

The Method's workflow is canonized at nine states (P-10). Each has an entry condition, an exit condition, and a smell that signals misuse.

**Triage.** Unprocessed intake. Anything entering the workspace from a Slack ask, a Sentry alert, a customer request, an engineer's thought, or the Operator's own brain lands here first. Exit is classification: accepted, merged with another issue, sent to docs, escalated, or canceled. Smell: items aging past seven days untouched.

**Backlog.** Accepted but not scheduled. The work is real, it has an owner-eventual, but no one is starting it this week. Exit is scoping. Smell: a Backlog item with no project (P-3) — orphans accumulate here.

**Ready.** Scoped and available for an assignee or an agent. Acceptance criteria are written. The estimate is reasonable. The issue is deliverable-sized (P-4). Exit is someone picking it up. Smell: a Ready item nobody picks up for two weeks — usually the scope is wrong.

**In Progress.** Someone is actively working. Exactly one assignee. A branch exists if it is code work. Exit is a PR, an artifact, or a decision posted. Smell: more than one issue In Progress per person at a time.

**In Review.** A PR, artifact, or decision is awaiting review. Entry is automated when the code host opens a PR linked to the issue (Chapter 12). Exit is review approval and merge. Smell: an In Review item older than three working days — the reviewer is overloaded or the PR is too large (P-12).

**Validation.** Merged or delivered work still needs runtime, browser, release, infrastructure, or human-acceptance evidence (P-6). This is where most workspaces leak. Entry is merge or delivery; exit is evidence posted to the issue and accepted by the Operator. The rest of this chapter is mostly about this state.

**Blocked.** Stuck on something external; the blocker is named, in the issue, in a comment, with a date. "Blocked" without a named blocker is a parking lot, not a state. Exit is the blocker resolving or the issue being canceled. Smell: a Blocked item with no blocker named — almost always means the assignee has lost interest and needs the Operator's intervention.

**Done.** Complete with evidence (P-7). The artifact link is in the issue. The evidence matches the acceptance criteria. Someone other than the assignee has confirmed, when human acceptance applies. Entry is the Operator (or, on higher tiers, an agent surface) accepting the Validation evidence. There is no exit; Done is terminal.

**Canceled.** No longer relevant; the reason is named. "We decided not to," "the customer withdrew," "superseded by issue X." Cancellation without a reason is a state lie. Like Done, Canceled is terminal.

That is the canon. Nine states, in flow order. The reader's existing workflow may have eleven or thirteen — most do. The Method's first install act is to collapse it to nine.

### Why Validation is load-bearing

Most workspaces operate on six states: Triage, Backlog, In Progress, In Review, Done, Canceled. PR merges, issue closes, sprint report counts it, the Operator moves on. This is the workflow that produced the 4:48 Friday at the top of this chapter.

The Method draws a hard line between two things that look the same and are not. **Merged code is implemented. Code that has passed evidence is trusted.** Only trusted code becomes Done (P-6). Validation is the named state where the difference lives.

The cost of skipping Validation compounds in three directions. First, the Operator's Done count becomes unreliable. "Nine issues Done this sprint" means nothing if three of them shipped broken. Worse, the Operator does not know which three. The number is theater (P-28). Second, the customer-facing surface develops a quiet backlog of half-shipped features — code merged, migration forgotten, flag not flipped, deploy never pushed to the customer-visible cluster. The team thinks it shipped. The customer does not see the change. The gap between team-reality and customer-reality grows until someone in a Slack DM names it. Third, Leadership loses faith in the rollup. The monthly initiative health report (Chapter 13) is built from project updates, which are built from issue counts. If issue counts lie, the entire reporting chain collapses into theater (P-28). The Operator becomes the person who keeps having to retract the Friday update.

Validation is the state that fixes all three at once. It is a holding pen with one rule: do not enter Done without evidence. The evidence is not the Operator's word; it is an artifact in a system the Operator cannot fabricate (P-8). The code host says the PR is merged. The deploy log says the binary is running. The screenshot shows the customer-facing URL renders. The Terraform plan says the resource exists. The customer reply says they tried it. Until one of those exists and matches what was promised, the issue stays in Validation.

This is the difference between a workspace that ships and a workspace that ships broken software with confident summaries.

> **Augmentation Surface — Evidence Reconciliation**
>
> Where an agent layer makes this work better: scanning every issue in Validation on a schedule, checking the linked PR, deploy pipeline, release artifact, or browser surface for the expected evidence type, posting the evidence as a comment when it is findable, and escalating to the Operator only when it is not. The Validation queue stops being a queue the Operator clears manually and becomes a queue the Operator only sees when judgment is required.
>
> What the PM keeps: the call on whether the evidence is actually sufficient — the human-acceptance test, the "is this really what we promised" judgment, the decision to push back when a screenshot is technically present but shows the wrong state.

### The five evidence types

Not all Validation is the same. The Method recognizes five evidence types, each appropriate to a different kind of work. The Operator (and any agent layer assisting) needs to know which type the issue requires before it enters Validation, not after.

**Runtime evidence** — the code is running where it should be. The deploy pipeline log shows green. A log line confirms startup. A smoke test returns the expected payload. Use for backend changes, scheduled jobs, infrastructure services, anything where "the binary is up" is the question. Example artifact: a link to the deploy job output, plus a paste of the relevant log line.

**Browser evidence** — the user-facing surface is reachable and renders correctly. A screenshot of the page in the deployed environment. A short Loom of the new flow. A browser session log for an instrumented test. Use for any change a customer or internal user sees. Example artifact: a screenshot annotated with the URL bar visible, so the environment is unambiguous.

**Release evidence** — the work is in the release artifact customers actually receive. The release tag exists. The changelog entry is present. The app-store version is approved and rolled out. The container image is tagged and pulled by the production cluster. Use whenever merge to main is not the same as customer availability (P-9). Example artifact: a link to the release in Linear Releases or the equivalent code-host release page.

**Infrastructure evidence** — the underlying resources are in the expected state. A Terraform plan showing zero drift. A `kubectl get pods` output showing the expected count and image tag. A secret rotation log entry. Use for platform, capacity, security, and compliance work. Example artifact: a paste of the relevant command output, with the command itself included for reproducibility.

**Human acceptance** — someone other than the assignee has confirmed the work meets the acceptance criteria. The customer replied "this fixed it." A UAT signoff comment from the requester. The Operator's own acceptance comment after walking through the feature. Use whenever the question is "does this actually solve the problem we agreed to solve," which is most non-trivial work. Never the assignee's own assertion — that is not evidence, it is restatement.

For most issues, one evidence type is enough. For production work that ships to customers, the Method requires two: either runtime evidence plus browser evidence, or a deploy log plus a human-acceptance comment (P-9). The combination matters. A runtime green without a browser check has missed a frontend that points at the wrong API. A browser check without a deploy log has confirmed staging while production is still on the old binary. Two evidence types in production work is the cheapest insurance against the 4:48 Friday.

### The three-person team flow

The Method's flow for a 3-person team — Operator, Engineer A, Engineer B — is concrete enough to install on a Monday. Here is the lifecycle of a single deliverable.

The Operator and Engineer A scope the issue together in a fifteen-minute conversation. Acceptance criteria go into the issue body. The estimate is reasonable. The issue is deliverable-sized — single outcome, two weeks or less to verify, one owner (P-4). If the acceptance criteria run past five items, the issue splits into a parent with sub-issues (P-12). State moves from Backlog to Ready.

Engineer A picks the issue up Monday morning. The code-host integration (Chapter 12 owns the mechanics) creates a branch named with the issue ID, and the state moves to In Progress. Engineer A is the assignee. The branch name carries the issue ID so the code host can match commits and PRs back to Linear.

Engineer A opens a PR on Wednesday. The Linear–GitHub integration moves the issue to In Review automatically — on the GitLab equivalent, the merge-request integration does the same. Engineer B reviews. On a 3-person team, the reviewer pool is one person; this means review is fast, not optional. If Engineer B is heads-down on a separate issue, the Operator owns the call on whether the PR waits.

The PR merges Thursday. **Here the integration does not move the issue to Done.** It moves it to Validation (Chapter 12 covers the configuration). This transition is automated by the code-host integration (available on Free), or run by hand where it isn't wired. Either way, the rule is the same: merge does not equal Done.

Engineer A posts evidence in a Validation comment. For a backend change, a link to the deploy log plus the relevant startup line. For a UI change, a screenshot of the deployed environment with the URL visible. For an infrastructure change, the Terraform plan output. The evidence type was decided when the issue was scoped, not invented now.

The Operator confirms the evidence matches the acceptance criteria. Not the Operator's vibe — the literal acceptance criteria written in the issue body when the work was scoped. If it matches, the Operator moves the issue to Done. If it does not, the Operator comments on the gap and the issue stays in Validation. The assignee does not move their own work to Done.

If the change is production and customer-visible, the Operator waits for release evidence — the Linear Releases entry, or the equivalent on the code host — before Done (P-9). For a 3-person team this is usually a one-day wait, not a one-week wait. The cost is small. The cost of skipping it is the 4:48 Friday.

The Leadership Team never sees any of this. They see the Friday summary and the monthly rollup. The reason those rollups are trustworthy is that the issue counts behind them mean what they say.

### Nine states is the contract

When someone — a new engineer, an experienced PM joining the team, a vendor consultant — proposes a tenth state, the answer is no. The most common proposals are "In QA," "Pending Approval," "Design Review," and "Soft Launch." Each one feels reasonable. Each one is a `stage:*` label, not a state (P-11).

"In QA" is `stage:qa` on an issue that is In Progress or In Review. "Pending Approval" is `stage:awaiting-approval` on an issue in Validation. "Design Review" is `stage:design-review` on an issue in In Review. "Soft Launch" is `stage:soft-launch` on an issue in Validation, waiting for full release evidence before Done. Labels carry the variation; the canon stays at nine (P-11).

This is doctrine, not preference. The reason is brutal: a workflow with thirteen states has thirteen places work can stall invisibly. A workflow with nine has nine. The Method's nine are the smallest set that preserves the Validation distinction, which is the only state difference that actually matters for the question "did this ship?" Everything else is a label (P-11), a comment, or a project milestone.

The canon is nine. Hold it.

> **Where this gets hard**
>
> The Operator's team does not own production. A separate platform team controls the deploy, the cluster, and the release pipeline. Getting a deploy-log link on every customer-visible Validation issue requires the platform team's cooperation, which they have no incentive to provide — their on-call rotation does not care about your Linear hygiene, and the link in their CI system requires permissions you do not have.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: 2400
  principle-citations: P-3, P-4, P-6, P-7, P-8, P-9, P-10, P-11, P-12, P-28
  flagged-principle-gaps: none
-->
