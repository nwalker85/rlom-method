<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 9 - Tier 4: Linear Enterprise and Portfolio Governance at Scale

For twelve years at TNI, the floor ran 300+ live human operators over XMPP across 15 to 20 concurrent commercial contracts. When a fiber cut or a carrier switch fault dropped in Rochester, you did not schedule a steering committee for next Thursday; you fired a scatter-gather broadcast into the floor channel (*"Spike in volume out of Rochester - if you have a call from there, send me the BTN and the issue"*), watched fifty simultaneous operator replies fan into your screen within forty seconds, isolated the trunk, shed the load, and issued a binding routing ruling on the spot. Ruling that fast across twenty contracts carried one brutal vulnerability: if the floor manager made up rules on impulse and held workers to a ledger he refused to obey himself, the floor would mutiny or rot. So we instituted the screenshot bargain. Every worker of those 300 had standing permission to paste a screenshot of any past ruling directly into the channel if a present ruling contradicted it. I learned not to argue with myself. More importantly, that floor proved the law that governs every enterprise operating model: **responsibility cannot be mandatory below and theatrical above.**

Walk into a forty-team enterprise workspace the Monday after an acquisition closes and look at how the naive v1 operating model dies. Leadership demands "one pane of glass across all 300 engineers and twenty active contracts," while below the executive deck every acquired department runs its own feral dialect of Linear. Team A imported 14 custom workflow states from Jira (`QA Blocked`, `UAT Signoff`, `Pending CAB`, `Soft Launch`); Team B disabled `Validation` and wired GitHub to mark issues `Done` on PR merge; Team C has 45 open projects and **0 of 45 with a project health badge set**; and Security just flagged that a contractor who rolled off in March still holds an active workspace seat because nobody wired identity deprovisioning to a single source of truth. When the VP of Engineering opens the portfolio rollup on Monday morning, the top-level green badge is pure theater built on unverified bottoms.

Linear Enterprise is the substrate built for that scale: **Multi-level Sub-teams** (up to 5 levels deep), **Sub-initiatives**, cross-workspace **Dashboards**, **SAML SSO and SCIM identity provisioning**, **Audit Logs**, **IP allowlisting**, **Public Asks Web Forms**, **Salesforce and Gong revenue intake**, and **Airbyte / data-warehouse export**. But signing the Enterprise order form does not install an operating system. It gives you the constitutional levers to govern 15 to 20 concurrent contracts and hundreds of human and synthetic actors under one admissible ledger (`P-23`, `P-28`).

### The federated operating contract - hub, spokes, and locality (`P-18`)

When organizations try to scale an operating methodology across thirty or forty teams, they fail in one of two opposite directions. Either central operations acts like a Gosplan politburo - locking every team into an identical cycle calendar, forcing security incident responders to use frontend feature templates, and requiring committee sign-off to add a component label - or central operations abdicates completely, letting forty teams invent forty incompatible state machines. Both corpses rot for the same reason: neither separates **constitutional invariants** from **local execution context**.

The Method scales across an enterprise through a **federated hub-and-spoke contract** anchored on **Locality wins (`P-18`)**:

- **The Constitutional Hub (Non-Negotiable Workspace Law)**: Owned by the central Operations / Platform spine. Every team and sub-team in the enterprise inherits and obeys five hard invariants without exception:
  1. **The nine-state workflow canon (`P-10`)**: The seven forward progression states (`Triage -> Backlog -> Ready -> In Progress -> In Review -> Validation -> Done`) plus `Blocked` and `Canceled`. No spoke may delete `Validation` (`P-6`) or invent a tenth state column; local sub-stages use `stage:*` labels (`P-11`).
  2. **The receipt requirement (`P-7`, `P-8`, `P-9`)**: Nothing transitions from `Validation` to `Done` without a verifiable artifact link in the timeline.
  3. **Human accountability (`P-14`, `P-15`)**: Every issue has a single named human `assignee`; autonomous agents sit solely in `delegate` with a complete verification packet.
  4. **The Friday cadence ledger (`P-19`, `P-27`)**: Every active project and initiative carries a live health badge (`On Track`, `At Risk`, `Off Track`) and a weekly written update. Never `0 of 45 projects with health set`.
  5. **The orthogonal root label axes (`P-16`)**: Workspace-wide prefixes (`type:`, `risk:`, `source:`, `agent:`) stay locked so portfolio queries never break.
