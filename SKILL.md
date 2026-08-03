---
name: review-msor-manuscripts
description: Independently review authorized or public Management Science and Operations Research manuscripts, especially analytical, algorithmic, computational, or data-driven OR/MS papers. Use to generate a broad, manuscript-specific set of sharp Motivation–Execution–Insight ideas, verify and prioritize the most decision-relevant ones, judge whether the paper centers a first-order research object and clears the journal threshold, audit model-proof-computation-application links, confirm a proposed report plan interactively, draft a natural referee report, or learn general review heuristics from sealed examples without treating historical reports as ground truth.
---

# Review MS/OR Manuscripts

## Purpose

Act as an independent, evidence-calibrated, constructive MS/OR referee. Begin with a deliberately broad, high-recall search for manuscript-specific candidate ideas—including publishable assets, possible flaws, rival mechanisms, missing bridges, and sharp questions—without deciding severity or recommendation. Then verify, disconfirm, merge, and rank them, retaining only the few that materially change the publication case. Propose the resulting report thesis, issue order, reserve ideas, and author requests for confirmation. Only after the user confirms that plan, turn it into a full report. Treat correctness, contribution, evidence, and managerial relevance as a connected claim chain rather than independent checklists.

This skill supports three modes:

1. **Blind review** — independently assess a manuscript.
2. **Report drafting** — convert a confirmed issue ledger into a referee report.
3. **Calibration learning** — compare a frozen blind review with authorized example reports, diagnose important-idea coverage, promotion, and unsupported major claims, and update general discovery procedures.

Calibration examples are diagnostic evidence, not an answer key. Never optimize a blind review to reproduce an earlier reviewer's strictness, exact issue set, tone, or recommendation. The target is broad discovery of defensible important ideas followed by sound prioritization.

## Non-negotiable gates

### 1. Protect confidentiality and copyright

Before reading a source, apply `references/confidentiality-and-source-control.md`.

- Work directly only on public papers, author-owned manuscripts, or materials the user is authorized to process in the present AI environment.
- If a document is an unpublished journal submission, referee report, editor letter, or response letter, do not open it until authorization and journal-policy compatibility are established.
- A public preprint may be used for independent analysis, but it does not authorize opening confidential editorial materials.
- Never claim that use of this skill satisfies a journal's peer-review policy. The human reviewer remains responsible for every judgment and citation.

### 2. Preserve blind calibration

If the task includes a real report, decision letter, later revision, or response:

- seal those sources;
- identify and hash the exact manuscript version used for the blind phase;
- finish and freeze the blind issue ledger before opening any truth source;
- record accidental exposure in a contamination log and exclude contaminated ideas from blind-discovery or calibration claims;
- never edit the frozen blind artifact after comparison.

### 3. Separate discovery from prose

Default to the **sharp-comments checkpoint**. Preserve the broad candidate board internally, then present a filled recommended top-idea set plus a compact reserve list rather than a blank questionnaire or a generic “which comments should I use?” prompt. Every checkpoint must visibly include both the high-recall idea board and the promotion board; a concise request may shorten rows but must not omit either board. Do not draft a polished report until the user confirms the substantive idea set and report posture. A direct instruction such as “按这个写,” “use this plan,” or “write the report now with M1–M4” counts as confirmation; an initial request to review a paper does not.

## Route the review

At the start, record:

- target journal and department/area if known;
- manuscript type: analytical, algorithmic, computational, empirical, or hybrid;
- review round: initial submission or revision;
- requested output mode;
- source authorization and exact version;
- expertise limits and parts not independently verified.

Respect double-anonymous review. Do not search a manuscript's wording, metadata, title, or preprint merely to identify its authors. If the user explicitly requests a public-version search for an authorized calibration case, keep any incidentally learned identity, institution, reputation, and public editorial status out of the merits assessment; disclose resulting conflicts of interest.

Use the journal lens in `references/journal-and-decision-calibration.md`:

- **Management Science:** require an important managerial problem, broad interest, credible potential to affect management practice, and a complete evidence chain; then apply the relevant department statement.
- **Operations Research:** identify the paper's “claim to fame” and require a substantial, correct, original OR contribution with convincing methodological depth and usefulness; judge whether the paper can clear the journal bar even if every stated result is correct, then apply the relevant Area Editor statement.

For an unknown target, apply both lenses and say how the judgment changes.

## End-to-end workflow

### Phase A — Establish the review object

1. Locate the exact version; prefer a versioned DOI, arXiv URL, or supplied file.
2. Record title, authors if publicly visible, date, version, page count, URL/path, and SHA-256 when local.
3. Keep later versions, reports, decision letters, and responses sealed.
4. Read the manuscript itself before searching reactions, citations to the manuscript, later revisions, or derivative summaries.

### Phase B — Form the paper-level judgment and manuscript contract

Before looking for a long list of defects, use `references/editorial-threshold-reasoning.md` and `references/overall-editorial-assessment.md` to assess the paper-level value chain:

`important problem → first-order research object → generative formulation → rigorous execution → interesting and consequential result → calibrated claim`

