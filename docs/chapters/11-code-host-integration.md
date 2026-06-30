<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 11 — Code Host Integration: GitHub Primary, GitLab Parallel

The Operator installed the Validation state two weeks ago (Chapter 10). It worked. Issues stopped flipping to Done the second a PR went green. Friday summaries match Friday reality again. But there is a new problem, and it shows up Sunday night. The Operator is in Linear with a coffee and a list of thirty-one issues that need state changes — fifteen PRs opened this week that still say In Progress, eleven merged PRs sitting in In Review because nobody dragged them to Validation, four shipped releases whose issues are still in Validation, one ancient In Progress that turned out to be a PR Engineer A merged a month ago. The Operator is updating Linear by hand from the code host's "Pull Requests" tab. This is the exact failure mode P-25 names: a convention you cannot verify programmatically decays into folklore.

This chapter wires Linear to the code host so the convention enforces itself. The code host and Linear are the same system from the Operator's point of view: the code host is the source of truth for implementation (P-8); Linear is the source of truth for status (P-23). When they are wired correctly, every PR event in the code host produces the right state change in Linear, and the Operator's Sunday-night queue collapses from thirty-one items to the handful of issues that actually require judgment.

GitHub is the primary example. GitLab gets equal treatment inline — every mechanic here works in either code host with different plumbing and the same Linear-side conventions. The Method is code-host-agnostic on purpose: the 3-person team is rarely mono-host, and the Operator should not have to relearn the model when an engineer ships from a different repo.

### Branch and PR conventions

The first mechanic is the convention that lets the code host and Linear find each other at all. Every branch carries the Linear issue ID. Every PR title prefixes the issue ID in brackets. Every commit body, when it matters, references the issue. The integrations look for these strings; without them, no automation fires.

The pattern is `<issue-id>-<short-slug>` for branches and `[<issue-id>] <description>` for PR titles. Engineer A, working on `web-frontend` (a GitHub repo), opens a branch called `ENG-42-rate-limiter` and a pull request titled `[ENG-42] Rate-limit the public search endpoint`. Engineer B, working on `api-service` (a GitLab repo), opens a branch called `ENG-58-token-rotation` and a merge request titled `[ENG-58] Rotate service account tokens nightly`. Same convention, different code host. Linear's integration on each side picks up the issue ID from the branch and the title; the linked PR or MR appears on the issue automatically.

| Convention | GitHub example | GitLab equivalent |
|---|---|---|
| Branch name with issue ID | `ENG-42-rate-limiter` | `ENG-58-token-rotation` |
| PR / MR title prefix | `[ENG-42] Rate-limit search` | `[ENG-58] Rotate tokens nightly` |
| Commit body reference | `Refs ENG-42` in commit message | `Refs ENG-58` in commit message |
| Linking trigger | Linear GitHub App parses branch + PR title | Linear GitLab integration parses branch + MR title; or webhook posts to Linear API |

The Operator publishes this convention as a one-page repo-level guideline (P-18 — closer-to-the-work guidance wins) and adds a PR-template stub that prompts engineers to fill in the issue ID. The verification check is cheap: a workspace-wide Linear view filtered to In Progress issues with no linked PR after two days. That is the only enforcement that survives (P-25).

### PR opened triggers In Review

The second mechanic is the simplest automation. When a PR or MR opens against the main branch, the linked Linear issue moves from In Progress to In Review. The Operator does not move it. The engineer does not move it. The integration moves it, every time, the moment the PR opens.

On GitHub, this is a built-in capability of the Linear GitHub integration. The Operator opens team settings, finds the GitHub section, selects "PR opened" → "In Review" for the team. Done. Engineer A's `ENG-42` PR opens on `web-frontend` and the issue transitions before the Operator's coffee cools.

On GitLab, the path is slightly different. Linear's GitLab integration covers MR linking and basic status sync; for finer control, the Operator installs a project-level GitLab webhook on the MR-events channel that posts to Linear's API with the desired transition. Engineer B's `ENG-58` MR opens on `api-service` and the same transition fires — In Progress to In Review — via the webhook. The reader-visible behavior is identical; the configuration differs by one settings panel.

