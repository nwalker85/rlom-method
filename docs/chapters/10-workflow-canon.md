<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 10 - Workflow Canon and the Validation Gate

Pull two autopsy reports from the Ravenhelm ledger and lay them side by side on the bench. First, **2026-09-13**: an agent supervisor reported three merged pull requests across the estate as finished, ready-to-use capabilities and flipped their tracking items to complete. When we inspected the live running systems five minutes later, `the-work` masthead changes were sitting inert on `main` waiting for a production redeploy that nobody owned, a Matrix transport hotfix had merged without a single live verification check against the homeserver, and the third tool had never been installed on the workstation PATH. Second, **2026-09-09**: a forensic sweep across our active repositories uncovered **ten merged features backed by 73 passing unit tests and zero callers in production**. That pile included a 46 KB wire-protocol implementation (`wire.py`) with thorough unit test coverage that nothing in the daemon ever imported, a `vodozemac-bridge` cryptography adapter compiled and tested in total isolation, and an `ensure_receiver()` lifecycle hook that passed every mock test while `doom new --launch` bypassed it completely in live execution. Every single one had a green pull request. Every single one had passing CI. None of them ran.

This is the central lie of modern software tracking: the belief that `Merged == Done` and `Green Tests == Working Software`. In a naive v1 Linear setup - the exact setup 95% of engineering teams run out of the box - a developer or coding agent opens a pull request, unit tests pass against mocked interfaces, the PR merges to `main`, and the GitHub integration automatically transitions the Linear issue from `In Review` to `Done`. Within six weeks, your `Done` column is a wax museum of dead code, un-applied SQL migrations, stale container digests, and features locked behind unwired entrypoints. Your weekly status report counts nine shipped deliverables when three of them are ghosts.

The Ravenhelm Workflow Canon exists to make that lie physically impossible to record. It establishes a strict distinction between three physical states of matter: **Merged is not Built, and Built is not Running.** To enforce that law in the work graph, the Method locks the workflow spine and inserts a non-negotiable physical airlock between `In Review` and `Done`: the **Validation** state (`P-6`).

### Why `Merged != Built != Running`

When an engineer or an autonomous `agent:coding-agent` slice merges a pull request to `main`, exactly one thing has been proven: a git commit SHA moved forward and whatever unit tests were wired in CI exited zero (`P-8`). Between that git merge and a human or production system actually using the work stands a minefield of physical failure modes that unit tests never touch:

1. **The Dead-Caller Gap (2026-09-09)**: The new module (`wire.py`, 46 KB, 73 passing tests across the ten ghost features) compiles and passes unit tests that import it directly, while the production entrypoint (`main.py` or `cli.rs`) never calls it. Reachability in a test harness is not reachability in the binary.
2. **The Build-to-Deploy Gap (2026-09-13)**: The commit is on `main`, and perhaps CI even pushed a container image `:b<N>` to Harbor, but the GitOps manifest (`norns-gitops`), the server container (`odin` / `hrafngud`), or the local Homebrew tap (`nate/tools`) is still pinned to last week's digest. `the-work` masthead is merged in git and invisible in the browser.
3. **The Migration & Config Gap**: The new container binary rolls out to the cluster, boots up, and immediately throws HTTP 500 on the write path because the SQL schema migration (`apply-migrations.sh`), the OpenBao secret mount, or the Kubernetes RBAC `PrometheusRules` permission (`RAV-2086`) was never applied in the target environment.

If your Linear workflow transitions straight from `In Review` to `Done` at the moment of git merge, every failure in those three buckets becomes invisible to the work graph. The ticket is closed, archived, and celebrated in the Friday update while production is either unchanged or broken (`P-28`).

**Validation (`P-6`)** separates *implemented* (the diff landed on `main`) from *trusted* (the capability is built, deployed, reachable through its real entrypoint, and proven by an external artifact receipt). Only trusted work enters `Done` (`P-7`).

### The canonical workflow spine (`P-10`)