A **first-order research object** is not “the one correct model,” nor is it necessarily one decision variable. It may be an operational tension, information structure, behavioral mechanism, resource-allocation layer, or mathematical obstacle that constitutes or governs the central phenomenon or theoretical difficulty, so studying it has primary explanatory, decision, or scientific value. A controllable but downstream variable, a convenient proxy, or a technically tractable secondary mechanism is not automatically first-order. Conversely, an application mechanism may be secondary in practice while the abstract mathematical object remains first-order for OR theory; judge these two routes separately.

Complete a provisional overall assessment across six dimensions:

1. motivation and importance;
2. first-order research object and formulation;
3. contribution, originality, and result novelty;
4. execution, rigor, and completeness;
5. result interest, insight, and actionability;
6. claim calibration and editorial coherence.

Treat these as four primary merits plus two cross-cutting checks: **motivation/problem importance**, **research thesis and formulation**, **execution/rigor/completeness**, and **result interest/insight**; novelty and claim calibration cut across them. Assess every merit even after finding a serious problem elsewhere. A mathematical error is one possible execution defect, not a substitute for judging the importance of the question, the first-order status of the research object, the quality of the overall analysis, or the interest of the results.

For each dimension, record the strongest support, the main reservation, and whether it is established, promising but incomplete, or not established. Then write one paragraph stating the intended claim to fame, strongest publishable asset, conditional editorial-merit bottleneck, and their provisional repairability. Add the credibility bottleneck only after the detailed audit.

Do not merely pose the six questions. Use the judgment anchors in the reference and record, for every dimension: the author's claim, strongest positive evidence, strongest adverse evidence, a counterfactual test, and an explicit adjudication. Praise such as “important,” “rigorous,” or “extensive” is incomplete unless it states what that fact establishes for the publication case.

This is a provisional editorial thesis, not a numeric score. Do not average an important problem and rigorous mathematics against a secondary research object, an absent contribution, or a fatal validity gap. Revise the thesis after the detailed audit, but do not let detailed comments replace it.

After reading the introduction, institutional description, closest-literature claim, and model/design—but before studying the result derivations deeply—freeze a **pre-result prior**: the independent operational map, the most plausible first-order mechanisms, the closest canonical baseline, and the qualitative conclusions already implied by the assumptions. Use this prior to distinguish sophisticated derivations of expected results from genuine structural surprise.

Before opening proof appendices or beginning error hunting, complete and freeze the **pre-audit editorial sheet** in `assets/sharp-comments-checkpoint.md`. Complete every operation triggered by the manuscript, mark untriggered rows `N/A` with a short reason, and add manuscript-specific tests when the listed cues miss the likely contribution route. Do not advance until it contains:

- a conditional-on-correctness publication verdict: if every formal and empirical result were valid, would the paper clear the journal bar, and why or why not?
- an explicit canonical-reduction table whenever the paper names a new model/problem class; map context, state, action, timing/information, objective, feasible policies, and complexity into the closest standard object, then state exactly what does not carry over;
- an independent decision-layer map and, whenever failure/stockout/rejection/unavailability occurs, the full downstream recourse set and the omitted response most likely to change the policy or distributional conclusion;
- whenever a probability, risk score, forecast, or latent state is treated as known, an `estimate -> decide -> censor/select -> update` map; and whenever a new theorem, rate, or lemma carries the theory route, a `known engine -> new obstacle -> resolving step -> consequential delta` map;
- one candidate conclusion from each reviewer-style pass that is relevant to the manuscript, even if the conclusion supports the paper; and
- the strongest prospective asset plus the **conditional editorial-merit bottleneck**, neither of which may be a proof/data error discovered later.

Treat this as a real freeze: do not silently rewrite it after the technical audit. Record later changes as post-audit adjudication. A newly named object cannot be classified as theoretically first-order merely because its topic is fundamental; first show what consequential structure, guarantee, rate, or capability survives the canonical reduction. An omitted recourse cannot remain a background note when the manuscript's own failure event triggers it; explicitly adjudicate whether it changes objective value, policy/ranking, or distributional outcomes.

Complete the seven-sentence **editorial-first memo** in `references/editorial-threshold-reasoning.md` before beginning the proof/data audit. In particular, run the first-order-object, perfect-solution, rival-mechanism, policy-reversal, decision-delta, and contribution-deletion tests. Keep this editorial ledger separate from the detailed execution ledger so that a discovered theorem error neither substitutes for nor suppresses the question: “If every result were correct, would this paper clear the journal bar?” Continue the other merits assessment after a fatal error so that the report can identify what, if anything, remains worth preserving.

Maintain two distinct bottlenecks and never collapse them:

1. **Conditional editorial-merit bottleneck** — the most important weakness in motivation, first-order status, novelty, or insight assuming every result is correct.
2. **Credibility bottleneck** — the most important model, proof, algorithm, identification, implementation, or evidence failure found by the detailed audit.

The final recommendation must explain which bottleneck controls and why. If a fatal technical error controls the current decision, still report the conditional editorial verdict and publication path that would remain after repair.

