# Contributing

Thank you for helping improve `review-msor-manuscripts`. Contributions should make the workflow clearer, safer, more reliable, or easier to evaluate without exposing review materials.

## Privacy boundary

Contributions may use only public project information or fully synthetic research and review artifacts. Examples, tests, fixtures, screenshots, logs, and issue descriptions must be safe for permanent public release.

Do not contribute or quote:

- real manuscripts, referee reports, editorial or decision letters, author responses, or revision histories;
- author, reviewer, editor, or submitter identities;
- manuscript numbers, submission identifiers, private URLs, access tokens, or credentials;
- local filesystem paths, attachment paths, document metadata, or machine-specific usernames; or
- confidential, copyrighted, embargoed, or otherwise nonpublic source material.

This prohibition applies even when material has been redacted or paraphrased. Build demonstrations and regression cases from scratch, label them as synthetic, and avoid distinctive details that could reconstruct a real case. Do not open a public issue or pull request to ask whether sensitive material is acceptable.

## Public/private separation

Treat this public repository as the complete release unit. Do not stage
nonpublic casework in a public branch, fork, pull request, issue, Git LFS object,
release asset, workflow artifact, or prior commit. Removing a file later does not
remove it from Git history.

If a separately authorized private evaluation environment exists, keep it
outside this repository and its fork network, with its own access controls and
retention rules. Transfer back only generalized logic or newly constructed
synthetic tests, after a fresh manual disclosure review. Private repository
visibility is an access control; it does not itself establish journal,
institutional, confidentiality, copyright, or AI-processing permission.

## Scope and design

Keep changes focused. Preserve the human confirmation gate, evidence calibration, confidentiality boundary, and separation between internal diagnostics and author-facing prose. New analytical prompts should support adaptive judgment rather than impose an issue quota or a rigid checklist.

Explain why a behavioral change is needed, what failure mode it addresses, and how it was evaluated. Tests of review behavior must use fully synthetic cases; passing a synthetic case is evidence about workflow behavior, not proof that a manuscript judgment is correct.

## Before opening a pull request

From the repository root, run:

```bash
python3 scripts/validate_public_skill.py
git diff --check
```

Then inspect the complete diff, including filenames and generated output, for accidental disclosure. The validator is a release-surface safeguard, not a substitute for human privacy review.

In the pull request, summarize the scope, validation performed, and any remaining limitations. Complete every privacy item in the pull request template.
