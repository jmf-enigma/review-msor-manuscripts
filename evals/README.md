# Synthetic behavior evaluations

This directory contains a compact regression suite for the review workflow. Every
manuscript fact, equation, institution, and result in the suite was invented for
testing. The suite contains no real manuscript text, title, author, submission
identifier, referee report, decision letter, or confidential source.

The suite tests review behavior, not phrase matching. A response may pass with any
clear organization or recommendation label if its evidence, scope, priority, and
repair logic satisfy the relevant invariants.

## Layout

- `prompts/` contains the only text supplied to case-running agents.
- `PROTOCOL.md` defines fresh-agent execution, freezing, contamination control, and
  scoring order.
- `sealed/manifest.json` indexes cases and defines the aggregate pass rule.
- `sealed/rubrics/` contains evaluator-only expected behaviors.

`sealed/` must never be mounted, quoted, summarized, or named to a case-running
agent. A runner should inject the contents of exactly one prompt rather than give
the agent access to this evaluation directory. The suite-local case keys are only
test labels; they are not manuscript identifiers.

## Intended use

Run the suite on a candidate version of the Skill before using the candidate's
outputs to revise it. Freeze the unedited outputs, then score them. A revised Skill
must be tested in a new run with fresh agents; an output cannot be regenerated or
polished in place after its rubric has been opened.

The pass rule is deliberately strict about critical safety and reasoning failures
and deliberately flexible about prose, section labels, comment counts, and exact
recommendation wording.