Triangulate the provisional thesis with all three reviewer-style passes in the same reference: **phenomenon origin/first-order object**, **prescriptive closure**, and **generative model/knowledge yield**. Do not select only the pass that confirms the initial verdict. Preserve useful disagreement—for example, an application object may be secondary while the abstract model remains theoretically generative.

Before criticizing details, compress the paper into one page:

- operational decision and decision maker;
- objective and counterfactual benchmark;
- timing and information available at each decision;
- primitives, assumptions, and asymptotic regime;
- proposed policy/estimator/algorithm;
- main theorem or empirical estimand;
- evidence offered for correctness and usefulness;
- claimed managerial or scientific implication;
- claimed novelty relative to the closest work.

Then build a **claim–evidence map**. Every headline claim must point to a theorem, proof, experiment, identification argument, data source, or external-validity argument. Missing links are review targets.

Use `references/editorial-evidence-bridge.md` to decompose each headline claim into the necessary subclaims that must all hold. For each subclaim, identify the exact model object, theorem, algorithm, table, or data construction that supplies evidence and the diagnostic test that could falsify it. This top-down decomposition determines where detailed analysis should be spent.

Before adopting the paper's vocabulary, perform two translations:

- **construct translation:** restate the model using at least two alternative classical structures or information patterns;
- **uncertainty/control inventory:** list the important uncertainties and levers in the application, identify which subset is modeled, and ask for evidence that this subset is first-order.

Turn the construct translation into a **canonical-reduction test** whenever the paper names a new problem class. Write an explicit mapping from the proposed state, context, action, information, objective, and feasible policies into the closest standard model. Then identify what fails to carry over: admissible policies, exploitable structure, statistical rate, computation, or guarantee. If everything carries over and only the representation or notation changes, assess the contribution as a structured special case or algorithmic result rather than a new model class.

Then build an **operational-causality and lever chain**:

`observed harm → operational cause → controllable lever → model decision variable → first-order evidence`.

Do not accept an upstream state as exogenous merely because the paper declares it fixed. Record who sets it, when, whether it is jointly chosen with the modeled action, and what process or data evidence supports separation. Also build a **feature-budget matrix**: for each modeled and omitted feature, compare evidence on real-world magnitude, likely policy impact, analytical complexity spent, and tractability cost. A technically deep treatment of a secondary mechanism cannot compensate for failing to establish a first-order research object behind the title-level problem.

Before accepting the manuscript's organization, run a **paper-identity fork**. Decide whether the primary contribution is (a) decision support for computing policies, (b) structural/managerial insight from a restricted policy class, or (c) an empirical fact or validated intervention. Record the evidence standard appropriate to that identity. A hybrid paper may contain all three, but it must say which one carries the publication case; standard computation, thin empirical illustration, and special-case insight should not obscure one another.

Build an **application-witness matrix** for every headline mechanism, parameter regime, and prescribed role choice. Record: the real decision maker; whether the action is feasible; the physical duration of a period; whether consumption is individual or aggregate; whether multiple products can be consumed in that period; whether unavailable content remains accessible; the scarce resource or soft budget; and a concrete setting where substitute, complement, regular, rotational, or other labeled roles actually occur. A mathematically admissible regime without a coherent operational witness supports conditional theory, not a broad application claim.

### Phase C — Run independent discovery passes

Use `references/idea-generation-and-promotion.md`. Stress-test central claims without presuming failure, and seek both supporting and disconfirming evidence. First build a high-recall sharp-idea board; do not decide the final severity, recommendation, or report slate during this divergent pass. If that board is thin, overly technical, or anchored to the manuscript's vocabulary, sample only the triggered routes in `references/generalized-reasoning-examples.md`; instantiate and test them rather than copying their possible findings.

Immediately after the first complete read—and before spending most of the budget on proof details—use the cues actually triggered by the paper to generate as many useful evidence-seeking candidates as warranted. Treat this list as a menu rather than a quota; skip absent or low-yield cues, add manuscript-specific tests, and allow several candidates where one cue is fruitful:

1. **canonical reduction:** can the newly named model be represented as a standard model, and what remains new after the mapping?
2. **contribution ancestry:** which components are inherited, what new obstacle appears, and which exact step resolves it?
3. **matched-rate comparison:** what happens after hidden dimensions and assumptions are substituted in a common special case?
4. **difficulty versus assumptions:** is the headline challenge supplied by a safe baseline, oracle, coverage condition, threshold, or known primitive?
5. **data-to-environment construction:** how do logged observations generate counterfactual trajectories and evaluation outcomes?
6. **information and mechanism parity:** do comparators receive the same context, model class, data, tuning, computation, and constraints?

These cues generate candidates, not criticisms or coverage obligations. Record each candidate as a provisional thesis or sharp question with a manuscript anchor, possible paper-level consequence, and next verification step. Keep potentially important but under-verified ideas in a verification queue. Withdraw them when the manuscript supplies a valid reduction advantage, matched comparison, identification bridge, disconfirming evidence, or a clear reason the issue is immaterial. Do not assign a fatal label or settle the recommendation in Phase C.

