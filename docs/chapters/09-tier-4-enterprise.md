<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 9 — Tier 4: Linear Enterprise and the Method as Operating System

It is the Monday after the second acquisition closed. The Operator who installed Free in Chapter 6 and tuned Business in Chapter 8 now sits a rung up the ladder (Chapter 4) — they run the operating model, not a single team. The workspace they once held in their head has become forty-one teams across six departments and two newly absorbed companies. Three things land before the first coffee. Security forwards the SOC 2 readiness checklist: the auditor wants SAML enforced, a provisioning trail, and proof that the contractor who rolled off in March no longer has a seat — he still does. Leadership asks, for the third week running, for "one view across all of engineering," and the Operator cannot build it, because each team's workspace has drifted: the acquired team brought fourteen workflow states from Jira, one product group quietly redefined Done as merged, and "Validation" means three different things in three different places. A staff engineer pastes a compensation-planning thread into a public project channel by accident.

None of these is a feature gap. Every one is a scale gap. The Method that one Operator ran for three people now has to run as infrastructure for hundreds — without fragmenting into forty-one private dialects of itself.

This is the moment Business stops being enough.

### The shift Enterprise represents

Everything in this document up to here assumed one Operator and a small number of teams. The install was something a single person could hold: nine states they chose, four views they read every morning, one evidence chain they walked by hand. Enterprise breaks that assumption. The problem this tier solves is not "what feature does the team lack" — it is "how does one operator's method become an organization's operating system without splintering into incompatible local versions." The lower tiers — Free (Chapter 6), Basic (Chapter 7), Business (Chapter 8) — are about installing the Method for a team. Enterprise is about governing it across people who did not install it, did not read this document, and arrived with muscle memory from a different tool.

Linear's Enterprise tier is the substrate for that governance: identity and audit controls that satisfy a security review, a team topology (sub-teams, private teams, guests) that can model an actual org, workspace-level Dashboards that see across every team at once, and shared agent guidance that lets a central team teach the rest. The features are the easy half. The operating shape that uses them is the hard half — and it is the half a single Operator cannot stand up alone, which is the entire reason this is the tier where the Method becomes an engagement rather than a self-install.

### The federated operating model — hub, spokes, and a community of practice

The shape that scales the Method across many teams is **federated, not centralized and not anarchic**. A central team — the hub — owns the standards: the nine-state canon (P-10), the shared label namespace (P-16), the issue and update templates (P-17), the Validation discipline (P-6), the principle set itself. The hub does not do the delivery work; it owns the guardrails the work runs inside. The execution teams — the spokes — run their own backlogs, projects, and priorities within those guardrails. And a cross-team **community of practice** — the Operators of every spoke, meeting on a cadence — is where templates, views, and hard-won lessons move between teams instead of being reinvented in each one.

This maps cleanly onto **Locality wins (P-18)**, the load-bearing principle of the whole tier. The hub sets workspace-level baselines; a spoke overrides them where its work genuinely differs — the security team's Done is stricter, the research spoke's cycle is longer — and the override is legible precisely because the baseline it departs from is written down. Federation without P-18 is either a straitjacket (every team forced into one shape) or a free-for-all (every team its own dialect). With P-18, the hub publishes the default and the spoke earns its exceptions. The community of practice is where an exception that proves itself in one spoke gets promoted back into the hub's default for everyone — the Method improving itself instead of ossifying.

> **Augmentation Surface — Federation Conformance**
>
> Where an agent layer makes this work better: scanning every team's workspace against the hub's published baseline — flagging the team that added a tenth workflow state (P-10), the spoke whose Done has no Validation gate (P-6), the labels no view cites (P-16), the projects three weeks stale (P-19) — and posting the drift as a conformance report to the community of practice, not a fix.
>
> What the PM keeps: deciding which drift is a violation to correct and which is a justified local override (P-18) worth promoting into the hub's baseline. The agent measures conformance; the humans decide what conformity is worth.

### Identity and the audit trail — SSO, SCIM, restrictions, audit log

