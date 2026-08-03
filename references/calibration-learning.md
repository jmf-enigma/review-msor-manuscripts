# Calibration Learning from Example Reviews

## Contents

- Objective and required artifacts
- Reviewer-stance reconstruction
- Comment normalization and adjudication
- Important-idea coverage, promotion, and safety taxonomy
- Reusable-trigger conversion
- Skill updates and calibration metrics

## Objective

Use real examples to improve two capabilities of an independent blind review:

1. broad coverage of important, manuscript-supported editorial ideas; and
2. selection of a small, defensible set of top priorities.

Do not optimize for issue-by-issue reproduction of an observed report. The independent blind review remains the primary artifact. Actual editor and referee reports are stance-dependent, incomplete, noisy expert labels: they supply candidate ideas and evidence about priority, but neither their presence nor their absence establishes validity or importance.

Retain blind-only ideas as `NOVEL–VALID` when they are independently supported and decision-relevant, including when they imply a different defensible publication thesis or repair path. Apply the strictest calibration to unsupported major claims—especially claims that drive the recommendation, demand paper-spine reconstruction, or displace supported top priorities.

Use these definitions:

- **Important idea:** a nonredundant, manuscript-supported judgment that changes the contribution, credibility, strongest asset, repair scope, or recommendation; it may be positive or negative.
- **Defensible top priority:** an idea that belongs in a limited top set under at least one explicit and reasonable publication thesis.
- **Fatal false positive:** an unsupported claim promoted into the controlling set that materially changes the recommendation or repair burden, or crowds out a supported priority.

## Required artifacts

Each case should contain:

1. source manifest;
2. contamination log;
3. frozen blind checkpoint and hash;
4. extracted actual-report issue ledger;
5. optional editor-decision and author-response ledgers;
6. comparison matrix;
7. root-cause analysis;
8. proposed skill changes;
9. validation result on a later case.

Never place confidential case text inside the reusable skill.

## Reconstruct reviewer stance before normalizing comments

Do not begin by merging all reports into issue families. First reconstruct each reviewer as a separate reasoning process:

When files are separate, open and reconstruct all individual referee reports before reading an AE/DE synthesis or decision letter. The synthesis can reveal other reviewers' priorities and anchor the reconstruction. If the order cannot be preserved because sources are bundled, record that exposure in the calibration note; it does not contaminate an already frozen blind review, but it limits claims about independently reconstructing reviewer stances.

1. What does the reviewer accurately summarize and explicitly credit?
2. Which contribution route do they believe should carry the paper: first-order application object, generative modeling, methodological theory, decision support, empirical validation, or another route?
3. What is their primary unit of judgment: the real phenomenon, model primitives, theorem ancestry, policy benchmark, evidence chain, or cumulative analytical program?
4. What rival object, baseline, cross-setting comparison, counterfactual, or stress test produces each major concern?
5. What intermediate inference turns that comparison into a judgment about motivation, first-order status, execution, or insight?
6. Which result do they identify as the strongest surviving asset, and why?
7. What repair would change their assessment, how extensive is it, and why does that imply the recommendation?

Represent the logic as:

`positive prior → publication thesis → comparison operation → intermediate inference → paper-level judgment → repair scope → recommendation`.

Only after this reconstruction should comments be normalized. Reviewers can legitimately apply different publication theories: one may test whether the application object is first-order, another whether the prescriptive chain is closed, and another whether a new model generates a rigorous cumulative body of knowledge. Preserve those differences, then inspect how the AE/DE weights and synthesizes them. Otherwise, issue matching destroys the reasoning the calibration is meant to learn.

## Normalize comments before matching

Represent both blind and actual comments as:

`object → claimed defect → evidence → consequence → requested repair`

Match on the underlying defect and consequence, not wording. One actual comment may map to several blind symptoms and vice versa.

Then build a case-level candidate-idea pool from the blind review, referee reports, editor letters, and authorized response material. The pool is not ground truth and need not be exhaustive. Independently adjudicate each idea against the manuscript before using source agreement.

Keep four fields orthogonal:

- **source relation:** blind-only / observed-only / overlap;
- **independent validity:** supported / disputed / unsupported / unverifiable;
- **importance:** top-tier / important / secondary;
- **blind outcome:** generated-and-promoted / generated-but-reserved / partial / absent.