- **The Execution Spokes (Justified Local Overrides under `P-18`)**: Within those five guardrails, each department and squad owns its local surface. The infrastructure spoke defines its own `component:*` labels, enforces stricter Terraform/K3s `Validation` proofs, and runs continuous flow without Cycles; a product spoke runs two-week Cycles, customizes its bug intake templates (`P-17`), and tunes its local **Agent Guidance** and **Skills** for its own repositories.
- **The Operators' Court (Community of Practice)**: The Operators across all spokes meet on a fixed monthly cadence to review conformance drift and promote proven local patterns. When one spoke builds an agent Skill or an Ask template that cuts triage time in half, the hub promotes it to the workspace standard. And just like the XMPP floor at TNI, the hub's rules are admissible against leadership: if an executive tries to inject un-scoped work straight into `In Progress` bypassing `Triage` (`P-20`) or demands a feature be marked `Done` before `Validation` clears (`P-6`), any spoke Operator has standing authority to cite the principle number (`P-6`, `P-13`) and hold the gate.

| Governance Layer | Owned By | Locked Across All 40 Teams (Constitutional) | Customizable Per Spoke (`P-18` Locality) |
| :--- | :--- | :--- | :--- |
| **Workflow & States** | Workspace Hub | 9 canonical states (`P-10`); manual/verified `Validation -> Done` gate (`P-6`) | `stage:*` sub-state labels (`P-11`); branch naming prefixes |
| **Hierarchy & Rollup** | Portfolio / Hub + Spoke Leads | Parent Initiatives -> Sub-initiatives -> Projects -> Issues (`P-2`, `P-3`) | Cycle length (or continuous flow); internal project milestone granularity |
| **Identity & Custody** | Security / Hub Owner | SAML SSO, SCIM lifecycle, IP restrictions, MCP/OAuth App approval (`P-14`) | Team Admin delegation; scoped Guest invites on contractor teams |
| **Agents & Guidance** | Hub + Repo Maintainers | Global Agent Guidance (`P-14`, `P-15` packet law, no auto-`Done`) | Team Agent Guidance, repo `AGENTS.md`, domain-specific Skills |
| **Reporting & SLA** | Hub + Spoke Operators | Friday Project/Initiative update cadence + health badge (`P-19`, `P-27`) | Spoke-specific SLA clocks (`P-25`); team-level operational views |

### Multi-level Sub-teams and Sub-initiatives - modeling 20 contracts without noise

On Basic and Business, teams and initiatives sit in flat lists. That works for five squads and three company objectives; it collapses when you manage 40 squads across 6 business units or 15 to 20 concurrent client/platform contracts.

Enterprise unlocks **Multi-level Sub-teams** (nested up to five levels deep) and **Sub-initiatives** (hierarchical objective trees). Install both using strict structural discipline (`P-24`):

1. **Keep the Sub-team tree to two or three levels maximum**: Even though Linear permits five levels of team nesting, five levels of organizational vanity chart produces a sidebar nobody can navigate. Model **Level 1** as the Department or Contract Portfolio (`Platform-Estate`, `Commercial-Products`, `Security-Ops`) and **Level 2** as the concrete execution squads (`Norns-Cluster`, `Identity-Bifrost`, `Client-Web`). Settings, templates, labels, and agent guidance configured at the Level 1 parent team cascade cleanly down to every child squad while preserving isolated backlogs and cycle boards at Level 2.
2. **Bind Sub-initiatives to verifiable quarterly contracts (`P-2`)**: At portfolio scale, a single root **Initiative** (*"FY26 Sovereign Cloud Reliability"*) is too broad for an individual squad's project to roll up to directly. Carve **Sub-initiatives** underneath it (*"Q3 Zero-Ambient Elevation Rollout"*, *"Q3 Multi-Region Database Custody"*), assign a single named executive or principal owner to each sub-initiative, and attach the concrete execution **Projects** (`P-3`) to the sub-initiatives. Health and Friday updates (`P-19`) now roll up cleanly from the shop floor (`Issue -> Project -> Sub-initiative -> Root Initiative`) without losing fidelity (`P-27`).
3. **Use Private-Team Issue Sharing for cross-perimeter handoffs**: When a walled `Security-Embargo` or `M&A` private team needs a platform squad to patch a kernel parameter or rotate a certificate without exposing the entire confidential team backlog, use Enterprise **private-team issue sharing** to project that single scoped deliverable across the boundary while keeping the parent vault sealed.

