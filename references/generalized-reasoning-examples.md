# Generalized Reasoning Examples

## Purpose and use

Use these examples to widen manuscript-specific discovery when the first-pass idea board is thin, overly technical, or anchored to the authors' framing. They illustrate reasoning operations, not expected criticisms. Select only examples whose cue is genuinely present, instantiate them with the manuscript's own objects, and actively seek the listed disconfirmation.

For every triggered example, write:

`cue → operation → possible finding → disconfirmation → promotion condition`

Do not copy an example's possible finding into a report without performing the operation. A disconfirmed candidate is evidence in the paper's favor and may become a positive asset. Add new manuscript-specific routes when none of these examples captures the paper's contribution.

Use one promotion gate throughout: promote only after the operation has been performed, manuscript-specific evidence is sufficient for the proposed wording, the finding affects a central claim or publication path, and the stated disconfirmation has not resolved it. Otherwise keep the idea on Hold, use it as supporting or positive evidence, or retire it.

## Motivation and first-order-object examples

### 1. Headline harm versus modeled lever

- **Cue:** The paper motivates a consequential operational harm but optimizes only one tactical lever while important upstream or downstream decisions are fixed.
- **Operation:** Build the cause–lever chain and compare the focal lever with the strongest rival lever under a perfect-policy counterfactual.
- **Possible finding:** The comparison may confirm that the focal lever remains first-order after credible rivals are allowed, or show that it is useful only within a narrower conditional problem.
- **Disconfirmation:** Institutional evidence, variance decomposition, or policy-reversal tests show that the focal lever materially controls the harm after rival mechanisms are allowed.
- **Promotion condition:** Promote when first-order status carries the application contribution or when the rival mechanism changes policy rankings, welfare, or distributional effects.

### 2. Decision rights and operational witness

- **Cue:** A theorem recommends assigning, positioning, sequencing, or switching roles among resources, products, workers, or policies.
- **Operation:** Construct one concrete witness with a named decision maker, timing, availability, authority, and cost; verify that the proposed counterfactual is feasible for that actor.
- **Possible finding:** The witness may establish a feasible and actionable prescription, or show that a valid mathematical comparison lies outside the stated decision maker's authority.
- **Disconfirmation:** The institution permits the switch, the relevant costs are represented, and the same actor controls all compared choices.
- **Promotion condition:** Promote when managerial insight is a headline contribution and the recommended action is infeasible or belongs to a different decision maker.

### 3. Omitted behavioral recourse

- **Cue:** The model compresses a consequential post-decision response into a terminal outcome or one outside option; failure, rejection, stockout, or delay are non-exhaustive examples.
- **Operation:** Enumerate retry, wait, within-category substitution, cross-category substitution, abandonment, and other plausible recourse; test which omitted response could reverse the focal policy or distributional conclusion.
- **Possible finding:** Realistic recourse may leave the result intact, or may show that it describes a restrictive response regime rather than the broader phenomenon claimed.
- **Disconfirmation:** Process data or bounded sensitivity analysis shows that realistic recourse is rare or leaves the policy and insight unchanged.
- **Promotion condition:** Promote when recourse changes the objective, ranking, fairness, or interpretation—not merely aggregate fit.

### Normative intervention versus the baseline that generates the harm

- **Cue:** An observed group disparity, service gap, risk, or access shortfall motivates adding a fairness, safety, or responsibility penalty to an otherwise standard objective.
- **Operation:** Ask whether a correctly specified baseline optimizer would generate the observed harm under the manuscript's stated shares, revenues, costs, constraints, and information. If not, identify the omitted primitive, upstream decision, nonoptimization, or conflict of objectives that must create it.
- **Possible finding:** The normative term may address a genuine efficiency–equity conflict, or may compensate for a misspecified baseline whose missing mechanism is itself the first-order research object.
- **Disconfirmation:** Institutional or empirical evidence shows that the focal baseline decision systematically creates the harm even after the relevant costs, constraints, and upstream choices are represented.
- **Promotion condition:** Promote when the need for the normative intervention and the paper's causal or managerial spine depend on this generative premise. Do not presume that population weighting or equal-group protection is uniquely correct.

