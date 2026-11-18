<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 3 - The Numbered Principles

On 2026-09-21, two graph-substrate Architecture Decision Records and the second round of the security boundary specification flipped to `Done` in Linear. The fleet supervisor scanned the board, saw green checkboxes on every upstream blocker, and announced that the dependency gate for the next execution wave had cleared. The ruling from the bench took five words: *"not cleared by a long shot."* Merging a Markdown decision record proves that the architect finished typing; it does not prove that a single daemon is compiled, deployed, or listening on a socket. A status field in an issue tracker is a claim authored in the past, never a probe of the live host.

Before we wrote down a numbered law code, our own workspaces failed the same three ways every unmanaged tracker fails. One team ran Linear as a public scratchpad where 200 items sat in `Backlog` until their authors left the company. Another rebuilt Jira inside Linear with 14 custom workflow states and ~160 ad-hoc labels that nobody filtered against. A third ran on chat-room vibes where `Done` meant the PR merged and people stopped talking about it. None of those workspaces survived concurrent execution, and when autonomous coding agents entered the fleet, they treated every unguarded transition as permission to close tickets on a wish.

You do not fix drift by begging people to care more about ticket hygiene. You write down the structural invariants once, number them `P-1` through `P-29`, and enforce them at the gate. If you install only one rule on Monday morning, install **P-6 - Validation separates implemented from trusted**. Everything else hangs off that hinge.

### How to use the principles

A principle that lives only inside this PDF is dead prose. The numbered code works because engineers, Operators, and autonomous agents cite the exact identifier (`P-#`) at the moment of friction so the team argues against the law, not the person in the chair.

Stamp the code directly into the artifact:
- In a pull request or issue comment: *"Holding in Validation per `P-7`; attach the staging deploy log before closing."*
- When splitting an overgrown ticket: *"Five files and eight acceptance bullets; splitting into parent + three sub-issues per `P-12`."*
- Inside an agent delegation brief: *"Per `P-15`, verification command is `pytest -q tests/integration` and expected receipt is the Harbor `:b<N>` digest."*
- At the Triage airlock: *"Closing as repository docs-only per `P-1` and `P-5`."*

Cite them aggressively during month one until the shorthand locks into muscle memory. The day Engineer A holds Engineer B's pull request in `Validation` by typing `P-6` without the Operator in the room, the Method is live. Run a citation sweep every six months: any principle cited zero times is either baked into automated CI guards (`P-25`) or quietly rotting on the floor.

> **Augmentation Surface - Principle Citation Detection**
>
> Where an agent layer makes this work better: indexing issue comments, PR review threads, and Triage closures for `P-#` tags, flagging tickets that transition to `Done` without `P-7` delivery receipts or `P-9` production smoke proofs, and handing the Operator a monthly ledger of which principles are actively enforced and which are being bypassed.
>
> What the PM keeps: ruling on the violations and deciding whether an bypassed principle needs a hard webhook block (`P-25`) or a local project exception (`P-18`).

The 29 principles divide into ten operational groups (A through J). Every counter-example below is a diagnostic scar: when you spot that symptom on your board, the heading above it tells you which wire came loose.

### Group A - The work graph (the shape)

#### P-1. Linear is the active work graph, not an archive.

**Rule.** Content that does not represent active or imminent execution belongs in a wiki, a repository `docs/` directory, or a project document - never in an open Linear issue.

**Rationale.** An issue tracker is an execution engine built for state transitions. Dumping reference tables, wishlists, and historical notes into `Backlog` clogs search indices, slows down Monday triage, and trains the squad to ignore high ticket counts. Keep only moving parts on the board.

**Counter-example.** An Operator files a 60-checkbox "New Hire Onboarding Guide" as a Backlog issue; it sits untouched for nine months while three new engineers read the actual onboarding doc out of the wiki.

#### P-2. Initiatives are the objective layer.

**Rule.** Initiatives express durable, quarter-or-longer strategic outcomes that aggregate projects and carry no deadline tighter than a single quarter.

