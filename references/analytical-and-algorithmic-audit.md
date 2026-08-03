# Analytical and Algorithmic Audit

## Reconstruct before checking

Write a compact formal contract:

- state and filtration/information set;
- action and feasibility;
- event timing;
- transition law and independence assumptions;
- objective and benchmark;
- horizon or stationary regime;
- scaling parameter and asymptotic statement;
- algorithm inputs and computational operations.

Many sharp comments arise from two individually reasonable definitions that do not match across sections.

## Assumption-to-use table

For every substantive assumption, record:

| Assumption | Where stated | Where used in proof | Used in numerics/application? | What fails without it? |
|---|---|---|---|---|

Prioritize strict positivity, boundedness, irreducibility, stationarity, independence, known distributions, unique initial state, finite support, convexity, regularity, and nondegeneracy.

Also derive the closure of each assumption family. A symmetric distance function, a normalization, a support partition, or a monotonicity condition may force equalities among parameters that later sections treat as independent. Check that state/group partitions cover the full declared support, with special attention to extreme groups and boundary mass.

For safe learning, separate three logically different assumptions:

1. **baseline certification:** why the baseline is known to satisfy the constraint in the unknown environment;
2. **sampling support:** which contexts, states, and actions the baseline visits;
3. **identification geometry:** whether those visits span every parameter direction needed by non-baseline policies.

A positive empirical eigenvalue on observed baseline data does not establish support for never-selected actions or uniform coverage over future contexts. Executing a baseline also cannot create a structural convexity property of the loss class.

## Guarantee-semantics table

For every safety, service, reliability, fairness, or violation statement, fill:

| Manuscript phrase | Protected unit | Random variable | Time aggregation | Population aggregation | Probability/expectation quantifier |
|---|---|---|---|---|---|
|  | patient/job/episode/state |  | stagewise/cumulative | individual/average/worst group | pathwise/chance/high-probability event/expectation |

Do not treat `E[sum_h c_h] >= M`, zero expected violation regret, zero realized threshold crossings, and a pathwise no-harm guarantee as interchangeable. Check that theoretical and empirical violation metrics refer to the same object.

## Theorem audit

Check:

- quantifier order and whether constants are uniform;
- existence of optimal policies/solutions and attainment;
- feasibility of constructed policies;
- stability, recurrence, and invariant-distribution claims;
- interchange of limits, expectations, derivatives, minima, and stationary limits;
- lower bounds used as benchmarks;
- relaxations and whether their direction is correct;
- duality assumptions and complementary slackness;
- rounding, tie breaking, empty queues, boundary capacity, and degenerate optima;
- concentration assumptions and dependence;
- whether lemmas prove the exact object used later;
- whether the theorem statement includes every dependency visible in the proof.

Do not declare a proof invalid solely because a step is terse. State the missing justification and attempt to supply it. A concern becomes a defect when the missing step is false, requires an unstated material assumption, or changes the rate/result.

For adaptive concentration, explicitly define the history `F_{t,h}` and check the conditional statements actually needed by the proof, such as

`E[epsilon_{t,h} | F_{t,h}, Z_{t,h}, A_{t,h}] = 0`

and a conditional MGF bound. Marginal zero mean, boundedness, or sub-Gaussianity does not imply these conditions after policy-dependent action selection. Account separately for within-episode dependence, repeated entities, delayed outcomes, and latent severity.

For matrix-weighted norm inequalities, conjugate the operator explicitly: the relevant quantity is typically `||M^(1/2) A M^(-1/2)||_2`, not `||A||_2`. Non-orthogonal similarity preserves eigenvalues but not singular values or spectral norm. Test disputed statements with a diagonal weight matrix and a `2×2` coordinate-swap or shear.

## Proof-method novelty audit

When a lemma, tail bound, state-space-collapse device, relaxation, or decomposition is part of the paper's claim to fame, create a comparison table:

| Item | Current result | Closest canonical result | Exact delta |
|---|---|---|---|
| process assumptions |  |  |  |
| drift/regularity assumptions |  |  |  |
| jump control | almost sure, moment, MGF, geometric, or none |  |  |
| conclusion | expectation, tail, rate, steady state |  |  |
| constants/parameter dependence |  |  |  |
| role in main theorem |  |  |  |

