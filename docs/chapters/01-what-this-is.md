<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 1 - What This Is and Who It's For

We built v1 of this operating model for our own house first, admired the architecture diagram for a week, got bored of the daily sweeping, and looked away. When we finally ran an audit against the live Ravenhelm Linear workspace, the ledger handed back the corpse: **14 workflow states, ~160 labels, and 0 of 45 active projects with a health status set**. The Backlog view returned 217 issues. Twelve had been filed six months earlier in the founder's own voice; the rest had drifted in from Engineer A, Engineer B, and an automated Slack intake pipe bolted onto the workspace during a hopeful afternoon and never opened again. Four projects sat at the top of the tree: two abandoned, one named `misc`, and one doing honest work. When someone asked for the status of the platform build, the answer was a guess dressed up as a sentence. Ninety minutes of clicking through custom view filters produced nothing worth reading aloud. We closed the tab.

Systems that depend on the architect's ongoing enthusiasm rot the day the architect gets busy. An operating model that does not mechanize its own maintenance is just a wiki page waiting to lie to you.

### The spine: why the social layer does not transfer

This book is the first volume of the **Ravenhelm Operations Methodology**, a three-part engineering *dōmbōc* (from Old Norse *dómr* and Old English *dōm*: *what is laid down; the judgment*) comprising **RLOM** (The Work Graph), **RDOM** (The Factory Floor), and **RROM** (The Custody Gate). The machinery across all three books was not hatched in an agile seminar. It came off two live floors where bad state killed real operations.

The first floor was twelve years at TNI running 300+ human operators over XMPP across 15 to 20 concurrent telecom and support contracts. Running a floor at that scale teaches you fast that orchestration is not a ceremony problem; it is queue management, load shedding, routing, ISP escalation, and real-time scatter-gather. When a fiber cut spiked call volume out of upstate New York, one broadcast went into the room - *"Spike in volume out of Rochester - if you have a call from there, send me the BTN and the issue"* - and fifty simultaneous replies fanned back into a single human reducer to isolate the trunk fault in ninety seconds. To rule at speed across twenty contracts without losing the room, the record had to be admissible against the person in the chair. Operators had standing permission to screenshot a past offhand ruling in chat and paste it back when a new ruling contradicted it. I learned to not argue with myself. Responsibility cannot be mandatory below and theatrical above.

The second floor was counterintelligence for the J3B capital fleet, where building, flying, and commanding capital ships inside one alliance meant a single compromised pilot through the door ended a war. Every applicant handed over full API keys; we read employment histories for quiet gaps and cross-referenced wallet journals at 3 a.m. Two structural laws came out of those nights. First: **tools deliver evidence, but ultimately I was the one who clicked the accept/reject button**. Automation parses the ledger, flags the anomaly, and stacks the receipts on the bench, yet accountability always chains to a named human actor. Second: separations of power exist to make innocence demonstrable, not merely to catch a thief. When producer, commander, and witness sit in one undivided pool, nobody can prove who verified the gate.

Then we brought those exact control structures to a fleet of autonomous AI coding sessions, and hit the seam that defines this trilogy: **the control structures transfer from humans to AI agents; the social layer does not.**

A human operator on XMPP self-heals from a slightly ambiguous brief, asks a clarifying question when the schema looks wrong, and feels a flash of shame when caught pasting a lazy status update. An autonomous agent has no conscience, no fear of a screenshot, and no common sense outside its token window. Agents fail literal, brittle, and silent. Left without hard mechanical gates, an agent marks a Linear issue `Done` when a pull request merges even though the service is crashing in production; routes around a path-protection hook by spawning `python3 -c` with shell redirection; and verifies a corrupted database restore by comparing two empty strings (`"" == ""`) and printing `matches backup ()` with exit code `0`. What 300 humans enforced by social contract and chat screenshots, an agent-augmented engineering organization must enforce by physics:

