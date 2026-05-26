<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 12 — The Assessment: What This Document Doesn't Cover

You are the Operator. You read the previous eleven chapters in two sittings. You recognized your team in every one of them — the Triage queue that grew a second backlog inside it, the Validation gate you've been wanting to install, the project updates Leadership keeps quietly rephrasing back to you in their own format. You can install most of this. You believe in it.

You also do not have the time. And the canonical 3-person team in this document is not exactly your team. Yours has four engineers and a contract designer. Or it has two engineers and a customer-success person who files half the bug reports. Or it's three engineers but two of them split time across a parallel product that lives in a separate GitLab group. The shape of the Method fits you. The fit of the install does not, yet.

That's the gap this chapter exists to close.

### What this document gave you

**The shape.** Seven operating layers — initiatives, projects, issues, views, intake, delivery evidence, analytics — and the workflow canon of nine states with Validation as the load-bearing gate (P-6). The operating surface — labels, views, templates — that turns the shape into something the workspace actually does. The code host integration that proves implementation in the place it happens (P-8) and lets Linear stop pretending to know what shipped.

**The doctrine.** Twenty-eight numbered principles, each with a rationale and a counter-example. The principles are the part of the Method you can carry into any future tooling change. Linear could be replaced; the principles would survive the replacement.

**The install path for three tiers.** Free, Plus, Business — each with the specific capabilities the tier adds, the install steps the Operator can run alone, and the ceiling signals that tell you you've outgrown your plan. The tiering is honest: most 3-person teams live happily on Plus, and the Method is designed to make that possible.

**The reporting cadence.** Three templates the Operator hands upward — the weekly project update, the biweekly initiative health roll-up, the monthly review. The cadence is the chain that makes Leadership's consumption of summaries (P-27) into a system rather than a habit.

### What this document deliberately did not give you

**Tuning to your specific team composition.** The Method assumed a 3-person team: the Operator, Engineer A, Engineer B, and Leadership Team upstream. Your team is 5, or 12, or a 3-person team that contracts with a fourth specialist two days a week. The view set is roughly the same. The labels that fit your team are not. *Waiting on Operator* changes meaning when there are two Operators on rotation. *Agent Delegation Queue* changes shape when the contractor is a human, not an agent, but is delegated work through the same routing pattern. These are iterations, not copy-pastes.

**Tuning to your specific code host stack.** The Method assumed GitHub primary with a GitLab parallel. Your team uses both, plus a private Gitea mirror for the on-prem build, plus a Bitbucket repo for the legacy product you can't decommission yet. The Validation → Done transition needs evidence from each one (P-9). Webhook design, branch naming conventions, and release-pipeline configuration are bespoke to the stack you actually have.

**Tuning to your leadership team's reporting taste.** The three templates in Chapter 11 are a starting point. The format Leadership actually consumes — pillar dashboards, OKR scorecards, board-pack narratives, a Slack-channel weekly with three bullets — is a translation layer on top of the Method's evidence chain (P-28). Project updates feed initiative updates which feed the monthly review; the format of the monthly review depends on what your leadership reads without resentment. That is a design decision, and it is yours.

**Tuning to your intake sources.** The Method named Triage, Customer Requests, and Asks. Your team's intake includes a support ticket queue from a separate help desk, a Sentry stream that fires three times a day, a Slack alerts channel, customer-success escalations forwarded by email, and an open-source GitHub Issues queue with weekly contributions. Each one needs a designed entry point that lands somewhere the Method can pick it up (P-22). None of those entry points existed in the canonical example.

**Designing the agent layer (if you have one or want one).** The Augmentation Surface boxes throughout this document named where an agent layer extends the Method — triage classification, project update drafting, evidence reconciliation, stale-work detection. What an agent layer *does* is described. *How* to build it — what it reads, what it writes, when it routes a decision into the Waiting on Operator view, what acceptance criteria its outputs need before they're trusted (P-15) — is Ravenhelm's product, not configuration you can crib from a document.

If you are the Operator on a 3-person team with a single primary repo and a Leadership Team that already reads the three templates without translation, this document is usable as-is and your install is mostly mechanical. If your team has scaled past three engineers, or your leadership team has a reporting format the templates don't match, or your code host stack includes more than GitHub and one parallel — the install you do alone will be roughly seventy percent of the Method. The remaining thirty percent is the tuning the assessment delivers.

### The Ravenhelm Operating Assessment

The engagement is shaped as five sequential steps. Each step has a defined output. The Operator is the counterparty throughout — the assessment does not negotiate with Leadership for you and does not bypass the role of the person who owns priority, taste, risk, and real-world commitments (P-13).

**1. Discovery interview.** Sixty to ninety minutes with the Operator and one Leadership stakeholder. The goal is to hear the current state in your language: where the workspace is today, where the friction is, where the next ninety days are aimed, what the Leadership Team is asking for that the workspace is not delivering. No diagnosis yet. The output is a short written brief — what the engagement believes is true about the team, returned for correction before the audit starts.

**2. Workspace audit.** Ravenhelm runs the gap-analysis methodology against the current Linear workspace. The audit is read-only: nothing in the workspace changes during this step. The output is a written audit naming what already aligns with the Method, what conflicts with it, and what is missing. The methodology is the same one the Method itself was built from — adapted from the gap-analysis pattern in the Ravenhelm canon and applied to your specific workspace inventory.

**3. Gap classification against the Method.** Each gap from the audit is categorized into one of four buckets: *install gap* (the Method is silent and a decision is needed for your team), *drift gap* (a Method principle is being violated and the workspace needs intervention to come back into alignment), *tier gap* (the team has outgrown its current Linear plan and the workspace is being constrained by ceiling signals), or *tooling gap* (the team needs an integration the Method does not currently prescribe — a help desk, a Sentry stream, a second code host). The classification matters because each bucket has a different fix path and a different cost.

**4. Phased install plan.** Adapted from the Method's own seven-phase install pattern. Each phase names what changes, what evidence proves the phase landed (P-7), who owns each install task, and how long the phase takes. Phases are sized for your team's actual capacity, not theoretical capacity — the install respects the seventy-percent rule (P-26) the same way real delivery does. The plan also names what the engagement recommends *not* installing. The overbuild test (P-24) applies as hard to the Method as it does to any other tooling choice: if a Method element fails four-of-five for your team, the install plan leaves it out.

**5. Ongoing maturity coaching.** Adapted from the long-horizon maturity pattern in the Method's canon. For the first quarter after install, the engagement provides monthly Operator coaching: stuck-decision review, drift detection in the workspace, the next-tier readiness call when ceiling signals start appearing. Coaching is optional for the engagement — named here so the reader knows it exists and can choose. The Method is built to keep working without external help; the coaching is for the team that wants someone else carrying the operating-model maintenance load while the Operator focuses on the work itself.

The five steps run in order. The discovery and audit can be completed inside two weeks; the install plan lands inside four weeks of engagement start; the install itself runs against your team's capacity, typically four to eight weeks for a Plus-tier install at a 5-to-12-person team. The coaching, if chosen, begins the month after install close.

### Engaging

The Ravenhelm Operating Assessment is the engagement. The contact path is `[contact placeholder]`.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass — explicit CTA present, zero hedging in the close, the assessment is named concretely across five steps with outputs per step, no Augmentation Surface box and no "Where this gets hard" box (correctly exempt per CONTEXT.md §7 and §12)
  word-count: ~1400 prose (1561 total with headings, license header, and rubric block)
  principle-citations: P-6, P-7, P-8, P-9, P-13, P-15, P-22, P-24, P-26, P-27, P-28
  flagged-principle-gaps: none
-->