> **Augmentation Surface - Portfolio Conformance and Health Auditor**
>
> Where an agent layer makes this work better: running an automated nightly sweep across all 40 sub-teams and every active initiative tree. The conformance agent flags any spoke that added an unauthorized workflow state (`P-10`), any project missing its health badge or overdue on its Friday update (`P-19`), any issue moved to `Done` without a linked PR or `Validation` artifact comment (`P-6`, `P-7`), and any sub-initiative whose child projects are `At Risk` while the parent sub-initiative still claims `On Track` (`P-28`).
>
> What the PM keeps: reviewing the conformance docket at the weekly portfolio sync, ruling on whether a spoke's deviation is an earned local override (`P-18`) or an operational violation, and holding spoke leads accountable for dishonest green rollups.

### Sovereign identity spine - SAML, SCIM, Audit Logs, and App Custody

In the J3B counterintelligence model and across Ravenhelm's sovereign identity stack (Zitadel / Keycloak / OpenBao), access is never an ambient favor that lingers after a contract ends; it is a cryptographic lease tied to active identity. On lower tiers, revoking an offboarded engineer or contractor requires a human remembering to open `Settings -> Members` and click remove. At 300+ actors, human memory fails, and orphaned seats become security incidents.

Enterprise hands you four hard custody locks to satisfy both SOC 2 / ISO 27001 auditors and real operational security (`P-25`):

- **SAML 2.0 SSO Enforcement**: Bind workspace authentication exclusively to your central Identity Provider (Okta, Zitadel, Microsoft Entra, Google Workspace). No local passwords, no side-door magic links.
- **Automated SCIM Provisioning and Deprovisioning**: Wire SCIM group mappings directly to your Linear Sub-team hierarchy. When an engineer joins the `Platform` group in the IdP, SCIM seats them in the right Linear sub-team automatically; the minute HR or Security terminates their identity lease at contract end, SCIM revokes their Linear session token and deprovisions their paid seat within seconds. The contractor from March never lingers until October.
- **Immutable Workspace Audit Log & IP Restrictions**: Stream the Enterprise Audit Log (recording every permission change, team visibility toggle, API key creation, and data export) into your central SIEM / ClickHouse forensics store, and lock workspace reachability behind your corporate VPN / Tailscale egress CIDR ranges where required.
- **Third-Party OAuth, MCP, and Agent App Review (`P-14`)**: Lock workspace integration permissions so individual engineers cannot silently authorize unvetted third-party bots or external MCP servers against the work graph. Every external integration and registered AI Agent requires explicit approval by the **Workspace Owner**, with a named human custodian recorded in the ledger.

### Cross-workspace Dashboards and Warehouse Export (`P-23`, `P-27`)

In Chapter 8, Business-tier **Insights** gave one Operator time-series visibility inside a team view. At Enterprise scale, executive leadership and portfolio directors cannot click through forty separate team views every Monday morning to piece together whether the company is shipping (`P-27`).

Enterprise unlocks composable multi-team **Dashboards** and native **Airbyte / Data Warehouse sync**.

#### 1. The Portfolio Executive Dashboard

Build a single locked Workspace Dashboard for Leadership containing four high-signal panels across all sub-teams:
- **Portfolio Health Matrix**: Active Projects grouped by Sub-initiative and Health status (`On Track`, `At Risk`, `Off Track`), highlighting any project whose update is >7 days stale (`P-19`).
- **Validation Gate Integrity**: Issues sitting in `Validation` >5 business days by sub-team (`P-6`) - the exact radar that exposes where merged code is failing to reach customers (`P-9`).
- **SLA Breach & Incident Clock Ledger**: Active and breached SLA timers across all production contracts (`P-25`), sliced by `source:*` and `risk:*`.
- **Human vs. Synthetic Throughput & Cycle Time**: Deliverable cycle time (`In Progress -> Done`) across spokes, segmented by human execution vs. `agent:*` delegation.

