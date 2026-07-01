# RLOM Numbered Principles — Canonical Scaffold

This is the canonical list of numbered principles cited as `P-#` throughout the Method. Chapter 3 (The Numbered Principles) expands each one with full rationale and a counter-example. Every other chapter cites from this list.

**Do not invent new P-# numbers in chapters other than Chapter 3.** If your chapter needs a principle not on this list, leave a `<!-- PRINCIPLE_GAP: short description -->` flag in your draft.

**Derivation note (for Chapter 3 author).** Principles P-1..P-28 are derived from `10-doctrine.md` (P-1..P-13, R-1..R-6, O-1..O-12, D-1..D-8) in the source repo, neutralized per `_shared/CONTEXT.md` §5. Where the source rule referenced Ravenhelm-internal artifacts (offices, Norse names, specific repos), the principle has been restated in generic terms that apply to any 3-person team in Linear. P-29 (SemVer release naming) was added later by doctrine ADR-0001.

---

## Group A — The work graph (the shape)

**P-1. Linear is the active work graph, not an archive.**
If a piece of content does not represent active or imminent execution, it belongs in a wiki, a `docs/` directory, or a project document — not in Linear.

**P-2. Initiatives are the objective layer.**
Initiatives express durable outcomes that roll up projects. They do not have deadlines tighter than a quarter. They are the stable planning frame; projects come and go beneath them.

**P-3. Projects are the main execution container.**
Issues belong to projects. A project answers: what is being built, by when, by whom, with what milestones, blocked by what. Active work without a project is a smell.

**P-4. Issues are deliverable-sized.**
An issue has a single outcome, a defined scope, exit criteria, and one owner. An issue that requires more than two weeks to verify should be split.

**P-5. Documentation owns deep context.**
ADRs, design docs, runbooks, and decision narratives live outside Linear and are linked to. Linear issues do not embed long-form documentation.

---

## Group B — Evidence and validation

**P-6. Validation separates implemented from trusted.**
Code that is merged is *implemented*. Code that has passed runtime, browser, release, infrastructure, or human-acceptance evidence is *trusted*. Only trusted code becomes Done. This is the single most load-bearing principle in the Method.

**P-7. Evidence beats assertion.**
For any claim of completion, the issue must point to an artifact: PR URL with merged status, deploy log, screenshot, document, or acceptance comment from someone other than the assignee. No artifact, no Done.

**P-8. The code host proves implementation.**
Merge state, CI results, deploy logs, and runtime evidence live in the code host (GitHub or GitLab) or in systems the code host references. Linear links to them; Linear does not duplicate them.

**P-9. Production work does not go Done before release evidence.**
For issues that ship to customers, the Validation → Done transition requires release evidence: runtime smoke plus browser proof, or deploy log plus acceptance comment.

---

## Group C — Workflow canon

**P-10. The workflow canon is nine states.**
The Method's workflow has exactly nine states: Triage, Backlog, Ready, In Progress, In Review, Validation, Blocked, Done, Canceled. Adding states is a smell.

**P-11. Stage labels carry the things that look like states but aren't.**
"In QA," "Pending Approval," "Design Review," "Soft Launch," and similar are not states — they are `stage:*` labels applied during In Progress, In Review, or Validation. The canon stays at nine.

**P-12. Prefer parent issues with sub-issues over giant single issues.**
If an issue's acceptance criteria list more than five items, or the implementation spans more than two files or two days, split into a parent issue with sub-issues.

---

## Group D — The Operator

**P-13. The Operator owns priority, taste, risk, and real-world commitments.**
These four do not delegate. An agent layer or an Engineer can propose a priority change, surface a risk, or draft a commitment — but the Operator decides. This is the load-bearing principle for the human role.

**P-14. Agents are executors, not owners.**
Specialist agents can be delegated work. Human ownership stays explicit on every issue via the assignee field, even when a `delegate` field is set to a bot.