### Multiplicative harm and rival uncertainties

- **Cue:** The operational harm is a product or nonlinear combination of an estimated risk/severity term and a dynamic exposure, volume, duration, or consequence term.
- **Operation:** Map the uncertainty, update frequency, intervention sensitivity, and policy-ranking sensitivity of each factor separately and jointly. Ask why one factor receives the full stochastic model while another is fixed or known.
- **Possible finding:** The modeled factor may dominate under a credible institutional separation, or the omitted uncertainty may be equally first-order and change rankings or learning feedback.
- **Disconfirmation:** Data, process evidence, or sensitivity analysis shows that uncertainty in the fixed factor is small or does not materially change the policy relative to the modeled factor.
- **Promotion condition:** Promote a first-order positioning burden when the application contribution depends on the chosen uncertainty being primary; a joint replacement model is not automatically required if a narrower theoretical route survives.

## Execution and credibility examples

### 4. Guarantee semantics

- **Cue:** Application language appears to promise protection at a stronger unit, horizon, aggregation, or probability level than the formal quantity may provide; safety, fairness, reliability, and robustness are non-exhaustive settings.
- **Operation:** Match the protected unit, conditioning event, horizon, aggregation order, and probability quantifier across theorem, metric, experiment, and application claim.
- **Possible finding:** The formal and applied objects may align, or the guarantee may protect an expectation or aggregate while the prose implies realized, individual, stagewise, or pathwise protection.
- **Disconfirmation:** A theorem establishes the stronger object, or a transparent conversion bound connects the formal and claimed guarantees at relevant scale.
- **Promotion condition:** Promote when the semantic gap changes what a decision maker may safely infer or when it controls the headline claim.

### 5. Theory-to-implementation equivalence

- **Cue:** The implementable method replaces a theoretical set, objective, transition, oracle, or update with a surrogate, relaxation, heuristic, or learned proxy.
- **Operation:** Put the theoretical and implemented formulas, information sets, and feasible sets side by side; trace approximation and estimation error through the guarantee.
- **Possible finding:** The bridge may establish exact or controlled transfer, or reveal that the experiments evaluate a different policy or problem from the one covered by the theorem.
- **Disconfirmation:** Exact equivalence, a valid approximation bound, or exact-small-instance comparisons connect the implementation to the theoretical object.
- **Promotion condition:** Promote when the empirical claim relies on the theorem or when the bridge can materially change feasibility, ranking, or performance.

### Noncommuting surrogate transformations

- **Cue:** The implementation moves a scale factor, expectation, clipping/capping operator, normalization, threshold, or nonlinear map outside the theoretical expression.
- **Operation:** Compare the formulas symbolically, then construct the smallest admissible instance that tests equality and policy ranking. Common checks include whether `a min{b,x}` equals `min{b,ax}` and whether `f(E[X])` equals `E[f(X)]`.
- **Possible finding:** The surrogate may preserve the theoretical policy under a valid homogeneity or monotonicity argument, or may reverse decisions and become a distinct heuristic.
- **Disconfirmation:** An algebraic identity, order-preservation theorem, or approximation bound covers the actual parameter range and information set.
- **Promotion condition:** Promote when the manuscript presents experiments or deployment results as evidence for the analyzed policy, guarantee, or mechanism.

### 6. Logged data used as an interactive environment

- **Cue:** Static or policy-generated observations are reused to simulate, train, choose, and evaluate sequential decisions.
- **Operation:** Trace `data → estimator → action → outcome → feedback`; identify the randomized unit, estimand, overlap, censoring, and whether evaluation is independent of policy construction.
- **Possible finding:** The design may identify the intended policy effect, or support only model-based counterfactual or in-sample simulation claims.
- **Disconfirmation:** A defensible experimental or off-policy design, independent outcome generator, or transparent semi-synthetic scope supports the claimed evidence level.
- **Promotion condition:** Promote when field, causal, or real-world effectiveness language depends on the unsupported bridge.