Absence from an observed report is not negative evidence against a blind idea. Presence in an observed report is not sufficient evidence of validity or priority. Editor adoption is useful auxiliary evidence, not truth.

## Adjudicate the observed review

Before treating an observed comment as a learning signal:

1. verify its manuscript facts and cited definitions;
2. redo any algebra or logical implication;
3. separate the valuable question from a possibly incorrect proposed answer;
4. record whether the editor adopted it as must-have, acknowledge/repair, optional, or not adopted;
5. distinguish journal taste and field terminology from correctness.

Reviewer reports can contain wrong acronym expansions, reversed inequalities, narrow conventions, or requests the editor deliberately declines. Learn the trigger only after adjudication.

## Diagnostic comparison labels

Use labels to explain discovery and promotion, not to compute a strict reproduction score.

### Blind-idea dispositions

- **Overlap:** captures the same supported underlying idea and paper-level consequence as an observed source.
- **Partial:** sees the area but misses the important mechanism, scope, or consequence.
- **NOVEL–VALID:** blind-only, independently supported, and decision-relevant; retain it even when it implies an alternative defensible review thesis.
- **Supported-secondary:** correct but not a top priority; this is not a false positive.
- **Scope/taste alternative:** defensible under a different explicit publication thesis; preserve the disagreement.
- **Unsupported:** manuscript facts, derivation, or reasoning do not sustain the claim.
- **Fatal false positive:** unsupported and promoted into the controlling set, recommendation, or paper-spine repair burden.
- **Contaminated:** plausibly suggested by an exposed truth source; exclude from blind evidence.

### Important-idea coverage labels

- **Generated and promoted:** independently discovered and placed in a defensible top set.
- **Generated but not promoted:** discovered, but ranked too low or left unresolved; diagnose promotion separately from discovery.
- **Partial coverage:** adjacent route found, but the consequential mechanism or inference is missing.
- **Absent-important:** independently supported and important, yet no meaningful blind counterpart exists.
- **Secondary observed-only:** sound but not important enough to count as a material coverage failure.
- **Non-generalizable:** depends on private editor taste or facts unavailable in the manuscript.
- **Disputed:** the observed idea may itself be weak or incorrect.

## Root-cause taxonomy for material calibration errors

Run root-cause analysis only for: (1) an independently supported important idea that was not generated, (2) an important idea that was generated but not promoted, or (3) an unsupported major/fatal claim. Do not analyze every observed-only minor comment as a failure. Do not write “I should have been more careful.” Identify the failed operation:

- **Extraction failure:** missed a definition, equation, figure, footnote, or assumption.
- **Link failure:** read both pieces but did not compare them.
- **Transformation failure:** failed to substitute, rescale, condition, or track units.
- **Counterexample failure:** did not test a boundary or minimal instance.
- **Benchmark failure:** did not ask for an oracle, ablation, or closer comparator.
- **Literature failure:** searched by topic but not by method/result.
- **Evidence-scope failure:** accepted a broader label than the data support.
- **Cause–lever failure:** audited the modeled decision but did not test whether it is connected to the operational cause of the headline harm.
- **Feature-priority failure:** accepted extensive modeling of a secondary mechanism without comparing omitted first-order mechanisms.
- **Application-witness failure:** accepted a mathematically admissible regime, joint-consumption pattern, or role assignment without constructing a real setting with compatible period length, availability, decision rights, and scarce resources.
- **Paper-identity failure:** noticed tension among an algorithm, special-case insights, and an application but did not force the manuscript to identify which component carries the publication case and evidence standard.
- **Behavioral-recourse failure:** saw a failure/stockout state but did not enumerate realistic next actions or test whether omission changes policy and distributional outcomes.
- **Editorial-priority failure:** found the issue but ranked it too low.
- **Expertise boundary:** required specialized knowledge not available or not verified.
- **Contamination/anchoring:** later information distorted the supposedly blind judgment.
- **Canonical-reduction failure:** accepted a newly named model without explicitly mapping it into the closest standard structure and checking what survives.
- **Rate-normalization failure:** compared displayed rates without substituting hidden dimensions and aligning assumptions, domains, and oracle requirements.
- **Guarantee-semantics failure:** accepted words such as safe, zero violation, or fair without matching the unit, aggregation, and probability quantifier to the theorem.
- **Restricted-policy benchmark failure:** audited the solver but not the performance loss from the simple policy class itself relative to the unrestricted optimum.
- **Mechanism-label provenance failure:** verified a total algebraic identity but did not trace whether named economic effects retained the same primitive terms after substitution or regrouping.
- **Outside-view failure:** stayed inside the manuscript's application vocabulary instead of independently mapping actors, decision layers, and rival first-order research objects.
- **Pre-result-baseline failure:** judged a theorem after seeing its derivation without first recording what its assumptions and the closest standard model already predicted.
- **Insight-threshold failure:** recognized a correct result but did not test its surviving delta, mechanism, decision/belief change, consequential regime, or robustness.
- **Surviving-core failure:** catalogued strengths and weaknesses without running deletion tests to identify what publishable asset remains after removing the application, method, or strongest disputed claim.
- **Separability-burden failure:** either demanded a larger model automatically or accepted an omitted upstream/downstream decision as exogenous without testing whether it dominates or reverses the focal policy.
- **Positive-asset failure:** focused on objections and did not identify the strongest result that could carry a bounded publication path.
- **Reviewer-stance collapse:** normalized comments across reviewers before reconstructing their distinct publication theses, counterfactual operations, strongest assets, and repair logic.
- **Counterfactual-operation failure:** recorded that a reviewer requested feature X or experiment Y but did not recover the comparison or falsification test that made the request editorially meaningful.
- **Audit-displacement failure:** a vivid proof, algorithm, or data defect replaced rather than supplemented the conditional-on-correctness judgment of motivation, first-order status, novelty, and insight.
- **Triggered-cue execution failure:** an outside-view cue was plainly present, but the relevant operation was listed as background rather than executed or adjudicated as a candidate idea.

