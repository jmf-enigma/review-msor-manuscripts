# Editorial-Threshold Reasoning for MS/OR Papers

## Contents

1. Freeze an outside view
2. Judge problem importance
3. Judge first-order status
4. Judge result interest and insight
5. Judge execution quality
6. Run three complementary reviewer passes
7. Match the paper's primary identity
8. Run contribution deletion tests
9. Synthesize survival and repairability
10. Write the editorial-first memo
11. Learn from calibration cases

## Purpose

Judge the manuscript's **publication case**, not merely whether its mathematics or experiments contain defects. Run this reasoning before the deep proof/data audit and keep its conclusions in a separate ledger. A technically correct paper can fail because it studies a secondary object or produces only expected conclusions; a paper with repairable local errors can remain promising because a strong core insight survives.

Use three independent tracks:

1. **Motivation and research-thesis track:** Is the question important, and is the selected object first-order for the operational phenomenon or theoretical difficulty?
2. **Execution track:** Is the overall analysis rigorous, deep, complete, and faithful from formulation through evidence? Mathematical correctness is one component.
3. **Result and insight track:** Are the results interesting, nontrivial relative to a disciplined baseline, and consequential for decisions or knowledge?

Do not let success or failure on one track substitute for judgment on another.

### What “first-order research object” means

Do not ask whether the model is the uniquely “correct” representation. Ask whether the selected object has primary intellectual or operational status:

The object need not be a single decision variable. It may be an operational tension, information structure, behavioral mechanism, resource allocation layer, mathematical obstacle, or empirically unidentified relationship. Judge the object the paper actually organizes knowledge around—not merely the variable its optimization program controls.

- **Operational route:** variation or intervention in the object materially governs the outcome, policy, or managerial tension after plausible rival mechanisms are considered.
- **Theoretical route:** the object isolates a fundamental obstacle or structure whose resolution advances a broader OR model class, even if the motivating application must be narrowed.

An object is secondary when it is mainly a downstream symptom, a proxy determined by an omitted upstream choice, an artifact of the chosen formulation, or a tractable mechanism whose resolution leaves the central phenomenon essentially unchanged. A paper may legitimately study a secondary component, but it must not use the importance of the larger domain to claim first-order significance for that component.

Assess four primary merits in every review:

1. **Problem importance and motivation:** Is the question consequential and credibly established?
2. **Research thesis and formulation:** Is the research object first-order, and is the abstraction generative rather than merely convenient?
3. **Execution, rigor, and completeness:** Is the thesis carried through appropriately and convincingly, including but not limited to correctness?
4. **Result interest and insight:** Does the result change understanding, capability, or action beyond what the assumptions already imply?

Novelty, evidence scope, and claim calibration cut across these four merits. Complete all four judgments even if one contains a decisive failure; the surviving strengths determine whether a bounded revision path exists.

## 1. Freeze an outside view before reading the results deeply

After reading the abstract, introduction, institutional description, related-work claim, and model/design—but before studying the main derivations or result discussion—record:

- the real phenomenon and decision consequence;
- the decision maker, action, timing, objective, and constraints;
- the two or three most plausible first-order drivers from institutional logic or cited evidence;
- the closest standard model or managerial baseline;
- the qualitative conclusions a knowledgeable reader would predict directly from the assumptions;
- what result would genuinely change that prior.

Preserve this **pre-result prior**. Later algebra can make a mechanically expected conclusion look sophisticated. The prior supplies a disciplined baseline for judging surprise and value.

Freeze the prior as a pre-audit editorial artifact before reading proof appendices or searching for errors. It must also contain a conditional-on-correctness publication verdict, the strongest prospective asset, the conditional editorial-merit bottleneck, and one conclusion from each reviewer pass. Do not rewrite this artifact after the technical audit; show post-audit adjudication separately. This prevents a vivid theorem or data error from displacing the distinct question of whether a fully correct paper would make a threshold-clearing contribution.

If the paper is empirical, replace “qualitative conclusions” with expected signs, mechanisms, heterogeneity, and plausible alternative explanations before reading the estimates.

## 2. Judge problem importance and motivation independently