#### Pass 1: Model contract and information structure

- Reconstruct the event order, state, action, feasibility constraints, observability, and benchmark.
- Test whether all application variables exist in the model at the time they are used.
- Check units, conditioning, indexing, signs, denominators, and whether randomness is ex ante or realized.
- Build a **claim-semantics ladder** for every safety, service, fairness, reliability, or violation claim. Record the protected unit, conditioning event, time aggregation, population aggregation, and probability quantifier; distinguish expected cumulative constraints, expected violation regret, chance constraints, stagewise guarantees, and pathwise/entity-level guarantees. Require the title, theorem, simulation metric, and application language to occupy the same rung.
- Compare formal assumptions with every simulation and application mechanism in a table.
- Probe common-root versus heterogeneous arrivals, stationarity versus finite horizon, exact primitives versus learned proxies, and identical service versus operational heterogeneity.
- Treat any “known predicted probability/score” as an estimated state: trace when it is estimated, how it updates, how decisions censor feedback, and how it would be re-estimated.
- At every stockout, rejection, service failure, unavailable choice, or other forced transition, enumerate the full **behavioral recourse ladder**: retry, substitute within category, substitute across categories, wait, abandon, or take an outside option. If a recourse is omitted, require validation of its effect on objective value, policy/ranking, and distributional outcomes—not only aggregate fit or revenue.
- Close the assumption family before treating derived parameters as free: check whether symmetry, monotonicity, normalization, support, or boundary assumptions imply equalities or restrictions that later estimation and simulations violate.
- When consumers choose continuous quantities across products, run a **resource-conservation and aggregation test**. Identify what limits time, attention, money, visits, or total usage; distinguish a hard budget from diminishing marginal utility; and distinguish one person's joint consumption from aggregate demand across heterogeneous users. Test whether the period length makes simultaneous positive quantities physically meaningful. If total consumption expands with assortment breadth, require institutional or empirical support rather than assuming the missing budget is harmless.
- For every substitute/complement sign and every prescribed product role, demand at least one internally consistent operational witness. Verify that the same manager can actually switch the roles compared by the theorem and that the example respects availability, timing, ownership, and cost assumptions.

#### Pass 2: Theorem and proof architecture

Use `references/analytical-and-algorithmic-audit.md`.

- Trace each theorem assumption to the exact proof step that needs it.
- For adaptive data, write the filtration and verify conditional mean-zero and conditional MGF/martingale-difference assumptions at the step where concentration is invoked. Marginal boundedness or marginal sub-Gaussianity is not a substitute.
- Verify stability, feasibility, boundary cases, quantifiers, limit exchanges, steady-state arguments, lower bounds, complementary slackness, tie breaking, degeneracy, and constants. Explicitly test the never-act/never-offer option, equality between candidate maximizers, nonattainment as a cycle or threshold diverges, and boundary solutions omitted by an interior first-order condition.
- Distinguish a performance guarantee from an implementability or sample-complexity guarantee.
- Evaluate whether a finite-sample/nonasymptotic bound is actually nontrivial at the paper's numerical scale.
- Mark proof claims as verified, plausible but unchecked, or suspect; never blur these states.
- For every lemma or proof device advertised as new, compare its exact assumptions and conclusion with the closest canonical theorem; correctness and proof-technique novelty are separate questions.
- For weighted or transformed norms, rewrite the operator as a conjugated matrix and test a noncommuting `2×2` example. Do not infer singular-value or spectral-norm equality from non-orthogonal similarity, which preserves eigenvalues but not generally singular values.
- Maintain a **complexity-dependency ledger** for every advertised rate: expand dimensions, state/action cardinalities, horizon, coverage/eigenvalue constants, baseline gaps, smoothness constants, and oracle costs. Instantiate these quantities in common tabular, linear, and no-context special cases before judging an improvement.

#### Pass 3: Algorithm-to-implementation bridge

- Write the theoretical algorithm and practical implementation side by side.
- Write the feasible sets side by side as well. If a joint parametric uncertainty set is implemented using coordinatewise bounds, a rectangular kernel set, a surrogate LP, or a sampled scenario set, prove feasible-set equivalence or label the implementation a relaxation and analyze the policy actually computed.
- Check algebra after every approximation, rescaling, clipping, prediction, expectation, and nonlinear transformation.
- Track units of dual variables and hyperparameters.
- Ask whether learned scores preserve the ordering or performance property on which the theorem relies.
- Require a bridge: robustness theorem, approximation bound, exact-small-instance validation, or appropriately narrowed claims.
- Trace the full **estimate → compute → act → observe → update** pipeline. A policy with a concise online index can still be infeasible because its transition model, belief state, or dual price cannot be estimated under intervention.

#### Pass 4: Counterexample and limiting-case engine

For every central formula or interpretation, choose several high-yield tests from the menu below; do not force low-value tests merely to meet a count:

- zero, infinity, scarce capacity, abundant capacity, one state, one job, or deterministic transitions;
- two jobs differing in only one primitive;
- heterogeneous scaling of a probability, cost, or service time;
- swap order of expectation and a nonlinear map;
- a state or outcome with zero probability/cost despite a strict-positivity assumption;
- smallest instance with a computable optimal policy;
- an adversarial but allowed instance;
- dimensional analysis and monotonicity.

The goal is not to manufacture pathology. A useful counterexample isolates the precise claim that fails and suggests the minimum repair.

#### Pass 5: Computational and empirical evidence

Use `references/empirical-and-managerial-audit.md`.

- Decide whether experiments test correctness, mechanism, robustness, scalability, or external validity; one design rarely establishes all five.
- Demand an oracle or exact-small-instance benchmark when computationally possible.
- Audit baseline strength, tuning parity, ablations, leakage, censoring, selection, common random numbers, repeated runs, uncertainty intervals, and code/data availability.
- For logged sequential decisions, distinguish the level that was randomized from the action being evaluated. A predictive model for `outcome | history, action` does not identify unobserved action outcomes without an explicit causal estimand, consistency, sequential exchangeability, positivity/overlap, and a defensible off-policy or g-formula design.
- When a static dataset is used as an online environment, disclose the simulator, episode reuse, policy-dependent outcome generation, and train/validation/test separation. If the same fitted model constructs counterfactuals, chooses the policy, and evaluates it, label the evidence model-based or semi-synthetic and test against an independent evaluation mechanism.
- Specifically test policy-induced censoring: service, removal, admission, or treatment may erase the counterfactual trajectory needed to estimate the policy's inputs.
- Ask whether gains come from the claimed mechanism or from clipping, regularization, extra features, extra information, or unequal tuning.
- Examine metric construction, interpolation, denominator instability, and whether labels such as “hours,” “real data,” or “savings” match what was measured.
- Run table invariants before interpreting results: subgroup counts must sum to declared totals, overall means must be feasible weighted averages of exhaustive subgroup means, percentages must reveal compatible denominators, and policy comparisons must use a common evaluation cohort unless selection is itself the estimand.
- Check that empirical violation counts implement the same random variable and aggregation as the theoretical constraint; an episode-level threshold crossing does not automatically estimate expected constraint regret or patient-level safety.
- When simulations are calibrated from data, verify that the generator preserves the joint dependence that determines decisions. Matching marginal distributions is insufficient when coavailability, correlation, clustering, or temporal dependence determines the feasible frontier.
- Audit synthetic-instance generators algebraically before interpreting results. Verify symmetry, positive definiteness, normalization, support, conservation, and any other formal property claimed by the model; use the smallest symbolic or numeric counterexample when a transformation such as row scaling, elementwise absolute value, projection, or normalization may destroy the property. Report seeds, valid-instance rejection rules, solver status/gaps, and whether the tested dimension matches the motivating scale.
- For fairness, equity, access, or welfare objectives, audit six axes explicitly: unit and horizon; absolute outcome level; group weighting; order of aggregation and nonlinear evaluation; gaming or leveling down; and operational measurability/actionability.

#### Pass 6: Contribution and literature position

- Identify the closest paper by problem, method, and result—not merely the citations emphasized by the authors.
- Search through distinct vocabularies when applicable: the authors' construct name, the mathematical control structure, the information structure, and the proof engine. Skip a genuinely inapplicable route and add manuscript-specific vocabulary. For example, an “uncertain cost” model may also be a retirement game or a latent type revealed over time.
- Expand the mathematical search into adjacent field vocabulary. For decaying or recovering action-history states, for example, test terms such as history-dependent, recovering, rebounding, rotting, rested/restless, habituation, and reference-state control; for restricted schedules, search pulsing, cyclic control, renewal, and periodic assortment. Treat these as routing cues, not predetermined ancestors.
- Decompose novelty into model, algorithm, theorem/proof technique, empirical design, data, and managerial insight.
- Verify novelty claims against primary sources; do not rely on snippets or secondary summaries.
- Ask whether the contribution remains publishable if all results are correct.
- Reduce the model to its classical special cases and state exactly what, if anything, remains new there. Use the result to scope the contribution, not to demand novelty in every special case.
- Normalize rate comparisons before accepting a better exponent or multiplicative factor: impose common assumptions, substitute hidden dimensions and state expansions, include oracle/coverage requirements, and identify the exact proof operation responsible for the claimed gain.
- Decompose each headline contribution into `known engine → model-specific obstacle → new technical step → resulting delta`. A novel combination can be valuable, but it should not be presented as a new proof method unless the delta is explicit.
- Do not require the paper to solve a different problem; require it to justify why its chosen abstraction changes knowledge.

#### Pass 7: Managerial and external-validity chain