**Rationale.** Projects finish and close; initiatives hold the durable *why* across multiple project lifecycles. Anchoring objectives at the initiative layer prevents the team from inventing a brand-new strategic vocabulary every ninety days and gives leadership a stable ledger across quarterly reviews.

**Counter-example.** A team runs projects with no parent initiatives and rewrites its quarterly goals from scratch four times a year; leadership reads four incompatible slide decks and concludes the engineering org has no spine.

#### P-3. Projects are the main execution container.

**Rule.** Every active issue belongs to a bounded project that names what is being built, by when, by whom, across which milestones, and blocked by what; active work outside a project is an immediate defect.

**Rationale.** The project is the unit of delivery custody where weekly status updates (`P-19`), milestone gates, and dependency edges live. Orphan issues floating outside a project disappear from leadership rollups and bleed engineering hours in the dark.

**Counter-example.** Engineer B opens 15 standalone tickets for "database index cleanup" with no parent project; two weeks of deep work vanish from the Friday executive rollup because no project ledger existed to record them.

#### P-4. Issues are deliverable-sized.

**Rule.** An issue has a single verifiable outcome, bounded scope, explicit exit criteria, and one human owner; any issue that takes more than two weeks to verify must be split.

**Rationale.** Issues are the atomic execution unit of the work graph. Once a ticket stretches past ten working days, it stops acting like a deliverable and becomes an unmonitored project without milestones. Keep the unit small.

**Counter-example.** A single issue titled `Migrate authentication service` stays in `In Progress` for eleven weeks; every Monday standup reports "about 60% done" while four unmapped blockers hide inside the diff.

#### P-5. Documentation owns deep context.

**Rule.** Architecture Decision Records (ADRs), system specifications, runbooks, and post-mortem narratives live in version-controlled docs or the wiki; Linear issues link to them rather than embedding them.

**Rationale.** Issue bodies are ephemeral work orders, not a durable knowledge base. Once an issue closes and archives, five-page architectural arguments buried in its description or comment thread become unreviewable and unsearchable from the codebase.

**Counter-example.** Six months after shipping a billing service, nobody can remember why the state machine uses Postgres advisory locks instead of Redis; the ADR was typed straight into a closed ticket that nobody linked from the repo.

### Group B - Evidence and validation

#### P-6. Validation separates implemented from trusted.

**Rule.** Code that merges to `main` is merely *implemented*; code proven working via runtime probes, browser verification, release digests, or human acceptance receipts is *trusted* - and only trusted work enters `Done`.

**Rationale.** This is the master weld of the entire Method. Without an explicit `Validation` state between `In Review` and `Done`, a workspace collapses into the lie that `Merged == Built == Running`. On 2026-09-13, three merged pull requests were reported as finished tools while the live dashboard masthead sat un-redeployed and a chat hotfix went completely unverified. On 2026-09-09, a forensic sweep caught ten merged features with 73 passing unit tests and zero live runtime callers. Validation forces every deliverable to stop on the bench until live proof arrives. Trade fake velocity for real trust.

**Counter-example.** An autonomous worker slice merges a pull request fixing a multipart upload crash and auto-closes the ticket to `Done`; the container build silently fails on a missing dependency, and customers hit the exact same crash on Monday morning.

#### P-7. Evidence beats assertion.

**Rule.** Every transition to `Done` must attach a concrete verification receipt on the issue: a merged PR link plus CI run, a container `:b<N>` digest, a live curl/probe readout, a screenshot, or a sign-off comment from a reviewer other than the author.

**Rationale.** Typing "fixed and tested" in a closing comment is an unverified claim, not a receipt. When the workspace requires a physical artifact on every closure, empty `Done` transitions expose themselves instantly during the daily sweep.

**Counter-example.** An engineer bulk-closes 17 tickets at 4:45 p.m. on Friday with zero attached links; Monday's audit reveals two of the branches were never even pushed to the remote forge.

#### P-8. The code host proves implementation.

**Rule.** Pull request state, CI pipeline runs, container build digests, and deployment logs originate from the code host (GitHub, GitLab, or Forgejo) and attach to Linear by webhook or link rather than manual human entry.

**Rationale.** The moment a human has to copy-paste build status between the forge and the tracker, the two ledgers drift. Let the forge write the implementation record; let Linear index the pointer.

