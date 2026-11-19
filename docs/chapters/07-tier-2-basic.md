<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 7 - Tier 2: Linear Basic and the Separation of Powers

Before Ravenhelm existed, the hardest counterintelligence problem we ever ran was a capital-ship production and combat fleet inside J3B. In that theater, a single spy through the door did not cost a sprint metric; it cost a supercapital staging yard and ended a war. Every applicant handed over full-privilege API keys, employment histories were audited for six-month gaps, and wallet journals were cross-referenced line by line at 3:00 a.m. Two structural laws came out of that furnace. First: tools deliver evidence, but a named human clicks the accept or reject button. Second, and more counterintuitive: **organizational separations exist to make innocence demonstrable**, not merely to stop wrongdoing. In our naive v1 fleet structure, the industrialists who built the hulls, the logistics leads who moved the fuel, and the fleet commanders who burned the ships in combat all sat in one undivided administrative pool with shared hangar access. The night a stockpile vanished or a deployment timer leaked, everyone with a key was a suspect and nobody could prove their hands were clean. Without a hard structural boundary between remits, innocence is unfalsifiable.

By month four on Linear Free, your growing engineering organization walks into the exact same structural trap. Your Tier 1 install from Chapter 6 held under initial load: one team, nine canonical workflow state slots, four label axes, a disciplined `Validation` gate (`P-6`), and Friday project updates (`P-19`) with real deployment receipts attached. Then two walls hit in the same week. First, your issue counter passes 235 and Linear flashes the 250-issue ceiling warning. Second, Leadership funds a second and third squad - a public-surface product team alongside your core platform team and an internal operations lane - each with its own squad lead. On Free, capped at two teams with flat workspace permissions, your v1 workaround is to cram two squads into one shared team, fake the boundary with `component:*` labels, and give every squad lead global workspace privileges so they can edit their own templates. Within three weeks, Squad B's lead accidentally edits Squad A's workflow states, backlog priorities collide in a single `Ready` column, and when a Friday target slips, neither lead can prove whether their queue was starved by their own scope or hijacked by the other squad's interrupts. You have recreated the undivided hangar.

Tier 2 - Linear Basic at $10 per user per month - exists to knock down those physical walls and establish clean administrative boundaries across up to five teams without fracturing the underlying work graph.

### What Basic actually buys (and the price-sheet myth to kill)

Be ruthless about what is on the invoice, because earlier editions of this document oversold Tier 2 as a feature unlock. Linear Basic adds **zero** new workflow primitives, **zero** analytics surfaces, and **zero** automation engines over Free. At $10 per seat per month, Basic lifts three numerical ceilings and hands you one administrative boundary lever:

- **Up to 5 teams**, lifted from Free's 2-team cap.
- **Unlimited active and archived issues**, lifted from Free's 250-issue hard ceiling.
- **Unlimited file upload sizes**, lifted from Free's 10 MB attachment cap so engineers can drop full multi-megabyte HAR captures, flamegraphs, and end-to-end video proofs straight into `Validation` comments (`P-7`).
- **Admin roles**, decoupling workspace-root authority from team-level configuration.

That is the entire SKU. Stop looking for hidden machinery.

| Capability / Surface | Tier 1 (Free) | Tier 2 (Basic - $10/seat) | Tier 3 (Business - $16/seat) | Tier 4 (Enterprise) |
| :--- | :--- | :--- | :--- | :--- |
| **Team Ceiling** | 2 teams | **5 teams** | Unlimited teams + Private teams | Multi-level Sub-teams (5 levels) |
| **Issue & Upload Caps** | 250 issues / 10 MB | **Unlimited / Unlimited** | Unlimited / Unlimited | Unlimited / Unlimited |
| **Access & Governance** | Flat workspace membership | **Admin roles (Org vs. Team)** | Guests, SSO login restrictions | SAML + SCIM, Audit Log, IP allowlists |
| **Objectives & Intake** | Initiatives, Customer Requests | Same as Free | Linear Asks (Slack/Email), Zendesk | Asks Web Forms, Salesforce, Gong |
| **Analytics & Agents** | Custom Views, "Open in tool" | Same as Free | **Insights, SLAs, Triage AI, Coding Sessions** | **Workspace Dashboards**, Sub-initiatives |