Separate the importance of the domain, the phenomenon, and the exact research question. A paper about healthcare, fairness, platforms, sustainability, or AI does not inherit the importance of that domain automatically.

Establish six links:

1. **Stake:** identify the operational, welfare, scientific, or economic consequence and its credible magnitude.
2. **Decision exposure:** identify who repeatedly faces the decision, how often, and what is lost under current practice.
3. **Unresolved tension:** state why existing theory, methods, data, or practice cannot already answer the question.
4. **Breadth:** explain whether the issue travels beyond one organization, dataset, parameter choice, or technical niche.
5. **Solution value:** specify what becomes possible if the question is solved well.
6. **Motivating evidence:** verify that cited facts actually measure the phenomenon rather than selection, censoring, supply, equilibrium, or a different decision layer.

Run two counterfactuals:

- **No-paper test:** What important decision, explanation, or scientific capability remains unavailable if this paper does not exist?
- **Perfect-answer test:** If the paper answered its exact question perfectly, would the resulting knowledge or decision improvement be material?

Adjudicate motivation as **established**, **promising but under-evidenced**, **important domain but narrow question**, or **not established**. Keep this judgment separate from whether the model is first-order: a major problem can be represented by a secondary object, and an abstract theoretical object can be important without a large immediate application.

## 3. Judge whether the research object is first-order from an independent map

### 3.1 Reconstruct the decision system outside the paper's vocabulary

Map the application into decision layers:

| Layer | Actor | Decision and timing | Main state/constraint | How it affects the outcome |
|---|---|---|---|---|
| Upstream design/capacity |  |  |  |  |
| Focal operational decision |  |  |  |  |
| Downstream behavior/recourse |  |  |  |  |
| Learning/equilibrium feedback |  |  |  |  |

Then mark which layers the model endogenizes, fixes, or omits. Do not demand every realistic feature. Scrutinize an omitted feature only when it can plausibly **create the motivating phenomenon, dominate the modeled lever, reverse the policy ranking, eliminate the modeled problem, or invalidate the proposed action**.

### 3.2 Run seven first-order-object counterfactuals

1. **Constitutive-object test:** Remove or hold fixed the selected object. Does the central phenomenon or theoretical difficulty substantially collapse, or does essentially the same problem remain elsewhere?
2. **Perfect-solution test:** If the organization implemented the model-optimal policy perfectly, would the motivating outcome materially improve? If not, the model may solve a mathematically clean but secondary problem.
3. **Rival-object test:** Construct the strongest plausible competing research object—an upstream decision, downstream behavior, alternative uncertainty, or canonical mathematical structure—and compare their explanatory and decision value.
4. **Dominance/policy-reversal test:** Perturb the leading omitted driver in the smallest diagnostic model. Ask whether it dominates the modeled object or makes the headline prescription reverse, disappear, or become infeasible.
5. **Separation test:** When upstream or downstream decisions are declared exogenous, require institutional timing, ownership, process, or data evidence that separate optimization is meaningful.
6. **Application-invariance test:** Across every headline example, verify that availability, capacity, consumption, cost, state, and decision rights retain the same operational meaning. A shared metaphor is not a shared first-order object.
7. **Theory-survival test:** If the application mapping fails, strip it away and ask whether the abstract object still isolates a fundamental OR difficulty with a substantial result.

### 3.3 Adjudicate first-order status

Use one of four conclusions:

- **Operationally first-order:** the object materially governs the phenomenon or decision, and evidence or institutional structure supports the abstraction.
- **Theoretically first-order:** the application link may be limited, but the object isolates a fundamental OR difficulty and yields a substantial result.
- **Conditionally first-order:** centrality or separability is plausible but not established; narrower scope or a diagnostic robustness exercise may suffice.
- **Secondary/wrong-layer:** a rival object plausibly creates most of the phenomenon, supplies the difficulty, or overturns the recommendation; the claimed contribution is not established at its current scope.

State the burden of proof. Do not convert “the paper omitted feature X” into a major comment unless the counterfactual tests explain why X changes the publication case.

