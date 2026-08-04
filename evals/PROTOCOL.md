# Forward-test protocol

This protocol separates case execution from expectation-aware scoring. It is a
forward test: the candidate Skill is fixed before any case output is generated,
and each generated output is frozen before its rubric is opened.

## Roles and access

Use three roles with separate contexts:

1. **Run controller.** Selects the candidate Skill snapshot and injects prompts.
   It does not edit agent responses.
2. **Case agents.** One newly created agent per case. A case agent receives the
   candidate Skill and the literal contents of one file under `prompts/`. It must
   not receive this protocol, the sealed manifest, any rubric, another case, a
   previous output, or a summary of expected behavior.
3. **Scoring agents.** Created only after outputs are frozen. A scoring agent
   receives one frozen transcript, its matching sealed rubric, and the scoring
   rules from the sealed manifest. It does not rerun or rewrite the review.

The agent-visible Skill snapshot must exclude `evals/sealed/`. Prefer an isolated
staging copy that excludes the entire `evals/` directory, with the selected prompt
injected by the controller. Merely telling an agent not to read an accessible
rubric is not adequate sealing.

## Before a run

1. Assign a new run label. Never reuse a label after any rubric has been opened.
2. Freeze the candidate Skill snapshot. Compute a SHA-256 digest from the sorted
   list of relative file names and their SHA-256 hashes, excluding `evals/` and
   transient files.
3. Record the model, model configuration, tool policy, Skill digest, prompt file
   hash, start time, and whether network access is disabled. Network access should
   be disabled because all evidence needed by these cases is synthetic and
   self-contained.
4. Verify that no case agent inherits a prior chat, prior case output, rubric text,
   manifest focus label, or developer commentary about the case.

## Execute and freeze

Run all cases independently. Parallel execution is allowed, but every case must
start in a fresh agent context. Give the agent the selected prompt verbatim and do
not add hints after launch.

For each case, preserve two raw artifacts:

- the complete event transcript, including tool calls and source-access attempts;
- the final user-facing response exactly as emitted.

Immediately after completion, compute a SHA-256 hash for each artifact and append
the hashes, byte counts, completion time, and agent configuration to an append-only
run record. Treat those files as frozen. Do not correct formatting, remove failed
tool calls, add missing analysis, or ask the same agent for a better answer. A retry
is a new run with a new label and a fresh agent.

If a case agent accesses `sealed/`, another case output, or any alleged companion
source not authorized by the prompt, mark the case contaminated. Preserve the
transcript, but do not count the run as a valid forward test.

## Score only after freezing

After all selected outputs are frozen, an independent scoring agent may open the
sealed manifest and one matching rubric. Score semantic evidence, not strings:

- `1` means the invariant is substantively satisfied;
- `0.5` means it is present but materially incomplete or mis-scoped;
- `0` means it is absent, contradicted, or supported only by generic language.

Multiply by the invariant weight. A case passes only if it reaches its point
threshold and satisfies every critical invariant. A prohibited behavior marked as
a critical failure overrides the numeric score. Do not require a particular
heading, issue count, ordering phrase, or recommendation label unless the rubric
states that the underlying priority logic is itself critical.

Record a short evidence span or transcript event for every score. Do not compare
case outputs with one another until all individual scores are complete.

## Forward comparison after a Skill change

A post-change run must use the same prompt bytes and execution policy, but new case
agents and a new run label. Compare:

- per-invariant scores and critical failures;
- unsupported-major and fatal-false-positive counts;
- whether the strongest asset and controlling bottleneck remain correctly scoped;
- source-access or authorization violations;
- aggregate pass/fail under the sealed manifest.

Use wording overlap and exact recommendation agreement only as descriptive notes.
An improvement is a stronger invariant score without a new critical failure, not a
closer imitation of an earlier answer.
