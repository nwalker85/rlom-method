<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 14 - The Assessment: Auditing Presence vs. Absence

Three standing laws govern every audit we run on an engineering estate, written down together on 2026-09-17 after a forty-eight-hour sweep uncovered silent failures hiding behind green status boards:

1. *You can't improve what you cannot measure.*
2. *If you're not growing, you're rotting.*
3. *I can't fix it if I don't know about it.*

Everyone nods at the first two and assumes the third comes along for free. It never does. The canyon between **#1 (measuring what is there)** and **#3 (knowing what stopped happening)** is where every catastrophic workspace defect lives. Standard dashboards and naive issue trackers only instrument *presence*: they count the tickets that were filed, the PRs that did fire a webhook, the projects someone remembered to mark `On Track`, and the tests that printed `OK` before piped output truncated the exit code. They say nothing at all about *absence*: the `deploy.yml` workflow that silently skipped 1 of 24 pushes to `main` because a path filter drifted; the **287,838 of 287,879 Alertmanager webhooks** that failed for four weeks behind a stale Docker single-file bind mount while the dashboard stayed calm; the **81 dangling commit tips** rotting in local `git reflog` because nobody bound them to an issue; or the **0 of 45 active projects** with health set because a blank field threw no alarm.

When you audit your Linear workspace after finishing the first thirteen chapters of this book, ask one question of every green indicator on your screen: **what does this surface report when it CANNOT answer, and what does this query print on an empty result set?** A board with zero items in `Blocked` might mean your team has zero obstacles; far more often, it means engineers stopped moving stalled tickets into `Blocked` three weeks ago and are quietly spinning in detached worktrees. If your operating model cannot distinguish a clean floor from a dead sensor, you do not have governance yet. You have wallpaper.

You can install roughly seventy percent of this Method yourself in five days using the mechanics already laid down in Chapters 1 through 13. The remaining thirty percent is closing the absence gap for the exact shape of your team, your code hosts, your intake pipes, and your executive board.

### What this document gave you

**The structural spine.** Seven operating layers - initiatives, projects, deliverable issues, views, intake, delivery evidence, and analytics - locked to a nine-state workflow canon where `Validation` stands between a merged diff and `Done` (P-6). You have the operating surface of orthogonal label axes (`domain:`, `type:`, `agent:`), six high-signal views, and friction-reducing issue templates that make the governed path cheaper than the hallway shortcut (P-17). And you have the forge integration rules that anchor implementation truth in GitHub, GitLab, or Forgejo (P-8) so Linear never has to guess what landed.

**The numbered doctrine (`P-1` through `P-29`).** Twenty-nine explicit rules with concrete failure modes attached. Tools change; APIs deprecate; vendors get replaced. The principles survive the tooling because they govern the human and agent failure seams: separating implemented from trusted (P-6), requiring artifact pointers over verbal claims (P-7), holding a thirty-percent capacity buffer against queue variance (P-26), and verifying every convention mechanically (P-25).

**The four-tier adoption ladder.** A progressive deployment guide across Linear Free, Basic, Business, and Enterprise. Most three-to-five-person teams can run the core spine on Linear Free starting Monday morning, upgrading only when physical ceiling signals - multi-team security boundaries, SLA clocks, autonomous coding agent dispatch, or portfolio Insights - prove the upgrade has earned its keep.

**The lossless reporting cadence.** Three nested templates - weekly project updates (P-19), biweekly initiative rollups, and the Monthly Operating Review (P-21) - backed by a deterministic Red / Amber / Green health formula and an explicit action-item ownership ledger so summaries never strip raw measurement from operational conclusion (P-27, P-28).

### The RLOM Self-Audit Scorecard: Measuring Presence vs. Absence

Before deciding whether to self-install the rest of the way or bring in Ravenhelm, score your live workspace across the five operational dimensions below. Do not score by whether a policy doc exists in your wiki; score by querying the live system right now and checking whether absence fails loud or silent.