#### 2. One-way Data Warehouse Export (`P-23`)

When Finance, RevOps, or Executive BI needs Linear execution data joined against ERP contract margins, cloud spend, or customer ARR in Snowflake, BigQuery, or ClickHouse, enable Enterprise's **Airbyte / warehouse export**. Enforce one strict directional law from `P-23` (**Linear is the system of record for execution**): data flows **out** of Linear into the warehouse for analytical joins; nothing in the BI stack or external spreadsheets ever writes status, priority, or scope back into Linear. And remember: a warehouse table is only as honest as the `Validation` gate underneath it (`P-28`). If spokes mark issues `Done` on merge without runtime proof, your warehouse BI dashboards simply render lies in higher resolution.

### Enterprise intake at the perimeter - Asks Web Forms, Salesforce, and Gong

At 300+ people and 20 active contracts, intake crosses the organizational perimeter. Enterprise unlocks three high-volume intake pipes:
- **Linear Asks Web Forms**: Hosted, SAML-authenticated (or public customer-facing) structured web portals where field operations, partner teams, or enterprise clients submit requests without holding a Linear seat or living in your internal Slack workspace.
- **Salesforce and Gong Integrations**: Native bindings that link commercial opportunity records, renewal blockers, and recorded customer call transcripts directly to **Customer Requests** (`P-22`), attaching true contract revenue weight and customer tier metadata to the signal in `Triage`.

Here the floor-manager discipline matters most: **the wider the intake funnel, the harder the `Triage` gate must hold (`P-20`, `P-22`).** Never wire a Salesforce opportunity request or a public Asks Web Form straight into an engineering team's `Backlog` or `Ready` column. Every external submission lands in `Triage`. A $500k renewal tag on a Customer Request gives the Operator real commercial evidence when prioritizing next quarter's project scope (`P-13`), but a sales rep attaching an account to a feature request never bypasses architectural scoping (`P-4`, `P-22`).

### Ceiling signal - when the methodology becomes permanent infrastructure

There is no Tier 5 on Linear's pricing page. Once you are on Enterprise, you own every software primitive Linear makes. The ceiling at Tier 4 is never missing software; it is **organizational entropy outrunning part-time stewardship**. You know you have crossed from "a tool we configured" into "mission-critical enterprise infrastructure that needs dedicated architectural installation" when any of these three failure modes appears:

- **Post-merger or multi-department taxonomy fracture**: You have 20 to 50 teams, three legacy trackers half-migrated, and each business unit is running a divergent workflow dialect that makes portfolio Dashboards mathematically meaningless.
- **The theatrical green rollup (`0 of 45 health set` / false `Done` syndrome)**: Executive Dashboards show 95% sprint completion and clean burndown charts while production customer incidents climb and multi-contract deliverables slip by quarters because `Validation` (`P-6`) and Friday truth-telling (`P-19`, `P-28`) are being gamed below the deck.
- **Ungoverned agent fleet sprawl**: Hundreds of engineers are dispatching autonomous coding agents (`Claude Code`, `Codex`, `Cursor`, custom MCP bots) across dozens of repositories with no unified delegation contract (`P-14`, `P-15`), no worktree custody standard, and no automated verification gate.

When those signals hit, hiring another program manager to chase status in Slack only adds noise to the channel. You have to re-anchor the spine.

> **Where this gets hard**
>
> Signing a Linear Enterprise contract switches on SAML, Sub-teams, Dashboards, and Salesforce sync in ten minutes. Harmonizing forty engineering squads across three time zones onto a single nine-state workflow canon (`P-10`), enforcing `Validation` receipts (`P-6`) across independent DevOps pipelines, wiring SCIM group custody, and standing up a federated Operators' Court where executive rollups cannot be gamed takes seasoned architectural authority from outside the local political tree.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: ~2650
  principle-citations: P-2, P-3, P-4, P-6, P-7, P-8, P-9, P-10, P-11, P-13, P-14, P-15, P-16, P-17, P-18, P-19, P-20, P-22, P-23, P-24, P-25, P-27, P-28
  flagged-principle-gaps: none
-->