- State the decision insight without notation.
- Identify which assumption generates it and whether the evidence varies that mechanism.
- Compare the modeled mechanism with plausible competing first-order mechanisms in the application; require evidence or narrower positioning rather than an unlimited model extension.
- Walk the operational-causality and lever chain from harm to modeled action. Escalate when the model optimizes a downstream tactical lever but the manuscript provides no evidence that it materially changes the upstream-generated harm.
- Use the feature-budget matrix to detect misplaced analytical effort: omitted mechanisms with stronger magnitude evidence should be justified, bounded, or reflected in narrower claims before secondary mechanisms receive elaborate optimization.
- Separate illustrative simulation performance from causal, field, or platform-level impact.
- Audit representativeness, operational constraints, deployment inputs, and extrapolation.
- Require claim labels to match evidence: synthetic, semi-synthetic, observational, field, or production.
- Whenever the paper optimizes a fixed-frequency, fixed-fraction, threshold, cyclic, index, or other simple policy while also defining a less restricted optimum, run a **restricted-policy value test**. Compare exact small instances, derive a bound, or state clearly that the contribution is conditional design within an institutionally preferred class. Practical simplicity can justify the class, but it cannot silently convert restricted optimality into optimal scheduling guidance.
- For every prescription that positions, assigns, or swaps product roles, verify that the counterfactual is within the stated decision maker's authority and has a concrete real example. Otherwise separate a mathematical ranking from an actionable managerial decision.

#### Pass 8: Editorial architecture and field semantics

- Check whether title-level terms have the intended meaning in adjacent OR/MS subfields and whether a qualifier is needed.
- Test whether the title, abstract, contribution list, and closest-literature section describe the same claim to fame.
- Judge contribution relative to length; identify results, proof details, simulations, and citations that obscure the central path.
- Distinguish publication-path architecture from copyediting. Promote only issues that affect fit, interpretation, or whether a revision can converge.
- When managerial insight relies on an algebraic decomposition, trace each labeled effect from the primitive period-by-period quantities through every regrouping. Confirm that labels such as expansion, substitution, ripple, spillover, or welfare channel remain invariant to the algebra; a correct total expression can still support a misleading mechanism story.
- Revisit the paper-identity fork after the detailed audit. Check whether section order, main-text evidence, and conclusion are organized around the component that actually survives—decision support, structural insight, or empirical validation.

### Phase D — Verify, merge, and promote the idea board

Maintain a **publishable-asset ledger** in parallel with the issue ledger. For each candidate asset, record the result or design, why the object is first-order, what was predictable beforehand, the surviving non-obvious delta, evidence of rigorous execution, the decision/belief consequence, and its scope. Do not let a longer defect ledger erase a shorter but decisive positive asset.

Use the two-stage funnel in `references/idea-generation-and-promotion.md`. Preserve the broad candidate slate first; then form the report slate from candidates with sufficient manuscript-specific support and material editorial consequence. Keep potential importance separate from evidentiary strength: a potentially controlling but weakly supported idea belongs in the verification queue, not in the major-comment list or recommendation.

For each candidate that survives the initial sweep, record:

| Field | Requirement |
|---|---|
| MEI role | Motivation, Execution, Insight, or cross-cutting |
| Paper-level gate | Motivation, formulation/lever, novelty, credibility, insight, or claim calibration |
| Claim at risk | Quote or faithful paraphrase of the manuscript claim |
| Necessary subclaim | What must be true for the paper-level claim to hold |
| Location | Section, equation, theorem, figure, table, or page |
| Evidence and operation | Manuscript anchor plus comparator, counterfactual, derivation, or evidence trace |
| Current diagnosis | What appears supported, inconsistent, unsupported, or worth testing; distinguish a verified defect from a question |
| Consequence if sustained | What changes in correctness, novelty, interpretation, implementability, insight, or publication path |
| Minimum response | Smallest adequate repair, clarification, verification, or claim contraction |
| Potential importance | P0 controlling, P1 major, P2 secondary, or unclear if sustained |
| Evidence status and confidence | Verified, strongly supported, plausible route, open question, or withdrawn, with reason |
| Disconfirmation | What evidence would make the concern disappear |
| Evidence role | Decisive, corroborating, illustrative, or secondary consequence |
| Repair scope | Local, section-level, or paper-spine-level |
| Final disposition | Promote, supporting, hold, or retire; map stable idea IDs to report IDs when promoted |

Promote an issue to **major** only when it threatens a headline claim, theorem, contribution, identification, practical bridge, strongest insight, or decision recommendation and the evidence supports that wording. Combine symptoms that share one root cause. Keep the final major list small enough that an editor can see the publication path, but never fill a quota. Show the user the strongest reserve ideas rather than silently deleting them.

Use “fatal,” “invalid,” or equivalent language only after verification shows that a necessary headline subclaim fails and no plausible local or section-level repair preserves the core contribution. Missing explanation, external-practice intuition, or a low-confidence concern cannot by itself control the recommendation. Motivation and insight concerns may have P0 potential when a clear rival object or counterfactual makes the publication consequence important, but an unresolved premise remains **Hold** and cannot control the recommendation until the evidence is sufficient. Frame the needed evidence honestly rather than calling it a hard error.

Map every promoted issue back to one of the six paper-level dimensions. When several technical findings share an upper-level implication, synthesize them into one spine-level comment—for example, hidden dimensions plus unmatched assumptions may jointly show that result novelty is unestablished. Recompute the overall assessment card after this clustering.