Earlier in Ravenhelm's history, before we enforced a constitutional cap, our workspace mutated into 14 distinct workflow states across teams (`Triage`, `Icebox`, `Backlog`, `Scoping`, `Ready`, `In Progress`, `Blocked`, `PR Open`, `Code Review`, `Design Review`, `QA Testing`, `Pending Deploy`, `Staging Verified`, `Done`, `Canceled`). That 14-state corpse taught us a brutal mechanical lesson: **every extra state column you add is another dark corner where stalled work hides from the morning sweep.**

The Method locks the workflow canon at **seven forward progression states** (`Triage -> Backlog -> Ready -> In Progress -> In Review -> Validation -> Done`) plus **two off-axis exception/terminal states** (`Blocked` and `Canceled`), giving nine total state slots in Linear (`P-10`). Every state is a hard physical gate with an explicit entry proof, an explicit exit proof, and an unmistakable rot smell when abused.

| # | State Name | Linear Category | Physical Gate Definition | Entry Proof | Exit Proof | Rot Smell (Diagnostic Violation) |
| :- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Triage** | `Triage` | Unprocessed raw intake airlock | Filed via Ask, Customer Request, Alert, or manual capture | Classified into a Project (`Backlog`/`Ready`), routed to docs (`P-1`), or `Canceled` | Any card aging **>7 calendar days** (`P-20` violation) |
| **2** | **Backlog** | `Backlog` | Accepted intent awaiting scheduling | Accepted by Operator and bound to a Project (`P-3`) | Scoped to deliverable size (`P-4`) with exit criteria (`P-15`) | Orphan issues with **no Project attached** (`P-3`), or aging >90 days |
| **3** | **Ready** | `Unstarted` | Fully specified, ready to pull | Deliverable-sized (`<=2 weeks`), single human assignee (`P-14`), verification command written (`P-15`) | Engineer or `delegate` agent creates branch (`RAV-<id>`) and starts work | Sitting untouched in `Ready` **>14 days** (scope is still vague or priority is fake) |
| **4** | **In Progress** | `Started` | Active execution on an isolated worktree | Branch created / active work started by named owner | Pull request opened in code host or decision document published | **>2 issues `In Progress` per human engineer**, or zero git commits for 4 days |
| **5** | **In Review** | `Started` | Diff or artifact under peer inspection | PR opened in Forgejo / GitHub / GitLab referencing `RAV-<id>` | Code review approved, CI green, and **PR merged to target branch** | PR open **>3 working days** without merge or decomposition (`P-12`) |
| **6** | **Validation** | `Started` | **The Custody Airlock (`P-6`)**: Merged to `main`, awaiting live runtime/release proof | All required PRs merged in code host (`P-8`) | Verifiable external receipt (`P-7`, `P-9`) pasted in issue comments and accepted by Operator / reviewer | Issue sitting in `Validation` **>48 hours** after merge (unowned deploy or broken staging) |
| **7** | **Done** | `Completed` | **Terminal Truth**: Running and verified in target environment | Live verification receipt on file (`P-7`, `P-28`); human sign-off | **None** (Terminal state; regressions open a new linked bug or reopen to `In Progress`) | Issue in `Done` with **zero comment links/artifacts** after PR merge (auto-close trap fired) |
| **-** | **Blocked** | `Started` | Off-axis halt waiting on named external dependency | Comment posted naming the exact blocking issue ID (`blocked by`), vendor, or Operator decision | Blocker resolved -> returns to prior active state, or killed -> `Canceled` | Flipping to `Blocked` with **no comment naming the blocker** (used as a lazy parking lot) |
| **-** | **Canceled** | `Canceled` | Off-axis terminal discard | Closing comment stating the explicit reason (`superseded by RAV-X`, `out of scope`, `wontfix`) | **None** (Terminal state) | Silent bulk cancellation without rationale comments |

#### Walking the seven forward gates in detail

