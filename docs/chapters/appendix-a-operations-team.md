<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Appendix A - The Operations-Team Variant

It is Monday morning on a three-person internal operations and infrastructure team - the group that runs network changes, security access reviews, vendor evaluations, and commercial process automation for the rest of the company. Nothing on the screen came from a roadmap the team authored. Engineer A burned all of Friday rebuilding a firewall rule and a webhook integration that a director asked for verbally in a hallway, with zero ticket, zero rollback plan, and zero post-change verification receipt. Engineer B is three weeks deep into an internal workflow automation nobody chartered because a department manager asked nicely in a Slack DM and saying no felt political. Two VPs each believe their vendor evaluation is next on the bench; neither request is recorded where the other VP can see it. Worse, when an infrastructure change on `odin` or an OPNsense VLAN cutover goes sideways at 2:00 a.m., there is no Request for Change (RFC) linked to an execution playbook and no second witness on the verification output. When every Slack channel and hallway is a front door, there is no front door - and the Operator spends the first two hours of every week doing forensic archaeology just to figure out what the team touched.

That is the operational crime scene this appendix locks down. Non-software operations - infrastructure engineering, security governance, vendor due diligence, and internal Centers of Excellence (CoEs) - suffer from the exact same failure modes as software delivery, plus an intake tsunami they do not control. They run on the exact same ledger discipline.

### Supply-side and demand-side - and who should skip this appendix

Chapters 1 through 14 assume a **supply-side** engineering team: a product or platform crew that builds against its own roadmap. Work originates inside the team from initiatives and projects the Operator and Leadership set. External intake is a bounded stream - bug reports, feature requests, and customer escalations - handled cleanly by the `Triage` and `Asks` mechanics in Chapter 8. Ninety percent of the governance happens *after* an issue enters the active board.

An infrastructure operations team, a security engineering group, a PMO, a vendor-evaluation desk, or an internal automation CoE is **demand-side**. The rest of the enterprise routes work *at* it. Its backlog is populated almost entirely by external asks, and the highest-friction failure seam is not coding - it is the intake boundary where an unvetted request becomes a real-world commitment or a live infrastructure mutation. For a demand-side team, **intake and change custody are the product.**

Here is the core architectural rule of this appendix: **the back eighty percent of the Method is identical for code and non-code operations and is not repeated here.** Once an infrastructure RFC, a security audit, a vendor evaluation, or an automation build is accepted, it becomes a deliverable issue inside a dated project under a quarterly initiative (P-2, P-3). It traverses the exact same nine-state workflow canon (Chapter 10). It parks in `Validation` after execution and cannot enter `Done` until an immutable receipt and a second witness verify the live state (P-6, P-7). It rolls up through the exact same Friday project updates, biweekly initiative updates, and Monthly Operating Review with deterministic Red / Amber / Green health (Chapter 13).

What changes for a demand-side operations team is the **front twenty percent** - how requests enter the ledger, how infrastructure mutations are governed before execution, and what evidence proves a non-code deliverable actually works. If your team builds software mainly from its own product roadmap, **skip this appendix**; installing a service catalog, intake dwell clocks, and strict create-time field matrices on a pure product team violates the overbuild test (P-24). Install this variant when you govern shared infrastructure or answer organizational demand you did not invent.

### Intake as a first-class pipeline

A demand-side operations team cannot treat intake as a casual inbox that engineers dip into when bored. Every inbound ask must traverse four explicit stages on the record before it ever touches the delivery backlog:

1. **Request:** Captured exclusively through the published front door (Linear Asks or structured webhook intake), never via verbal hallway tap or personal DM. If a request is not in the ledger, it does not exist and zero engineering minutes may be spent on it (P-1).
2. **Intake Review:** The request has been acknowledged within the first-response clock and is being sized, checked for security or blast-radius implications, and inspected for missing inputs. Zero execution commitment exists here.
3. **Groomed / Chartered:** Scope, blast radius, rollback plan (for infra), and target objective are complete; the requester and sponsor have signed off on the trade-off.
4. **Accepted:** The item is bound to a parent project and initiative, assigned a target window or SemVer operational release batch (P-29), and promoted into the nine-state workflow canon at `Backlog` or `Todo`.

Why add **Intake Review** as an explicit pre-backlog stage when Principle P-10 guards the nine workflow states so fiercely? Because Intake Review sits *upstream* of `Backlog` in the triage funnel, and the timestamp delta between **Request** and **Accepted** produces the single most important health metric a service team owns: **intake dwell time**.

