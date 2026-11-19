# RLOM Shared Context - READ FIRST

This file is **read by every chapter-writing agent before drafting or editing**. It is the source of truth for voice, style mechanics (`STYLE-GUIDE.md`), terminology boundaries, callout formats, the rubric every chapter must pass, and the canonical 14-chapter (+ Appendix A) ordering for **Book I of the Ravenhelm Operations Methodology** (*The Sovereign Engineering Trilogy: RLOM · RDOM · RROM*).

If anything in this file contradicts an individual chapter brief, this file wins.

---

## 1. Document Identity

- **Title:** Ravenhelm Linear Operating Method (RLOM)
- **Series Position:** Book I of *The Ravenhelm Operations Methodology* (*The Sovereign Engineering Trilogy: RLOM · RDOM · RROM*)
- **Author:** Nathan Walker / Ravenhelm LLC
- **License Posture:** RLOM Community License 1.0 (free to read and self-install internally; commercial advisory and implementation via Ravenhelm LLC).
- **Reader Profile:** A single PM Operator running a 3-person team (the Operator, Engineer A, and Engineer B) reporting to a leadership team, scaling up to multi-contract enterprises supervising both human engineers and autonomous coding agents.

---

## 2. Voice, Posture, and Mechanics (`STYLE-GUIDE.md`)

Every chapter obeys the ten mechanical rules of the unified Ravenhelm style register:

1. **Zero Prose Em-Dashes (`—`):** Replace every `—` in prose with `;` (when joining two weighted clauses/pivots) or ` - ` (spaced hyphen for parentheticals/asides).
2. **Start at the Crime Scene on the Bench (Never in the Lecture Hall):** Kill throat-clearing openers (*"In modern software engineering..."*, *"For decades, organizations have..."*). Open with the broken workspace on the bench, the exact date, the exact metric (`14 workflow states, ~160 labels, and 0 of 45 projects with health set`), or the production scar.
3. **Show the Corpse of v1 ("The Wrong One We Built First"):** Never present a principle as if it fell from the sky whole. Show the naive v1 built first, the failure mode that killed it under real load, and the constraint that forced the real design.
4. **High-Low Collision (Cathedral Math + Shop-Floor Nouns):** Collide exact technical primitives (`GraphQL mutation`, `webhook HMAC`, `DAG topological sort`, `RAV-<id>`) with blunt physical nouns (`corpse`, `hinge`, `wreckage`, `receipt`, `blindfold`).
5. **Bench Imperatives Over Brochure Descriptions:** Unwind nominalizations and brochure verbs into direct second-person shop-floor recipes.
6. **Rhythm: Long-Build Verse -> Short-Knife Breakdown:** Accumulate evidence in multi-clause paragraphs, then land the verdict in a knife sentence of 5 words or fewer inside the paragraph (*"The contract is vibes."* / *"Fix the mechanism."*).
7. **Repetition Must Carry a Receipt:** Never repeat a phrase for rhetorical rhythm alone; the second occurrence must add the paperwork.
8. **Exact Numbers Always:** Use exact numbers from the ledger (`14 workflow states and ~160 labels`, `0 of 45 projects`, `300+ actors across 15-20 contracts`), never vague approximations.
9. **Lineation: Paragraphs by Default:** Keep narration and analysis in solid paragraphs; knife sentences cut *inside* the paragraph after a long sentence.
10. **Terminology Boundaries:**
    - **No Myth / Codex vocabulary leakage:** Personal codex terms (*Wyrd Rune*, *Saga's Vow*, *Althing*, *Ráð*, *Four Codices*, *Valknut OKR*, *Jarl*, *Thegn*, *Skald*, *Berserkr*) belong to personal codex writing and never leak into ops docs.
    - **Real running system receipts allowed:** Real estate systems (`Bifrost`, `Heimdall`, `Vitki`, `Ullr`/`Yager`, `Idunn`, `Doom`/`Doomcourt`, `EAT`, `Snotra`, `Harbor`, `OpenBao`, `Valkyrie`, `Norns`) and operational lineage receipts (TNI 300-person XMPP floor management, J3B counterintelligence verification) are valid architectural receipts when introduced with their functional role.

---

## 3. The Canonical 3-Person Team Scaffold

Every chapter grounds its mechanics in the canonical 3-person team so a small team never drowns in enterprise ceremony, while showing how the exact same spine scales to multi-team and agent-fleet operations:

- **The Operator** - the PM / technical lead / fleet supervisor. The reader IS the Operator.
- **Engineer A** and **Engineer B** - the builders (and, from Chapter 8 onward, delegated coding-agent slices operating under human sign-off).
- **The Leadership Team** - the upward-facing audience that consumes project updates and initiative health without browsing raw tickets.

---

## 4. Formatting & Structure

- Markdown only; valid under `.markdownlint.yml`.
- Every chapter file opens with the two-line license comment block:

  ```markdown
  <!-- LICENSE: © 2026 Ravenhelm LLC. Licensed material. -->
  <!-- All rights reserved except as granted in LICENSE. Inquiries: nate@ravenhelm.co -->
  ```

- `## Chapter N - Title` is the H2 root of its own file (`###` for sections, `####` sparingly).
- Numbered principles are cited inline as `P-1` through `P-29` (defined in `docs/_shared/PRINCIPLES.md` and expanded in Chapter 3).
- Every chapter (except Chapter 14) includes an `Augmentation Surface` callout and closes with a `Where this gets hard` callout referencing `nate@ravenhelm.co`, followed by a `<!-- RUBRIC_CHECK -->` comment block.

---

## 5. Canonical 14-Chapter + Appendix Ordering

1. **Chapter 01 (`01-what-this-is.md`):** What This Is and Who It's For
2. **Chapter 02 (`02-seven-layers.md`):** The Seven Operating Layers
3. **Chapter 03 (`03-numbered-principles.md`):** The Numbered Principles (`P-1`..`P-29`)
4. **Chapter 04 (`04-operator-role.md`):** The PM Operator Role
5. **Chapter 05 (`05-operating-surface.md`):** The Operating Surface: Labels, Views, Templates
6. **Chapter 06 (`06-tier-1-free.md`):** Tier 1: Linear Free Install
7. **Chapter 07 (`07-tier-2-basic.md`):** Tier 2: Linear Basic and the Separation of Powers
8. **Chapter 08 (`08-tier-3-business.md`):** Tier 3: Linear Business and the Seam Where Agents Enter
9. **Chapter 09 (`09-tier-4-enterprise.md`):** Tier 4: Linear Enterprise and Portfolio Governance at Scale
10. **Chapter 10 (`10-workflow-canon.md`):** Workflow Canon and the Validation Gate
11. **Chapter 11 (`11-cycles-roadmaps-cadence.md`):** Cycles, Roadmaps & Cadence
12. **Chapter 12 (`12-code-host-integration.md`):** Code Host Integration: GitHub Primary, GitLab & Forgejo Parallel
13. **Chapter 13 (`13-reporting-up.md`):** Reporting Up: Project Updates, Initiative Health, and the Monthly Review
14. **Chapter 14 (`14-the-assessment.md`):** The Assessment: Auditing Presence vs. Absence
15. **Appendix A (`appendix-a-operations-team.md`):** The Operations-Team Variant