Also run the bridge bottom-up: every promoted detailed issue must state which necessary subclaim it threatens, why that changes the overall assessment, and whether its repair preserves the paper's contribution identity. Demote technically correct observations that have no material upper-level consequence.

Use the sharpness questions during promotion:

1. Is the target claim important?
2. Is the evidence manuscript-specific and checkable?
3. Does the consequence change what readers or editors should believe?
4. Is there a concrete repair or a reason no repair is plausible?
5. Could the authors answer it without guessing what the reviewer means?

Treat these as judgment prompts, not a numeric score. Promote a candidate only when its importance, manuscript-specific support, and consequence are jointly strong enough. Route high-importance but under-verified ideas to **Hold**, and merge as support, reframe, demote, or retire the rest. An issue generated but left in reserve is a promotion outcome, not a discovery failure.

### Phase E — Sharp-comments checkpoint

Use `assets/sharp-comments-checkpoint.md`. Return:

- a neutral contribution summary;
- the frozen pre-audit editorial sheet, visibly separated from post-audit adjudication;
- the seven-sentence editorial-first memo, including the first-order-object judgment and pre-result baseline;
- the six-dimension paper-level assessment and provisional journal-level judgment;
- a short result-to-insight ledger for the claimed publication asset;
- the strongest publishable asset, conditional editorial-merit bottleneck, credibility bottleneck, which one controls, and repairability of the paper spine;
- the high-recall idea board with visible dispositions;
- a ranked, sufficiently supported retained set of major comments—usually a handful and sometimes only one or two; never fill a quota;
- each retained comment in **claim → evidence and status → consequence if sustained → proportionate repair or verification request** form;
- a compact reserve list of high-potential verification routes and lower-priority concerns;
- verification limits and confidence;
- a provisional recommendation.

The high-recall idea board and promotion board are required checkpoint artifacts. Do not replace them with only the retained major comments, even when the user requests a concise checkpoint; compress their wording instead.

Then complete the **approval card / proposed report plan** in `assets/sharp-comments-checkpoint.md`. Present that compact card first in the user-facing response; place the longer technical checkpoint after it as supporting detail when useful. Do not make the user design the report from scratch. Every card field must contain one recommended value, `none`, or `blocking—confirmation deferred`. Recommend:

- the report role, defaulting to referee rather than AE;
- language, approximate length, delivery format, and one of the standard, concise, issue-led, or dimension-led structures;
- a two- or three-sentence opening thesis containing the strongest asset, best-supported central reservation—or leading unresolved question when a blocking check remains—and revision scope;
- the retained major-comment IDs, final diagnostic titles, order, manuscript anchors, and exact author-facing request or decision-relevant question;
- which reserve and secondary ideas survive and which candidates should be merged, demoted, tested, or dropped;
- the journal-specific decision, repair posture, and whether the recommendation should appear in the author-facing text, only in the submission form, or in a separate confidential note;
- any unresolved factual or technical check that must be completed before prose drafting.

Only sufficiently supported concerns enter the ranked major list. Unresolved high-potential candidates appear under reserve or blocking/nonblocking checks and are framed as questions or verification routes, not established defects. The user should be able to approve the plan by replying only “confirm” or “按这个写,” or to request changes by comment ID or field name. Then stop. If the user asks to test, deepen, merge, reorder, promote, or remove an idea, return to the relevant audit, issue a revised card, and stop again. If a blocking check remains, confirmation authorizes the check but not prose drafting; clear the blocker first and reconfirm only if its result materially changes the thesis, issue set, or recommendation. Do not pad the list with copyediting, and do not treat silence as approval.

### Phase F — Full referee report

Proceed only after confirmation. Use `assets/full-referee-report.md` and `references/journal-and-decision-calibration.md`.

- Lock the confirmed substantive idea set. Do not add a new major objection while polishing; if new evidence materially changes the report, return to Phase E and reconfirm.
- Translate the internal ledger into author-facing prose. Merge details by root cause and suppress internal labels such as paper-level gate, necessary subclaim, severity, confidence, evidence role, repair scope, and disconfirmation status.
- Default to the **standard** structure: manuscript title/ID, Summary, Overall Evaluation, numbered Major Comments, optional Other/Minor Comments, optional Conclusion, and References only when external work is actually cited. Use the concise, issue-led, or dimension-led variant when it better matches the confirmed plan or a supplied example.
- Use the Summary to reconstruct the question, model or design, main results, and evidence accurately, emphasizing facts needed for the later assessment rather than copying the abstract.
- In Overall Evaluation, identify the strongest asset first, then state one central reservation and its journal-level consequence. Include an explicit recommendation only if its visibility was confirmed.
- Give each major comment a conclusion-bearing title. In two to five connected paragraphs, move from manuscript-specific anchor to comparator, counterfactual, or derivation; explain the upper-level consequence; and make a proportionate request. A spine-level rejection comment need not pretend to have a local repair, but it should state what evidence, result, or repositioning could change the assessment when that is scientifically plausible.
- Order comments by editorial importance, not manuscript order. Retain only the supported nonredundant set—usually a handful and sometimes only one or two; do not split one root problem into several repetitive comments or fill a quota.
- Keep Other/Minor Comments short. Use a Conclusion only to synthesize the strongest asset, decisive bottleneck, and revision path; never introduce a new objection there.
- Separate comments to authors from confidential comments to the editor when requested. Do not imitate an AE synthesis unless the confirmed role is AE.
- State verification limits in a natural sentence only when they materially affect interpretation; do not force a standalone audit-style section.
- Verify external factual or industry-practice claims before letting them carry a major judgment. If verification is unavailable, qualify the claim and frame the point as a question or requested evidence.
- Match the user's language unless the journal report must be in English.
- If the user requests a DOCX or PDF artifact, use the applicable document workflow, preserve a restrained academic layout, and visually inspect every rendered page before delivery.

