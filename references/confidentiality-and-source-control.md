# Confidentiality and Source Control

## Default boundary

Treat an unpublished submission, referee report, editor/decision letter, author response, and unpublished supplement as confidential. A user's possession of a file does not by itself establish permission to process it with a generative-AI system.

Proceed without further authorization only when the material is clearly public, is the user's own work, or the user explicitly confirms both authority and compatibility with applicable journal/institution rules.

## INFORMS-specific caution

Management Science states that manuscripts or portions may not be uploaded to cloud or local generative-AI systems that store data or use inputs for training. AI may be used in review only if it does not retain, share, or train on manuscript content and fully complies with INFORMS confidentiality standards; the review team remains responsible for the report. See the current [Management Science ethical guidelines](https://pubsonline.informs.org/page/mnsc/guidelines-for-ethical-behavior-in-publishing) and [submission guidelines](https://pubsonline.informs.org/page/mnsc/submission-guidelines).

Operations Research states that submitted manuscripts and report/decision-specific material may not be uploaded to public-access generative AI, while openly posted material such as an arXiv or SSRN paper may be used; privacy-preserving techniques meeting its stated principles may be used. See the current [Operations Research generative-AI guidelines](https://pubsonline.informs.org/page/opre/generative-ai-guidelines).

Some INFORMS journals adopt a stricter prohibition. For example, the [INFORMS Journal on Computing Reviewing and Generative Artificial Intelligence Policy](https://pubsonline.informs.org/page/ijoc/aipolicy) says generative AI should not assist manuscript review and expressly extends confidentiality to reports and decision communications.

Policies can change and differ by journal. Verify the exact target journal's current rule before handling nonpublic editorial material. Do not infer that a private, local, or enterprise AI setting is compliant without confirming retention, sharing, training, and institutional requirements.

## Authorization gate

Before opening a nonpublic source, obtain a clear answer to:

1. Is the user an author, editor, authorized reviewer, or otherwise permitted to share it?
2. Does the target journal/institution allow this AI-assisted use?
3. Does the configured product's retention/training regime satisfy that policy?
4. Are there coauthor, participant, platform, NDA, personal-data, or copyright restrictions?
5. Can the task instead use a public preprint, redacted extract, or user-written summary?

If any answer is unknown, continue with public sources and keep the nonpublic source sealed.

## Double-anonymous review

INFORMS generally uses double-anonymous review and instructs referees not to try to identify authors. Do not search exact phrases, unique titles, metadata, or author pages for identity discovery. Public-version discovery is permissible only when it is independently authorized and compatible with the target journal's rule; incidentally learned identity must not affect the merits review. Report a resulting conflict of interest to the editor.

## Version discipline

For a blind review, create a source manifest containing:

- exact title and public identifier;
- version and date;
- direct URL or local path;
- file SHA-256;
- page count;
- retrieval date;
- files intentionally sealed;
- accidental exposures.

Never silently review the newest preprint when the case concerns an earlier submission. Later versions may encode reviewer feedback.

## Contamination handling

If a later version, report, decision, response, discussion, or citation to the focal paper is accidentally seen:

- record the source, scope, and time of exposure;
- identify which candidate comments it could have suggested;
- exclude those comments from blind hit-rate metrics unless independently documented before exposure;
- keep them available as post-comparison evidence, clearly labeled.

## Safe calibration pattern

1. Public/authorized manuscript only.
2. Independent review and frozen hash.
3. User confirmation that truth materials may be processed.
4. Truth-source extraction in a separate directory.
5. Comparison artifact; no edits to the blind artifact.
6. Generalized skill updates with no manuscript text or confidential facts embedded in the reusable skill.