### 7. Dependence erased by calibration

- **Cue:** A synthetic generator matches marginal frequencies or moments but independently generates components whose joint occurrence determines feasibility or value.
- **Operation:** Construct two admissible joint distributions with the same reported marginals and compare the induced feasible frontier, policy, or risk.
- **Possible finding:** The conclusion may be stable across plausible joint laws, or may be driven by a dependence assumption that marginal calibration does not identify.
- **Disconfirmation:** Empirical joint resampling, a validated dependence model, or sensitivity bounds show the conclusion is stable across plausible joint laws.
- **Promotion condition:** Promote when dependence changes the sign, magnitude, feasibility, or distributional character of the claimed result.

### 8. Comparator information and resource parity

- **Cue:** The proposed method receives richer context, tuning, model class, computation, forecasts, or feasibility information than its baselines.
- **Operation:** Equalize information, tuning budget, constraints, data access, and computational budget; add the strongest feasible comparator or an ablation isolating the claimed component.
- **Possible finding:** The gain may persist under matched resources and support the proposed mechanism, or may be explained materially by a comparator asymmetry.
- **Disconfirmation:** Gains persist under matched resources and against a comparator representing the closest operational alternative.
- **Promotion condition:** Promote when superiority over prior practice is central and the unmatched resource plausibly explains a material share of the gain.

## Contribution and insight examples

### 9. Canonical reduction and surviving delta

- **Cue:** The manuscript names a new model class, formulation, or algorithmic framework.
- **Operation:** Map state, action, information, objective, feasible policies, and guarantee into the closest standard structure; identify exactly what fails to carry over.
- **Possible finding:** A consequential new obstacle and capability may survive the mapping, or the contribution may instead be a useful structured special case or representation.
- **Disconfirmation:** A new obstacle survives the mapping and the paper supplies a consequential resolving step, guarantee, or capability unavailable to the ancestor.
- **Promotion condition:** Promote when novelty and paper identity depend on the broader claim; otherwise use the mapping to sharpen a positive, narrower contribution.

### 10. Matched-assumption result comparison

- **Cue:** A displayed rate, bound, approximation factor, or complexity improves on prior work while dimensions, constants, or assumptions differ.
- **Operation:** Expand hidden dependencies and specialize both results to a common domain, information structure, oracle model, and standard small regime.
- **Possible finding:** A nontrivial improvement may survive normalization, or the apparent advantage may disappear, change source, or be purchased by a stronger primitive.
- **Disconfirmation:** A nontrivial advantage survives normalization and can be traced to a specific new proof or algorithmic step.
- **Promotion condition:** Promote when the normalized comparison changes the claimed result novelty or practical scale.

### 11. Difficulty supplied by assumptions

- **Cue:** A safe baseline, exact oracle, coverage condition, known dynamics, separability, or other strong primitive neutralizes the obstacle used to motivate the paper.
- **Operation:** State which part of the learning, optimization, or implementation burden the assumption supplies; test the smallest relaxation that restores the advertised difficulty.
- **Possible finding:** The primitive may be a benign condition under which a new difficulty remains, or it may itself resolve much of the claim-to-fame challenge.
- **Disconfirmation:** The primitive is institutionally standard, is itself learned or implemented by the paper, or the main delta survives its relaxation.
- **Promotion condition:** Promote when the assumption changes contribution identity, applicability, or comparison with the closest work.

### 12. Restricted-policy value

- **Cue:** The optimized policy class is substantively narrower than the feasible policy set used by the surrounding optimality or managerial claim; threshold, cyclic, fixed-frequency, and index policies are non-exhaustive examples.
- **Operation:** Solve exact small instances, derive a performance bound, or compare with a relaxation or dynamic-programming benchmark.
- **Possible finding:** The restricted class may be optimal or near-optimal in relevant regimes, or the result may be conditional design within an interpretable class rather than general optimal policy guidance.
- **Disconfirmation:** The class is optimal under stated conditions, has a useful worst-case guarantee, or loses little across relevant regimes for an institutional reason.
- **Promotion condition:** Promote when unrestricted optimality is claimed or when the omitted value could overturn the managerial prescription.

