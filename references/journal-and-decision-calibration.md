# Journal and Decision Calibration

## Management Science lens

The current [Management Science editorial statement](https://pubsonline.informs.org/page/mnsc/editorial-statement) and [submission guidelines](https://pubsonline.informs.org/page/mnsc/submission-guidelines) characterize the journal as publishing rigorous, original scientific research on the practice of management. A regular paper should address issues important to managers and executives, interest a wide segment of the management-science community, have potential to affect management practice, and make a contribution commensurate with its length. Apply the journal-wide standard first and the relevant department statement second.

Translate that mission into four review questions:

1. Is the managerial decision important outside the motivating organization or narrow instance?
2. Does the method reveal a new decision principle, not merely improve a score?
3. Does the evidence support the claimed managerial scope?
4. Can a reader identify when the insight applies, fails, and changes action?

Technical correctness is necessary but not sufficient. Conversely, practical motivation cannot compensate for an unsupported theorem or empirical claim.

For every manuscript, assess all four merits: problem importance, first-order status of the research object, execution quality, and result/insight interest. Under the MS journal-wide lens, management relevance, rigor, and broad interest form a conjunctive baseline; department statements then determine whether the primary contribution may be theoretical, methodological, empirical, or application-based.

At MS, contribution is judged relative to length. Treat excessive length, a literature laundry list, or proof/simulation hierarchy that obscures the central insight as an editorial-path issue when it prevents broad readers from seeing the contribution; do not confuse this with sentence-level copyediting.

## Operations Research lens

Use the current [Operations Research editorial statement](https://pubsonline.informs.org/page/opre/editorial-statement), [Area Editor statements](https://pubsonline.informs.org/page/opre/editorial-statement/area-editors-statements), [reviewer guidelines](https://pubsonline.informs.org/page/opre/reviewer-guidelines), and linked [Guidelines for Operations Research Referees](https://pubsonline.informs.org/pb-assets/filesopre/OR_referee_guidelines-1725472691280.pdf). Identify the paper's “claim to fame”: the central insight that deserves amplification to OR readers.

Apply two threshold questions early:

1. If every result were correct, would the paper still make a substantial enough contribution for OR?
2. Is there a credible path from the present paper to publication, or would satisfying the requests require a fundamentally different paper?

Then evaluate correctness, originality, significance, exposition, computational evidence, and reproducibility in the manuscript's area.

For every manuscript, assess the same four merits rather than reducing OR review to proof checking. OR permits more than one route to impact: a standout foundational or methodological contribution may carry the paper without immediate implementation, while an application-led paper may carry it through important real-system impact. Both routes still require significance, rigorous execution, and an identifiable claim to fame.

### Area-sensitive contribution trade-offs

Use the exact current department or Area Editor statement when available. Do not impose one universal method/application mix:

- mature application domains generally require a sharper methodological or structural delta;
- a genuinely new, consequential application can sometimes support a more modest methodological increment when the modeling and evidence are compelling;
- decision-support papers require actionable inputs, scalability, and decision value;
- structural-theory papers require a first-order object, a nontrivial delta, and accessible insight;
- implemented-innovation papers require measurable benefit and independent verification.

These are contribution routes, not permission to ignore weak dimensions. Record positive and adverse evidence on motivation, first-order object, execution, and insight before deciding which route carries the paper.

## Decision logic

### Paper-level synthesis before selecting a label

Use `overall-editorial-assessment.md` to identify the manuscript's strongest publishable asset and its decisive bottleneck. The recommendation is a gate judgment, not an average score:

- an important domain does not compensate for a paper that fails to establish a first-order operational or theoretical research object;
- rigorous execution does not compensate for an absent or reducible contribution;
- a novel theorem does not compensate for a fatal correctness gap;
- a strong paper spine can remain publishable despite several contained proof, evidence, positioning, or exposition repairs.

State whether the decisive concern is local, section-level, or paper-spine-level. This repairability diagnosis should determine the recommendation more than the raw number of comments.

Always use the decision labels provided by the journal or review form. The following internal calibration is a reasoning aid, not an official universal taxonomy.

### Reject

Recommend rejection when one or more of these holds:

- the central result is wrong and no contained repair is visible;
- novelty or significance is below the target-journal bar even if correct;
- the evidence cannot support the headline claims without a new study, new data, or a fundamentally different model;
- multiple major gaps leave no coherent revision path;
- repairing the paper would change its central question or contribution identity.

Distinguish “promising topic” from “publishable paper.” Good ideas without a clear bounded path may still warrant rejection.

### Major revision / revise and resubmit

Use when the contribution could clear the bar and a coherent path exists, but publication requires substantive scientific work such as:

- a new or repaired theorem/proof;
- a material model extension or claim contraction;
- new identification, robustness, baselines, or experiments;
- a defensible theory-to-implementation bridge;
- major repositioning against close literature.

List the minimum sufficient path. Do not turn a major revision into an unlimited wishlist.

For OR, a major revision means the paper is on a path to publication and, if the stated concerns are adequately resolved, the next decision should normally be minor revision or accept. For MS, do not import that exact implicit contract: use major revision only when a finite and credible path exists, but the DE retains the final contribution and fit judgment.

### Minor revision

Use only when central correctness, contribution, and evidence are already established. Remaining work should be bounded clarification, presentation, a localized robustness check, or a repair that does not alter the scientific conclusions.

For OR, minor revision is an implicit acceptance commitment if the authors respond in good faith. Do not assert the same formal promise for MS.

### Accept

Reserve for manuscripts whose remaining defects are negligible. “I like the idea” is not an acceptance criterion.

### Reject and resubmit

Do not casually invent this option. MS does not list it as a standard referee decision; a rejected manuscript may return only if the responsible editor explicitly invites it. OR uses reject-and-resubmit sparingly for a promising idea without a current publication path, and the resubmission should be close to a new paper; this determination belongs to the editorial team, not an unsolicited referee promise.

## Recommendation consistency tests

Before finalizing, ask:

- Would the recommendation remain the same if the authors answered every minor point?
- Are the top two comments sufficient to explain the recommendation?
- Does each requested remedy fit within one revision cycle?
- Am I rejecting because the paper chose a different scope, or because the chosen scope is unjustified?
- Have I separated uncertainty about a proof from an actual proof error?
- If recommending revision, can I state a plausible acceptance condition?

## Report architecture

A useful first-round report contains:

1. neutral summary of question, method, and main contribution;
2. overall assessment and journal-level stakes;
3. ranked major comments with evidence, consequences, and repairs;
4. limited minor comments;
5. transparent verification limits;
6. recommendation consistent with the comments.

Label author-facing requests as **must-have** or **nice-to-have** when useful, and state whether each must-have can plausibly be completed in one revision. If confidential editor comments are requested, include the recommendation, two to four sentences on the decisive reasons and repairability, confidence, and expertise limits. Do not hide a scientific objection from the authors while using it to justify a negative recommendation.

For a revision, organize around prior concerns and the adequacy of responses. Do not invent an entirely new first-round standard unless newly revealed evidence makes it necessary.

Also audit title-level field semantics. Terms such as “scheduling,” “learning,” “robustness,” or “causal” can have established meanings in neighboring communities; recommend a qualifier when needed for accurate routing and reader expectations, without demanding irrelevant literature merely for terminology.
