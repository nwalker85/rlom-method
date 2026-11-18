#!/usr/bin/env python3
"""Typeset Ravenhelm Linear Operating Method (RLOM) as publication-grade PDF using Typst.

Compiles two editions:
  dark   - bone on obsidian (screen edition, matching RDOM Dark and RROM Dark)
  print  - obsidian on bone paper (the print / digest edition)

Faces: Source Serif 4 (proposition/body), IBM Plex Mono (evidence/folios/code/colophon).
Trim: 5.5 x 8.5 in (digest chapbook / executive monograph).
"""
import os
import re
import sys
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT, "docs", "chapters")
ASSETS_DIR = os.path.join(ROOT, "assets")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
OUTDIR = ROOT

BYLINE = "Nathan Walker"
IMPRINT = "Ravenhelm Publishing Series LLC"
COPYRIGHT = "© 2026 Ravenhelm LLC. All rights reserved."

CHAPTER_FILES = [
    ("01-what-this-is.md", "01", "What This Is and Who It's For", "INSTALL PATH · BOOK I OF THE TRILOGY · P-1 · P-2 · P-6 · P-13 · P-16 · P-27 · P-28", "The Workspace Rot Confession · Floor-Manager Lineage · The 3-Person Scaffold · The Contract"),
    ("02-seven-layers.md", "02", "The Seven Operating Layers", "INSTALL PATH · ARCHITECTURE · P-1 · P-2 · P-3 · P-4 · P-5 · P-6 · P-7 · P-8", "Curing Altitude Drift · Initiatives · Projects · Issues · Views · Intake · Evidence · Analytics"),
    ("03-numbered-principles.md", "03", "The Numbered Principles", "CANON · 29 NUMBERED PRINCIPLES · P-1 THROUGH P-29", "The Work Graph · Evidence & Validation · Workflow Canon · The Operator · Surface · Cadence"),
    ("04-operator-role.md", "04", "The PM Operator Role", "INSTALL PATH · HUMAN AUTHORITY · P-6 · P-7 · P-13 · P-14 · P-15 · P-19 · P-27", "XMPP Floor Management · Counterintelligence Judgment · The 5-Level Practice Ladder"),
    ("05-operating-surface.md", "05", "The Operating Surface: Labels, Views, Templates", "INSTALL PATH · MECHANICS · P-4 · P-11 · P-15 · P-16 · P-17 · P-18 · P-24", "Curing 160-Label Noise · Orthogonal Label Axes · The 6 Core Views · Issue Templates"),
    ("06-tier-1-free.md", "06", "Tier 1: Linear Free Install", "INSTALL PATH · WEEK ONE WORKBENCH · P-1 · P-2 · P-3 · P-6 · P-10 · P-16 · P-17", "Defeating the Hal Problem · Five-Day Bring-Up · Running on Free · The Ceiling Signal"),
    ("07-tier-2-basic.md", "07", "Tier 2: Linear Basic and the Separation of Powers", "TIER 2 UPGRADE · SEPARATION OF POWERS · P-6 · P-7 · P-13 · P-18 · P-20 · P-24", "Producer, Commander, and Witness · Administrative Boundaries · Standing Up the Second Team"),
    ("08-tier-3-business.md", "08", "Tier 3: Linear Business and the Seam Where Agents Enter", "TIER 3 UPGRADE · AGENT GOVERNANCE · P-6 · P-7 · P-13 · P-14 · P-15 · P-20 · P-25", "Why the Social Layer Does Not Transfer · Insights & SLAs · Governing Coding Agents"),
    ("09-tier-4-enterprise.md", "09", "Tier 4: Linear Enterprise and Portfolio Governance at Scale", "TIER 4 UPGRADE · FEDERATED SCALE · P-2 · P-13 · P-14 · P-15 · P-18 · P-21 · P-28", "Multi-Contract Floor Control · SAML/SCIM Identity · Sub-Teams · Portfolio Dashboards"),
    ("10-workflow-canon.md", "10", "Workflow Canon and the Validation Gate", "INSTALL PATH · WORKFLOW CANON · P-6 · P-7 · P-8 · P-9 · P-10 · P-11 · P-12", "Why Merged != Built != Running · The Nine States · The Five Evidence Types · Defeating Auto-Close"),
    ("11-cycles-roadmaps-cadence.md", "11", "Cycles, Roadmaps & Cadence", "CADENCE & HORIZON · P-2 · P-3 · P-4 · P-19 · P-21 · P-24 · P-26", "Killing Sprint Velocity Theater · The 70% Capacity Rule · Plan-of-Record vs. What-If Roadmaps"),
    ("12-code-host-integration.md", "12", "Code Host Integration: GitHub Primary, GitLab & Forgejo Parallel", "INTEGRATION · FORGE MECHANICS · P-6 · P-7 · P-8 · P-9 · P-23 · P-25 · P-29", "Inline RAV-ID Guards · Defeating the Auto-Close Trap · Self-Hosted Webhooks · SemVer Releases"),
    ("13-reporting-up.md", "13", "Reporting Up: Project Updates, Initiative Health, and the Monthly Review", "INSTALL PATH · EXECUTIVE REPORTING · P-2 · P-13 · P-19 · P-21 · P-27 · P-28", "Why a Summary Is a Lossy Transform · Separating Measurement from Conclusion · RAG Health"),
    ("14-the-assessment.md", "14", "The Assessment: Auditing Presence vs. Absence", "DIAGNOSTIC AUDIT · PRESENCE VS. ABSENCE · P-1 THROUGH P-29", "Three Aphorisms of Operational Hygiene · What Fails Silently · The Ravenhelm Assessment"),
    ("appendix-a-operations-team.md", "A", "The Operations-Team Variant", "APPENDIX A · DEMAND-SIDE INTAKE & COE GOVERNANCE · P-1 · P-6 · P-16 · P-20 · P-22", "Supply-Side vs. Demand-Side · Service Catalog · CoE Field Discipline · Non-Code Ledgers"),
]