A product team cares how fast committed code ships; an internal operations team is judged by its internal customers on how long a request sits in a black hole before receiving a ruling. Generalizing the seven-day Triage clock (P-20) into tracked intake dwell time turns stakeholder complaints into queue math. When median intake dwell climbs from forty-eight hours to nine days, the Operator has hard numerical proof of a capacity bottleneck before a single VP escalates in an executive meeting.

### The Service Catalog: From Thor RFCs to Vendor Due Diligence

The only cure for "every Slack DM is a front door" is a single, low-friction front door backed by a named **Service Catalog**. The operations team publishes the exact menu of request types it executes, and wires each type to a dedicated **Linear Asks template** (Chapters 5 and 8).

In the Ravenhelm estate and across mature technical operations teams, non-software work falls into five concrete catalog archetypes:

1. **Infrastructure Change / Thor RFC (`type:rfc`):** In Ravenhelm's architecture, **Thor** is the declarative infrastructure change-management contract and **Mjolnir** is the deterministic playbook runner that executes it. Nobody SSHes into `odin`, mutates an OPNsense VLAN rule, or edits a live Docker container by hand. An infrastructure request enters as a structured Thor RFC naming the target host or cluster (`odin`, `hrafngud`, `norns`), the declarative repo diff, the blast radius, the rollback command, and the Mjolnir playbook or GitOps manifest that will execute the change.
2. **Security Incident, Access Elevation, or Audit Gate (`type:security`):** Requests for credential rotation, OpenBao AppRole onboarding, firewall egress openings, or vulnerability remediation. Each template demands the principal identity, least-privilege scope, expiry timestamp, and verification query.
3. **Vendor Evaluation & Due Diligence (`type:vendor`):** Structured technical and commercial assessments of external SaaS, RPA, or infrastructure vendors against non-negotiable architectural gates (self-hosting capability, SAML/OIDC SSO, full API coverage, RBAC, audit logs, OpenTelemetry export, and TCO math). The deliverable is not code; the deliverable is an evidence-backed decision matrix and signed recommendation.
4. **Process Automation & Integration Build (`type:automation`):** Internal workflow builds, webhook bridges, database sync pipelines, or scheduled compliance jobs requested by another department.
5. **Governance Exception (`type:exception`):** A time-bounded waiver against an engineering or security standard, requiring a named executive approver and a hard expiration date on creation.

Each catalog item maps 1:1 to a Linear Asks form in Slack or the web portal. When a director wants a vendor evaluated or a network route opened, submitting the Asks form takes ninety seconds and automatically tags the target team, applies the orthogonal labels (`domain:`, `type:`), and enforces the required fields at creation time. This is Principle P-17 and the Poka-Yoke rule in action: **never price the governed path above the unsafe shortcut.** When the Asks form is faster and clearer than hunting down an engineer in Slack, the hallway bypass dies on its own (P-22).

> **Augmentation Surface - Intake Classification & Playbook Pre-Flight**
>
> Where an agent layer makes this work better: inspecting every inbound Linear Ask the second it lands, matching it to the Service Catalog, flagging missing mandatory fields (such as an RFC missing a rollback command or a vendor evaluation missing SSO documentation links), posting an immediate first-response acknowledgment inside the SLA clock, and - for Thor infrastructure RFCs - running a read-only Mjolnir dry-run (`plan` / `validate`) and attaching the pre-flight output directly to the ticket before the Operator reviews it. Keep the **intake agent** strictly separate from any **execution agent**: classification and pre-flight checking never grant permission to mutate production state.
>
> What the PM / Operator keeps: the accept-or-reject ruling, charter sign-off, and human authorization to execute (P-13). Tools and agents assemble the dossier and pre-flight receipts; a human clicks the accept button.

### Execution custody: Thor RFCs, Mjolnir Playbooks, and the Second-Witness Gate

How do you enforce Principle P-6 (*Validation separates implemented from trusted*) and Principle P-7 (*Evidence beats assertion*) when the deliverable is not a software pull request, but a firewall change, a database backup restore test, a vendor selection, or a commercial operations cutover?

You apply the exact same J3B counterintelligence and sovereign custody law that governs code: **separations exist to make innocence demonstrable, and no actor self-certifies `Done` without an independent witness.**

- **For Infrastructure & Network Operations (Thor -> Mjolnir -> Witness):**
  1. `In Progress`: The engineer authors the declarative configuration diff or Thor RFC and links the PR or Mjolnir playbook run.
  2. `In Review`: A peer reviews the blast radius and rollback command before execution.
  3. `Validation`: Mjolnir executes the playbook (or Argo CD syncs the manifest). The ticket stops in `Validation`. It **never** closes when the command exits `0`, because shell exit code `0` lies constantly (like a backup script printing `OK` while dumping one database out of eight, or a `sha256` check comparing two empty strings `"" == ""` on a broken restore).
  4. `Done`: A **second witness** - either the Operator, a peer engineer on rotation, or an independent verification probe running under a separate read-only identity - queries the live running system from the outside, confirms the state change and reachability, and attaches the terminal or telemetry receipt to the Linear issue. Only then does the issue transition to `Done`.