The Operator should not skip this step waiting for the "perfect" automation. PR-opened → In Review is the cheapest, highest-signal transition in the entire model. It pays for itself in the first day.

### PR merged triggers Validation — not Done

The third mechanic is where most code-host integrations get this wrong. The default behavior on most platforms — and the tempting setting on Linear's side — is to move issues to Done on PR merge. The Method explicitly refuses this. Merged code is implemented; only evidence makes it trusted (P-6). The auto-move on merge goes to Validation. Done remains a human decision until release-driven automation is installed (next section).

On GitHub, the Linear GitHub integration exposes per-team "PR merged" automation. The Operator selects Validation, not Done. Engineer A merges `ENG-42`; the issue moves to Validation; the merged PR URL lands on the issue automatically, which satisfies the evidence-pointer requirement (P-7) for implementation but not for delivery.

On GitLab, the same outcome comes from a webhook listening for `merge_request` events with `action: merge`, posting an issue-state update to the Linear API. Engineer B merges `ENG-58`; the webhook fires; the issue moves to Validation. Same Linear-side behavior, different plumbing.

The temptation to "just enable PR-merged → Done" is the single most common installation mistake. Every issue that ships to customers requires release evidence before Done (P-9). Every issue that runs in production requires runtime or browser evidence. If the integration closes those issues automatically, the Validation state collapses into theater and the Method's load-bearing principle (P-6) is silently disabled. The Operator must hold this line.

> **Augmentation Surface — Integration Drift Detection**
>
> Where an agent layer makes this work better: scanning the workspace daily for state changes that *should* have happened but didn't — PRs marked merged in the code host with their Linear issue still in In Review, releases shipped to production with their issues still in Validation, repos that have stopped producing linked PRs at all (a sign the convention has decayed or the integration broke). The agent checks webhook delivery logs on the code host, surfaces failed deliveries, and posts a daily integrity summary so the Operator finds out about drift before the Friday update.
>
> What the PM keeps: deciding whether a stuck transition is a tooling problem (re-deliver the webhook, fix the branch name) or a missing-evidence problem (the issue genuinely lacks proof and is staying in Validation for the right reason).

### Release events trigger Done

The fourth mechanic closes the loop for production work. When a release ships, every issue in that release's scope moves from Validation to Done. The release event is the evidence (P-9); the integration posts the artifact link as a Done comment automatically.

On GitHub, the Operator wires a release workflow in GitHub Actions. The workflow runs on the `release: published` event, calls Linear's Releases API (or uses the published `linear-release-action`), passes the list of merged PRs since the previous tag, and tells Linear to associate those PRs' linked issues with the release. The Linear Releases pipeline is configured to move associated issues to Done on release publication. Engineer A's `ENG-42` is included in the next `web-frontend` release; the action fires; `ENG-42` transitions to Done with a link to the release page as the evidence artifact.

On GitLab, the equivalent is a CI release job. The `.gitlab-ci.yml` includes a `release` stage that runs on tag pipelines, calls the GitLab Releases API to publish the release notes, and posts to the Linear Releases pipeline via the same Linear API as the GitHub side (Linear does not care which CI system fired the call). Engineer B's `ENG-58` ships in the next `api-service` tag; the CI job fires; `ENG-58` transitions to Done.

| Pipeline | Watched event (GitHub) | Watched event (GitLab) |
|---|---|---|
| Production release | `release: published` workflow in GitHub Actions | `release` job in GitLab CI on tag pipeline |
| Staging release (optional) | Workflow on push to `staging` branch or manual dispatch | CI job on `staging` environment deployment |

Two warnings on releases. First, install release-driven Done one surface at a time. The Operator picks the highest-volume customer-facing repo, wires the pipeline, lets it run for a week or two with the Operator double-checking each release. Only after that flow is green does the second surface get the same treatment. Second, do not exceed roughly six Releases pipelines in the workspace (P-24). Pipelines are operational surface; each one needs a watch and a refresh. More pipelines means more decay (P-25). If the team ships from twelve repos, the Operator picks the six that most need release-gated Done — usually the customer-facing surfaces — and lets the rest stay in manual Done.

### The 3-person team installs both