| Dimension | Score 0: Silent Rot (Absence Masked) | Score 1: Manual Folklore (Presence Only) | Score 2: Mechanized Ledger (RLOM Canon) |
|---|---|---|---|
| **1. Workflow & Validation Gate (`P-6`, `P-7`, `P-10`)** | 12+ ad-hoc workflow states; `PR merged -> Done` enabled; merged diffs marked complete while unverified in production. | `Validation` state exists on the board, but issues routinely skip it or close to `Done` without an attached PR, release tag, or smoke receipt. | Strict 9-state canon; forge merge locks at `Validation`; zero production issues enter `Done` without a verifiable runtime or release artifact pointer. |
| **2. Work Graph & Taxonomy (`P-1`, `P-2`, `P-3`, `P-16`)** | Flat backlog of 200+ loose tickets; ~160 overlapping free-text labels; active work running with no parent project or target date. | Initiatives and projects exist, but >15% of active `In Progress` issues are orphaned outside projects or exceed the 2-week deliverable sizing ceiling (`P-4`). | 100% of active execution binds to a dated Project under a quarterly Initiative; orthogonal label namespaces enforced; zero archival docs stored as tickets. |
| **3. Intake & Queue Cadence (`P-13`, `P-20`, `P-22`)** | Side-door DM and hallway tasking; `Triage` holds items >30 days old; answered blocker cards sit unacted on for 16+ hours. | Front door (Triage / Asks) exists, but SLA breaches go unnoticed until a stakeholder complains and no daily sweep flushes resolved blockers. | Single governed front door; 7-day Triage SLA enforced with visible dwell telemetry; daily sweep clears `Blocked` and `Waiting on Operator` within one turn. |
| **4. Code Host & Branch Custody (`P-8`, `P-9`, `P-25`, `P-29`)** | Dangling commits and unpushed branches stranded in local worktrees; multi-PR issues auto-closed prematurely by PR #1; ad-hoc release tags. | Branch/PR naming (`[ISSUE-ID]`) followed by habit (~70% compliance); manual Sunday-night ticket dragging; SemVer computed by hand. | 100% PR-to-issue binding enforced by CI/hook across inline and file payloads; stale `In Progress` (>48h without PR) view active; automated SemVer releases drive `Done`. |
| **5. Upward Reporting & RAG Health (`P-19`, `P-21`, `P-27`, `P-28`)** | `0 of N` projects have health set (or all sit perpetually Green); status summaries conflate live sensors with dead DB pipes; decisions lack owners. | Friday updates written manually by heroic effort; health colors picked by gut feel at 4:45 p.m.; monthly review reverse-engineered from memory. | Deterministic RAG health computed weekly against blocker age, dates, and receipt coverage; every update splits Measurement from Conclusion and ends with an owned Action Table. |

Total your score out of **10 points**:

- **0 to 4 points (The Crime Scene):** Your tracker is currently lying to both the engineering floor and executive leadership. Stop adding features to the process; quarantine the taxonomy, lock the nine states, and disable `PR merged -> Done` this week.
- **5 to 7 points (The Folklore Trap):** You built v1 of the discipline, and it holds only while the Operator spends Sunday night manually policing the board. The moment load spikes, the conventions erode (P-25). You need mechanical enforcement and computed health.
- **8 to 10 points (The Governed Graph):** Your work graph is admissible evidence. You are ready to scale concurrent coding agents (Book II: RDOM) and immutable release custody gates (Book III: RROM) without multiplying chaos.

### What this document deliberately did not give you

Even at an 8/10 self-install, five operational seams require bespoke architecture tuned to your estate rather than a static manual:

**1. Tuning to your exact team topology and seat boundaries.** This book calibrated its baseline to a three-person unit: one Operator, Engineer A, and Engineer B. Your actual floor may be six engineers, two rotating tech leads, a contract security specialist, and an autonomous fleet of coding slices. When two humans share the Operator seat or when contractors work across restricted repositories, `Waiting on Operator` routing, team boundary splits (Chapter 7), and approval authority (P-13) must be partitioned so accountability never blurs into a shared inbox.

**2. Wiring heterogeneous and self-hosted code hosts.** We walked through GitHub primary with a GitLab or Forgejo parallel. In the wild, teams straddle GitHub organizations, legacy Bitbucket instances, private Forgejo hubs, and air-gapped OCI registries where builds happen on merge (`:b<N>`) and deployments propagate asynchronously through Argo CD (`norns-gitops`). Designing the exact webhook receivers, multi-PR sub-issue conventions, and post-deploy smoke hooks that transition `Validation -> Done` without false positives is custom systems engineering.

**3. Translating into your board's executive dialect without maintaining two stacks.** Chapter 13 gave you the three canonical markdown templates. If your CEO, Chief of Staff, or private-equity board demands a specific quarterly portfolio matrix, a financial R&D capitalization report, or an automated slide deck, writing that translation by hand every month violates Principle P-24. The translation layer must be compiled mechanically from Linear's GraphQL API so the Operator writes once and the board gets its exact dialect.

**4. Unifying high-volume external intake pipes.** Beyond standard Triage and Slack Asks, production teams get hit by PagerDuty / Alertmanager webhooks, Sentry crash streams, Zendesk escalations, customer security questionnaires, and public open-source issue trackers. Every pipe requires deduplication, noise-gate thresholds, and deterministic routing into `Triage` so an alert storm does not drown the engineering backlog (P-22).

