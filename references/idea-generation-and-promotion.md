# Sharp-Idea Generation and Promotion

## Contents

1. Build a high-recall idea board
2. Promote by importance and evidence
3. Apply root-control and promotion guardrails
4. Present the confirmation checkpoint
5. Calibrate discovery and promotion

## Purpose

Separate two different review abilities:

1. **Discovery:** generate a broad but bounded set of manuscript-specific ideas that could materially change the Motivation–Execution–Insight assessment.
2. **Promotion:** select the few ideas that most strongly control the paper's contribution, credibility, or publication path.

Do not optimize discovery for exact agreement with a historical reviewer. A sound alternative objection, counterfactual, comparator, or positive insight is valuable even when no observed report contains it. Apply strictness primarily to evidentiary claims—especially alleged fatal errors—not to whether an idea follows the same route as another reviewer.

## Stage 1 — Build a high-recall sharp-idea board

After freezing the pre-result prior and completing the first full read, generate candidates before deciding what the final report will contain. Keep every genuinely distinct, manuscript-specific route and stop when further candidates are duplicative or immaterial; do not target a count.

Candidates may be:

- a negative diagnosis;
- a positive publishable asset;
- a comparator or literature route requiring verification;
- a counterfactual that could change first-order status;
- a technical or empirical falsification test;
- a conditional question whose answer would change the assessment.

Seek coverage across the dependent MEI chain:

- **Motivation:** consequential stake, first-order object, cause–lever link, rival object, closest prior capability, unresolved gap.
- **Execution:** formulation, assumptions, proof, algorithm, computation, identification, data, evidence, and claim fidelity.
- **Insight:** pre-result baseline, surviving non-obvious delta, mechanism, regime boundary, decision/belief change, strongest asset.

Also include at least one candidate about the paper's positive core and repair path. These are coverage prompts, not mandatory criticisms.

Maintain a **publishable-asset ledger** beside the issue board. For each serious positive candidate, record the result or design, why the object is first-order or appropriately scoped, what was predictable beforehand, the surviving non-obvious delta, execution evidence, the decision or belief consequence, and its boundary. Do not let a longer defect list erase a shorter but decisive positive asset.

For each candidate, keep the smallest trace that preserves the idea and why it matters:

| Field | Requirement |
|---|---|
| ID, thesis, and MEI role | State the possible paper-level point in one sentence and its route |
| Trigger, anchor, and operation | Manuscript cue/location plus comparator, counterfactual, derivation, boundary test, or evidence trace |
| Potential consequence | What readers, editors, or decision makers would believe differently if sustained |
| Evidence and next step | Verified/supported/question/withdrawn plus the one check that could resolve it |
| Dependency/status | Root, independent, contingent, symptom, duplicate, conflict; candidate/support/hold/withdraw |

Add disconfirmation, repair scope, confidence, stance, or fuller claim decomposition only for candidates whose promotion or wording is genuinely uncertain. The board is a memory and comparison device, not a form-completion target.

Do not discard a candidate merely because:

- it differs from the manuscript's framing;
- it was absent from an observed referee report;
- it is not yet a polished author request;
- another candidate currently seems more serious.

Withdraw or demote it when the manuscript supplies disconfirming evidence, the demand changes the research question unfairly, or the paper-level consequence is immaterial.

## Stage 2 — Promote by importance, not by comment count

Promotion is a comparative judgment. For every serious candidate ask:

1. **Centrality:** Does it affect the title-level claim, first-order object, claim to fame, strongest theorem, primary evidence, or strongest insight?
2. **Counterfactual power:** If resolved in the paper's favor, would the overall assessment change? If ignored, could the main conclusion remain intact?
3. **Evidence strength:** Is there enough manuscript-specific support for the proposed wording and severity?
4. **Distinctiveness:** Does it add a different root diagnosis, or merely repeat another issue's symptoms?
5. **Editorial consequence:** Does it change contribution, credibility, interpretation, recommendation, or repair scope?
6. **Repair consequence:** Can the concern be answered locally, by bounded repositioning or extension, or only by replacing the paper spine?
7. **Answerability:** Could the authors identify the required evidence, comparison, derivation, or claim change without guessing what the reviewer means?

Keep three judgments orthogonal.

### Importance class

- **P0 — controlling:** changes the paper's first-order status, claim to fame, strongest asset, credibility of the central result, or feasible publication identity.
- **P1 — major:** materially changes a central claim or evidence route but does not alone determine the paper's identity.
- **P2 — useful secondary:** worth the authors' effort but not central to the recommendation.

### Evidence verdict

- **Sufficient:** supports the proposed wording and importance.
- **Targeted check needed:** potentially consequential, but a specific literature, proof, data, or institutional check remains.
- **Insufficient:** cannot presently support an author-facing conclusion.

