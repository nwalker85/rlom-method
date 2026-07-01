#!/usr/bin/env bash
#
# compile.sh — concatenate the 14 RLOM chapters (plus the Operations-Team appendix) into a single-file edition.
#
# Usage:
#   ./scripts/compile.sh > build/rlom.md
#   ./scripts/compile.sh --with-shared > build/rlom-annotated.md
#
# Output: a single Markdown document with a generated table of contents,
# chapters in canonical order, and a horizontal rule between each chapter.
#
# Notes:
#   - Chapters carry their own license header; the compiled doc preserves the
#     first one and strips duplicates from later chapters.
#   - Chapters end with a <!-- RUBRIC_CHECK --> HTML comment; the compiled doc
#     keeps these (useful for audit) but they could be stripped for publication.
#
# Exit codes:
#   0 — success
#   1 — chapter file missing
#   2 — invalid argument

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHAPTERS_DIR="${ROOT}/docs/chapters"
SHARED_DIR="${ROOT}/docs/_shared"

WITH_SHARED=0
case "${1:-}" in
    --with-shared) WITH_SHARED=1 ;;
    "" ) ;;
    *)
        echo "Usage: $0 [--with-shared]" >&2
        exit 2
        ;;
esac

CHAPTERS=(
    "01-what-this-is.md"
    "02-seven-layers.md"
    "03-numbered-principles.md"
    "04-operator-role.md"
    "05-operating-surface.md"
    "06-tier-1-free.md"
    "07-tier-2-basic.md"
    "08-tier-3-business.md"
    "09-tier-4-enterprise.md"
    "10-workflow-canon.md"
    "11-cycles-roadmaps-cadence.md"
    "12-code-host-integration.md"
    "13-reporting-up.md"
    "14-the-assessment.md"
    "appendix-a-operations-team.md"
)

# Verify all chapter files exist before printing anything
for ch in "${CHAPTERS[@]}"; do
    if [ ! -f "${CHAPTERS_DIR}/${ch}" ]; then
        echo "ERROR: missing chapter file: ${CHAPTERS_DIR}/${ch}" >&2
        exit 1
    fi
done

# Title block (license header from chapter 1 is preserved at the top)
printf '# Ravenhelm Linear Operating Method\n\n'
printf '*A tiered, human-centric operating model for running a software team on Linear.*\n\n'
printf '© 2026 Ravenhelm LLC. Licensed material.\n\n'
printf -- '---\n\n'

# Generated table of contents
printf '## Table of contents\n\n'
i=1
for ch in "${CHAPTERS[@]}"; do
    title=$(grep -m1 -E '^## (Chapter|Appendix)' "${CHAPTERS_DIR}/${ch}" | sed 's/^## //')
    if [ -z "${title}" ]; then
        title="Chapter ${i}"
    fi
    anchor=$(printf '%s' "${title}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | tr -s '-')
    printf -- '- [%s](#%s)\n' "${title}" "${anchor}"
    i=$((i + 1))
done
printf '\n---\n\n'

# Optionally include the authoring spec (useful for internal review builds)
if [ "${WITH_SHARED}" -eq 1 ]; then
    printf '## Authoring spec (internal)\n\n'
    printf '### CONTEXT\n\n'
    cat "${SHARED_DIR}/CONTEXT.md"
    printf '\n---\n\n'
    printf '### PRINCIPLES scaffold\n\n'
    cat "${SHARED_DIR}/PRINCIPLES.md"
    printf '\n---\n\n'
fi

# Chapters — strip the license header from all chapters after the first (kept at the top of the compiled doc)
first=1
for ch in "${CHAPTERS[@]}"; do
    if [ "${first}" -eq 1 ]; then
        cat "${CHAPTERS_DIR}/${ch}"
        first=0
    else
        # Skip leading license HTML comments and blank line
        sed -e '/^<!-- LICENSE:/d' -e '/^<!-- TODO: replace with final license/d' "${CHAPTERS_DIR}/${ch}"
    fi
    printf '\n---\n\n'
done