**P-15. Agent delegation requires acceptance criteria and a validation command.**
Setting a delegate on an issue requires a scope comment naming outcome, scope, validation command(s), expected artifact, and repo or file paths. Vague delegation produces vague output and is the most common source of wasted agent capacity.

---

## Group E — The operating surface

**P-16. Labels exist to serve views.**
A label not cited by any view is a candidate for deletion. Labels are an index, not an organizational scheme.

**P-17. Templates lower the cost of doing the right thing.**
Every recurring work type — bug, feature, research spike, production incident, agent delegation — gets an issue template. Templates make the right behavior the default behavior.

**P-18. Locality wins.**
Closer-to-the-work guidance is more authoritative. A repo-level convention overrides workspace defaults for that repo. A project description overrides workspace defaults for that project. An issue's acceptance criteria override project defaults for that issue.

---

## Group F — Cadence

**P-19. Active projects get a status update every week.**
A project with no update for seven days surfaces in a stale-projects view. The cadence is non-negotiable; the format can compress when there's nothing to say.

**P-20. Triage has a seven-day SLA.**
By day seven, an item in Triage is classified — accepted, merged, canceled, converted to a customer request, escalated to the Operator, or moved to docs-only. Stale Triage surfaces before this threshold.

**P-21. Initiative updates run biweekly; the monthly review rolls initiatives up to Leadership.**
Project updates feed initiative updates; initiative updates feed the monthly review. Each layer compresses the one below it; Leadership consumes the top of the stack.

---

## Group G — Intake and feedback

**P-22. Customer feedback does not directly become scope.**
A customer request is captured and triaged. Conversion to a project or issue is an Operator decision (or, once trust is established, an agent-layer decision routed through a Waiting-on-Operator view). No item flows from customer request to In Progress without Triage.

**P-23. The system of record is Linear.**
Two-way sync with external trackers is debt — drift is harder to debug than re-entry. Webhooks in are fine; bidirectional sync is not.

---

## Group H — System hygiene

**P-24. The overbuild test.**
Before adopting any new feature, label, view, or template, answer five yes/no questions: does it help the Operator decide faster, does it help an executor execute faster, does it preserve evidence we'd otherwise lose, does it reduce repeated PM work, does it make risk visible earlier. Four or more yes — adopt. Three or fewer — skip.

**P-25. Verify what you enforce.**
Don't enforce a convention you can't check programmatically. A rule that requires manual policing decays into folklore.

**P-26. Capacity commits to seventy percent.**
Sprint or cycle planning commits seventy percent of expected capacity. The remaining thirty percent is reserved for unplanned work: production incidents, urgent decisions, agent-delegation overhead. Committing to a hundred percent is committing to lateness.

---

## Group I — Reporting

**P-27. Leadership consumes summaries, not raw Linear.**
The Operator's job is translation. Leadership reads project updates and initiative health; they do not browse the workspace.

**P-28. The evidence chain holds.**
Initiative health rolls up from project updates. Project updates roll up from issue evidence. Evidence rolls up from the code host. Break any link and the chain collapses into theater.

---

## Group J — Releases

**P-29. Releases are named with Semantic Versioning.**
Every release carries a `MAJOR.MINOR.PATCH` version, derived from Conventional Commits by `semantic-release` or `release-please` rather than chosen by hand. Consistent SemVer naming keeps a growing release surface legible — it is the reliable answer to "which version shipped what."

---

## Citation legend (for chapter authors)

When citing in prose:

- "The Method treats Linear as an active work graph (P-1) rather than a wiki."
- "Validation is load-bearing (P-6): merged code is implemented, but only evidence makes it trusted."
- "Production releases require runtime evidence before Done (P-9)."

When citing in tables, use parenthetical: `(P-#)` or `(P-#, P-#)` for compound citations.

When citing as a sidebar or rule heading, use the principle ID as a tag: `**P-6. Validation separates implemented from trusted.**`