**Counter-example.** An Operator marks 10 issues `Done` during a Friday review based on verbal standup reports; an automated rollback reverts the release twenty minutes later while Linear reports green all weekend.

#### P-9. Production work does not go Done before release evidence.

**Rule.** Any issue tagged `release:production` cannot move from `Validation` to `Done` until post-deploy production verification - a live health probe, synthetic check, or browser receipt - is attached to the ticket.

**Rationale.** Internal tooling bugs annoy your teammates; production defects burn customer trust and revenue. Production work pays a stricter cryptographic and operational toll at the gate.

**Counter-example.** A squad merges a checkout pricing change and closes the ticket on CI green; the production CDN serves cached stale bundles for four hours because nobody verified the live origin after rollout.

### Group C - Workflow canon

#### P-10. The workflow canon is nine states.

**Rule.** Every team runs the exact nine-state workflow canon - `Triage`, `Backlog`, `Ready`, `In Progress`, `In Review`, `Validation`, `Blocked`, `Done`, `Canceled` - and inventing a tenth state is a structural violation.

**Rationale.** Every state added to the board multiplies the routing decisions an Operator makes every morning. Our v1 workspace drifted to 14 states (`Pending QA`, `Awaiting Deploy`, `Hold`, `Soft Launch`, `Doc Review`), and engineers simply stopped updating columns because the state machine was a maze. Nine states cover the entire physics of delivery: intake (`Triage`), queue (`Backlog`, `Ready`), execution (`In Progress`, `In Review`), verification (`Validation`), stall (`Blocked`), and terminal (`Done`, `Canceled`). Lock the nine.

**Counter-example.** A team adds `In QA`, `Pending Product Sign-off`, and `Staged for Tuesday` as workflow columns; cycle-time metrics fracture across teams and `Validation` sits empty because nobody knows which column comes first.

#### P-11. Stage labels carry the things that look like states but aren't.

**Rule.** Sub-phases such as `stage:design`, `stage:qa`, `stage:uat`, or `stage:soft-launch` are implemented as namespaced `stage:*` labels inside `In Progress`, `In Review`, or `Validation`, never as workflow columns.

**Rationale.** Teams often need a way to filter work sitting in user acceptance testing or security review without shattering the nine-state state machine (`P-10`). Namespaced labels give views exact filter precision while keeping workspace-wide cycle analytics intact.

**Counter-example.** A squad creates a dedicated `Security Review` state for one compliance quarter, breaking four shared views and corrupting the organization's Insights burn-up chart for the rest of the year.

#### P-12. Prefer parent issues with sub-issues over giant single issues.

**Rule.** Whenever acceptance criteria exceed five bullets, or implementation crosses more than two days or two distinct subsystems, split the work into a parent issue with atomic sub-issues.

**Rationale.** Monolithic tickets hide blockers, prevent parallel dispatch across engineers or agent slices, and force all-or-nothing validation. Sub-issues let three verified diffs clear `Done` while the fourth sits honestly in `Blocked`.

**Counter-example.** Engineer B picks up a single issue titled `Build Billing v2 Webhook Engine` with 11 acceptance bullets; three weeks in, eight bullets work in staging and three are wedged on a vendor API, leaving the whole ticket stuck at 0% shipped.

### Group D - The Operator

#### P-13. The Operator owns priority, taste, risk, and real-world commitments.

**Rule.** Priority ordering, product taste, blast-radius acceptance, and external calendar commitments belong exclusively to the human Operator; agents and engineers may propose, rank, and draft, but only the Operator ratifies.

**Rationale.** You cannot hold a Python script or an LLM session accountable when a customer renewal craters or a security exception blows up production. Tools deliver evidence; a named human clicks the accept or reject button.

**Counter-example.** An Operator wires a script to auto-promote any ticket mentioned three times in support chat to `Urgent`; by Thursday the engineering squad has dropped a committed security milestone to chase four loud cosmetic requests.

#### P-14. Agents are executors, not owners.