## Converting an adjudicated calibration error into a reusable trigger

For every material coverage, promotion, or safety failure, write:

1. **Observable cue:** what in the manuscript should trigger scrutiny?
2. **Reasoning operation:** what exact comparison or derivation should be run?
3. **Failure signature:** what result indicates a problem?
4. **Escalation rule:** when does it become a major comment?
5. **Disconfirmation:** what would resolve it?

Example pattern:

- Cue: a theoretical cost is multiplied by a job-specific probability, while the practical target clips an unweighted future outcome.
- Operation: substitute the application cost into the theoretical target before moving multiplicative terms outside nonlinear operators.
- Signature: heterogeneous probabilities imply different effective clip thresholds or reversed rankings.
- Escalation: major when experiments are presented as implementing the guaranteed policy.
- Disconfirmation: a derivation proving equivalence or a correctly weighted target and capacity price.

## Updating the skill

Promote a new rule only when it is:

- general across a recognizable class of papers;
- actionable from observable manuscript cues;
- concise enough to use during review;
- not redundant with an existing rule;
- validated on at least one later sealed case when possible.

Track every modification in the case comparison artifact. Preserve unsuccessful heuristics in the case record, not the core skill.

## Useful metrics

Prefer qualitative adjudication unless the case set and labels justify aggregation. After blind freeze, make these the primary diagnostics:

- **important-idea coverage:** which independently supported top-tier or important ideas were generated, partially generated, or absent;
- **top-priority selection:** whether the blind top set is defensible and which important generated ideas were under-promoted;
- **NOVEL–VALID retention:** whether blind-only supported ideas were preserved rather than deleted for lack of observed overlap;
- **unsupported-major audit:** unsupported claims that entered the major set;
- **fatal false-positive count:** target zero.

Observed-report overlap, exact ranking agreement, and recommendation agreement are secondary diagnostics. They describe agreement with one noisy reviewer set, not calibration success. Do not require complete comment coverage or identical recommendation labels. A different but better-supported top issue can improve the review.

For editorial-threshold calibration, compare reasoning on:

- problem-importance and motivation judgment;
- strongest publishable asset;
- first-order-object classification and strongest rival object;
- ranking of expected versus consequential results;
- execution quality beyond the presence or absence of hard errors;
- decisive bottleneck;
- repair scope and the logic connecting it to the recommendation.

A matching recommendation with a different decisive rationale is only partial editorial overlap. Conversely, a different recommendation may remain defensible when it follows from a supported alternative bottleneck or publication thesis. Metrics aid reflection; they do not replace substantive diagnosis or independent adjudication.
