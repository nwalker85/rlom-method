<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->

## Chapter 12 - Code Host Integration: GitHub Primary, GitLab & Forgejo Parallel

Three wreckage piles sit on the Ravenhelm workbench from the week we wired git forges to the issue ledger without respecting their failure modes. First: on 2026-09-11, a post-session sweep across five active repositories uncovered **81 dangling commit tips and 15 unpushed branches** surviving only in local `git reflog` (`freyr` alone held over twenty worktrees; `gjallarhorn` held seventeen). Real grammar compilers and state machines had been written on the floor, never bound to a tracked pull request or a Linear issue ID, and left to rot in detached checkouts. Second: to stop untracked PRs, we installed a pre-tool hook (`prs-require-linear-issue`) that inspected `curl` PR-creation payloads for a `RAV-<id>` reference. The v1 regex parser only read inline `-d '{"title":...}'` flags; the first time an engineer passed a multiline PR body via `--data @/tmp/pr.json`, the guard failed closed on a valid `RAV-` reference because it never opened the file on disk. Third: once PRs carried `RAV-<id>` in their titles, GitHub's native Linear integration did exactly what its factory defaults promised - the instant PR 1 of a four-part migration merged (a schema doc prep), Linear auto-closed the entire parent issue as `Done`. Parts 2, 3, and 4 vanished from the active work graph while nothing ran in production.

Unbound branches disappear into `reflog`. Brittle regex guards block valid work and train engineers to route around the hook. Default auto-close rules turn a multi-PR deliverable or an unverified merge into a premature victory lap. Left to human memory, the Operator ends up spending Sunday night with a cup of coffee and thirty-one stale tickets across two browser tabs: fifteen open PRs whose issues still read `In Progress`, eleven merged diffs stuck in `In Review`, four shipped releases still parked in `Validation`, and one zombie ticket whose code landed a month ago. Updating the tracker by hand from the forge's Pull Requests tab is the exact decay Principle P-25 warns against: any convention you cannot enforce and verify mechanically rots into folklore by week four.

This chapter wires Linear to your code host so the state machine runs on physical events without lying about completion. From the Operator's seat, the forge and the tracker are two halves of one ledger: the code host is the sole authority for implementation state (P-8); Linear is the sole authority for workflow status and portfolio rollup (P-23). Wire the seam properly, and every branch push, pull request, merge, and signed release drives the exact state transition the Method requires - stopping at `Validation` on merge and advancing to `Done` only when production or release receipts exist.

We show GitHub as the primary rail alongside GitLab and self-hosted Forgejo in parallel. Every mechanic here runs on all three forges with identical Linear-side rules and one settings panel or webhook receiver of difference. A three-person team rarely lives on a single pure host forever; your operating model should not fracture when a service moves from GitHub to a private Forgejo hub.

### Branch and PR conventions (and avoiding the multi-PR auto-close trap)

Before any webhook can fire, the forge and Linear have to agree on a primary key. Every git branch carries the Linear issue identifier. Every pull request or merge request prefixes that identifier in the title. Every commit body references the issue ID. Without those tokens in the payload, the integration is blind.

The canonical pattern is `<issue-id>-<short-slug>` (or `<type>/<issue-id>-<short-slug>`) for branch names and `[<issue-id>] <description>` for PR titles. On a Ravenhelm repo, a slice working on `RAV-1541` checks out a dedicated worktree on branch `feat/rav-1541-dashboard` and opens `[RAV-1541] Add TurnPhase state machine projection`. On a canonical three-person product team, Engineer A on `web-frontend` (GitHub) pushes branch `ENG-42-rate-limiter` and opens `[ENG-42] Rate-limit the public search endpoint`; Engineer B on `api-service` (GitLab) pushes `ENG-58-token-rotation` and opens `[ENG-58] Rotate service account tokens nightly`. Both forges parse the token and bind the PR object directly onto the Linear issue card.

| Convention | GitHub example | GitLab / Forgejo equivalent |
|---|---|---|
| Branch name with issue ID | `ENG-42-rate-limiter` | `ENG-58-token-rotation` / `feat/rav-1541-dashboard` |
| PR / MR title prefix | `[ENG-42] Rate-limit search` | `[ENG-58] Rotate tokens nightly` |
| Commit body reference (non-closing) | `Refs ENG-42` in commit message | `Refs ENG-58` in commit message |
| Linking trigger | Linear GitHub App parses branch + PR title | Linear GitLab integration or Forgejo webhook bridge parses branch + title |

Now disarm the **Auto-Close Trap** before it bites your multi-PR issues. Linear's native GitHub App treats any PR carrying the parent issue ID in its branch or title (or magic words like `Fixes ENG-42` / `Closes ENG-42` in the PR body) as a terminal link: when that PR merges, Linear transitions the linked issue straight to the team's configured merge state. If an issue requires three sequential PRs - say, a database migration PR, a backend worker PR, and a frontend cutover PR - merging PR #1 will prematurely transition the parent issue out of `In Progress` while two-thirds of the work remains unwritten.