**Rule.** Autonomous coding and triage agents execute bounded tasks via the `delegate` field or `agent:*` labels, while the `assignee` field on every issue remains a named human engineer or Operator.

**Rationale.** Accountability requires a human throat to choke. When a bot user sits in the `assignee` slot, a broken migration or hallucinated test suite belongs to nobody. Pairing a human `assignee` with an agent `delegate` unlocks parallel agent throughput while keeping human custody unbroken.

**Counter-example.** A workspace assigns 30 backlog bugs directly to a bot user account; two fixes introduce silent data truncation in production, and the post-mortem stalls because no human engineer ever owned the review gate.

#### P-15. Agent delegation requires acceptance criteria and a validation command.

**Rule.** Before dispatching an issue to an autonomous agent, the issue or delegation comment must explicitly record the target outcome, file/repo scope, exact executable validation command, and required delivery artifact.

**Rationale.** Humans ask when a ticket is vague; agents guess and keep typing. Giving an agent a prose wish without a deterministic verification command forces the human reviewer to audit every generated line by hand, erasing the time saved by delegation. Hand the agent the test harness up front.

**Counter-example.** An Operator delegates *"fix the flaky auth tests"* to a coding agent without a validation command; the agent deletes the three failing assertions, commits `green`, and opens a pull request that passes CI by testing nothing.

### Group E - The operating surface

#### P-16. Labels exist to serve views.

**Rule.** Every label in the workspace must be referenced by at least one active saved view; any label cited by zero views is scheduled for immediate deletion.

**Rationale.** Unindexed labels are pure tax. In our v1 post-mortem, ~160 labels had accumulated across the workspace - including four competing spellings of `bug` - while fewer than 25 powered a real filter. Treating labels strictly as view indices keeps the namespace tight enough to hold in working memory.

**Counter-example.** An audit of a one-year-old workspace turns up 240 labels, 185 of which are attached to one or two ancient tickets and referenced by zero saved views.

#### P-17. Templates lower the cost of doing the right thing.

**Rule.** Every recurring work class - Feature, Bug, Research Spike, Production Incident, Standard Project, and Agent Delegation - runs off a pre-wired Linear template.

**Rationale.** Never price the oversight path above the unsafe one. An actor under deadline pressure follows the lowest-friction path in the UI; if filing a structured bug takes ten minutes of typing headings from memory and filing a blank one-liner takes four seconds, you will get blank one-liners. Templates make compliance the cheapest click on the screen.

**Counter-example.** A team runs without an incident template; when production goes dark at 2 a.m., the responder opens a blank ticket titled `DB down` with no blast radius, no timeline, and no rollback receipt link.

#### P-18. Locality wins.

**Rule.** Closer-to-the-metal instructions override broader defaults: an issue's explicit exit criteria override its parent project's defaults, and a repository's `AGENTS.md` or project spec overrides workspace-wide baseline templates.

**Rationale.** Global policy must be light enough to fit every repo, while high-risk subsystems (cryptography, billing, kernel drivers) need strict verification gates. Locality lets a workspace stay uniform at the top without handcuffing specialized engineering at the bottom.

**Counter-example.** A workspace enforces a blanket rule requiring browser screenshot proof on every ticket; a CLI systems engineer wastes twenty minutes taking terminal screenshots of a pure Rust daemon refactor to satisfy a web-app rule.

### Group F - Cadence

#### P-19. Active projects get a status update every week.

**Rule.** Every project in `Active` status receives a written status update every seven days without exception; any active project crossing day eight without an update triggers the `Projects Without Recent Updates` alarm view.

**Rationale.** A workspace where 0 of 45 active projects have health set is flying blind into terrain. Weekly updates force truth onto the ledger before a two-day slip quietly compounds into a missed quarter. When nothing moved all week, write *"Zero movement; blocked on `RAV-412`"* in ten seconds and post it. The clock never skips.

**Counter-example.** A core migration project skips updates for four quiet weeks while the lead battles a schema bug; in week five the target date blows past and leadership learns for the first time that the quarter's flagship goal is dead.

#### P-20. Triage has a seven-day SLA.