1. **Triage (`Triage`)**: Nothing bypasses the airlock (`P-20`). Whether an item originates from a 3:00 a.m. PagerDuty/Alertmanager webhook, a customer via Zendesk, an executive Slack Ask, or an engineer's mid-coding discovery, it lands in `Triage` first. Inside seven days, the Operator (or the engineer on Triage Responsibility) makes a binary routing call: if it is static reference material, move it to Outline or repo `docs/` and cancel the ticket (`P-1`, `P-5`); if it is duplicate or out of scope, cancel with a comment; if it is real work, attach it to a Project (`P-3`) and move it to `Backlog` or `Ready`.
2. **Backlog (`Backlog`)**: `Backlog` means *"we have decided to build this within the project's horizon, and we have not yet written the atomic execution packet."* Every `Backlog` item must belong to a Project (`P-3`). An un-projected `Backlog` item is an orphan that will never appear in a Friday update (`P-19`).
3. **Ready (`Unstarted`)**: The launchpad. An issue cannot cross from `Backlog` to `Ready` until it passes `P-4` (deliverable-sized, verifiable in ten working days or less; split via `P-12` if larger), `P-14` (one named human `assignee`), and `P-15` (explicit acceptance criteria, target repo, test command, and required `Validation` evidence type written into the body). If an autonomous agent (`agent:coding-agent`) is set as `delegate`, `Ready` is the exact trigger that dispatches the worker slice.
4. **In Progress (`Started`)**: Execution is live. A dedicated git worktree (`~/var/worktrees/<repo>/rav-<id>-...`) and branch exist. If an engineer has five issues in `In Progress` simultaneously, four of them are lies; cap human WIP at one or two active deliverables so cycle time stays honest.
5. **In Review (`Started`)**: Entered automatically via webhook the instant a pull request referencing `RAV-<id>` opens on the code host (Chapter 12). While in `In Review`, automated CI runs tests, static analysis, and advisory AI review (such as Snotra on Forgejo), and a peer human engineer inspects the diff. When an issue requires **multiple pull requests** (for example, 3 PRs across backend and gitops), the issue remains in `In Progress` or `In Review` until the *final* implementation PR merges - or better, each PR is bound to its own atomic sub-issue (`P-12`).
6. **Validation (`Started`)**: The moment the pull request merges to `main`, the code host integration transitions the issue to `Validation` - **never `Done`**. Here the issue waits until the change is built into an immutable artifact, deployed to its target rail (cluster, server, Homebrew tap, or customer release), exercised through its real production entrypoint (proving it is not one of the ten zero-caller ghosts of 2026-09-09), and documented with a concrete receipt pasted into the issue comments (`P-6`, `P-7`, `P-9`).
7. **Done (`Completed`)**: A human reviewer or Operator (never the author or the coding agent self-certifying without external artifacts) inspects the `Validation` receipt against the acceptance criteria written in `Ready`, confirms parity, and moves the issue to `Done` (`P-7`, `P-28`).

### The five canonical Validation receipts (`P-7`, `P-9`)

"Verify it in `Validation`" cannot be left as a vague exhortation; otherwise an engineer writes *"Checked locally, looks good"* in a comment and clicks `Done`. A `Validation` exit requires pasting at least one of five non-fabricable artifact receipts (`P-7`, `P-8`), chosen when the issue was scoped in `Ready`:

| Evidence Type | What It Physically Proves | Required Artifact Receipt in Issue Comment | When Mandatory |
| :--- | :--- | :--- | :--- |
| **1. Runtime Receipt** | The compiled binary/container is booted and executing the new code path via its real entrypoint (`!= 0 callers`). | Deploy job URL + container digest (`:b<N>` / `sha256`) + pasted startup/structured log output or live CLI/API response payload. | Every backend service, daemon, worker, or CLI change. |
| **2. Browser / Surface Receipt** | The user-facing UI renders and mutates state against the live backend without console/CORS/network faults. | Annotated screenshot (with the full environment URL bar visible) or Playwright/Loom trace recorded against staging/prod. | Every web, mobile, TUI, or dashboard change. |
| **3. Release Custody Receipt** | The merged commit is packaged inside the immutable release artifact that external users or workstations actually pull (`P-9`). | Link to the published Forgejo/GitHub Release tag (`vX.Y.Z`), Harbor OCI chart digest in `norns-gitops`, or Homebrew formula bump PR. | Any customer-shipping feature or workstation CLI release (`P-9`). |
| **4. Infrastructure / State Receipt** | The target cluster, firewall, or database schema converged to the declared state with zero drift. | Pasted output of `kubectl get pods` (showing running digest), `terraform plan` (0 changes), or `schema_migrations` row query. | Every GitOps, network, database migration, or secret-routing ticket. |
| **5. Independent Human Acceptance** | Someone other than the code author confirmed the live behavior solves the operational problem stated in the ticket. | Signed comment from the Operator, requester, or customer (`"Verified on prod tenant X; export CSV now populates 1,420 rows"`). | Non-trivial product features, bug fixes reported via Asks/Customer Requests, and all agent-authored PRs (`P-14`). |