def markdown_to_typst_via_pandoc(md_path, edition):
    """Converts a Markdown file to Typst syntax via pandoc with post-processing."""
    raw_md = open(md_path, "r", encoding="utf-8").read()

    # Strip HTML license comments and rubric checks
    cleaned_md = re.sub(r"<!--.*?-->", "", raw_md, flags=re.S)

    # Strip the top-level chapter heading since Typst renders custom chapter opener
    cleaned_md = re.sub(r"^\s*#+\s+(Chapter\s+\d+|Appendix\s+[A-Z]).*?\n", "", cleaned_md, count=1, flags=re.M)

    res = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "typst"],
        input=cleaned_md,
        text=True,
        capture_output=True,
        check=True
    )
    return res.stdout

def build_typst_document(edition):
    """Assembles the complete Typst source code for the requested edition."""
    if edition == "print":
        ink = "#0B0C0E"
        paper = "#EDE8DC"
        ash = "#6F6A62"
        garnet = "#A3222F"
        gold = "#96752C"
        card_bg = "#E2DDD1"
        card_border = "#B0A898"
        raven_logo = "assets/ravenhelm-raven-black-eye.svg"
    else:  # dark
        ink = "#EDE8DC"
        paper = "#0B0C0E"
        ash = "#8E939B"
        garnet = "#A3222F"
        gold = "#C4A45A"
        card_bg = "#14171C"
        card_border = "#2B303A"
        raven_logo = "assets/ravenhelm-raven-bone-eye.svg"

    def format_toc_title(t):
        wrap_targets = [
            "Tier 2: Linear Basic and the Separation of Powers",
            "Tier 3: Linear Business and the Seam Where Agents Enter",
            "Tier 4: Linear Enterprise and Portfolio Governance at Scale",
            "Code Host Integration: GitHub Primary, GitLab & Forgejo Parallel",
            "Reporting Up: Project Updates, Initiative Health, and the Monthly Review",
        ]
        if t in wrap_targets and ": " in t:
            p1, p2 = t.split(": ", 1)
            return p1 + ":#linebreak()" + p2
        return t

    toc_p1_lines = []
    for file_name, num, title, badge_text, summary in CHAPTER_FILES[:8]:
        label_id = f"ch-{num.lower()}"
        toc_title = format_toc_title(title)
        toc_p1_lines.append(f'  #toc-entry("{num}", [{toc_title}], "{label_id}", "{summary}")')
    toc_p1_str = "\n".join(toc_p1_lines)

    toc_p2_lines = []
    for file_name, num, title, badge_text, summary in CHAPTER_FILES[8:]:
        label_id = f"ch-{num.lower()}"
        toc_title = format_toc_title(title)
        toc_p2_lines.append(f'  #toc-entry("{num}", [{toc_title}], "{label_id}", "{summary}")')
    toc_p2_str = "\n".join(toc_p2_lines)

    preamble = f'''
#let ink = rgb("{ink}")
#let paper = rgb("{paper}")
#let ash = rgb("{ash}")
#let garnet = rgb("{garnet}")
#let gold = rgb("{gold}")
#let card_bg = rgb("{card_bg}")
#let card_border = rgb("{card_border}")

#set document(
  title: "Ravenhelm Linear Operating Method (RLOM)",
  author: "{BYLINE}",
  keywords: ("RLOM", "Ravenhelm", "Linear", "Operating Model", "Validation Gate", "Autonomous Agents", "Work Graph")
)

#set page(
  width: 5.5in,
  height: 8.5in,
  margin: (top: 0.85in, bottom: 0.85in, inside: 0.85in, outside: 0.75in),
  fill: paper
)

#set text(
  font: "Source Serif 4",
  size: 9.6pt,
  fill: ink,
  lang: "en",
  hyphenate: true
)

#set par(
  justify: true,
  leading: 0.68em,
  first-line-indent: 1.1em,
  spacing: 0.72em
)

// Suppress heading hyphenation
#show heading: set text(hyphenate: false)

// Headings styling
#show heading.where(level: 1): it => block(
  spacing: 0.4em,
  text(font: "Source Serif 4", size: 19pt, weight: 600, fill: ink)[#it.body]
)

#show heading.where(level: 2): it => block(
  spacing: 1.1em,
  text(font: "Source Serif 4", size: 13pt, weight: 600, fill: garnet)[#it.body]
)

#show heading.where(level: 3): it => block(
  spacing: 0.9em,
  text(font: "Source Serif 4", size: 10.5pt, weight: 600, fill: ink)[#it.body]
)

#show heading.where(level: 4): it => block(
  spacing: 0.7em,
  text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: ash, tracking: 0.08em)[#it.body]
)

// Code styling: inline raw code
#show raw.where(block: false): it => box(
  fill: card_bg,
  inset: (x: 2.5pt, y: 0pt),
  outset: (y: 2.5pt),
  radius: 2pt
)[#text(font: "IBM Plex Mono", size: 8.0pt, it)]

// Code styling: block code
#show raw.where(block: true): it => block(
  width: 100%,
  clip: true,
  breakable: true,
  fill: card_bg,
  stroke: 0.5pt + card_border,
  inset: 7pt,
  radius: 3pt,
  spacing: 0.9em,
  text(font: "IBM Plex Mono", size: 6.8pt, fill: ink, it)
)

// Quote / Callout styling
#show quote: it => block(
  width: 100%,
  breakable: true,
  fill: card_bg,
  stroke: (left: 2.5pt + garnet, rest: 0.5pt + card_border),
  inset: (x: 9pt, y: 7pt),
  radius: (right: 3pt),
  spacing: 0.9em,
  text(style: "italic", size: 8.8pt, it.body)
)

// Table styling
#show table: set text(font: "IBM Plex Mono", size: 6.8pt)
#show table.cell.where(y: 0): set text(weight: "bold", fill: ink)

// Math equation styling
#show math.equation.where(block: true): set text(size: 8.2pt)

// Table of Contents custom entry helpers (RLOM standard)
#let toc-prelim(title, label-id) = [
  #v(0.25em)
  #block(width: 100%)[
    #text(font: "Source Serif 4", size: 8.6pt, style: "italic", fill: ink)[#link(label(label-id))[#title]]
    #box(width: 1fr, pad(x: 4pt, repeat([#text(fill: ash, size: 7pt)[. ]])))
    #text(font: "IBM Plex Mono", size: 7.8pt, fill: ash)[#context counter(page).at(label(label-id)).first()]
  ]
]

#let toc-entry(num, title, label-id, summary) = [
  #v(0.24em)
  #grid(
    columns: (18pt, 1fr),
    gutter: 5pt,
    text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet)[#num],
    [
      #block(width: 100%)[
        #text(font: "Source Serif 4", size: 8.4pt, weight: 600, fill: ink)[#link(label(label-id))[#title]]
        #box(width: 1fr, pad(x: 4pt, repeat([#text(fill: ash, size: 7pt)[. ]])))
        #text(font: "IBM Plex Mono", size: 7.8pt, fill: ash)[#context counter(page).at(label(label-id)).first()]
      ]
      #v(0.05em)
      #text(font: "Source Serif 4", size: 7.0pt, fill: ash)[#summary]
    ]
  )
]

// ==========================================
// 1. FRONT COVER
// ==========================================
#page(
  margin: (x: 0.85in, top: 0.9in, bottom: 0.9in),
  numbering: none,
  header: none,
  footer: none
)[
  #align(center)[
    #v(0.35in)
    #image("{raven_logo}", width: 2.25in)
    #v(0.40in)
    #text(font: "IBM Plex Mono", size: 7.0pt, fill: garnet, tracking: 0.14em)[THE RAVENHELM OPERATIONS METHODOLOGY · BOOK I]
    #v(0.12in)
    #text(font: "Source Serif 4", size: 16.5pt, weight: 600, fill: ink)[Ravenhelm Linear Operating]
    #v(0.08in)
    #text(font: "Source Serif 4", size: 14.5pt, weight: 400, fill: garnet)[Method]
    #v(0.28in)
    #block(width: 82%)[
      #set par(leading: 0.65em)
      #text(font: "IBM Plex Mono", size: 7.0pt, fill: ash, tracking: 0.10em)[A TIERED, RECEIPT-DRIVEN OPERATING MODEL FOR RUNNING A SOFTWARE TEAM AND AGENT FLEET ON LINEAR]
    ]
    #v(1fr)
    #text(font: "Source Serif 4", size: 10.5pt, weight: 600, fill: ink)[{BYLINE}]
    #v(0.06in)
    #text(font: "IBM Plex Mono", size: 7.2pt, fill: ash, tracking: 0.12em)[RAVENHELM LLC · 2026]
    #v(0.15in)
  ]
]

// ==========================================
// 2. VERSO / COPYRIGHT & IMPRINT
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(1.4in)
  #align(center)[
    #text(font: "Source Serif 4", size: 13pt, weight: 600)[Ravenhelm Linear Operating Method]
    #v(0.18in)
    #text(font: "Source Serif 4", size: 9.5pt, style: "italic", fill: ash)[
      "Code that is merged is implemented.\\
       Only code proven in live reality is trusted."
    ]
    #v(0.08in)
    #text(font: "IBM Plex Mono", size: 7pt, fill: garnet, tracking: 0.14em)[THE VALIDATION AXIOM (P-6)]
  ]
  #v(1fr)
  #set text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.04em, hyphenate: false)
  #set par(justify: false, first-line-indent: 0em, leading: 0.9em)
  *Ravenhelm Linear Operating Method (RLOM)* \\
  Book I of *The Ravenhelm Operations Methodology* (*RLOM · RDOM · RROM*) \\
  Version 1.0.3 (2026-11-17) \\
  Authored by {BYLINE}. \\
  {COPYRIGHT} \\
  Published by {IMPRINT}. \\
  \\
  Distributed under the *RLOM Community License 1.0*. \\
  Free to read and implement internally. Verbatim, unmodified copies may be redistributed for non-commercial, personal, or educational purposes. Commercial training, certification, and third-party RLOM services reserved by Ravenhelm LLC. \\
  \\
  Inquiries: nate\\@ravenhelm.co · ravenhelm.co \\
  Source repository: github.com/nwalker85/rlom-method \\
  \\
  Set in Source Serif 4 and IBM Plex Mono. \\
  Typeset using Typst on macOS. \\
  #v(0.4in)
]

// ==========================================
// 3. TABLE OF CONTENTS (RLOM STANDARD)
// ==========================================
#page(
  margin: (top: 0.65in, bottom: 0.65in, inside: 0.85in, outside: 0.75in),
  numbering: none,
  header: none,
  footer: none
)[
  #v(0.08in)
  #align(left)[
    #text(font: "Source Serif 4", size: 20pt, weight: 600, fill: ink)[Contents]
  ]
  #v(0.12in)

  #toc-prelim("How to read it", "front-how-to-read")
  #toc-prelim("The principles at a glance", "front-principles")

  #v(0.6em)

{toc_p1_str}
]

#page(
  margin: (top: 0.65in, bottom: 0.65in, inside: 0.85in, outside: 0.75in),
  numbering: none,
  header: none,
  footer: none
)[
  #v(0.12in)
{toc_p2_str}
]

// ==========================================
// 4. HOW TO READ IT
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(0.3in)
  #align(left)[
    #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[GUIDE]
    #v(0.08in)
    #heading(level: 1, numbering: none, outlined: true)[How to Read It] <front-how-to-read>
    #v(0.05in)
    #line(length: 100%, stroke: 0.5pt + ash)
  ]
  #v(0.15in)

  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[IN ORDER] \\
  #set text(size: 8.8pt)
  The chapters build on each other from the seven-layer work graph to the four plan tiers, the nine-state workflow canon, code-host integration, upward reporting, and workspace auditing. Chapter 3 (*The Numbered Principles*) establishes the 29 rules cited throughout every subsequent chapter as `P-1` through `P-29`.

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[BY ROLE - THE INSTALL PATH] \\
  #set text(size: 8.8pt)
  *Install Monday (Linear Free, 3-Person Team):* Chapters 01, 02, 04, 05, 06, 10, 13 (Skim Chapter 03; defer 07, 08, 09, 11, 12, 14 until needed). \\
  *PM Already on Basic:* Chapters 01, 03, 07, 10, 11, 12, 13 (Then revisit Chapter 05 to tune labels and views). \\
  *Evaluating Business or Coding Agents:* Chapters 03, 08, 10, 12, 13, 14. \\
  *Leadership & Executive Sponsor:* Chapters 01, 13, 14. \\
  *Operations, PMO & CoE Teams:* Chapters 01, 02, 05, 08, 13, Appendix A.

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[BY NEED - RECOVERY & SCALING] \\
  #set text(size: 8.8pt)
  *Cleaning Up Label & Workflow Rot:* Read Chapters 01, 05, 06, 10. \\
  *Stopping Premature "Done" & Auto-Close Traps:* Read Chapters 03, 10, 12. \\
  *Fixing Executive Blindness & Status Theater:* Read Chapters 02, 11, 13, 14.

  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7.8pt, weight: 600, fill: garnet, tracking: 0.12em)[NAVIGATING THIS BOOK] \\
  #set text(size: 8.8pt)
  The bookmark outline carries every chapter and section. Chapter openers list the operating scope and the numbered principles each chapter cites.
]

// ==========================================
// 5. THE PRINCIPLES AT A GLANCE
// ==========================================
#page(numbering: none, header: none, footer: none)[
  #v(0.25in)
  #align(left)[
    #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[CANON]
    #v(0.06in)
    #heading(level: 1, numbering: none, outlined: true)[The Principles at a Glance] <front-principles>
    #v(0.04in)
    #line(length: 100%, stroke: 0.5pt + ash)
  ]
  #v(0.08in)
  #set text(font: "IBM Plex Mono", size: 6.6pt, fill: ash)
  #set par(justify: false, first-line-indent: 0em, leading: 0.68em)

  #text(weight: "bold", fill: garnet)[GROUP A - THE WORK GRAPH (THE SHAPE)] \\
  #text(fill: ink)[P-01] Linear is the active work graph, not an archive \\
  #text(fill: ink)[P-02] Initiatives are the objective layer \\
  #text(fill: ink)[P-03] Projects are the main execution container \\
  #text(fill: ink)[P-04] Issues are deliverable-sized \\
  #text(fill: ink)[P-05] Documentation owns deep context \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP B - EVIDENCE AND VALIDATION] \\
  #text(fill: ink)[P-06] Validation separates implemented from trusted \\
  #text(fill: ink)[P-07] Evidence beats assertion \\
  #text(fill: ink)[P-08] The code host proves implementation \\
  #text(fill: ink)[P-09] Production work does not go Done before release evidence \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP C - WORKFLOW CANON] \\
  #text(fill: ink)[P-10] The workflow canon is nine states \\
  #text(fill: ink)[P-11] Stage labels carry the things that look like states but aren't \\
  #text(fill: ink)[P-12] Prefer parent issues with sub-issues over giant single issues \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP D - THE OPERATOR] \\
  #text(fill: ink)[P-13] The Operator owns priority, taste, risk, and real-world commitments \\
  #text(fill: ink)[P-14] Agents are executors, not owners \\
  #text(fill: ink)[P-15] Agent delegation requires acceptance criteria and a validation command \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP E - THE OPERATING SURFACE] \\
  #text(fill: ink)[P-16] Labels exist to serve views \\
  #text(fill: ink)[P-17] Templates lower the cost of doing the right thing \\
  #text(fill: ink)[P-18] Locality wins \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP F - CADENCE] \\
  #text(fill: ink)[P-19] Active projects get a status update every week \\
  #text(fill: ink)[P-20] Triage has a seven-day SLA \\
  #text(fill: ink)[P-21] Initiative updates run biweekly; monthly review rolls up to Leadership \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP G - INTAKE AND FEEDBACK] \\
  #text(fill: ink)[P-22] Customer feedback does not directly become scope \\
  #text(fill: ink)[P-23] The system of record is Linear \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP H - SYSTEM HYGIENE] \\
  #text(fill: ink)[P-24] The overbuild test (four of five yes to adopt) \\
  #text(fill: ink)[P-25] Verify what you enforce \\
  #text(fill: ink)[P-26] Capacity commits to seventy percent \\
  #v(0.3em)
  #text(weight: "bold", fill: garnet)[GROUP I - REPORTING & GROUP J - RELEASES] \\
  #text(fill: ink)[P-27] Leadership consumes summaries, not raw Linear \\
  #text(fill: ink)[P-28] The evidence chain holds \\
  #text(fill: ink)[P-29] Releases are named with Semantic Versioning
]

// ==========================================
// 6. RUNNING HEADERS & BODY PAGES
// ==========================================
#set page(
  numbering: "1",
  number-align: center,
  footer: context [
    #set text(font: "IBM Plex Mono", size: 7.5pt, fill: ash, tracking: 0.08em)
    #align(center)[#counter(page).display("1")]
  ],
  header: context [
    #set text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.14em)
    #let page_num = counter(page).get().first()
    #let is_chapter_opener = query(heading.where(level: 1)).any(h => h.location().page() == page_num)
    #if not is_chapter_opener [
      #if calc.odd(page_num) [
        #align(right)[RAVENHELM LINEAR OPERATING METHOD]
      ] else [
        #align(left)[{BYLINE} · RLOM METHOD]
      ]
    ]
  ]
)

'''

    body_chapters = []
    for file_name, num, title, badge_text, summary in CHAPTER_FILES:
        chapter_path = os.path.join(DOCS_DIR, file_name)
        if not os.path.exists(chapter_path):
            continue
        typst_content = markdown_to_typst_via_pandoc(chapter_path, edition)

        is_appendix = num in ("A", "B")
        label_prefix = "APPENDIX" if is_appendix else "CHAPTER"

        chapter_header = f"""
#pagebreak()
#v(0.8in)
#align(left)[
  #text(font: "IBM Plex Mono", size: 8.5pt, weight: 600, fill: garnet, tracking: 0.16em)[{label_prefix} · {num}]
  #v(0.08in)
  #heading(level: 1, numbering: (..n) => "{num}", outlined: true)[{title}] <ch-{num.lower()}>
  #v(0.12in)
  #text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.08em)[{badge_text}]
  #v(0.05in)
  #line(length: 100%, stroke: 0.5pt + ash)
]
#v(0.3in)
"""
        chapter_block = chapter_header + typst_content
        body_chapters.append(chapter_block)

    colophon = f'''
// ==========================================
// 8. COLOPHON
// ==========================================
#pagebreak()
#set page(numbering: none, header: none, footer: none)
#v(1fr)
#align(center)[
  #image("{raven_logo}", width: 1.1in)
  #v(0.25in)
  #set text(font: "IBM Plex Mono", size: 7pt, fill: ash, tracking: 0.04em, hyphenate: false)
  #set par(justify: false, first-line-indent: 0em, leading: 0.95em)
  Ravenhelm Linear Operating Method (RLOM) \\
  Book I of The Ravenhelm Operations Methodology (RLOM · RDOM · RROM) \\
  Version 1.0.3 (2026-11-17) \\
  Authored by {BYLINE}. \\
  {COPYRIGHT} \\
  Published by {IMPRINT}. \\
  Distributed under the RLOM Community License 1.0. \\
  Set in Source Serif 4 and IBM Plex Mono. \\
  Typeset using Typst on macOS. \\
  ravenhelm.co · nwalker.cc
]
#v(0.6in)
'''

    return preamble + "\n".join(body_chapters) + colophon

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    for edition in ("dark", "print"):
        typ_content = build_typst_document(edition)
        typ_path = os.path.join(OUTDIR, f"build-rlom-{edition}.typ")
        with open(typ_path, "w", encoding="utf-8") as f:
            f.write(typ_content)

        if edition == "dark":
            pdf_path = os.path.join(OUTDIR, "RLOM-v1.0.3-dark.pdf")
        else:
            pdf_path = os.path.join(OUTDIR, "RLOM-v1.0.3.pdf")

        cmd = [
            "typst", "compile",
            "--root", ROOT,
            "--font-path", FONTS_DIR,
            typ_path,
            pdf_path
        ]
        print(f"Compiling {edition} edition -> {pdf_path}...")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error compiling {edition}:", res.stderr, file=sys.stderr)
            sys.exit(res.returncode)
        print(f"Successfully compiled {pdf_path}")

        # Clean up temporary .typ file
        if os.path.exists(typ_path):
            os.remove(typ_path)

if __name__ == "__main__":
    main()