Two rules prevent premature closure:

1. **One deliverable, one PR where possible; sub-issues when multi-PR is mandatory.** If a feature spans multiple repositories or staged deployments, create child sub-issues (`ENG-42a`, `ENG-42b`, `ENG-42c` or separate linked issues) so each PR binds 1:1 to its own verifiable unit of work (P-4).
2. **Use `Refs <ISSUE-ID>` instead of closing keywords on preparatory PRs.** When a preparatory PR (such as an ADR or test fixture) touches a parent issue without completing its implementation, reference `Refs ENG-42` in the body rather than `Fixes ENG-42`, and configure the team's merge transition to land in `Validation` - never `Done`.

If you enforce PR issue references with a client-side or CI guard (`prs-require-linear-issue`), test the guard against how engineers and agents actually invoke the CLI: parse both inline JSON arguments (`-d` / `--data`) and file-redirected payloads (`--data @file`, `gh pr create --body-file`), or check the PR payload server-side in a forge Action where the title string is already normalized. A guard that chokes on `--data @file` does not improve hygiene; it teaches workers to bypass the guard.

Publish the naming rules in the repository root's `AGENTS.md` or `CONTRIBUTING.md` (P-18 - guidance lives next to the code) and drop a two-line PR template into `.github/pull_request_template.md` (or `.forgejo/pull_request_template.md`). Then wire the verification view that keeps the rule alive (P-25): a workspace-wide Linear filter showing any issue in `In Progress` for more than forty-eight hours with zero linked branches or PRs. That view catches dangling local work before it turns into eighty-one orphaned `reflog` tips.

### PR opened triggers In Review

The first state transition is pure mechanical plumbing. The moment a non-draft PR or MR opens against `main`, the linked Linear issue moves from `In Progress` to `In Review`. Neither the engineer nor the Operator touches the board.

On GitHub, open Linear's team workflow settings under the GitHub integration and map **On PR open -> In Review** (leaving **On draft PR open -> In Progress** so work-in-progress diffs do not flood the review queue prematurely). When Engineer A opens `[ENG-42]` on `web-frontend`, Linear moves `ENG-42` into `In Review` inside two seconds.

On GitLab, enable the native Linear GitLab integration for MR status sync, or point a project-level Merge Request webhook at Linear's API to fire the state mutation on `action: open`. When Engineer B opens `[ENG-58]` on `api-service`, the identical transition fires. Turn this on day one; it eliminates half of the Operator's manual board-gardening immediately.

### PR merged triggers Validation - never Done

This is the hinge where most workspaces break their own ledger. Both GitHub and Linear nudge you to wire **PR merged -> Done**. Refuse that default. On 2026-09-13, three merged pull requests in our estate were celebrated as finished tools while the `the-work` masthead had never been redeployed to production and a Matrix hotfix sat completely unverified. **Merged is not built; built is not deployed; deployed is not verified running (P-6).**

Configure the code-host integration so that **PR merged transitions the issue to `Validation`**, never `Done`.

On GitHub, open the team's GitHub workflow automation panel in Linear and set **On PR merge -> Validation**. When Engineer A squash-merges `ENG-42` into `main`, Linear moves the ticket from `In Review` to `Validation` and attaches the merged commit receipt to the issue timeline. That satisfies the implementation pointer (P-7, P-8), and simultaneously places the ticket in the Operator's `Validation` queue waiting for runtime smoke proof or release verification (P-9).

On GitLab and Forgejo, wire the merge event (`action: merge` on a merge request, or `pull_request` closed with `merged: true`) to mutate the Linear issue state to the team's `Validation` state UUID.

Hold this line against every complaint that clicking `Done` after verification takes an extra ten seconds. The instant `PR merged -> Done` is enabled on a production repository, `Validation` is bypassed, unshipped merges masquerade as customer value, and your status reports become fiction.

> **Augmentation Surface - Integration Drift & Dangling Work Detection**
>
> Where an agent layer makes this work better: sweeping the estate daily to cross-check git state against Linear state - flagging worktrees with uncommitted diffs or unpushed branches that lack a bound Linear issue, catching merged PRs whose Linear issues remained stuck in `In Review` due to a dropped webhook, and identifying multi-PR parent issues that were prematurely pushed into `Validation` while sibling branches are still open. The agent inspects webhook delivery logs on the forge, retries failed payloads, and posts a morning reconciliation receipt so drift never survives until Friday.
>
> What the PM keeps: ruling on every discrepancy - whether a stuck issue in `Validation` is waiting on a delayed deployment pipeline or lacks real runtime proof and must be kicked back to `In Progress`.

