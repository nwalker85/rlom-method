# RLOM Shared Context — READ FIRST

This file is **read by every chapter-writing agent before drafting**. It is the source of truth for tone, brand rules, neutralization rules, callout formats, the rubric every chapter must pass, and the canonical 12-chapter ordering.

If anything in this file contradicts your individual chapter brief, this file wins.

---

## 1. Document identity

**Title:** Ravenhelm Linear Operating Method (RLOM)
**Author:** Ravenhelm LLC
**License posture:** Freemium consulting deliverable that doubles as a sales funnel.
**Reader profile:** A single PM running a 3-person team — one operator/PM, two engineers — reporting to a vague "leadership team." Technical enough to install Linear themselves but not senior enough to have designed an operating model from scratch. They have pain. They are looking for a method.

---

## 2. Voice and tone

Compressed, peer-level, expert. Direct claims with reasons. Plain English. Short sentences when the claim is sharp; longer ones only when the structure is doing real work. The reader should feel met where they are, not lectured.

**Banned:**
- Hedging ("it's worth noting," "arguably," "perhaps")
- Filler ("in today's fast-paced," "at the end of the day")
- Marketing-speak ("synergy," "leverage," "best-in-class," "world-class")
- Restatement paragraphs ("In this chapter we will explore...")
- Emoji
- Norse / Ravenhelm / real-client names (see §5)

**Encouraged:**
- Numbered principles cited inline as `P-#`
- Concrete examples using the canonical 3-person team
- Tables for tier comparisons, capability matrices, integration parallels
- Bullets only when content is genuinely enumerative

---

## 3. The canonical 3-person team

Every chapter must use this team concretely **at least once**.

- **The Operator** — the PM. The reader IS the Operator.
- **Engineer A** and **Engineer B** — not gendered, not given personalities, not given specialties unless the example needs them.
- **The Leadership Team** — vague upward-facing audience. Consumes project updates and initiative health. Never named individuals.

Do not introduce additional personas (designers, customer success, security leads) unless the chapter genuinely requires one — and if so, name them by function, never personally.

---

## 4. Formatting

- Markdown only.
- `##` for chapter title (the chapter is the H2 root of its own file).
- `###` for sections.
- `####` used sparingly — only when structurally required.
- Prose by default. Bullets only when content is genuinely enumerative (a list of states, a list of label namespaces, an install checklist).
- Tables for tier comparisons, capability matrices, integration parallels.
- Code fences for templates, command examples, label syntax.
- No rogue HTML except the license block at the top.

---

## 5. Brand and neutralization rules