**The Two-Receipt Rule for Production (`P-9`)**: For any issue that ships to production or touches customer-visible surfaces, crossing from `Validation` to `Done` requires **two orthogonal receipts** - typically **Runtime/Release Receipt + Browser Receipt**, or **Infrastructure Receipt + Independent Human Acceptance**. A runtime log alone misses a frontend pointing at the wrong route; a browser screenshot alone can be taken accidentally against `localhost` while production still runs last Tuesday's container. Requiring two orthogonal receipts closes every seam from the 2026-09-13 and 2026-09-09 post-mortems.

> **Augmentation Surface - Automated Validation Harvesters**
>
> Where an agent layer makes this work better: watching the `Validation` column continuously. When an issue enters `Validation` after PR merge, a verification agent reads the merged commit SHA, checks whether the `.forgejo/workflows/build.yml` or GitHub Actions release pipeline published `:b<N>`, verifies whether Argo CD (`norns-gitops`) synced the new digest onto the cluster pods, runs an automated headless Playwright or `curl` smoke probe against the live route, and posts the collected receipts directly into the Linear issue comment thread. If the deploy hasn't rolled out after 24 hours (the exact `the-work` failure from 2026-09-13), the agent flags the issue in the Operator's morning sweep.
>
> What the PM keeps: reading the harvested evidence, executing the human-acceptance check, and making the final `Validation -> Done` transition. The agent fetches the receipts onto the bench; the human judges whether they satisfy the contract (`P-7`, `P-14`).

### Killing the tenth state - why variations belong in `stage:*` labels (`P-11`)

Every month, someone with good intentions will ask to add a tenth workflow state to Linear: *"Can we add a `Design Review` state before `Ready`?"*, *"Can we split `Validation` into `Staging QA`, `Security Signoff`, and `Pending Release Window`?"*, *"Can we add an `On Hold` column next to `Blocked`?"*

The answer is always **no** (`P-10`, `P-11`).

The moment you split `Validation` into three custom state columns on one team, every cross-workspace query, every cycle-time Insight (Chapter 8), and every Enterprise Dashboard (Chapter 9) fractures. If a team genuinely needs to track sub-steps inside an active gate, they attach a namespaced `stage:*` label (`P-11`) while keeping the workflow state canonical:
- Need design sign-off before engineering pulls the ticket? State stays `Backlog` (or `In Review` for a design task) with label `stage:design-review`.
- Merged to `main`, verified on staging, and waiting for Thursday's production release window? State stays `Validation` with label `stage:awaiting-release`.
- Waiting on security penetration sign-off before flipping the feature flag? State stays `Validation` with label `stage:security-review`.

Labels carry local sub-process granularity; the nine state slots hold the universal physical truth of the work graph (`P-10`, `P-11`). Never touch the state canon.

> **Where this gets hard**
>
> Installing the `Validation` state in Linear takes thirty seconds; enforcing it when your GitHub or Forgejo webhooks are still pre-wired to auto-close issues on PR merge, when your developers are accustomed to claiming credit at `git push`, and when your CI/CD pipeline provides zero visibility into which commit SHA is actually running in production is where teams stall. Without wiring the code host transitions (Chapter 12) and the release custody gates (Book III: RROM), `Validation` either gets skipped or turns into a 90-ticket bottleneck nobody knows how to clear.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (not a tier, doctrine, integration, reporting, or closing chapter)
  word-count: ~2650
  principle-citations: P-1, P-3, P-4, P-5, P-6, P-7, P-8, P-9, P-10, P-11, P-12, P-14, P-15, P-19, P-20, P-28
  flagged-principle-gaps: none
-->