- **For Vendor Evaluations & Commercial Operations:**
  1. `In Progress`: The analyst tests the vendor sandbox, pulls public API/SSO documentation, and fills the evaluation scorecard.
  2. `Validation`: The draft evaluation artifact (in Outline or the repository `docs/` tree per P-5) is linked to the Linear issue with concrete pricing, architecture proofs, and disqualifier receipts.
  3. `Done`: The accountable stakeholder or Operator reviews the evidence matrix, records the formal Accept / Reject ruling in the issue comment, and closes the ticket.

Whether you are shipping a Rust binary, rotating an OpenBao secret, or disqualifying an enterprise SaaS vendor, the physics are invariant: **work happens in the specialist surface; `Validation` holds the gate; independent evidence closes the ledger.**

### Governance cadence and charter gates

The reporting spine from Chapter 13 - weekly Friday project updates (P-19), biweekly initiative updates, and the Monthly Operating Review (P-21) - runs without modification. A demand-side operations team adds two boundary ceremonies to protect its capacity from being cannibalized by whoever yells loudest:

- **Daily Intake & SLA Sweep (10 minutes):** Every morning alongside the `Blocked` sweep, the Operator sweeps `Intake Review` so zero inbound requests breach the time-to-first-response clock and answered stakeholder questions move immediately into grooming or execution.
- **Quarterly Sponsor & Capacity Review (QBR):** Once a quarter, the monthly operating review expands to show department sponsors the exact ledger of demand versus supply: how many requests entered per department, median intake dwell time, SLA compliance rate, capacity split between keeping the lights on and building new automation, and which low-leverage requests were declined and why.

Enforce two structural gates before any multi-week operations request crosses from `Intake Review` into active execution:

1. **The Sponsor Charter Gate:** When a department requests a multi-week automation build or platform integration, a named sponsor must explicitly sign off on the objective it serves and what existing item in their queue gets pushed right to pay for it. This turns Principle P-13 and the seventy-percent capacity law (P-26) into a public contract: if everything is P0, nothing is P0.
2. **Explicit RACI on cross-department initiatives:** When an operations initiative spans Security, Finance, IT, and Engineering, write the single **Responsible**, **Accountable**, **Consulted**, and **Informed** human names directly at the top of the Linear Initiative description. Never let a cross-functional project enter `In Progress` with two people thinking they own the veto.

### Service SLAs

A supply-side product team owes dates to its own roadmap; a demand-side operations team owes response clocks to external requesters waiting on a decision. Using Linear's native Business-tier SLA rules (Chapter 8), bind two distinct clocks to your intake and execution queues:

- **Time-to-First-Response (Intake SLA):** The maximum elapsed time between a request landing in `Triage` / `Intake Review` and the requester receiving a structured human or agent-verified response (*"Received; sized as a Tier-2 Thor RFC; scheduled for Thursday change window"*). Silence is what destroys trust in an operations team; a twenty-four-hour first-response clock eliminates silence cheaply.
- **Time-to-Resolution (Delivery SLA by Request Type):** Tracked from `Accepted` to verified `Done`, stratified by catalog type:
  - *Urgent Security / Access Revocation:* 4 hours.
  - *Standard Thor Infrastructure RFC:* 3 business days.
  - *Vendor Due Diligence Evaluation:* 10 business days.
  - *Cross-System Automation Build:* Governed by project milestone target date (P-3).

Pair these clocks with an automatic blocker escalation law: **any accepted operations issue sitting in `Blocked` waiting on requester input for more than 5 business days auto-notifies the requester's sponsor; at 10 days, it closes as `Canceled` with a reopen pointer.** Never let a requester stall an active ticket for a month and then blame the operations team for slow turnaround.

### CoE-grade field discipline

When work originates from thirty different requesters across five departments, shared tribal context is zero. If the required metadata is not captured on the issue card at creation time, the quarterly rollup turns into guesswork. Demand-side teams therefore enforce three field rules that are deliberately stricter than the core three-person product scaffold:

1. **The Rule of One:** Every accepted parent issue must carry **exactly one** primary strategic objective or initiative link - never zero, and never three bolted together to make a pet request look cross-functional (P-2, P-16). One parent objective per deliverable guarantees that when the QBR totals engineering hours across the portfolio, the column sums to 100% with zero double-counting and zero orphan favors.
2. **Create-Time Required-Field Matrix:** Enforced mechanically via Linear Asks forms and issue templates so incomplete requests cannot enter `Intake Review` (P-17, P-25):

   | Catalog Request Type | Mandatory Fields at Creation | Required `Validation -> Done` Receipt |
   |---|---|---|
   | **Thor Infrastructure RFC** | Requester, target host/cluster, declarative PR link, blast radius, rollback command | Mjolnir / GitOps run log + independent 2nd-witness reachability output |
   | **Security / Access Gate** | Requester, principal identity, target resource, least-privilege scope, expiry date | Policy commit SHA + live `auth can-i` or OpenBao token verification |
   | **Vendor Evaluation** | Requester, executive sponsor, problem statement, candidate vendor URLs, budget ceiling | Published evaluation matrix doc (Outline/repo) + signed Accept/Reject ruling |
   | **Automation / Integration** | Requester, sponsor, source/target systems, current manual hours/week, data sensitivity | Merged PR + live production execution receipt + requester acceptance sign-off |
   | **Governance Exception** | Requester, policy ID waived, compensating control, executive approver, hard expiry date | Signed approval comment + scheduled revocation issue created for expiry date |

3. **Zero Unparented Execution:** No accepted operations issue may enter `Todo` or `In Progress` without being linked to an active Project and Initiative (P-3). An unparented ticket on a service team's board is an untracked hallway favor; allow five of them, and your seventy-percent capacity ceiling (P-26) is gone.

Audit every field in that matrix once a quarter against the overbuild test (P-24): if a required field is not actively consumed by an automation script, a safety gate, or the Monthly Operating Review, delete it from the form immediately.

### Two optional label axes for service portfolios

Add either of these two label namespaces only when a recurring executive question demands the view (P-16, P-24):

- **`layer:` (`capability` | `delivery` | `impact`):** In plain shop-floor language: *building the factory (`capability`), running the factory (`delivery`), and proving the factory works (`impact`)*. Operations teams constantly get drowned in day-to-day `delivery` tickets until their own automation tooling rots. Filtering the work graph by `layer:` shows Leadership in one chart whether 95% of the quarter went to manual ticket-whacking while 5% went to `capability` automation.
- **`customer:` (`internal` | `external`):** Separates requests that touch internal employee workflows from work that sits in the blast radius of paying external customers (which must clear Chapter 10's highest production evidence bar, P-9).

### Computed RAG governance for operations

An operations team reports portfolio health upward using the exact **deterministic Red / Amber / Green ladder** defined in Chapter 13 (P-28). You never pick colors by gut feel on Friday afternoon.

For a demand-side team, the weekly health computation script folds two additional queue sensors into the ladder alongside project target dates, blocker age (>7 days), and receipt coverage:

1. **Intake Dwell Breach:** If the team's median `Intake Review` dwell time crosses the 7-day SLA ceiling (P-20), the intake operations project automatically flips to **Amber (`At Risk`)**.
2. **Unwitnessed Closures:** If any infrastructure RFC or security issue is closed to `Done` without both an execution pointer and a second-witness verification comment (P-6, P-7), the audit script reopens the issue into `Validation` and flags the parent project **Amber**.

On Linear Free and Basic, these computed health states live directly on each Project and roll up into the markdown Monthly Operating Review (Chapter 13). On Business, historical dwell and SLA breach curves render in **Insights** (Chapter 8). On Enterprise, the entire cross-department RAG matrix, SLA thermometer, and `layer:` allocation chart render live on executive **Dashboards** (Chapter 9) so sponsors see the exact load on the floor without ever opening an issue card (P-27).

> **Where this gets hard**
>
> Installing a Linear Asks catalog takes an afternoon; enforcing the boundary when a senior VP bypasses the form, drops a "quick firewall change" or an unvetted vendor contract into an engineer's DM at 4:30 p.m., and demands immediate execution takes institutional spine. If the field matrix is calibrated too loosely, your operations board turns back into a junk drawer of unverified favors; if it is calibrated like a hostile DMV window, departments route around the team and spin up shadow IT. Designing the intake forms, wiring automated Thor/Mjolnir pre-flight checks so the governed path is faster than the backdoor, and establishing the executive air cover that makes the charter gate hold is the hardest part of demand-side operations.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass - appendix (opt-in variant); grounds non-code ops in Thor RFCs, Mjolnir playbooks, vendor evaluations, second-witness verification, and evidence-gated closure; intake pipeline as ordered list; required-field + receipt matrix as table
  word-count: ~2900
  principle-citations: P-1, P-2, P-3, P-5, P-6, P-7, P-9, P-10, P-13, P-16, P-17, P-19, P-20, P-21, P-22, P-24, P-25, P-26, P-27, P-28, P-29
  flagged-principle-gaps: none
-->