### Final disposition

- **Promote:** include in the retained report slate.
- **Supporting:** merge beneath a promoted root issue or keep as a secondary comment.
- **Hold:** keep visibly in the reserve/verification queue; it cannot control the recommendation yet.
- **Retire:** resolved, duplicative, immaterial, or unfair.

Do not compute a mechanical score or require a fixed number in each class. A candidate may have **P0 potential** but remain **Hold** because its evidence needs a targeted check. Recommend the smallest nonredundant, sufficiently supported P0/P1 set that explains the publication path, while showing the user the strongest held and supporting ideas so that a valid alternative route is not silently lost.

Stop deepening the board once the MEI judgments, strongest asset, controlling root(s), important alternatives, and realistic repair path are supported. Run another diagnostic only if it could change verification, promotion, report order, recommendation, or the requested repair.

Before ordering, distinguish:

- **root:** creates or controls other concerns and determines paper identity or repair scope;
- **independent branch:** remains consequential after the root is repaired;
- **contingent branch:** matters only if the current paper spine is retained;
- **symptom/evidence:** helps establish another diagnosis but should not become its own major comment.

The first major comment should normally instantiate the controlling root named in the overall thesis. Depart from that order only when an independent issue more directly invalidates the central contribution.

### Promotion guardrails

- A high-confidence **fatal correctness or identification claim** requires a verified derivation, counterexample, contradiction, or design failure. Otherwise phrase it as a question or verification route.
- A **Motivation or Insight judgment** may be important before it is mathematically falsified. State the rival object, counterfactual, missing evidence, and conditional consequence rather than pretending it is a hard error.
- A detailed flaw does not automatically control the recommendation. Rank importance separately from evidentiary certainty and rerun the paper-identity deletion test: if correcting or deleting the affected route leaves the strongest asset intact, the flaw may be major without controlling the paper.
- Do not let a verified error in a secondary application, heuristic, or experiment displace an unresolved first-order or ancestry question about the primary contribution. Conversely, do not demote a verified bridge error when the paper explicitly makes that bridge indispensable to its claim to fame.
- A precise equivalence, subsumption, or matched-result question may be promoted when manuscript-internal mapping shows that the answer changes contribution identity, even if external priority cannot yet be verified. Phrase the author burden accurately; do not assert that the result is known.
- For a title-level **first-order application claim**, a concrete rival cause or lever plus the manuscript's lack of comparative institutional, empirical, or counterfactual evidence can support the conclusion that first-order status is **not established**. Do not claim that the rival dominates without evidence. Name the comparison that could decide the issue and the narrower conditional or theoretical contribution that would survive.
- When a theorem or algorithm carries the publication case, perform one exact comparison with the closest canonical object or cited predecessor. Match state, action, information, assumptions, policy class, oracle, complexity measure, and guarantee or rate as applicable; then isolate `inherited engine -> new obstacle -> resolving step -> consequential delta`. If external priority remains unresolved, promote a precise author-facing comparison question rather than guessing.
- For a normative penalty or constraint, test the premise that the baseline system actually generates the motivating harm and identify the omitted cost, constraint, upstream decision, behavior, or objective conflict responsible. Promote the point only when this premise affects the need for, interpretation of, or policy induced by the intervention.
- An issue that was generated but left in reserve is a **promotion problem**, not a discovery failure. Record the distinction.
- Preserve alternative valid comments. Historical reviewer agreement is evidence of relevance, not the definition of relevance.

## Stage 3 — Present ideas for user confirmation

At the sharp-comments checkpoint, present:

1. the recommended, sufficiently supported P0/P1 idea set in report order;
2. a compact reserve list of held or supporting ideas that the user may test, merge, promote after verification, or drop;
3. the strongest positive asset and the proposed overall thesis;
4. unresolved checks whose result could change the ranking;
5. the proposed report format and recommendation posture.

The checkpoint should make clear what the reviewer thought of, not merely what survived into the final retained comments. After the user confirms the idea set, draft the full report from that substantive lock.

Keep candidate IDs stable. When an idea enters the report, record the mapping, for example `I4 → M1`; do not silently renumber ideas in a way that hides their discovery or promotion history.

## Calibration target

When an observed report later becomes available, use it to ask:

- Did the blind process generate the important underlying idea, even through a different valid route?
- If generated, was it promoted appropriately?
- Did the blind process produce additional well-supported and decision-relevant ideas?
- Did it make any unsupported high-severity claim?
- Did its top ideas identify the paper's strongest asset, controlling bottleneck, and realistic repair path?

Do not require exact wording, complete reviewer-comment coverage, or identical recommendation labels. Missing a sound controlling issue matters; missing a minor stylistic request generally does not. A different but better-supported top issue may improve the review rather than reduce its quality.
