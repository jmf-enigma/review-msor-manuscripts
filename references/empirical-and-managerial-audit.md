# Empirical, Computational, and Managerial Audit

## Identify what the evidence is meant to establish

Label each study component as evidence for one or more of:

- correctness;
- mechanism;
- performance relative to alternatives;
- robustness;
- scalability;
- external validity;
- managerial impact.

Do not let a simulation designed for performance silently carry a field-impact claim.

## First-order mechanism inventory

Before judging the chosen model, list the application's main:

- uncertainties;
- information updates;
- constraints;
- decision levers;
- sources of outcome variation.

Ask which are plausibly first-order and what evidence supports that ranking. If the paper studies a deliberately partial mechanism, require correct positioning and scope—not an obligation to solve the entire application.

For a predicted risk or probability, explicitly ask whether it is fixed, dynamically updated, miscalibrated, correlated with exposure, or selectively observed after intervention.

## Operational cause and lever alignment

Write the application chain before evaluating the proposed policy:

`observed harm → operational cause → actor with control → feasible lever → model decision variable → evidence of first-order effect`.

For every state declared exogenous, ask who chose it, at what stage, under which objective, whether it evolves after action, and whether the modeled decision is organizationally separable from it. A downstream policy can be a useful mitigation without being the root-cause solution, but the paper must measure or bound that role.

Create a feature-budget table with columns for modeled/omitted status, empirical magnitude, expected policy sensitivity, technical complexity devoted, and tractability cost. Escalate when the paper omits a strongly evidenced first-order mechanism while spending most of its analytical budget on a weakly evidenced secondary mechanism.

## Behavioral recourse after failure

At a stockout, rejection, unavailable option, service failure, or treatment denial, enumerate feasible responses: within-option substitution, cross-option substitution, retry, wait, abandon, and outside choices. If the model omits a prevalent response, a proxy validation must compare:

1. objective value;
2. selected policy, assortment, or ranking;
3. subgroup or distributional outcomes.

An aggregate revenue upper bound alone does not establish policy or fairness robustness.

## Data provenance and realism

Record which elements are real, simulated, imputed, predicted, or generated from the model. A dataset with real covariate trajectories but synthetic treatments, outcomes, labels, or arrival processes is semi-synthetic.

Check:

- population and sampling frame;
- inclusion/filtering criteria;
- train/test splitting unit and temporal leakage;
- repeated entities or correlated observations;
- missingness and censoring;
- whether intervention removes future outcomes and creates selective labels;
- whether “normal” or untreated units can identify the counterfactual trajectory of removed/treated units;
- representativeness of operational load, capacity, and heterogeneity;
- licensing, privacy, and reproducibility.

Before claiming that code or data were not supplied, inspect the cover page, submission manifest, electronic companion, and supplementary-file listing. Distinguish “not visible in the manuscript PDF,” “submitted confidentially,” “available to reviewers,” and “publicly reproducible.”

### Logged decisions and counterfactual outcomes

When a paper evaluates a policy using observational or trial logs, record separately:

- what was randomized, if anything;
- the action the proposed policy chooses;
- who chose that action in the data and using which history;
- whether all time-varying confounders and treatment history are observed;
- overlap for every action in relevant history/context strata;
- the causal estimand and the assumptions connecting logged outcomes to policy outcomes.

Randomizing a treatment target, protocol arm, encouragement, or eligibility rule does not automatically randomize the visit-level medication, dose, routing, or service action optimized by the paper. A regression for `outcome | history, action` is predictive unless consistency, sequential exchangeability, and positivity are defended. Prefer patient/entity-level cross-fitting and appropriate off-policy, g-formula, or doubly robust evaluation; otherwise require model-based or semi-synthetic labeling.

### Static logs used as an online environment

If a finite historical dataset produces many more online episodes, clairvoyant-policy values, or outcomes under actions not observed in the logs, document the generator explicitly. Audit:

1. whether entities or trajectories are resampled or simulated;
2. which model generates each counterfactual next state and outcome;
3. whether the same observations fit the generator, tune the policy, and evaluate it;
4. patient/entity-disjoint and time-respecting train/validation/test splits;
5. validation against held-out factual transitions, behavior-policy OPE, an independently specified simulator, or prospective silent deployment;
6. propagation of simulator misspecification and distribution shift.

Calling fitted predictions “ground truth counterfactuals” does not create an independent ground truth.

## Baselines and mechanism identification

A fair benchmark should receive comparable information, tuning effort, model class, and compute. Add:

- a simple strong baseline;
- the closest literature method;
- an exact/oracle benchmark on small instances;
- an ablation for each added component;
- a nuisance-control baseline for clipping, regularization, extra features, or target transformation.