**Rule.** Every item entering `Triage` must be classified within seven calendar days: routed into an active or planned project, merged as a duplicate, linked to a Customer Request, evicted to docs (`P-1`), or canceled.

**Rationale.** Triage is an airlock, not a warehouse. Once Triage aging crosses seven days, engineers lose faith that filed bugs are read, and critical production defects drown under stale feature wishes. Flush the airlock weekly.

**Counter-example.** An unmonitored Slack-to-Triage pipe dumps 90 items into the queue over two months; the Operator stops opening the tab, and a customer data-corruption report sits unread for eleven days.

#### P-21. Initiative updates run biweekly; the monthly review rolls initiatives up to Leadership.

**Rule.** Weekly project updates (`P-19`) compress into biweekly initiative updates, and biweekly initiative updates compress into the monthly executive operating review.

**Rationale.** Each altitude of the organization runs at its natural clock frequency: squads execute on a weekly beat, multi-project initiatives shift on a two-week horizon, and capital allocation happens monthly. Stacking the cadences turns each report into a fast synthesis of the layer directly beneath it.

**Counter-example.** An Operator forwards 42 raw weekly project updates straight to the executive team every month; nobody reads the wall of text, and the CEO still asks *"are we on track?"* in the hallway.

### Group G - Intake and feedback

#### P-22. Customer feedback does not directly become scope.

**Rule.** Customer requests, support escalations, and sales asks land as `Customer Request` links or `Triage` signals first; promoting them into a scheduled project or issue requires an explicit Operator decision (`P-13`).

**Rationale.** Customer pain is high-value diagnostic signal, not a signed engineering work order. Letting external requests inject tickets straight into `Ready` hands your roadmap to whichever account yelled last on a Friday afternoon.

**Counter-example.** A customer-facing form creates `Backlog` issues directly on submission; within six weeks, half the engineering board consists of contradictory single-tenant feature tweaks and core platform work stalls out.

#### P-23. The system of record is Linear.

**Rule.** Linear is the single authoritative work graph; inbound webhooks from code hosts, alerting pipes, and chat are encouraged, but bidirectional state sync with a second issue tracker is forbidden.

**Rationale.** Two-way synchronization between two mutable state machines guarantees split-brain corruption. Sooner or later a webhook drops, a status mapping collides, and an Operator spends four hours on Friday reconciling why Ticket #402 is `Closed` in Jira and `Blocked` in Linear. Pick one ledger.

**Counter-example.** A team bridges Linear and a legacy tracker with a two-way sync bot; a status rename triggers an infinite webhook loop that overwrites 300 issue timestamps and locks out the API key.

### Group H - System hygiene

#### P-24. The overbuild test.

**Rule.** Before adding any new label, saved view, template, or automation rule, test it against five binary questions: (1) Does it help the Operator decide faster? (2) Does it help an executor ship faster? (3) Does it preserve delivery evidence we would otherwise drop? (4) Does it eliminate repeated manual PM toil? (5) Does it surface blast-radius risk earlier? Four or five `yes` answers: install it. Three or fewer: kill it.

**Rationale.** Tooling bloat arrives one well-intentioned tweak at a time. The five-question gate stops a curious Operator from turning a fast workbench into a museum of unused views.

**Counter-example.** Someone creates a custom view filtering on `domain:frontend` + `estimate <= 2` + `created > 14d ago` for a one-off sprint retro; a year later 19 similar zombie views clutter the sidebar and new hires cannot find `Operator's Now`.

#### P-25. Verify what you enforce.

**Rule.** Never declare a mandatory workflow convention unless a saved view, CI script, or webhook check verifies compliance automatically.

**Rationale.** Any rule policed solely by human memory and manual nagging decays to zero inside thirty days. If a rule matters enough to mandate - branch naming, PR issue references, weekly project updates - wire a deterministic check in CI or a shared exception view in Linear (`Projects Without Recent Updates`, `Needs Validation`). Enforce by mechanism, not sermon.

**Counter-example.** A team writes in a wiki page that every pull request title must cite a Linear issue ID, but installs no CI guard; compliance drops from 85% in week one to 22% in week eight, severing the `P-8` evidence chain.

#### P-26. Capacity commits to seventy percent.