### Release events trigger Done

For customer-facing and production services, the loop closes when a verified release ships and proves reachability. Once your `Validation` gate is habit, you can automate the `Validation -> Done` transition by binding it to the actual release artifact and post-deploy smoke gate (P-9).

On GitHub, wire a GitHub Actions workflow triggered on `release: published` (or on successful completion of the production deploy workflow). The job queries the commit range between the previous release tag and the new tag, extracts every merged PR and its bound Linear issue ID, attaches the release tag and artifact URL to each issue as permanent receipt evidence, and moves those issues from `Validation` to `Done` via Linear's Releases API. When `ENG-42` ships inside `web-frontend` release `v2.5.0`, the release pipeline stamps the receipt and closes the ticket.

On GitLab or Forgejo Actions, the equivalent is a release pipeline stage running on signed tag creation or GitOps deployment confirmation. The runner publishes the release notes, confirms the artifact digest landed in the registry, and calls Linear's GraphQL API to transition the included issues out of `Validation` and into `Done`.

| Pipeline | Watched event (GitHub) | Watched event (GitLab / Forgejo) |
|---|---|---|
| Production release | `release: published` workflow in GitHub Actions | `release` job in GitLab CI / `.forgejo/workflows/release.yml` |
| Staging verification (optional) | Workflow on push/deploy to `staging` environment | CI job on `staging` deployment or Argo CD sync receipt |

Obey two constraints when automating `Validation -> Done`. First, bring release automation online **one repository surface at a time**. Start with your highest-volume production service, run it for two weeks while manually auditing every auto-closed ticket against live production, and only wire the second repository once the first is rock-solid. Second, cap workspace release pipelines at roughly six active surfaces for a small team (P-24). Every automated pipeline is machinery that can fail silently (for instance, when a workflow lacks a trigger path or a token expires). Six surfaces can be audited; twenty surfaces rot in the dark (P-25).

### Naming releases: Semantic Versioning

A release pipeline that stamps completion receipts onto Linear issues requires a deterministic name for every release. Under Principle P-29, every release in the workspace uses strict **Semantic Versioning (`MAJOR.MINOR.PATCH`)** - never ad-hoc strings like `prod-friday-fix`, `v2-final`, or bare dates.

A version string is a compact contract between engineering and operations:

- **MAJOR (`2.4.1 -> 3.0.0`):** Breaking API, schema, or configuration change requiring coordinated migration or cutover.
- **MINOR (`2.4.1 -> 2.5.0`):** Backward-compatible feature addition.
- **PATCH (`2.4.1 -> 2.4.2`):** Backward-compatible bug fix or security patch.

Never compute version bumps by hand in a Slack thread on release afternoon. Derive them mechanically from Conventional Commits (`fix:` -> PATCH, `feat:` -> MINOR, `feat!:` or `BREAKING CHANGE:` -> MAJOR) using `release-please`, `semantic-release`, or your repository's automated release-PR script. When commits are disciplined, the changelog, the SemVer tag, and the Linear release receipt generate themselves. When Leadership asks in Chapter 13's monthly review which release resolved a customer escalation, the issue card points straight to `v2.5.0` and its immutable commit range.

### The 3-person team across mixed code hosts

Here is how this looks on the floor without forcing a religious migration across code hosts. Suppose Engineer A works in `web-frontend` on GitHub, Engineer B works in `api-service` on GitLab, and core platform tools live in a self-hosted Forgejo instance. You do not burn two weeks migrating repositories just to satisfy a tracker.

Instead, you hold the Linear contract constant and swap the thin adapter at the edge:

1. **Identical workflow canon:** All three repositories feed the exact same nine Linear states and hit the exact same `Validation` gate.
2. **Identical naming grammar:** Every engineer and coding agent uses `<issue-id>-<slug>` branches and `[<issue-id>]` PR prefixes regardless of which git remote `origin` points to.
3. **Host-specific edge wiring:** GitHub uses the native Linear GitHub App (`PR merge -> Validation`); GitLab uses the GitLab integration + MR webhook; Forgejo uses the lightweight webhook bridge below.

By the time work rolls up into Friday's project update and the monthly executive review (Chapter 13), the underlying git host is completely invisible. Leadership sees one coherent ledger.

### Self-hosted forges - the Forgejo / Gitea webhook bridge

When you run a sovereign, self-hosted forge such as Forgejo or Gitea, Linear has no native first-party App to click-install. If you leave the forge unbridged, every branch and `[RAV-123]` PR title sits disconnected from the work graph, and you are right back to manual ticket dragging.

Build a tiny, stateless webhook receiver to bridge the gap. When a pull request opens or merges on Forgejo, Forgejo POSTs a JSON webhook payload to your receiver. Your bridge executes three deterministic steps against Linear's GraphQL API (`https://api.linear.app/graphql`):

