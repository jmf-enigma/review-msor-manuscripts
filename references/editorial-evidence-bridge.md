# Connecting Overall Judgment to Detailed Analysis

## Contents

1. Core bridge and integrated contract
2. Top-down claim decomposition
3. Bottom-up editorial mapping
4. Root synthesis and evidence roles
5. Multi-dimensional consequences
6. Editorial bridge matrix

## Core principle

An overall judgment must be earned by manuscript-specific lower-level evidence. A detailed finding matters editorially only when its consequence for the paper-level contribution is made explicit.

Use the complete bridge:

`paper-level claim → necessary subclaim → manuscript object → diagnostic test → finding → upper-level implication → editorial consequence`

Run it in both directions:

- **top-down:** start from the paper's intended claim to fame and identify what must be true for it to hold;
- **bottom-up:** start from verified technical, modeling, or empirical findings and determine which paper-level claim they weaken.

This prevents two common failures: unsupported statements such as “the contribution is unclear,” and orphan comments that identify a local defect without explaining why an editor should care.

Before decomposing claims, compress the manuscript into one integrated contract containing:

- operational decision and decision maker;
- objective and counterfactual benchmark;
- timing and information available at each decision;
- primitives, assumptions, and asymptotic regime;
- proposed policy, estimator, or algorithm;
- main theorem or empirical estimand;
- evidence for correctness and usefulness;
- claimed managerial or scientific implication;
- novelty claim relative to the closest work.

This contract is broader than a formal model summary. It reveals breaks among the application actor, mathematical object, result, evidence, and claimed contribution before local audit details accumulate.

## Top-down claim decomposition

For every title-level or contribution-list claim, write two to five necessary subclaims.

### Example: “a new general model and algorithm”

Necessary subclaims may include:

1. the model is not merely a standard formulation under state augmentation or reparameterization;
2. the generality is real under the theorem's assumptions and complexity measures;
3. the algorithm solves the stated model rather than a relaxation with different feasible policies;
4. the closest literature cannot obtain the same result under matched assumptions;
5. the new model produces a consequential structural, computational, or statistical delta.

Corresponding detailed tests include canonical reduction, assumption closure, dimension substitution, feasible-set comparison, and closest-result ancestry.

### Example: “the method safely improves real decisions”

Necessary subclaims may include:

1. formal safety protects the unit and event implied by the application language;
2. required baseline information and coverage are available before unsafe exploration;
3. logged data identify or credibly simulate outcomes under the proposed policy;
4. implementation computes the policy covered by the guarantee;
5. comparator information and tuning are fair;
6. the observed gain is attributable to the claimed mechanism.

Corresponding tests include guarantee-semantics mapping, information timing, causal/offline evaluation, theorem–implementation equivalence, benchmark parity, and component ablations.

### Example: “the paper addresses an important managerial problem”

Necessary subclaims may include:

1. the motivating outcome is measured credibly;
2. the stated decision maker controls the modeled lever;
3. the lever materially affects the outcome relative to omitted mechanisms;
4. operational constraints and behavioral responses do not overturn the recommendation;
5. the result changes an action or understanding beyond the motivating organization.

Corresponding tests include the cause–lever chain, feature-budget analysis, behavioral recourse, process evidence, external validity, and actionability.

## Bottom-up editorial mapping

For each verified detailed issue, ask four questions:

1. Which necessary subclaim does it contradict or leave unsupported?
2. Which paper-level dimension does that subclaim support—importance, formulation, novelty, credibility, insight, or claim calibration?
3. Is the finding an isolated repair, one symptom of a shared root cause, or a direct break in the paper spine?
4. What is the smallest repair, and would that repair preserve the manuscript's contribution identity?

Examples:

| Detailed finding | Immediate consequence | Upper-level implication |
|---|---|---|
| hidden dimension absorbs state/action size | displayed rate comparison is not like-for-like | result novelty and claim calibration are not established |
| safe baseline must excite every parameter direction | exploration difficulty is supplied by an assumption | execution may assume away the claim-to-fame challenge |
| policy comparator lacks context available to the proposed method | observed performance gain is not attributable to the algorithm | empirical evidence and managerial superiority claim are unsupported |
| omitted upstream inventory decision likely creates the observed shortage | modeled tactical action may not control the headline harm | motivation-to-formulation link and application contribution fail |
| expected cumulative constraint is described as zero individual violations | theorem protects a different object than the application claim | credibility and claim calibration fail together |
| a new lemma is a canonical result under the same assumptions | proof may be correct but not methodologically new | novelty is narrower than claimed, without necessarily affecting correctness |

## Synthesis: from several details to one major comment

Do not promote every symptom separately. Cluster findings when they support the same root diagnosis.

Use this structure:

1. **Paper-level judgment:** state the threatened contribution link.
2. **Necessary subclaims:** say what would need to be true.
3. **Detailed evidence:** give the strongest two or three manuscript-specific tests/findings.
4. **Synthesis:** explain why the findings share one root cause rather than being unrelated details.
5. **Editorial consequence:** state what readers can no longer believe and how this affects the journal case.
6. **Repair path:** request the minimum analysis that would re-establish the upper-level claim, or require claim contraction.

Illustrative form:

> The manuscript has not yet established that its headline rate is a substantive advance. This conclusion is not based on the rate table alone: the complexity parameter absorbs state/action size, the comparator is evaluated under a different model class, and the apparent horizon improvement is not traced to a new proof step. Together these points prevent an assumption-matched comparison, so the result novelty remains unclear. The paper should specialize both results to one common regime, expand every hidden dependency, and identify the exact technical source of any surviving improvement.

## Distinguish root evidence from supporting symptoms

For each major comment, label details as:

- **decisive evidence:** independently sufficient to threaten the paper-level claim;
- **corroborating evidence:** strengthens the diagnosis but is not sufficient alone;
- **illustrative symptom:** helps readers see the issue but should not drive severity;
- **secondary consequence:** follows after the root problem is accepted.

For example, inability to define the new model's delta may be decisive for novelty; an overlong related-work section is only a symptom of that unclear contribution. Conversely, a false main lemma is decisive for credibility even if no editor explicitly mentioned proof exposition.

## One detail can affect several upper-level dimensions

Some findings have multiple legitimate consequences. State the primary one and avoid double counting.

- An oracle baseline may weaken **credibility** primarily and **novelty** secondarily because it changes the difficulty of the problem.
- An unfair benchmark weakens **evidence attribution** primarily and **claim calibration** secondarily.
- A reducible model weakens **novelty** primarily and may weaken **insight** if no new structure remains.
- Failure to establish a first-order research object weakens **formulation relevance** primarily and therefore also the claimed managerial or theoretical contribution; this is broader than whether one lever is literally “wrong.”

The overall recommendation should reflect the breadth of the root defect, not count each downstream consequence as a separate vote.

## Editorial bridge matrix

Use this during the sharp-comments stage:

| Overall claim/gate | Necessary subclaim | Detailed manuscript object | Test and finding | Evidence role | Upper-level consequence | Repairability |
|---|---|---|---|---|---|---|
|  |  |  |  | decisive / corroborating / illustrative |  | local / section / spine |

The matrix is complete only when:

- every negative overall judgment has at least one specific evidence path;
- every promoted major detail has a stated upper-level consequence;
- positive overall judgments also cite concrete evidence;
- the recommendation follows from the breadth, severity, and repairability of the mapped root causes.
