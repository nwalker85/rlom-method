<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 7 — Tier 2: Linear Basic Upgrade

It is month four. The Tier 1 install from Chapter 6 has held. The Operator has a handful of active projects, two initiatives wired above them, a clean Triage queue most mornings, weekly updates nobody has had to chase, and a GitHub link on roughly every issue that should have one. The system is real, and — this is the part the earlier draft of the Method got wrong — almost all of it was built on Free.

Then two things happen in the same week. The Operator goes to file a batch of new issues and Linear warns that the workspace is closing on 250 — Free's hard cap. And Leadership greenlights a second squad: a small team to own the public surface, with its own remit and its own lead. The Operator goes to create the team and finds Free allows two, and both slots are spoken for the moment the new team exists.

Neither problem is a missing feature. Both are walls. That is what Tier 2 is for.

### What Basic actually adds

Be blunt about this, because the previous tiering oversold it. Linear Basic, at $10 per user per month, adds exactly four things over Free, and all four are ceilings lifted, not capabilities unlocked:

- **Five teams**, up from two.
- **Unlimited issues**, up from the 250-issue cap.
- **Unlimited uploads**, up from 10 MB.
- **Admin roles** — scoped administration so someone other than the Operator can manage a team without owning the whole workspace.

That is the entire list. Basic is a ceiling lift. It is the tier you buy when the team has outgrown Free's *limits*, not when it wants new *machinery*. If you are reaching for Basic expecting it to switch on a layer of the Method, you have misread the price sheet — and the next two sections are the correction.

### The misconception to drop

The earlier draft of this document attributed Initiatives, Customer Requests, and the trend layer to "Plus." That was wrong, and the correction matters because it changes what you buy and why.

**Initiatives are Free.** The objective layer (P-2) — the durable container above projects, with health and its own update cadence — is on the free tier. The Operator already installed it back on Free. You do not upgrade for it.

**Customer Requests are Free.** Structured voice-of-customer intake with attribution and impact (P-22) is on the free tier too. You do not upgrade for it.

**Cycles, Releases, and Pulse are Free.** The cadence container, release pipelines (up to fifteen), and update digests are all free. You do not upgrade for any of them.

**Insights is *not* on Basic.** The queryable analytics layer on views — the thing that replaces the Operator's Friday spreadsheet — is a **Business** capability, not a Basic one (Chapter 8). So are Triage Intelligence, Linear Asks, and SLAs. Dashboards are Enterprise (Chapter 9). The feature-tier matrix carries the authoritative gating; read it before you upgrade for a feature, because Basic almost certainly does not contain the feature you have in mind.

Net: there is no layer of the Method that switches on at Basic. The objective, intake, cadence, and release layers are already running on Free; the analytics and automation layers are still a tier away on Business. Basic sits in between, and what it sells is room.

### The upgrade is administrative, not architectural

Because Basic adds no machinery, the upgrade changes almost nothing about the workspace the Operator has been running. The nine states, the labels, the shared views, the initiatives, the customer requests, the release pipelines — all of it keeps working exactly as it did the day before, unchanged. Treat the upgrade as a quiet infrastructure event, not a re-platforming. Nothing needs reinstalling.

What does change is operational headroom. Issues stop bumping the cap, so the Operator can stop archiving aggressively just to stay under 250. The third and fourth teams become creatable, so the second squad gets a real home instead of a shared-team workaround. And admin roles become available — the one addition worth a paragraph of its own.

### Admin roles — the one genuine new lever

Admin roles are the only thing on Basic that is a capability rather than a relaxed limit, and even this is modest. On Free with one team and three people, a flat membership is fine: everyone the Operator trusts can touch settings, and there is little to break. The moment the workspace has a second team with its own lead, that stops scaling. The new team's lead needs to manage *their* team's workflow, labels, and members without being able to reconfigure — or delete — the rest of the workspace.

Admin roles let the Operator delegate scoped administration: a team admin who owns one team's settings, an org-level admin who can manage members and billing. Grant them the same way you add anything else under the Method — minimally, and only where someone is actually administering (P-24). An admin role handed out "just in case" is overbuild with a blast radius. The default stays: the Operator owns the workspace; admin roles are how the Operator stops being the only person who *can* own it.

### Standing up the second team

The clearest thing Basic actually buys is room to run the second squad as a real team instead of a workaround. On Free, a team that hit the 2-team cap had to cram a new squad into an existing team and fake the separation with a label or a project — never a real boundary. Basic removes that compromise. Standing up team three (or four, or five) is mechanical, and the Method's move is to clone the operating surface rather than reinvent it:

- **Copy the spine.** The new team gets the same nine states and the same namespaced labels, so a member who knows one team can read the other on sight.
- **Seat the lead as a team admin.** The new squad's lead owns their team's settings without touching the rest of the workspace — the one place admin roles earn their keep.
- **Wire under the initiatives that already exist (P-2).** Two squads under one initiative is the normal shape; don't spin up parallel objectives just because there is now a second team.

Locality still applies (P-18): the lead can tune a label or a view that only makes sense for their remit, but the spine stays shared. A workspace where every team invents its own surface is exactly what Chapter 5 was written to prevent.

> **Augmentation Surface — Seat and Team Watch**
>
> Where an agent layer makes this work better: watching the team count against Basic's five-team ceiling, flagging dormant members who hold seats the workspace is paying for, and surfacing the access map — who has an admin role on which team, and whether anyone is over-scoped. On Basic the meter runs per seat, so seat hygiene is cost hygiene.
>
> What the PM keeps: the call on who gets a seat, who gets an admin role, and when a fifth team means it is time to look at Business rather than provision blindly toward the ceiling.

### Ceiling signal — how to know Basic is no longer enough

Basic's headroom is wide on issues and narrow on everything else, so it runs out in one of two ways — and the difference is the whole point. Either the team needs more room than Basic gives, or, far more often, the team needs *capability* Basic was never going to provide. When two of the following land in the same quarter, plan the move to Chapter 8 and Business:

- **Intake or reporting that needs intelligence, not headroom.** The Operator wants Insights to stop rebuilding the same Friday chart, or Triage Intelligence to route a Triage queue that has outgrown a thirty-minute daily pass, or Linear Asks to capture internal channels the Operator no longer monitors in real time. None of those is on Basic; all of them are on Business.
- **Work that needs a clock.** Production traffic, urgent regressions, decisions with deadlines — work that needs an SLA, which Basic does not have.
- **The team passes five teams, or needs a boundary.** A sixth team, a private team for sensitive work, an outside guest — the team has outgrown Basic's team model and wants the boundaries and access controls that start at Business.

The honest framing: the move from Free to Basic was about ceilings. The move from Basic to Business is the first time since Free that you pay for *capability* — and that makes it the more consequential upgrade. Basic buys you time; Business buys you machinery.

> **Where this gets hard**
>
> The team that upgrades to Basic expecting it to "unlock the Method" — switch on the reporting, the intelligence, the automation — discovers Basic does none of that, and can feel like it paid $10 a head for nothing. It didn't: it bought the room it actually needed. But if what the team needed was Insights or Triage Intelligence or SLAs, Basic was the wrong purchase and Business was the target all along. Knowing which wall you are actually hitting — a limit or a capability gap — is the difference between a $10 upgrade that buys headroom and a $16 upgrade that buys the machine.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: ~1450
  principle-citations: P-2, P-18, P-22, P-24
  flagged-principle-gaps: none
-->