- **Book I: RLOM (The Work Graph)** governs declared intent, workflow states, and validation receipts in Linear so the planning ledger never lies about what is running.
- **Book II: RDOM (The Factory Floor)** governs concurrent human and agent execution via the Ehwaz Doctrine: dependency-wave DAGs, isolated git worktree custody (`1 PR = 1 branch = 1 worktree`), and surgical context retrieval.
- **Book III: RROM (The Custody Gate)** governs immutable `:b<N>` artifact builds, three-rail deployment custody, live reachability verification, and zero-ambient privilege elevation so production matches the ledger.

### Who this is for

You are a single technical PM or engineering lead - the **Operator** - running a 3-person unit (the Operator, Engineer A, and Engineer B) and reporting up to a leadership team that wants trustworthy status without logging into your tracker. You know enough to configure Linear, wire up the GitHub, GitLab, or Forgejo webhook, write label rules, and enforce a state machine. You do not have three weeks to invent an operating model from scratch, and you already know what happens when a workspace runs on ad-hoc habits. We built the wrong one first and scraped the scorch marks off the bench. What follows is the working hardware.

The same structure scales cleanly to a 5- or 6-person squad, or a staff engineer holding the PM seat alongside code delivery, and expands across a 30-person multi-team organization without changing the underlying schema. Below two engineers and a contractor, the structural tax outweighs the yield; stay on a single flat Backlog view and a repository `docs/` folder until the seams split.

One team topology runs the graph in reverse: an internal operations, platform, or PMO unit whose board consists entirely of external requests. Core engineering teams are *supply-side* (they author and sequence their own board); service teams are *demand-side* (work arrives through an intake funnel). **Appendix A** rewires the front door - intake queues, dwell-time clocks, and service-catalog routing - without touching the shared execution core.

You need administrative access to Linear to install this book. You do not need an enterprise contract. Ten of the fourteen chapters run today on **Linear Free**. Chapters 7, 8, and 9 map the exact operational ceilings where Basic, Business, and Enterprise earn their seat price, treating tier boundaries as diagnostic load indicators rather than artificial paywalls.

### What the Method is

The Ravenhelm Linear Operating Method (RLOM) is a tiered, receipt-driven operating model built directly inside Linear's native primitives. Three load-bearing rules hold it up.

**Tiered by real operating friction.** RLOM steps across four capability tiers - Free, Basic, Business, and Enterprise - aligned one-to-one with Linear's billing boundaries. A 3-person team installs the spine on Free in seven days: initiatives, Customer Requests, cycles, Releases, Pulse, and the nine-state workflow canon all run at zero license cost. Basic adds zero workflow primitives; it simply lifts the 2-team and 250-issue caps when headcount grows. Business unlocks the automation and intelligence layer: Insights, Triage Intelligence, Asks, SLAs, and native agent delegation surfaces (`agent:coding-agent`). Enterprise governs federation across a fleet of teams via SAML SSO, SCIM provisioning, sub-teams, and portfolio Dashboards. Never upgrade a tier on a calendar schedule; upgrade when a specific queue fractures under load.

**Human-accountable at every gate.** The Operator owns priority, taste, risk, and real-world commitments (`P-13`). No cron job, webhook, or autonomous agent decides what matters next or certifies its own work as trusted. Agents surface drift, draft scope packets, and open pull requests; the Operator clicks the accept or reject button. Heavy enterprise frameworks like SAFe reorganize humans to serve the ceremony and then spend six months negotiating with reality. RLOM locks the workspace around the Operator's judgment and forces the tool to carry the receipts.

**Built on native silicon, not sidecars.** Initiatives, projects, issues, saved views, Triage, weekly project updates, code-host webhooks, and Releases do all the work. RLOM builds no shadow spreadsheets, no bidirectional sync bridges (`P-23`), and no custom-field bureaucracies that fight the schema. Initiatives hold quarter-scale outcomes (`P-2`). Projects hold bounded execution programs (`P-3`). Issues hold single-owner deliverables verifiable inside two weeks (`P-4`). Linear is the live work graph (`P-1`), never a museum; if an item is not moving toward production, evict it to a repository `docs/` tree or wiki.