1. **Extract and resolve the issue key:** Parse the `[<TEAM>-<NUMBER>]` token from the PR title or branch name, and query `issue(id: "RAV-123")` to resolve the human key into Linear's internal UUID and current workflow state.
2. **Enforce the non-closing state ceiling:** On PR open, transition the issue to `In Review`. On PR merge (`merged: true`), transition the issue to `Validation` - **never `Done`** - and guard against regressing an issue that has already been verified.
3. **Attach the permanent receipt:** Call `attachmentCreate` (or post a structured comment) linking the Forgejo PR URL, merge commit SHA, and author back onto the Linear issue card (P-7, P-8).

Two shop-floor lessons will save you an afternoon when wiring this bridge:

- **No `Bearer` prefix on Linear personal API keys:** If your bridge authenticates to Linear's GraphQL endpoint using a personal API key rather than an OAuth app token, pass the header raw: `Authorization: <lin_api_...>`. Developers running on OAuth muscle memory write `Authorization: Bearer <lin_api_...>`, receive HTTP `401 Unauthorized`, and spend three hours debugging valid credentials.
- **Stage the cutover behind a mirror or canary repo:** When migrating private repositories from GitHub to Forgejo, keep the webhook bridge running against a test repository first and verify both open and merge transitions on live PRs before retiring the old host's integration.

Keep the bridge under the overbuild ceiling (P-24): a hundred lines of stateless code that maps PR events to `In Review` and `Validation` and attaches the receipt URL. Never let a webhook bridge grow its own database or attempt bidirectional issue synchronization.

### Install order

Roll out code-host automation in five deliberate phases so you never automate a broken workflow:

1. **Lock the nine workflow states first (Chapter 10).** Confirm `In Review` and `Validation` exist on every team before connecting a single repository.
2. **Publish the branch and PR naming convention.** Commit the `<issue-id>-<slug>` and `[<issue-id>]` rules into `AGENTS.md` and `.github/pull_request_template.md` (or `.forgejo/pull_request_template.md`), and create the Linear view that flags `In Progress` issues older than 48 hours with no linked PR.
3. **Wire `PR opened -> In Review` and `PR merged -> Validation`.** Enable the GitHub App, GitLab integration, or Forgejo webhook bridge. Set merge transitions strictly to `Validation`. Run one issue end-to-end from branch creation to merge and confirm it parks in `Validation` with the PR link attached. Hold at manual `Validation -> Done` for two full weeks.
4. **Wire SemVer and release-driven `Done` on one production repo.** After manual `Validation` is muscle memory, connect your primary production repository's release workflow (`release: published` or post-deploy verification) to transition shipped issues from `Validation` to `Done` with the SemVer tag receipt attached (P-9, P-29).
5. **Expand up to the six-pipeline ceiling.** Replicate release-driven `Done` only to the production surfaces that earn the maintenance cost (P-24, P-25).

### What not to do

Two anti-patterns will wreck your forge integration every time:

**Never sync GitHub Issues, GitLab Issues, or Forgejo Issues bidirectionally with Linear.** Linear is the single active work graph (P-1, P-23). Two-way issue synchronization creates split-brain state machines, infinite webhook loops, and dual triage queues where nobody knows which comment is authoritative. If external users file issues on a public GitHub repo, route them one-way into Linear's `Triage` queue as intake candidates, disable the native issue tab on private repositories altogether, and run all state transitions strictly inside Linear.

**Never let a PR title match auto-close an issue to `Done` without runtime evidence.** Whether through GitHub's default `Fixes #` magic words or Linear's native merge settings, allowing a `git merge` event to certify production delivery destroys Principle P-6. A merge proves code landed on a branch. Only a live check proves it works.

> **Where this gets hard**
>
> When your release topology decouples git merges from production reachability - such as multi-repo monorepo trains, immutable OCI `:b<N>` builds promoted through Harbor into a GitOps repository (`norns-gitops`) managed by Argo CD, or dual-surface tools that must ship simultaneously to a Kubernetes cluster and a Homebrew tap - a naive GitHub `release: published` webhook fires before the workload ever schedules on a node. Wiring the `Validation -> Done` gate to actual cluster sync and live health probes rather than git tag creation requires release-custody plumbing across the registry and orchestrator.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. nate@ravenhelm.co

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass - GitHub primary + GitLab/Forgejo equivalent for all five native mechanics (1) branch/PR convention, (2) PR-opened -> In Review, (3) PR-merged -> Validation, (4) release event -> Done, (5) mixed-host 3-person team install; plus self-hosted-forge webhook bridge (non-native hosts) and SemVer / semantic-release release naming (P-29)
  word-count: ~2850
  principle-citations: P-1, P-4, P-6, P-7, P-8, P-9, P-18, P-23, P-24, P-25, P-29
  flagged-principle-gaps: none
-->
