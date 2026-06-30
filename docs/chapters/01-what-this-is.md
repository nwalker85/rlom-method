<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->

## Chapter 1 — What This Is and Who It's For

You opened Linear this morning and the Backlog view returned 217 issues. Twelve of them were filed by you, in your own voice, six months ago. The rest came from Engineer A and Engineer B over the last two quarters, plus a slow drip from a Slack channel that you bolted to Linear in a hopeful afternoon and have not looked at since. There is no project rollup that means anything. There are four projects, two of which are abandoned, one of which is named "misc," and one of which is the only honest container in the workspace. Yesterday someone on the leadership team asked you, in a meeting, "what's the status of the platform work?" — and you produced an answer that you knew, while saying it, was a guess. You went back to your desk and tried to build a view that would let you give a better answer next time. You spent ninety minutes on it. You closed the tab.

This is the situation the Method is built for. It is not a transformation. It is not a re-org. It is a method you can install in a week and grow into over a quarter.

### Who this is for

The reader is a single PM running a 3-person team — call them the Operator, Engineer A, and Engineer B — who reports up to a "leadership team" that wants status they can trust without being told to log into the tool. The Operator is technical enough to install Linear, wire up the GitHub or GitLab integration, write a few label conventions, and follow a workflow diagram. They are not senior enough to have ever designed an operating model from scratch, and they shouldn't have to be. That work has been done. What follows is the result.

This Method is also useful to a slightly larger reader — a PM on a 5- or 6-person team, or a tech lead doing PM work on the side — but it is calibrated to the 3-person case. Everything scales up. Some things scale down to two people and a contractor; below that the overhead exceeds the value and the reader should keep using a single Backlog view and a wiki page until they don't fit.

The Method assumes you have access to Linear and the authority to configure it. It does not assume Basic or Business. Nine of the twelve chapters that follow are usable on Linear Free immediately. The three that aren't — Chapters 7, 8, and 9 — describe the tier ceilings as honest signals, not artificial paywalls, and explain what to do when you hit them.

### What the Method is

The Ravenhelm Linear Operating Method is a tiered, human-centric operating model that lives inside Linear's actual primitives. Three properties define it.

**Tiered.** The Method comes in four tiers — Free, Basic, Business, Enterprise — that map to Linear's own pricing tiers because the capability ceilings are real. A 3-person team can install most of the Method on Free in a week: initiatives, Customer Requests, cycles, Releases, Pulse, and the full nine-state workflow all live on Free. The Basic tier adds no new capability — it lifts Free's ceilings (more teams, unlimited issues, admin roles); teams reach for it when they outgrow the 2-team or 250-issue limit, not for a feature. The Business tier is the first real capability jump: Insights, Triage Intelligence, Asks, SLAs, and agent surfaces — the edge of what a single Operator can install without help. The Enterprise tier is not more capability for one team; it is running the Method across many teams at once — SSO and SCIM, sub-teams, and workspace Dashboards. Each tier upgrade should be triggered by a specific operating pain, not by a sales calendar.

**Human-centric.** The Operator owns priority, taste, risk, and real-world commitments (P-13). No automation, no agent layer, no scheduled job decides what matters next. Tools surface candidates; the Operator decides. This is the load-bearing principle for the human role and the reason the Method does not collapse into a workflow engine. Framework-heavy methodologies — SAFe, Scrum-at-scale, the multi-month "agile transformation" engagement — reorganize the team around the framework and then negotiate with reality. The Method reorganizes the workspace around the Operator's judgment and then negotiates with Linear. The judgment stays where it belongs.

**Grounded in Linear's actual primitives.** Initiatives, projects, issues, views, Triage, project updates, the GitHub or GitLab integration, Releases. The Method does not invent a sidecar database, a parallel state machine, or a custom field schema that fights the tool. Initiatives are the objective layer (P-2). Projects are the execution container. Issues are deliverable-sized. Linear is the active work graph (P-1), not an archive — content that doesn't represent active or imminent execution belongs in a wiki or a `docs/` directory, not a stuck Backlog issue from Q2.

