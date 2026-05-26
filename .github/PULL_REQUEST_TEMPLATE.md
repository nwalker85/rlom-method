# PR title (use a Conventional Commits prefix — see CONTRIBUTING.md)

## Summary

What changed and why. One or two sentences.

## Type

- [ ] `feat(chapter)` — net-new content
- [ ] `fix(chapter)` — editorial correction
- [ ] `feat(doctrine)` — new numbered principle (requires ADR — link below)
- [ ] `refactor(doctrine)` — restate a principle without changing meaning
- [ ] `chore(repo)` — plumbing, CI, lint
- [ ] `docs(meta)` — README, CHANGELOG, contributing docs

## If this touches doctrine

- [ ] An ADR exists in `docs/architecture/decisions/` describing the change.
- [ ] `docs/_shared/PRINCIPLES.md` is updated.
- [ ] Every chapter that cites the affected `P-#` has been reviewed.
- [ ] Link to ADR PR: <!-- #NNN -->

## Self-check (per `docs/_shared/CONTEXT.md` §12)

For chapter PRs:

- [ ] License header at top of every modified chapter
- [ ] `RUBRIC_CHECK` block at end of every modified chapter
- [ ] No Norse names, no Ravenhelm-internal jargon, no real client / employer names
- [ ] 3-person team appears concretely if the chapter touches the canonical example
- [ ] All non-obvious claims tied to a `P-#`
- [ ] "Augmentation Surface" and "Where this gets hard" callouts present (Chapter 12 exempt)
- [ ] Length within target (see chapter brief)

## Review notes

Anything reviewers should know.