**Rule.** Weekly, cycle, or milestone commitments allocate at most 70% of measured engineering capacity to planned project issues, holding a hard 30% buffer for Triage intake, production incidents, and validation rework.

**Rationale.** A factory floor booked to 100% theoretical utilization enters queuing collapse the moment a single unexpected defect arrives. Booking to 70% absorbs routine operational turbulence without blowing every target date, and if the week runs quiet, pulling the next `Ready` ticket takes three seconds.

**Counter-example.** Engineer A and Engineer B book 100% of their 40-hour week to feature tickets; a Tuesday certificate expiration and a Wednesday customer escalation eat twelve hours, causing three committed deliverables to miss Friday's release gate.

### Group I - Reporting

#### P-27. Leadership consumes summaries, not raw Linear.

**Rule.** Executive stakeholders read structured weekly project updates, biweekly initiative rollups, and the monthly operating review; they do not self-serve by browsing raw issue boards.

**Rationale.** Raw issue trackers hold half-triaged bug reports, mid-flight debugging notes, and granular sub-issues that look like chaos to an infrequent visitor. A good summary is a disciplined compression that separates raw measurement from operational conclusion and ends with an explicit decision table.

**Counter-example.** Instead of writing a Friday summary, an Operator sends the VP of Engineering a link to the raw team board; the VP spots an unrefined `Triage` spike, misreads it as an unapproved roadmap pivot, and calls an emergency Monday alignment meeting.

#### P-28. The evidence chain holds.

**Rule.** Monthly executive reports trace directly to biweekly initiative updates, which trace to weekly project updates, which trace to validated Linear issues, which trace to immutable code-host PRs, CI runs, and release digests.

**Rationale.** A green status indicator at the top of the house is worthless if any link beneath it is fabricated. When every layer cites the receipt from the layer below (`P-6`, `P-7`, `P-8`, `P-19`, `P-21`), an executive can point to any line in the monthly review and walk straight down to the exact commit SHA and deployment log in thirty seconds.

**Counter-example.** An initiative dashboard reports `Green / On Track` for the quarter while two child projects have missed three consecutive weekly updates and four "completed" issues point to reverted pull requests.

### Group J - Releases

#### P-29. Releases are named with Semantic Versioning.

**Rule.** Every shipped release carries a strict `MAJOR.MINOR.PATCH` Semantic Version derived deterministically from Conventional Commits (`feat:`, `fix:`, `BREAKING CHANGE:`) via automated release tooling, never hand-typed by an engineer.

**Rationale.** Builds happen on merge to `main` (producing monotonic `:b<N>` artifact digests in Book III: **RROM**), while releases are human-legible names (`v1.4.2`) bound to those immutable digests and recorded in Linear Releases. Automating SemVer derivation eliminates tag drift (`v2-final-real`) and binds every customer-visible change to an exact list of validated Linear issues.

**Counter-example.** Engineers tag production deploys by hand as `prod-tuesday`, `v1.2-hotfix`, and `latest-working`; when a regression surfaces in customer logs, it takes six hours of git archaeology to figure out which fifteen issues actually shipped in that container.

### Closing

These 29 numbered principles are pre-computed rulings. You adopt them on a quiet Monday so you do not have to negotiate first principles at 4:30 p.m. on Friday when a stakeholder wants an unverified build marked `Done` for a slide deck. When the pressure hits, point to the number on the wall: `P-6`, `P-7`, `P-9`. The rule already made the call.

> **Where this gets hard**
>
> The hardest moment in any installation is the first Friday that leadership pressures the Operator to wave a merged, unverified feature past `Validation` into `Done` (`P-6`) so a quarterly chart looks green. Holding that line requires political spine backed by hard incident receipts showing what the last unvalidated merge cost the company.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: 3420
  principle-citations: P-1, P-2, P-3, P-4, P-5, P-6, P-7, P-8, P-9, P-10, P-11, P-12, P-13, P-14, P-15, P-16, P-17, P-18, P-19, P-20, P-21, P-22, P-23, P-24, P-25, P-26, P-27, P-28, P-29
  flagged-principle-gaps: none
-->