For every newly named model or problem class, first complete an explicit canonical-reduction table covering context, state, action, timing/information, objective, feasible policies, and complexity. A theoretically important topic is not enough to establish a theoretically first-order *new object*. Identify the exact structure, rate, computation, or guarantee that cannot be obtained after reduction to the closest standard model. If no consequential delta survives, classify the contribution as a structured special case, algorithmic result, or combination rather than a new model class.

Whenever a failure, stockout, rejection, service denial, or unavailable choice is part of the model, enumerate downstream recourse before closing the first-order judgment. Promote the omitted response most likely to change objective value, policy/ranking, or distributional effects; do not leave it in a generic realism inventory.

## 4. Judge whether the result and insight clear the journal threshold

### 4.1 Build a result-to-insight ledger

For every result presented as central, record:

| Field | Required judgment |
|---|---|
| Plain-language result | State what changes, for whom, and under what conditions without notation |
| Pre-result baseline | What the assumptions and closest standard model already made likely |
| Surviving delta | What is learned beyond that baseline |
| Mechanism | Which countervailing forces or structural facts produce the delta |
| Decision/belief delta | What a manager, modeler, or theorist would do or believe differently |
| Regime and boundary | Where the conclusion applies, reverses, becomes trivial, or fails |
| Robustness | Whether existence/sign/order survives plausible functional-form or behavioral changes |
| Ancestry | Whether the closest literature already supplies the same conclusion |

### 4.2 Use an insight ladder, not a theorem count

Classify each central result provisionally:

0. **Restatement:** a definition, feasibility fact, or reformulation with no new consequence.
1. **Expected direction:** a monotonicity or comparative static directly encoded by the assumptions.
2. **Useful characterization:** a computable threshold, bound, ordering, sufficient condition, or quantitative magnitude.
3. **Structural insight:** a non-obvious policy form, countervailing-mechanism trade-off, reversal, phase boundary, or condition under which a simple rule is sufficient or fails.
4. **Portable principle:** a result that changes how a broader class of problems is modeled, solved, or managed and survives removal of the paper's labels.

This is not a numeric acceptance rule. Use it to locate the publication asset. A top-journal analytical paper normally needs at least one convincing level-3/4 asset, or a strong level-2 result paired with a separately substantial methodological, empirical, or application contribution. Several level-1 results do not become level 3 through volume or proof length.

### 4.3 Run seven insight tests

1. **Assumption-echo test:** Would a reader predict the result immediately from monotonicity, convexity, symmetry, or the sign imposed in the primitives? If yes, identify what exact part is still non-obvious.
2. **Competing-force test:** Does the theorem resolve forces that point in opposite directions, or merely formalize one force already assumed? Strong insight often identifies the boundary at which dominance changes.
3. **Decision-delta test:** Compare two otherwise identical decision makers, one knowing the result and one not. Specify the state in which their actions differ and why the difference matters.
4. **Belief-delta test:** For methodological work, state which previously plausible theorem, complexity expectation, or modeling belief must be revised.
5. **Restricted-policy test:** If the insight concerns a simple policy class, determine its value relative to the unrestricted optimum or explain why the institution exogenously requires that class.
6. **Robustness-of-existence test:** Separate whether the result's exact formula, direction, threshold existence, or mechanism survives beyond the convenient functional form. Do not demand a fully general model when a small perturbation can diagnose this.
7. **Portable-compression test:** Remove application labels and notation. If the contribution cannot be expressed as a mechanism, regime rule, or new capability in one or two sentences, its broader knowledge content may be weak.

Surprise alone is not value. A result driven by an implausible corner case may be unexpected but unimportant. Require both a nontrivial delta and a credible consequential regime.

## 5. Judge execution as rigor, depth, completeness, and closure

Do not reduce execution to finding mathematical mistakes. Assess six distinct dimensions:

| Execution dimension | Central question | Positive evidence | Failure mode |
|---|---|---|---|
| Thesis alignment | Does the analysis answer the question and study the object promised? | Every theorem, estimator, algorithm, and experiment advances the same contribution | Rigorous analysis of a different or secondary object |
| Difficulty engagement | Does the work resolve the hard part rather than assume or outsource it? | A new argument, identification strategy, or algorithm directly handles the obstacle | Oracle, coverage, exogeneity, or benchmark assumptions supply the answer |
| Formal/empirical validity | Are claims correct under their stated assumptions and design? | Sound derivation, identification, computation, and uncertainty treatment | False theorem, invalid estimator, implementation bug, or unidentified effect |
| Analytical completeness | Are central regimes, boundaries, countervailing forces, and limitations characterized? | Main cases and failure boundaries form a coherent account | A narrow interior result is narrated as a general theory |
| Robustness and mechanism | Does the paper distinguish structural conclusions from functional-form or design artifacts? | Targeted perturbations preserve or explain changes in the key result | Sensitivity tables vary secondary parameters while the core assumption is untouched |
| Operational/scientific closure | Can inputs be obtained, the method be run, and evidence support the claimed consequence? | End-to-end estimate–compute–act or theory–algorithm–evidence bridge | The formal object cannot be estimated, implemented, benchmarked, or validated |

For each row, record both the strongest positive evidence and the main limitation. Then adjudicate execution as:

- **rigorous and complete for the claim;**
- **rigorous but deliberately narrow;**
- **technically substantial but incomplete or misaligned;**
- **not credible at the claimed scope.**

A hard error may dominate the credibility verdict, but it remains one finding within the validity row. Continue assessing the other rows because they reveal whether a valuable and well-executed core survives a repair. Conversely, the absence of a detected error does not establish strong execution: the analysis may be shallow, assumption-driven, incomplete, or disconnected from implementation.

Judge execution relative to the paper's ambition. A parsimonious proof of a fundamental result can be excellent execution; hundreds of pages of derivations may be weak execution if they avoid the first-order difficulty or do not yield a coherent characterization.

## 6. Triangulate with three complementary reviewer passes

Run all three passes; do not treat them as fixed reviewer personalities or choose only the one that produces the harshest verdict.

### Pass A — Phenomenon-origin and first-order-object pass

- Ask why the observed practice or theoretical difficulty exists before adopting the paper's explanation.
- Construct the strongest rival research objects and compare settings in which each candidate mechanism is present or absent.
- Verify that the modeled state and action actually exist in every headline application.
- Test whether the chosen object remains primary after capacity, heterogeneity, persistence, recourse, upstream design, or another plausible driver is admitted.
- Output: the first-order-object classification and the minimum scope/model architecture that would make it credible.

### Pass B — Prescriptive-closure pass

- Trace behavioral primitives, resource constraints, state sufficiency, feasibility, and parameter meaning.
- Identify whether the paper studies the unrestricted decision or an institutionally restricted policy class; require a value benchmark or bounded within-class claim.
- Check that upstream object boundaries do not leak into managerial conclusions.
- Compare with the closest method under the same information structure, then inspect empirical or institutional grounding.
- Output: the weakest broken link in `behavior → feasible set → policy class → benchmark → ancestry → validation` and its repair scope.

### Pass C — Generative-model and knowledge-yield pass

- Identify what modeling choice creates tractability and whether it is intellectually productive rather than merely convenient.
- Map how one mechanism generates results across simple, intermediate, and general settings.
- Separate expected qualitative direction from valuable exact characterization and from genuinely less-intuitive structure.
- Identify the strongest unused implication of the paper's own general machinery and request it only when it yields portable guidance.
- Diagnose behavioral or functional-form boundaries with a bounded stress test rather than automatically demanding a replacement model.
- Verify that named mechanisms and intuition remain faithful to the algebra.
- Output: the cumulative knowledge produced, strongest structural asset, unrealized generative opportunity, and scientific boundary.

These passes can disagree. A model may be operationally weak under Pass A but theoretically generative under Pass C; Pass B may then determine whether its prescriptions remain credible. Preserve the disagreement and let the journal route and strongest surviving asset determine the synthesis.

## 7. Match the threshold to the paper's primary identity

| Primary identity | Minimum publication evidence | Common false substitute |
|---|---|---|
| Decision-support method | Correct formulation; implementable and scalable method; strong benchmark or bound; obtainable inputs; material decision value | A standard MIP tested on tiny instances |
| Structural/managerial insight | Non-obvious structure or mechanism; regime/boundary; feasible action; robustness of the qualitative conclusion | Many intuitive comparative statics or results only within an unbenchmarked policy class |
| Methodological OR theory | Exact delta against the closest ancestor; genuine new obstacle and resolving idea; consequential guarantee or capability | New terminology, direct component combination, or a rate with hidden dimensions |
| Empirical fact/intervention | Credible estimand or predictive target; independent evaluation; magnitude and uncertainty; mechanism/heterogeneity; scoped external validity | A model-calibrated or in-model counterfactual labeled “real-world validation” |