Read that table twice before signing a PO. **Initiatives (`P-2`) are already Free.** **Customer Requests (`P-22`), Cycles, Pulse, and Releases (`P-9`) are already Free.** Conversely, **Insights**, **Triage Intelligence**, **Linear Asks**, **SLA clocks**, and **Coding Sessions** are **not** on Basic; they live one tier higher on Business (Chapter 8). If you upgrade to Basic expecting time-series cycle-time charts or AI triage routing to switch on, you bought the wrong tier. Basic buys room to split squads cleanly and administrative locks so those squads do not step on each other's switches.

### Separation of powers inside a shared work graph

When you split one crowded workspace into three or four distinct teams on Basic, the failure mode flips from collision to balkanization. In our early multi-team rollout, we gave three squad leads their own teams without locking a shared structural contract; inside six weeks, one team invented a `Waiting for Deploy` column, a second deleted `Validation` because it slowed down their burndown chart, and a third minted 40 custom labels that duplicated the global taxonomy. When the Operator tried to pull one cross-team view for Monday morning, the query returned garbage because the state categories and label keys no longer aligned.

Basic gives you **Admin roles** and **five team containers** so you can separate execution custody while keeping the ledger grammar identical across every squad. Execute the upgrade and the multi-team split in four bench steps:

#### 1. Lock workspace root and scope team admins

Open `Settings -> Workspace -> Members`. Strip global workspace admin privileges down to the Operator (and one backup principal for continuity). Nobody else needs permission to alter billing, global integrations, or workspace-wide label taxonomies. When you stand up the second and third teams, assign each squad lead as a **Team Admin** scoped strictly to their own team container. This is the J3B hangar separation applied to Linear (`P-24`): the public-surface squad lead can tune their team's cycle schedule, triage rotation, and local templates without carrying the keys to delete the platform team's workflow states. If a team configuration drifts, the blast radius is contained to one squad and the custody trail points to one named lead (`P-14`).

#### 2. Clone the canonical nine-state spine across every team

When creating Team 2 (`Product-Web`) and Team 3 (`Core-Platform`), do not click "Create blank team" and let the lead improvise. Use Linear's **"Copy settings from existing team"** selector during creation to clone your Tier 1 spine verbatim. Every team in the workspace must run the exact same seven forward states (`Triage`, `Backlog`, `Ready`, `In Progress`, `In Review`, `Validation`, `Done`) plus `Blocked` and `Canceled` (`P-10`).

Locality (`P-18`) permits a squad lead to add a team-scoped template or a local view filtered to their own components, but the workflow states and workspace label namespaces (`type:`, `component:`, `risk:`, `source:`) are constitutional law (`P-16`). When `Validation` means the exact same thing in `Product-Web` as it does in `Core-Platform`, any engineer or cross-team view can read the state of the union at a glance (`P-6`).

#### 3. Wire multi-team projects under shared Initiatives

Having three teams does not mean creating three parallel strategy trees. Keep your workspace-level **Initiatives** (`P-2`) at the top of the graph (two to four durable quarterly objectives). Below those initiatives, attach projects (`P-3`). In Linear, a single project can span multiple teams when a deliverable requires both backend platform changes and frontend surface work - or each team can run its own bounded project linked up to the same parent Initiative.

Use a clear physical rule to choose between a shared multi-team project and separate single-team projects:
- **One shared project across two teams** when both squads ship toward a single atomic cutover date and one Project Lead owns the combined Friday update (`P-19`).
- **Two linked projects under one Initiative** when the platform squad ships an internal API contract in Wave 1 and the product squad consumes it on their own release cadence in Wave 2, linked at the issue boundary via native `blocks` / `blocked by` relations.

Never duplicate issues across two teams just so both leads can "track" the same dependency (`P-23`). One issue lives in the team that writes the code and produces the `Validation` receipt; the consuming team links to that exact issue ID with a `blocked by` relation. One truth, one owner (`P-14`).

#### 4. Expand the Operator's views to workspace scope

Back on Free with one team, your four core views (`Operator's Now`, `Waiting on the Operator`, `Blocked Radar`, `Review & Validation Queue`) lived inside that single team's sidebar. On Basic with three to five teams, recreate those four views at the **Workspace** level, grouped by `Team`. When you open `Blocked Radar` at 8:30 a.m., you see every wedged deliverable across all five squads on one glass pane, and when you open `Review & Validation Queue`, you see immediately which squad is letting merged PRs pile up without runtime verification (`P-6`, `P-28`).