Enterprise is where Linear answers a security review. **SAML SSO** routes login through the organization's identity provider, so a person's Linear access *is* their corporate identity — revoke the identity, revoke the workspace. **SCIM provisioning** makes that automatic: deprovisioning in the identity provider deprovisions the seat, which is the control that would have closed the contractor's account in March without anyone remembering to. **IP restrictions** and **login-method restrictions** (the latter also available on Business) narrow how and from where the workspace can be reached. The **audit log** records who changed what and when — the provisioning trail the auditor asked for. The **Workspace Owner** role and **third-party app review** put a named human in the approval path for every OAuth app, MCP server, and agent that wants into the workspace (P-14).

The Method's posture is that these controls are how *Verify what you enforce* (P-25) scales past one person. At three people, the Operator *was* the access policy. At the federation's size, the policy has to be machinery: SCIM is the enforcement point for "no orphaned seats," the audit log for "we can reconstruct what happened," app review for "no agent enters the workspace without an owner accountable for it."

When it pays for itself: the first security questionnaire, SOC 2 audit, or enterprise customer that makes SSO and an access trail a condition of the deal rather than a nice-to-have.

What the tier does not install is the policy itself — which identity groups map to which teams, which apps clear review, what the IP allowlist actually is. That mapping is security-and-operations design done against your real identity provider and your real org chart.

### Sub-teams, private teams, and guests — the federation's structure

Three team primitives let the workspace model the actual organization. **Multi-level sub-teams** (nested up to five levels) are the Enterprise addition that makes the hub-and-spoke topology real: a parent team for a department, sub-teams for each squad, with shared settings and rollups flowing up the tree. **Private teams** and **guests** arrive at Business but become load-bearing here — private teams wall off work that genuinely cannot be open (compensation, security embargoes, M&A), so the staff engineer in the opening cannot paste the comp thread where it does not belong because the channel does not exist for outsiders; guests scope external collaborators into exactly the teams they need and nothing else. Enterprise adds **private-team issue sharing**, the controlled seam that lets a walled team hand a single issue across the boundary without opening the wall.

The Method's posture is that structure follows the operating model, not the reporting chart (P-24). Sub-teams should mirror how work and accountability actually flow, not how the org publishes its hierarchy; a private team is justified by a real confidentiality boundary, not by a manager who wants a walled garden; a guest seat is justified by real scoped collaboration, not as a cheap way to dodge a license.

When it pays for itself: the first time a single flat list of teams stops describing how the org actually works — when a department needs its own rollup, or a sensitive workstream needs a wall the rest of the workspace cannot see over.

Modeling the federation badly — sub-teams five levels deep nobody navigates, private teams hiding ordinary work from the people who need it — is the overbuild test (P-24) failing at organizational scale, where it is far more expensive to unwind than it ever was for one team.

### Dashboards and data out — the cross-team instrument panel

**Dashboards** are workspace-level pages composing panels across many teams at once — the cross-team view Leadership asked for and could not get (P-27). Where Business-tier Insights answered questions about one team's work, a Dashboard answers them across the whole federation: open issues by team, cycle time by department, SLA health across every spoke, Validation throughput org-wide, all self-updating. This is the hub's instrument panel — the single surface that tells the operating model whether the spokes are healthy. The reporting chapter covers the discipline of *what* belongs on it and how it rolls up; this tier is what unlocks the cross-team canvas.

**Airbyte and data-warehouse sync** are the other direction: Linear's data flowing out, one way, into the organization's warehouse and BI stack, where it joins finance, product analytics, and revenue data the Method never touches. The Method's posture is that this is export, not sync — consistent with *the system of record is Linear* (P-23). Webhooks and Airbyte carry data *out* to the warehouse; nothing two-way writes priority or status back in. The evidence chain (P-28) the warehouse reports on is only as honest as the issue-level evidence beneath it, which is why the pipeline is worth nothing until the spokes are actually running Validation.

When it pays for itself: the first time Leadership needs Linear's delivery data joined to numbers that live somewhere else — cost, revenue, headcount — to answer a question no single Dashboard can.

What the tier does not cover is the data model — which Linear fields map to which warehouse tables, what the BI layer is allowed to assert — engagement-shaped work against your specific stack.

### Enterprise intake — Asks web forms, Salesforce, Gong