**Use:** "Ravenhelm" or "the Method" — never "RLOM" inside prose (it's fine in headers, the title block, and file names).
**Use:** "Linear" (proper capitalization).
**Use:** "GitHub" as the primary code-host example. **Always include a "GitLab equivalent"** parallel wherever integration mechanics are described.

**Strip from all source material before incorporating:**
- All Norse names: Mimir, Heimdall, Bifrost, Freyr, Forge, Odin, Norns, Hrafngud, Yggdrasil, Huginn, Munin, Thor, Vidar, Kvasir, Rig, Sleipner, Magni, Hrafngrima, Berserkr, Valknut, Asgard, Midgard, etc.
- All Ravenhelm-internal jargon: offices, the office model, the 11 offices, C-suite skeleton projects, `CEO-O*`/`CISO-O*`/etc. project codes, Office Model, AAS, RUNESTACK, RAVENMASK, RAVENMASKOS, HUGINN, MIMIR, YGGDRASIL, STANDARDS roots, `domain:*`/`root:*` label namespaces that name internal systems.
- All real client / employer / past-employer names: SoundHound, Quant, IntelePeer, EPAS, Domain Intelligence, Heimdall (as product), any of them.
- Nate. The reader is the Operator; the author is Ravenhelm LLC.

**Neutralization map for initiatives.** The source material's initiative names ("Runestack Platform Reliability," "Heimdall Operator Experience," etc.) must be replaced with generic archetypes that any reader can adopt:

| Internal name (do not use) | Generic archetype (use this) |
|---|---|
| Runestack Platform Reliability | Platform Reliability |
| Heimdall Operator Experience | Operator Experience |
| HUGINN / AAS / Edge Sensing | New Product Bring-Up |
| Identity, Governance, Agent Accountability | Compliance Readiness |
| Ravenhelm Infrastructure | First Revenue (or Infrastructure Readiness, depending on chapter need) |

**Neutralization map for projects.** Same approach — generic names that describe shape, not internal identity:

| Internal name (do not use) | Generic example |
|---|---|
| Runestack CI/CD Operating Spine | CI/CD Backbone |
| Heimdall Production Stability | Production Stability |
| HUGINN Tier 2.5 / AAS MVP | Internal Product MVP |
| Bifrost and Kvasir Platform Integration | Internal Tooling Integration |

**Neutralization map for label namespaces.** Strip internal vocabulary, keep the structural shape:

| Internal namespace (do not use) | Generic namespace (use this) |
|---|---|
| `root:RUNESTACK`, `root:YGGDRASIL`, etc. | Drop entirely. The Method does not prescribe a `root:` namespace. |
| `component:Heimdall`, `component:Bifrost`, etc. | `component:<service-name>` — let the reader fill in their own services. |
| `domain:Security`, `domain:AI Governance`, etc. | `domain:<area>` — examples can include security, infrastructure, product, operations. |
| `agent:pm-ready`, `agent:research-agent`, etc. | Mention only in Chapter 6 (Tier 3) as a forward-looking pattern; do not prescribe specific agent label values in the freemium document. |

---

## 6. Doctrine citation

Numbered principles live in **Chapter 3 (The Numbered Principles)**. The full canonical scaffold is in `_shared/PRINCIPLES.md` — every agent reads that file. Cite principles as `P-1`, `P-2`, ..., `P-28` throughout.

**Citation rule:** any non-obvious claim should be tied to a principle. If a claim has no principle, it either needs one (flag it in your chapter draft) or the claim doesn't belong.

The principles in `PRINCIPLES.md` are the canon. Do not invent new P-#'s in other chapters. If your chapter genuinely needs a principle that isn't in the scaffold, **flag it at the end of your draft** in a `<!-- PRINCIPLE_GAP: ... -->` HTML comment so I can reconcile.

---

## 7. Mandatory callout boxes

**Every chapter must contain exactly two callout boxes**, in this exact format:

> **Augmentation Surface — [Name]**
>
> Where an agent layer makes this work better: [one or two sentences naming the capability — triage classification, project update drafting, evidence reconciliation, stale-work detection, etc.]
>
> What the PM keeps: [one sentence naming the judgment the human retains].

> **Where this gets hard**
>
> [One or two sentences naming the failure mode at real-team scale or in messy business reality — never "it depends" or "every org is different." Name the specific break.]
>
> Ravenhelm assesses your operating surface and installs the Method tuned to your team, your code host, and your reporting structure. [contact placeholder]

**Placement.** The Augmentation Surface box appears where it makes structural sense in the chapter body. The "Where this gets hard" box is always the final element of the chapter, after all H3 sections.

**Exception.** Chapter 12 (The Assessment) has neither — the chapter itself is the answer to both. Chapter 12's brief covers this.

**Contact placeholder.** Use the literal string `[contact placeholder]` in the "Where this gets hard" box. Do not invent an email or URL.

---

## 8. License header

Every chapter file **opens** with this exact block (no prose before it):

```
<!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
<!-- TODO: replace with final license boilerplate and enforcement language -->
```

Then a blank line, then the `## Chapter N — Title` heading, then a blank line, then the opening paragraph.

---

## 9. Length

- Target: 800–2400 words per chapter (~3–8 pages).
- Hard floor: 800 words (chapters below this are under-developed).
- Hard ceiling: 2600 words (chapters above this are flabby).
- Chapter 3 (Principles) may run longer (up to 3500 words) because it carries 28 principle entries with rationale and counter-examples.

---

## 10. Funnel discipline

Every chapter ends with "Where this gets hard." The reader should finish each chapter slightly more aware of what they can't install alone. Not manipulative — accurate. The Method genuinely takes assessment work to install correctly; the freemium document gives them the shape, the engagement gives them the fit.

**Do not include:** agent prompts, prompt-chain templates, agent orchestration patterns, or detail on how to build an AI PM. Those are Ravenhelm product. The Augmentation Surface boxes describe *what* an agent layer does, never *how*.

---

## 11. The canonical 12-chapter ordering

Use this ordering in cross-references. If your chapter references another, use the chapter number from this list.

1. **What This Is and Who It's For** — opening contract; tiered, human-centric operating model in Linear.
2. **The Seven Operating Layers** — initiatives, projects, issues, views, intake, delivery evidence, analytics. The structural shape.
3. **The Numbered Principles** — P-1..P-28 with rationale and counter-examples. Cited by every other chapter.
4. **The PM Operator Role** — what the human owns, the PM Operator practice ladder, daily/weekly shape.
5. **The Operating Surface: Labels, Views, Templates** — the mechanics by which the Method shows up in the workspace.
6. **Tier 1: Linear Free Install** — what a single PM can install in one week on Free.
7. **Tier 2: Linear Plus Upgrade** — initiatives, Customer Requests, Insights, richer documents.
8. **Tier 3: Linear Business and the Edge of Self-Install** — Triage Intelligence, Asks, SLAs, agent surfaces, MCP. Where self-install begins to break.
9. **Workflow Canon and the Validation Gate** — the 9 workflow states and why Validation is load-bearing.
10. **Code Host Integration: GitHub Primary, GitLab Parallel** — PR linking, branch conventions, status automation, Linear Releases.
11. **Reporting Up: Project Updates, Initiative Health, Monthly Review** — three templates the Operator hands upward.
12. **The Assessment: What This Document Doesn't Cover** — CTA. No callout boxes; the chapter is the answer.

---

## 12. Universal per-chapter rubric (the gate)

A chapter is not "done" until every box is checked. **Self-check at the bottom of your draft as a `<!-- RUBRIC_CHECK: ... -->` HTML comment.**

**Structural**
- License header block present at top, exactly as in §8.
- Chapter opens with a problem the reader recognizes, not a chapter-summary paragraph.
- `## Chapter N — Title` is the H2. `###` for sections. No `####` unless structurally required.
- Length within target (800–2400 words; Chapter 3 may run to 3500).
- Markdown valid; no rogue HTML beyond license block and the optional `<!-- PRINCIPLE_GAP -->` / `<!-- RUBRIC_CHECK -->` comments.

**Content**
- The 3-person team (Operator + Engineer A + Engineer B + Leadership Team) appears concretely at least once.
- All non-obvious claims tied to a `P-#`.
- No Norse names, no Ravenhelm-internal jargon, no real client / employer names.
- Voice is peer-level expert; no hedging, no filler, no marketing-speak.
- Prose by default; bullets only where enumeration is genuine.

**Funnel**
- "Augmentation Surface — [Name]" callout present, in standard format.
- "Where this gets hard" callout present at chapter end, in standard format.
- CTA is implicit through pain visibility, not a hard sell.
- (Chapter 12 exempt; the chapter itself is the CTA.)

**Chapter-type additions** (your individual brief tells you which apply):

| Chapter type | Extra gate |
|---|---|
| Tier chapter (6, 7, 8) | "Ceiling signal" subsection: how the reader knows they've outgrown this tier. |
| Doctrine chapter (3) | Every principle numbered, rationale stated, counter-example given. |
| Integration chapter (10) | GitHub path primary; GitLab equivalent included for every mechanic. |
| Reporting chapter (11) | At least one concrete template (project update, initiative update, monthly review). |
| Closing chapter (12) | Explicit CTA, no hedging. Names what assessment includes. No Augmentation Surface or "Where this gets hard" boxes. |

---

## 13. Source material

The chapters draw from internal Ravenhelm operating model docs at `/Users/nate/docs/20-operations/linear/`. **Always neutralize per §5 before incorporating.** Your chapter brief names the specific source sections that apply to you.

Canonical source files:

| File | What's in it |
|---|---|
| `00-office-model.md` | Internal — DO NOT cite. Office registry is Ravenhelm-internal and must be neutralized away entirely. |
| `01-mvp-operating-model.md` | MVP shape, initiatives, projects, workflow states, labels, views, GitHub automation, releases, SLAs, triage, Asks, customer requests, insights, AI PM role, weekly rhythm. **Primary source for Chapters 2, 4, 6, 7, 9.** |
| `02-end-state-operating-model.md` | End-state targets. Useful for Chapter 8 (Tier 3 capabilities). |
| `03-mvp-implementation-plan.md` | Phases 0–7 for installing the MVP. Source for tier-install steps in Chapters 6, 7, 8, 10. |
| `04-path-to-end-state.md` | AI PM maturity levels (reframed as PM Operator levels in Chapter 4). Source for Chapter 4. |
| `05-linear-capabilities-inventory.md` | 20-category Linear capability list. Source for Chapter 5 and tier chapters. |
| `06-how-nate-uses-everything.md` | Per-capability adoption notes. Useful background. |
| `07-linear-gap-analysis.md` | Methodology used by the Ravenhelm Operating Assessment. **Primary source for Chapter 12.** |
| `09-guidebook.md` | The 12-chapter Ravenhelm spine. Useful for cross-validation. |
| `10-doctrine.md` | P-1..P-13, R-1..R-6, O-1..O-12, D-1..D-8. **Primary source for Chapter 3's principles** (already extracted and neutralized into `_shared/PRINCIPLES.md`). |
| `11-playbook.md` | Step-by-step recipes. Useful for Chapter 6 (install steps). |
| `12-reference.md` | Workspace inventory, label catalog, view catalog. Useful for Chapter 5. |

Read what you need. Do not bulk-quote — neutralize, compress, and rewrite in the Method's voice.

---

## 14. Output

Write your chapter to the exact path given in your individual brief. Do not write to any other path. Do not create supporting files.

When done, the final lines of your file should be:

```
<!-- RUBRIC_CHECK:
  structural: pass
  content: pass
  funnel: pass
  chapter-type-extras: pass
  word-count: <actual count>
  principle-citations: <list of P-# you cited>
  flagged-principle-gaps: <none | list>
-->
```

If any rubric line is `fail`, name what failed and why. The orchestrator will reconcile before publication.