A hybrid paper may contribute on several dimensions, but identify which row carries the publication case. Do not allow three sub-threshold components to masquerade as one threshold-clearing contribution unless their integration itself creates a new obstacle, resolving step, and consequential result that none of the components supplies separately.

## 8. Perform contribution deletion tests

Ask four questions:

1. Remove the application story. Does a substantial OR result remain?
2. Remove the new method. Does a new empirical or managerial fact remain?
3. Remove the strongest theorem or empirical result. Does any publishable core remain?
4. Replace the proposed machinery with the closest simple or canonical method. What consequential delta survives?

Use the answers to identify:

- the **strongest publishable asset**;
- the **conditional editorial-merit bottleneck** assuming every result is correct;
- whether the application, method, and insight are complements or attempted substitutes;
- whether repair preserves or replaces the paper's contribution identity.

## 9. Make the recommendation from survival and repairability

Keep two diagnoses separate:

- **conditional editorial-merit bottleneck:** what most limits importance, first-order status, novelty, or insight if every result is correct;
- **credibility bottleneck:** what most limits belief in the model, theorem, algorithm, identification, implementation, or evidence after detailed audit.

State a conditional-on-correctness recommendation and a credibility-adjusted recommendation. Then explain which bottleneck controls the current decision. A fatal proof defect may control publication today, but it must not erase a canonical-reduction, wrong-layer, or insight-threshold judgment; conversely, a correct theorem does not repair an absent publication contribution.

Do not count comments. Decide in this order:

1. Does an important problem and a first-order operational or theoretical research object survive the audit?
2. If every result is correct, does at least one contribution clear the identity-appropriate threshold?
3. Does the credibility audit leave that asset intact?
4. Can the decisive bottleneck be repaired without changing the central decision, main model, evidence design, or claim to fame?

Distinguish:

- **bounded repair:** clarification, positioning, a contained proof, scoped robustness, or claim contraction preserves the asset;
- **section reconstruction:** major new analysis is needed, but the same asset can remain central;
- **paper-spine reconstruction:** the lever, model, primary evidence, or contribution identity must change.

The last category normally cannot support an ordinary revision even when the topic is important and the execution is extensive.

## 10. Required editorial-first memo

Before listing proof, computation, or data defects, write seven sentences:

1. Judge the consequential problem, its evidence, and why solving it matters.
2. State the selected research object and its strongest first-order rival.
3. Judge whether the object is operationally first-order, theoretically first-order, conditionally first-order, or secondary/wrong-layer.
4. State what conclusions were predictable before reading the results.
5. Identify the strongest surviving result and why it exceeds—or fails to exceed—that baseline.
6. Judge the execution's rigor, depth, completeness, and end-to-end closure—not merely the presence or absence of errors.
7. Name the publishable core, both bottlenecks, which controls, repair scope, and provisional journal-level implication.

Sentence 7 must name both the conditional editorial-merit bottleneck and the post-audit credibility bottleneck, then state which controls. If either is absent, the memo is incomplete.

If any sentence can only be filled with “unclear,” convert that uncertainty into a specific evidence request rather than a generic criticism.

## 11. Learn editorial reasoning from calibration cases

When an actual editor or referee record becomes available, compare reasoning—not comment counts—on seven axes:

1. problem-importance judgment;
2. strongest publishable asset;
3. first-order-object judgment and strongest rival object;
4. expected-versus-consequential result classification;
5. execution-quality judgment beyond detected errors;
6. decisive bottleneck;
7. repair scope and recommendation logic.

For every disagreement, reconstruct the manuscript cue, counterfactual operation, intermediate inference, and editorial consequence. Learn a new operation only after checking that the observed comment is factually sound. Preserve independent correctness findings, but do not use them to avoid diagnosing why the actual editors valued or discounted the paper's central idea.