Search by proof structure, not only application keywords. A proof can be correct while its advertised methodological novelty is overstated; a known lemma can still be used in a novel and important way.

## Scaling and nonasymptotic claims

When a paper calls a bound finite-sample, meaningful, or nontrivial:

1. identify a valid trivial upper bound or benchmark;
2. retain constants and all important parameters;
3. plug in the numerical study's scale;
4. solve for the threshold at which the theorem improves on the trivial bound;
5. distinguish asymptotic optimality from practical accuracy.

An explicit finite-N expression can still be vacuous.

For cross-paper rate claims, build a matched-regime worksheet:

| Quantity | Proposed result | Comparator | Common specialization |
|---|---|---|---|
| state/action/context domains |  |  |  |
| hidden dimension/function complexity |  |  |  |
| horizon and episode count |  |  |  |
| coverage/eigenvalue assumptions |  |  |  |
| safe baseline oracle and gap |  |  |  |
| optimization/statistical oracle cost |  |  |  |
| resulting rate after substitution |  |  |  |

Never infer an improvement from one displayed exponent until hidden dimensions and assumption costs have been substituted in the same tabular, linear, or no-context special case. Trace each claimed factor improvement to the exact decomposition or confidence-radius step that produces it.

## Algorithm audit

Separate four questions:

1. **Definition:** Is the policy mathematically unambiguous?
2. **Information:** Are all inputs observable when the decision is made?
3. **Computation:** Can required values be obtained at the claimed scale?
4. **Guarantee:** Does the implemented approximation inherit any property of the ideal policy?

Add a fifth comparison whenever an optimization reformulation is used:

5. **Feasible-set identity:** Does every solution of the implementation correspond to one admissible model/policy in the theoretical problem, and vice versa?

A joint parameter confidence set couples transition, reward, or constraint coordinates. Replacing it with coordinatewise intervals or a rectangular transition polytope generally enlarges the feasible set. Solver tractability does not establish equivalence; require a realizing common parameter for every implemented kernel or analyze the relaxation separately.

Track offline versus online complexity, dependence on state dimension, numerical precision, training/sample cost, reoptimization under changing primitives, and whether an exponential representation is hidden behind a dimension-free regret bound.

Trace displayed pseudocode literally:

- mark loop and conditional scope;
- track which index/value survives after a loop closes;
- check initialization, ties, empty candidates, and return paths;
- instantiate the smallest full problem and compare the printed output with exhaustive enumeration.

Treat a pseudocode defect as verified at the manuscript level while separately checking whether released code repeats it.

For polynomial-time claims, distinguish bit complexity from dependence on numerical magnitude. Record payoff normalization, denominator/precision encoding, step-size restrictions, and whether a claimed polynomial method is only weakly or pseudo-polynomial in a value such as a capacity, payoff bound, or inverse tolerance.

For every assumed-known transition law, score, distribution, or cost, audit the **estimate–compute–act** chain:

- what data identify it;
- whether prior decisions censor or select those data;
- how estimation error propagates into priority order and performance;
- whether a structured/parametric approximation changes the claimed mechanism;
- whether added model complexity yields measurable decision value.

## Algebraic bridge tests

Whenever theory becomes a heuristic:

- write both formulas with the same units;
- substitute the application cost definition into the theoretical formula before simplifying;
- test heterogeneous multiplicative weights;
- check whether clipping, `min`, `max`, expectation, or nonlinear prediction commutes with scaling;
- check whether a global dual price becomes job-specific after rescaling;
- build a two-job numeric example to test whether rankings reverse.

## Optimality and mechanism benchmarks

Whenever feasible, request or construct:

- exact dynamic programming on a tiny state space;
- LP lower bound and realized optimality gap;
- exact version of the proposed policy versus its approximation;
- canonical policy under special cases;
- ablation isolating the proposed mechanism;
- scaling plots in the parameters appearing in the theorem.

These comparisons determine whether performance comes from the theorem's mechanism or from a favorable implementation choice.