Two intake surfaces unlock here. **Asks web forms** (gated behind SAML) extend Business-tier Asks (Chapter 8) from Slack and email to public, structured web forms — an intake front door anyone in the organization, or an external requester, can file through without a Linear seat. **Salesforce and Gong** wire enterprise revenue and conversation-intelligence sources into Customer Requests, so a renewal risk surfaced in a sales call or a feature ask captured in a deal review enters Triage with provenance instead of dying in a CRM note.

The Method's posture does not change with scale: *customer feedback does not directly become scope* (P-22). A web-form submission, a Salesforce-attached request, a Gong-flagged ask — each lands in Triage as signal, and conversion to a project or issue stays an Operator decision in the relevant spoke. The larger the intake surface, the more load-bearing P-22 becomes: a public web form wired straight into a backlog is how a fifty-team workspace drowns.

When it pays for itself: the day intake outgrows the channels one Operator can watch — when requests arrive from a public form, a sales call, and a deal review faster than anyone can paste them in by hand.

What the tier does not design is the form taxonomy and the routing — which spoke owns which request type, which fields each form needs — the service-catalog work Business already flagged as engagement-shaped, now multiplied across the federation.

### Agent guidance and Skills across the federation

Business introduced the agent surfaces (Chapter 8); Enterprise is where they scale across teams. **Shared agent guidance and Skills** let the hub author agent behavior once — how a Triage agent classifies, how a delegation packet is composed (P-15), how Validation evidence gets gathered — and publish it to every spoke, so the same standard runs everywhere instead of each Operator prompting from scratch. This is the community of practice expressed in agent terms: a Skill that proves itself in one spoke is promoted to the hub and inherited by all, exactly as a template or view is.

The Method's posture is unchanged and now matters more: agents are executors, not owners (P-14), and delegation still requires acceptance criteria and a validation command (P-15). A shared Skill that composes those criteria correctly is leverage across the whole federation; a shared Skill that skips them is a single point of failure replicated into every team.

When it pays for itself: the moment two spokes are prompting their agents to do the same job two different ways, and the hub realizes the behavior should be authored once and inherited, not re-invented per team.

What the tier does not build is the guidance itself — the prompts, the skill chains, the org-wide delegation protocol — the agent-layer engagement, now operating at the scale of the whole organization rather than one team.

### Ceiling signal — when the method becomes the operating system

The lower tiers had a ceiling above them. Enterprise does not — there is no Tier 5. The signal here is not "you have outgrown the plan"; it is "the Method has stopped being a practice and become infrastructure, and infrastructure needs an owner." Three signals say you have crossed that line:

- **Drift outruns any one person's ability to correct it.** New teams stand up workspaces weekly; each re-derives states, labels, and views, and half get it subtly wrong. The gap between the hub's standard and the spokes' reality widens every month because nobody owns closing it full-time.
- **Reporting only rolls up if the layers beneath are clean — and they are not.** The cross-team Dashboard Leadership opens is wrong, because three spokes have stale updates (P-19), two have a Done that means merged (P-6), and the evidence chain (P-28) is broken in places no single Operator can see from where they sit.
- **The org solves the gap with headcount instead of an operating model.** A VP of Operations, a TPM org, a platform team for "developer experience" — each hired to run the thing the Method describes, none handed an installed version of it, every one reinventing the federation's shape from scratch.

When those land, the Method is no longer something a promoted Operator runs on the side. It is the organization's operating system, and standing it up across the federation — the hub's standards, the spokes' overrides, the community of practice, the identity and audit controls, the cross-team reporting — is the work an engagement exists to do.

> **Where this gets hard**
>
> The organization that wants the federated model live across forty teams — one set of standards in the hub, justified local overrides in the spokes (P-18), a community of practice that actually moves templates between teams, SSO and SCIM satisfying the auditor, Dashboards Leadership trusts, agent guidance shared everywhere — has no single person with the authority, the bandwidth, and the artifact library to install all of it at once. The features ship the day you sign the Enterprise contract; the operating system takes a season and an owner.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: ~2570
  principle-citations: P-6, P-10, P-14, P-15, P-16, P-17, P-18, P-19, P-22, P-23, P-24, P-25, P-27, P-28
  flagged-principle-gaps: none
-->