### 13. Pre-result baseline and non-obvious insight

- **Cue:** The main structural result has the direction one would predict from monotonicity, convexification, pooling, scarcity, or another standard mechanism.
- **Operation:** Write the strongest prediction available before reading the derivation, then identify the theorem's surviving delta: boundary, magnitude, reversal, mechanism, decision change, or robustness.
- **Possible finding:** A consequential boundary, reversal, mechanism, or action change may survive the baseline, or the result may principally provide rigorous confirmation of an expected direction.
- **Disconfirmation:** The paper reveals a consequential regime boundary, counterintuitive reversal, precise mechanism, or robust action change that the baseline cannot supply.
- **Promotion condition:** Promote when insight is the publication route and no consequential surviving delta remains after the baseline is credited.

### 14. Surviving publishable core

- **Cue:** A broad application, novelty, or evidence claim appears weak, but one theorem, data construction, algorithm, or structural observation may still be valuable.
- **Operation:** Run deletion tests: remove the application story, disputed claim, standard method, and strongest result one at a time; ask what distinct and credible asset remains and which audience values it.
- **Possible finding:** A narrower paper identity and bounded repair path survive even though the original framing does not.
- **Disconfirmation:** Every candidate asset depends on the disputed spine, or the surviving result is routine relative to the closest work.
- **Promotion condition:** Always surface the strongest supported surviving core in the checkpoint; let it control repairability and recommendation when it offers a coherent publication path.

### Absorbing-action index ancestry

- **Cue:** Passive action evolves a Markov state while active action terminates, retires, resolves, or permanently absorbs the unit.
- **Operation:** Map the single-unit Lagrangian problem to retirement/optimal-stopping and Gittins-type constructions; separately map the system policy to Whittle, LP-priority, or related resource-allocation schemes. Distinguish index identity from the novelty of the system-level performance analysis.
- **Possible finding:** The index may be classical while a new finite-system guarantee, equilibrium argument, or tractable structure remains substantial; alternatively, both policy and guarantee may be inherited under matched assumptions.
- **Disconfirmation:** A consequential difference survives in ordering, indexability, admissible policies, assumptions, computation, or guarantee.
- **Promotion condition:** Promote an exact author-facing comparison question whenever the index or policy is a headline contribution, even if literature verification is incomplete; do not guess the answer.

### Main-lemma ancestry

- **Cue:** A new drift, concentration, state-space-collapse, tail, rounding, or approximation lemma is named as a primary technical contribution.
- **Operation:** Build a compact assumptions/conclusion table against the closest theorem families, including weaker moment, MGF, geometric-tail, or high-probability premises when relevant; identify the exact new obstacle, proof step, and downstream theorem delta.
- **Possible finding:** The lemma may supply a genuinely weaker assumption or sharper scale essential to the main result, or may repackage a known engine whose standard statement was compared too narrowly.
- **Disconfirmation:** An assumption-matched comparison establishes a consequential new conclusion or shows why existing results cannot deliver the main theorem.
- **Promotion condition:** Promote when the lemma carries the paper's theoretical novelty; if sources cannot be verified, request the table rather than alleging prior coverage.

## Anti-anchoring check

After using the examples, add at least one manuscript-specific candidate that does not come from this file. Then ask:

1. Did any example create a criticism merely because its vocabulary matched the paper?
2. Which candidate was disconfirmed and should become positive evidence?
3. Which important manuscript object has no corresponding example here?
4. Would the top idea set change if these examples had never been seen?

Retire keyword-driven candidates that lack manuscript-specific evidence. Preserve independently generated, well-supported ideas even when no template anticipated them.