### The shape, briefly

Chapter 2 lays down the seven operating layers that prevent work from collapsing into a flat pile: initiatives, projects, issues, views, intake, delivery evidence, and analytics. These seven layers operate like different clock frequencies on the same board. Engineers touch issues and delivery evidence continuously as commits land and pipelines run. The Operator sweeps intake and operational views daily, writes project updates every Monday (`P-19`), updates initiative health biweekly (`P-21`), and compiles analytics for leadership once a month. When the code host pushes merge and deploy receipts straight into the issue (`P-8`), evidence travels upward without a human acting as a copy-paste clerk.

Chapter 4 defines the PM Operator seat and its five-rung practice ladder, tracing the climb from a ticket Clerk who merely records what already happened up to an Operator who runs the dispatch board and a Chief of Staff who writes the rules across teams. Most workspaces operate at Rung 1 or Rung 2 because their tooling forces the PM to play secretary. RLOM is engineered to put you on Rung 3 inside thirty days and Rung 4 inside two quarters.

### The promise

Install the Free tier on Monday and the workspace stops bleeding by Friday. Within two weeks, every active project emits a structured weekly update that leadership reads without asking for a status meeting (`P-27`). Within three weeks, your state machine separates code that merely merged from code proven alive in the target environment (`P-6`) - the Validation gate in Chapter 10 that almost every naive workspace skips and pays for in production regressions. Within one quarter, the work graph generates more operational signal than you spend maintaining it. When leadership asks where the platform work stands, you won't spend ninety minutes building a view and closing the tab. You will read two sentences off the top of the Monday ledger.

The Method is a mechanical contract. You bring the judgment and one week of installation discipline; the schema brings the containment walls that keep a 14-state, 160-label garbage fire from ever growing back. Keep the ledger honest.

> **Augmentation Surface - Workspace Onboarding**
>
> Where an agent layer makes this work better: running a cold-start diagnostic sweep across an existing workspace before you touch a single setting - counting zombie Backlog issues, measuring the age of the oldest untriaged ticket, listing active projects with `0` health updates in the last 30 days, flagging unassigned in-flight work, and enumerating orphan labels cited by zero saved views (`P-16`). The agent dumps the forensic inventory onto the bench in thirty seconds so the Operator doesn't waste an afternoon clicking through dead tabs.
>
> What the PM keeps: deciding which wreckage gets cut in week one, which projects get killed outright, and which legacy noise gets quarantined until the core spine is running.

### What this is not

This is not an autonomous agent harness or a prompt pack. The Augmentation Surface callouts in each chapter mark the exact seams where an AI agent layer takes mechanical translation off the Operator's plate, while Book II (**RDOM**) details the worktree and wave-dispatch physics for running an agent fleet. Confusing your issue tracker with your prompt library gives you a workspace organized around bot chatter rather than shipped software.

This is not a vendor brochure for Linear. We standardized on Linear because its native object model matches the seven layers without custom-field surgery. If your current tracker enforces those seven layers cleanly, keep it. If you are evaluating tools, test whether they can enforce the nine-state workflow canon (`P-10`) and the code-host evidence chain (`P-28`) without plugins.

This is not an agile transformation. There are no story-point poker sessions, no 60-slide maturity decks, and no steering committees. Open the workspace, cut the dead states, wire the views, and enforce the Validation gate. It works in thirty days or you tore it out.

> **Where this gets hard**
>
> A single Operator can install this spine for one squad in a week. The friction multiplies when you add a second engineering team, inherit a workspace already choked with ~160 ad-hoc labels and three years of unlinked tickets, or need verifiable evidence chains spanning multiple repositories, CI pools, and release pipelines (`P-28`). At that altitude, workspace setup stops being a settings change and becomes distributed systems integration.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (Chapter 1 has no chapter-type extras)
  word-count: 1945
  principle-citations: P-1, P-2, P-3, P-4, P-6, P-8, P-10, P-13, P-16, P-19, P-21, P-23, P-27, P-28
  flagged-principle-gaps: none
-->