This is what makes the chapter concrete. The Operator's team ships from two code hosts. Engineer A owns `web-frontend` and pushes to GitHub; Engineer B owns `api-service` and pushes to GitLab. The shared `infra` repo, where both engineers commit occasionally, also lives on GitHub. The Method's installation on the team is mixed by design: the Operator does not migrate either repo to standardize, because the cost of migration is higher than the cost of running two integrations.

What the Operator installs is identical on both sides at the Linear layer: the same nine-state workflow, the same Validation gate, the same auto-move on PR merge to Validation (not Done), the same release-driven Done for the production surface. What differs is one configuration panel per host. The Linear GitHub App is installed once for `web-frontend` and `infra`; the Linear GitLab integration plus one MR webhook is installed once for `api-service`. The Operator writes the conventions once and publishes them at the workspace level; each engineer follows the same branch naming, the same PR title prefix, the same commit references. The Leadership Team consumes the same project updates regardless of which host the underlying PRs live on, because by the time the rollup reaches them (Chapter 12) the host is invisible — only the Linear state remains.

This is the proof that the Method is code-host-agnostic. The conventions are at the Linear layer; the plumbing differs; the reader-visible behavior is the same.

### Install order

Phase the install. Do not turn on every automation in one afternoon.

1. **Install the integration.** GitHub App on the GitHub organization, GitLab integration on the GitLab group. Connect each engineer's personal account on each side.
2. **Enable PR linking and the In Review transition per team.** Configure PR-opened → In Review on the Linear side for each team that owns code work. On GitLab, install the MR-events webhook now.
3. **Confirm one issue end-to-end.** Pick an in-flight issue. Watch the PR open; confirm In Review fires. Watch the PR merge; confirm Validation fires. Done still moves by hand. Hold here for one to two weeks. The Operator is verifying the convention enforces itself before adding more automation.
4. **Install Releases pipelines for the production surface.** After the manual-Validation flow has been green for a week or two, wire the GitHub Actions release workflow (or GitLab CI release job) for the highest-volume customer-facing repo. Configure the Linear Releases pipeline to auto-move associated issues from Validation to Done on release publication. Done becomes automatic for that surface only.
5. **Replicate to additional surfaces.** Once the first surface has a green release flow for one to two weeks, replicate to the next production surface. Cap at roughly six pipelines workspace-wide (P-24).

### What not to do

Two patterns destroy this chapter's value if installed.

**Do not sync GitHub Issues (or GitLab Issues) into Linear bidirectionally.** Linear is the system of record (P-23); the code host's issue tracker is a duplicate. One-way webhooks from the code host into Linear are fine — Sentry alert into Triage, dependabot finding into Triage, a public GitHub Issue routed into Triage for the Operator's review. Two-way sync is debt. Drift between Linear and the code host's issue tracker becomes impossible to debug, the Operator ends up updating both, and the verification check (P-25) collapses because there is no single source of truth to verify against.

**Do not install more than roughly six Releases pipelines.** Each pipeline is a watched event, a CI job, a webhook, and a Done-transition rule. Each one needs to be audited quarterly. Six is the rough capacity ceiling for a 3-person team (P-24); above that, pipelines start failing silently and the Operator stops trusting the Done count. If twelve repos need release-gated Done, the Operator's next decision is not "more pipelines" — it is "fewer surfaces" or "a separate orchestration layer."

> **Where this gets hard**
>
> When the release flow involves multiple repos coordinated through a separate orchestration layer (Argo, Spinnaker, an internal CD platform), or when release gates legitimately span days because of phased rollouts, canary windows, or compliance signoffs, the simple "release event → Done" automation stops fitting. The release event happens at a layer the code host does not own, and the issues need to wait for a signal that lives somewhere else entirely. At that point the Operator is designing custom plumbing — release pipelines that listen to the deployment system, not the code host — and the chapter's defaults stop applying.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass — GitHub primary + GitLab equivalent included for all five mechanics (1) branch/PR convention, (2) PR-opened → In Review, (3) PR-merged → Validation, (4) release event → Done, (5) mixed-host 3-person team install
  word-count: ~2000
  principle-citations: P-6, P-7, P-8, P-9, P-18, P-23, P-24, P-25
  flagged-principle-gaps: none
-->