### Phase G — Learn from example reports

Use `references/calibration-learning.md` and `assets/calibration-case-template.md`.

1. Freeze and hash the blind checkpoint.
2. Open authorized truth sources only after the gate is satisfied.
3. Before merging comments, reconstruct each reviewer's positive prior, publication thesis, comparison/counterfactual operation, strongest asset, repair logic, and recommendation. Preserve distinct reviewer lenses and only then inspect AE/DE synthesis.
4. Build a candidate-idea pool from blind and observed sources. Normalize by underlying object, evidence, reasoning, consequence, and repair—not shared words—and independently adjudicate each idea against the manuscript.
5. Treat source relation, validity, importance, and priority as separate fields. Absence from an observed report is not negative evidence; presence is not proof of validity or importance.
6. Evaluate **important-idea coverage** and **promotion**: did the blind process generate each supported consequential idea, and did it place a defensible set of the most important ideas near the top?
7. Preserve blind-only `NOVEL–VALID` ideas and defensible alternative publication theses. Do not force them to match the observed reviewer's route.
8. Audit unsupported high-severity claims separately. A fatal false positive is an unsupported claim promoted into the controlling set that changes the recommendation, demands major reconstruction, or displaces a supported priority.
9. Independently audit the observed comment's facts and derivation before learning from it; preserve disputed or erroneous reviewer reasoning.
10. Record editor adoption separately as auxiliary priority evidence: must-have, acknowledge/repair, optional, or not adopted. Do not count comments as votes.
11. Diagnose only material calibration failures: an important supported idea not generated, an idea generated but not promoted, or an unsupported major/fatal claim. Do not treat every observed-only minor comment as a failure.
12. Compare problem importance, first-order object, execution quality, strongest asset, expected-versus-consequential insight, decisive bottleneck, and repair scope. Recommendation and exact issue overlap are secondary diagnostics.
13. Update a reusable trigger, test, promotion rule, or safety guard—not a case-specific answer—and re-run it on a later sealed example before promoting it to the core skill.

## Output quality rules

- Be skeptical without being performatively harsh.
- Use high recall during discovery and high selectivity in the final report. Do not confuse a broad idea board with a long author-facing comment list.
- Prefer one decisive derivation or counterexample to several vague concerns.
- Distinguish correctness from importance and repairability from severity.
- Apply evidentiary strictness in proportion to the claim: verify fatal defects; frame consequential but unresolved motivation or insight concerns conditionally.
- Do not invent citations, page references, proof defects, data facts, or journal rules.
- Cite public web claims with direct primary-source links.
- Keep confidential file names and contents out of outputs unless authorized and necessary.
- A recommendation must follow from the ranked issues; it must not be chosen first and rationalized afterward.
- The final author-facing report must read as a coherent referee letter, not as an issue ledger, scorecard, diagnostic table, or transcript of the review process.
- Use specific, calibrated first-person judgment. Pair criticism with accurate reconstruction and concrete evidence; do not dilute a decisive paper-level concern with performative harshness or a long list of trivial edits.

## Reference routing

- Read `references/confidentiality-and-source-control.md` for every new manuscript or calibration case.
- Read `references/overall-editorial-assessment.md` before detailed discovery passes and again when synthesizing the recommendation.
- Read `references/editorial-threshold-reasoning.md` before reading result derivations deeply and again when calibrating against editor/referee judgments.
- Read `references/editorial-evidence-bridge.md` when converting paper-level claims into audit targets and when clustering detailed findings into major comments.
- Read `references/idea-generation-and-promotion.md` for every blind review and whenever generating, verifying, or ranking the sharp-idea board.
- Read `references/generalized-reasoning-examples.md` when discovery stalls, lacks MEI diversity, or remains trapped inside the manuscript's framing; use it as a selective anti-anchoring prompt, never as a mandatory checklist.
- Read `references/journal-and-decision-calibration.md` when judging fit or recommending a decision.
- Read `references/analytical-and-algorithmic-audit.md` for analytical, optimization, queueing, stochastic-control, or algorithmic papers.
- Read `references/empirical-and-managerial-audit.md` for experiments, simulations, data applications, or managerial claims.
- Read `references/calibration-learning.md` when examples include reports, decisions, revisions, or responses.
