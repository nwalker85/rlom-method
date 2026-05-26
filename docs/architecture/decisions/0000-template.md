# ADR-NNNN — <Short title in present tense>

- **Status:** proposed | accepted | superseded by NNNN | retired
- **Date:** YYYY-MM-DD
- **Decider:** @<github-handle>
- **Affected:** <list of P-# / chapters / docs touched>

## Context

What is the situation that requires a decision? What's changing in the world, in the workspace, or in the doctrine that makes the current state unworkable?

Cite the trigger — recurring incident, quarterly audit finding, capability adoption, leadership feedback. Doctrine doesn't change on aesthetic grounds.

## Decision

The decision, stated as a directive. One paragraph.

For a doctrine ADR:

- **New principle.** Full text of the new `P-#` (rule, rationale, counter-example).
- **Retire.** Which `P-#`, replaced by what (if anything), and how existing citations should be handled.
- **Renumber.** Old → new mapping. Existing citations get updated in the same PR sweep.
- **Restate.** Old wording → new wording, with the substantive change called out.

## Consequences

What changes as a result of accepting this decision?

- **For chapters:** which chapters need a citation sweep or rewrite.
- **For tooling:** which lint rules, templates, or `_shared/` files need updating.
- **For the reader:** what they will perceive differently (or not at all).

## Alternatives considered

What was rejected and why. At least two genuine alternatives. "Do nothing" counts and is sometimes the right call.

## References

- Source incidents, audit findings, prior ADRs, external docs.
- Pull request implementing the change.