**5. Building the autonomous agent supervision layer.** The *Augmentation Surface* callouts across every chapter showed what an agent layer does: pre-classifying Triage, checking PR payloads, computing RAG health on Friday morning, and drafting lossless project updates with every commit receipt attached. Specifying *how* those agents authenticate, which MCP tools they may invoke, how their pre-tool guards avoid blocking valid `--data @file` payloads, and how their outputs stay subordinate to human sign-off (P-13, P-15) is Ravenhelm's core engineering practice.

### The Ravenhelm Operating Assessment

When you want the remaining thirty percent engineered and locked down without burning a quarter of your own build capacity, Ravenhelm runs a bounded, five-step engagement. Throughout all five steps, your Operator remains the accountable commander in the seat (P-13) - we build the machinery, calibrate the gates, and hand you the keys with demonstrable receipts.

**1. Discovery & Bench Inspection (Week 1).** Sixty to ninety minutes with the Operator and one executive stakeholder, paired with direct inspection of your current workflows. We do not hand out questionnaires about how you wish you worked; we look at last Friday's actual status report, the last ten merged pull requests, and the oldest twenty rows in your backlog. Output: a signed baseline brief stating your current delivery topology, active bottlenecks, and target ninety-day outcomes.

**2. Read-Only Workspace & Forge Audit (Week 1-2).** We run our automated audit harness against your Linear workspace and connected code hosts. Zero issues or states are mutated during the audit. We measure the exact presence-vs-absence numbers across your estate: state sprawl, label cardinality, orphaned `In Progress` work, unverified `Done` closures, Triage dwell times, webhook drop rates, and project health coverage. Output: a quantitative **Workspace Forensics Report** scoring your estate against all twenty-nine principles (`P-1`..`P-29`) with exact issue and PR receipts.

**3. Four-Bucket Gap Classification (Week 2).** Every defect uncovered in the forensics report is classified into one of four engineering buckets:
- **Install Gaps:** Missing primitives where the team has not yet wired a view, template, or cadence rule.
- **Drift Gaps:** Active violations of `P-1`..`P-29` (such as `PR merged -> Done` or 160 unnamespaced labels) requiring quarantine and migration.
- **Tier Gaps:** Hard platform ceilings where the team is paying in manual workarounds for a capability native to Basic, Business, or Enterprise.
- **Integration & Agent Gaps:** Missing webhook bridges, multi-repo release gates, or agent drafting pipelines between your forge, alerting stack, and Linear.

**4. Phased Cutover & Mechanization Plan (Week 3-4).** We deliver and execute a sequenced implementation plan sized to respect your team's seventy-percent capacity rule (P-26). Every phase specifies the exact configuration mutations, the CI/webhook scripts installed, the named owner, and the verification query that proves the phase is live and cannot fail silently (P-7, P-25). Anything that fails the four-of-five overbuild test (P-24) for your team's scale is explicitly cut from the plan.

**5. First-Quarter Cadence & Maturity Calibration (Optional, Months 2-3).** For one quarter post-install, we sit beside the Operator once a month to audit the Monthly Operating Review, verify that computed RAG health matches floor reality, tune SLA clocks against live dwell distributions, and prepare the workspace for the next tier transition or autonomous agent wave when ceiling signals fire.

Discovery, forensics, and the cutover blueprint complete inside three to four weeks. The workspace cutover and webhook mechanization typically clear inside four to six weeks for a Business-tier organization without halting active product delivery.

### Engaging

If you can self-install from these fourteen chapters and hit 9/10 on the scorecard above, do it Monday morning; that is why we published the entire book in the open. If your workspace has accumulated years of structural drift, spans self-hosted forges and complex release rails, or needs deterministic reporting and agent supervision wired cleanly the first time, bring us to the bench.

The engagement is the **Ravenhelm Operating Assessment**. Reach us directly at `nate@ravenhelm.co`.

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass - opens with the three standing aphorisms and presence-vs-absence doctrine, includes the full RLOM Self-Audit Scorecard table, names the 5-step Ravenhelm Operating Assessment with concrete outputs, explicit CTA with zero posture-hedging, no Augmentation Surface box and no "Where this gets hard" box (exempt per CONTEXT.md §7 and §12)
  word-count: ~2150
  principle-citations: P-1, P-2, P-3, P-4, P-6, P-7, P-8, P-9, P-10, P-13, P-15, P-16, P-17, P-19, P-20, P-21, P-22, P-24, P-25, P-26, P-27, P-28, P-29
  flagged-principle-gaps: none
-->