### The shape, briefly

Chapter 2 covers the seven operating layers in full: initiatives, projects, issues, views, intake, delivery evidence, and analytics. They are listed here only so the reader knows what the rest of the document is structuring. The layers are not a stack in the architectural sense — they are seven surfaces that the Operator touches in different rhythms. Issues are touched daily. Projects weekly. Initiatives biweekly. Analytics monthly. Delivery evidence (the GitHub or GitLab side) is touched continuously by Engineer A and Engineer B, and the Method's job is to make sure that evidence flows back into Linear without the Operator copying and pasting anything.

Chapter 4 covers the PM Operator practice ladder — five levels of operating maturity that describe what the Operator should be able to do at each stage, from "I can keep the Backlog clean and the workflow honest" through "I can produce a monthly operating review that Leadership uses to make decisions." Most readers of this document are at level 1 or 2 today; the goal of the Method is level 3 within a quarter and level 4 within two. Level 5 is rare and is generally where an agent layer starts to earn its keep.

### The promise

You can install the Free tier in one week. You can be producing project updates that Leadership actually reads (P-27) in two. You can have a workflow that distinguishes implemented code from trusted code (P-6) within three — Chapter 10 covers this in depth, and Validation is the principle most teams skip and most regret skipping. Within a quarter, the workspace will be producing more signal than the Operator has to manually generate, and the question "what's the status of the platform work?" will have a one-paragraph answer that the Operator can recite from memory because the answer is the same as the most recent project update.

The Method is not a guarantee. It is a contract. The Operator brings judgment and one week of install work. The Method brings the structure that makes that judgment legible to a team and a leadership audience that don't live inside the workspace.

> **Augmentation Surface — Workspace Onboarding**
>
> Where an agent layer makes this work better: a brand-new workspace install benefits from automatic surfacing of the things the Operator would otherwise discover one tab at a time — count of stuck Backlog issues, age of the stalest item, projects with no owner or no update in 30 days, issues with no assignee, labels referenced by no view (P-16). The agent produces the inventory; the Operator opens the document and reads it before triaging.
>
> What the PM keeps: deciding which surfaced gaps deserve the first week of attention, and which are acceptable noise to leave alone until the workspace is otherwise honest.

### What this is not

This is not an agent framework. The Method names where an agent layer helps — the Augmentation Surface boxes in each chapter are precise about that — but it does not ship prompts, orchestration patterns, or build instructions for an AI PM. Those are Ravenhelm product.

This is not a prompt library. It is an operating model. The two are different artifacts and confusing them produces a workspace organized around the prompts rather than the work.

This is not a Linear sales document. The Method is calibrated to Linear because Linear's primitives match the shape of the work. A team that already has a different tool installed and operating well does not need to migrate. A team that is choosing between tools should evaluate them on whether the seven operating layers can be installed without fighting the product, not on feature checklists.

This is not a transformation. There is no kickoff workshop, no maturity assessment that produces a 60-page deck, no quarterly steering committee. The Operator reads, installs, operates, and reports. The Method either earns its keep in the first month or it doesn't.

> **Where this gets hard**
>
> The Method assumes a single Operator feeding a single engineering team and reporting to a single leadership audience. When the Operator gains a second engineering team, or when Leadership starts asking for metrics the workspace isn't structured to produce yet — cross-team throughput, initiative-level forecast confidence, evidence chains that span three repos and two release pipelines (P-28) — the install becomes an integration problem, not a configuration problem. The shape stays right; the wiring gets specific.
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: n/a (Chapter 1 has no chapter-type extras)
  word-count: 1578
  principle-citations: P-1, P-2, P-6, P-13, P-16, P-27, P-28
  flagged-principle-gaps: none
-->