If the proposed method clips a heavy-tailed target, compare against a clipped version of the baseline before attributing gains to a new decision principle.

## Simulation design and uncertainty

Audit:

- warm-up and terminal effects;
- steady-state versus finite-horizon alignment;
- common random numbers or paired seeds across policies;
- number of independent replications;
- confidence intervals for paired differences;
- hyperparameter selection on training/validation only;
- sensitivity to seeds, demand/capacity, misspecification, and tail behavior;
- multiplicity when many settings are searched;
- absolute outcomes alongside percentages.
- preservation of decision-relevant joint structure, including cross-attribute availability, correlation between primitives, clustered configurations, and temporal dependence.

Lines without uncertainty bands can conceal Monte Carlo variability; ten runs are rarely self-justifying for heavy-tailed systems.

A generator calibrated only to univariate marginals is not “real-data calibrated” for policy purposes when the feasible set or trade-off frontier depends on co-occurrence and correlation. Require joint-distribution diagnostics, empirical-vector resampling, or sensitivity bounds.

Before interpreting any table, run deterministic integrity checks:

- exhaustive subgroup counts sum to the declared total;
- an overall mean lies in the convex hull of exhaustive subgroup means and equals their denominator-weighted average;
- counts and percentages imply consistent integer denominators;
- complementary partitions agree across outcomes;
- every policy is evaluated on the same cohort, initial conditions, horizon, and random-number stream unless policy-induced selection is the explicit estimand.

If a table conditions on where each policy disagrees, is treated, survives, or remains observed, each column may describe a different selected population. Report policy-specific denominators and repeat the primary comparison on a common cohort.

## Metric audit

For every business metric:

1. write its equation;
2. verify units;
3. identify denominator and zero/small-denominator behavior;
4. check interpolation or discretization;
5. test monotonicity assumed by inverse mappings;
6. propagate uncertainty through transformations;
7. distinguish service counts, capacity units, labor hours, money, and welfare.

Do not call a reduction in unit-capacity review probability “reviewer hours” without equal service-time assumptions or an explicit conversion.

For clinical or risk applications, distinguish observed endpoints from scores and surrogates. If a policy changes variables that also enter the risk calculator used for evaluation, lower predicted risk may be mechanically induced by the scoring equation. Freeze and validate the risk model outside the policy-training loop, report observed hard outcomes and adverse events where possible, and scope claims to surrogate improvement otherwise.

For safety metrics, identify whether a displayed violation is a realized stage threshold, an episode-total event, expected cumulative utility, expected violation regret, a chance constraint, or an individual/pathwise guarantee. The empirical metric must estimate the theoretical object before it can be presented as validation of the safety theorem.

For fairness, equity, access, representation, or welfare metrics, additionally audit:

1. the affected stakeholder, unit, and audit horizon;
2. absolute outcome levels, not only between-group gaps;
3. whether and why group prevalence enters the objective;
4. the order of expectation and nonlinear aggregation;
5. whether parity can be achieved by withholding service, leveling down, or cancellation across decisions;
6. whether the decision maker can estimate, explain, monitor, and act on the metric.

Distinguish `fairness of an average policy` from `average fairness of realized decisions`; they coincide only under special conditions.

## Robustness quality

Vary the failure mode that threatens the claim. For prediction-driven policies, consider:

- global miscalibration;
- ranking error;
- subgroup miscalibration;
- temporal drift;
- correlation between prediction error and cost/exposure;
- selective observation after intervention;
- train/serve distribution shift.

Independent mean-zero perturbation is not a general test of uncalibrated predictions.

## Managerial claim chain

Require this sequence:

`operational mechanism → model comparative statics/decision rule → design that varies the mechanism → measured outcome → scoped managerial implication`

Flag where the chain breaks. Ask:

- Who can act on the result?
- What data and computation are required at deployment?
- Which constraints are abstracted away?
- Does the insight survive heterogeneity in service time, skill, routing, fairness, and capacity?
- Is the claimed saving directly measured or extrapolated?
- Would a manager know when not to use the policy?

Prefer scoped language such as “illustrative,” “semi-synthetic,” or “capacity-unit savings” when evidence does not justify production impact.

## Estimate–compute–act realism

For every practical algorithm, document:

1. which quantities must be estimated;
2. data availability under the current policy;
3. state-space or function-approximation complexity;
4. update frequency under drift;
5. online compute and operational constraints;
6. evidence that additional complexity improves decisions.

A state-space-independent performance expression does not establish scalable estimation or computation.