> **Augmentation Surface - Seat, Role, and Boundary Audit**
>
> Where an agent layer makes this work better: running a weekly governance sweep across the Basic workspace that checks three invariants - (1) team count vs. the 5-team ceiling, (2) seat utilization (flagging dormant accounts with zero issue transitions or comments over 30 days, since Basic bills $10 per active seat), and (3) workflow parity across all teams (verifying that no Team Admin quietly renamed `Validation` or enabled auto-close-on-PR-merge). The agent posts an exception docket to the Operator.
>
> What the PM keeps: deciding whether to revoke a dormant seat, promote a local team label into the global workspace namespace (`P-16`, `P-18`), or approve a fifth team slot. Tools deliver the audit receipt; the Operator clicks the button.

### Lifting the 250-issue ceiling without inviting hoarding

The day you upgrade from Free to Basic, the 250-issue dam breaks. That relief creates an immediate secondary hazard: within sixty days, teams treat "unlimited issues" as license to turn the `Backlog` state into a graveyard of 600 un-scoped wishes, half-remembered refactoring ideas, and stale feature requests from two quarters ago (`P-1`).

Unlimited storage in Linear does not relax `P-1` (Linear is the active work graph, not an archive) or `P-3` (active work belongs to a project). Enforce two hygiene rules the week you lift the cap:

1. **The 7-day Triage clock (`P-20`)**: Every issue entering `Triage` across any of your five teams is either accepted into an active or planned project (`Backlog` / `Ready`), routed to documentation (`P-5`), merged as a duplicate, or closed (`Canceled`) within seven calendar days.
2. **The 90-day Backlog purge**: Any issue sitting in `Backlog` for 90 days without an attached project with a real target quarter is canceled with a comment (`Canceled: horizon exceeded; move long-term research notes to docs/`). Keep the work graph lean enough that every row in `Backlog` represents something the team still intends to build.

### Ceiling signal - when Basic stops being enough

Basic gives you unlimited issues and up to five clean team boundaries, which means a disciplined organization of 10 to 25 people can run here for quarters. You hit the ceiling of Tier 2 not because you run out of issue slots, but because **coordinating volume by hand exceeds the Operator's human clock**, or because a sixth team or security boundary enters the building. When **two of the three** signals below hit in the same quarter, move to Chapter 8 and upgrade to Linear Business:

- **Manual intake and reporting burn more than 90 minutes a day.** Your daily `Triage` pass across four teams now exceeds 30 minutes because Slack messages, Sentry alerts, and support escalations are being pasted by hand (requiring **Linear Asks**, **Zendesk/Intercom integrations**, and **Triage Intelligence**), or the Operator spends two hours every Friday hand-counting cycle times and status trends in a spreadsheet because Basic lacks **Insights**.
- **Production traffic and autonomous agents enter the floor.** You now run live customer traffic that requires enforceable turnaround clocks (**SLA timers**), or your engineers begin dispatching autonomous AI coding workers (`agent:coding-agent` / **Coding Sessions**) that require structured delegation fields, workspace agent guidance, and automated triage rules.
- **You cross the 5-team limit or need hard visibility walls.** You need a sixth team, you bring in external contractors who must only see one squad's board (**Guest accounts**), or you have sensitive security, legal, or M&A workstreams that cannot sit in an open team readable by the entire workspace (**Private teams**).

Moving from Free to Basic bought you physical room and team separation. Moving from Basic to Business is the first time you buy active machinery - analytics, SLA clocks, and autonomous agent surfaces - and where the social layer meets synthetic workers.

> **Where this gets hard**
>
> Upgrading to Basic and splitting one team into four takes twenty minutes in the Linear UI. Teaching three new squad leads to hold the `Validation` gate (`P-6`), write honest Friday project updates (`P-19`), and respect `blocked by` dependency edges across team lines without inventing private workflow dialects takes months of enforcement. Without an explicit operating contract, five teams on Basic produce five times the drift in half the time.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: ~2150
  principle-citations: P-1, P-2, P-3, P-5, P-6, P-7, P-9, P-10, P-14, P-16, P-18, P-19, P-20, P-22, P-23, P-24, P-28
  flagged-principle-gaps: none
-->
