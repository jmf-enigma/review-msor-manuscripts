# Synthetic Mini-Review: From Sharp Idea to Report Prose

> **Provenance and scope:** This is a fully synthetic teaching illustration,
> constructed for this repository and not knowingly adapted from any specific
> real manuscript, referee report, decision letter, or submission. Its setting
> uses generic operations-research primitives only.

This example is deliberately compact. It illustrates how the Skill can identify
one potentially controlling issue, calibrate its evidence status, stop for human
confirmation, and then translate the confirmed idea into natural referee prose.
It is not a complete review and is not an evaluation answer key.

## Fictional manuscript snapshot

**Invented title:** *Pooling Before Production: Flexible Capacity and Inventory
Hedging in a Two-Factory Network*

The fictional paper studies two factories serving distinct regional markets.
Each factory positions inventory before final demand is realized. A flexible
production line can subsequently allocate capacity across the two products after
observing regional demand signals; dedicated lines cannot switch products.

The manuscript derives a low-dimensional state-dependent allocation rule by
decomposing its action into an inventory-hedging term and a post-signal
reallocation term. In a large-market sequence indexed by `n`, let `C_F^*(n)` and
`C_D^*(n)` be the optimal expected costs under the manuscript's respective
flexible- and dedicated-system specifications. Those specifications have not yet
been normalized to a common information and decision structure. For two proposed
policies, the manuscript reports the approximation gaps
`G_F(n) = C_F(pi_F,n) - C_F^*(n) = O(1)` and
`G_D(n) = C_D(pi_D,n) - C_D^*(n) = Theta(sqrt(n))`.

The two systems use the same demand and cost scaling and the same total nominal
capacity. However, `pi_F` observes both regional signals before allocating the
shared line and conditions jointly on both inventories, whereas `pi_D` uses
separable base-stock decisions fixed before those signals. The manuscript
interprets the difference between `G_F` and `G_D` as evidence that physical
flexibility, interacting with inventory hedging, changes the cost-gap rate.

For the illustration, assume the mathematical statements have not yet been
independently verified. The issue below concerns what the stated comparison can
establish even if both rate calculations are correct.

## Stage 1 — Proposed review plan

### Contribution capsule

The paper develops a tractable policy for coordinating inventory and a shared
flexible production line in a two-factory stochastic network, derives its
large-market performance, and argues that flexibility changes the relevant
cost-gap rate relative to dedicated production.

### Strongest asset

The structural decomposition behind the state-dependent allocation rule appears
to be the paper's strongest asset. It may offer a useful analytical description
of how pre-positioned inventory and ex-post capacity allocation interact, even if
the broader mechanism claim must be narrowed.

### Overall thesis

The manuscript may contain a publishable analytical core, but its headline
interpretation is not yet supported by a mechanism-isolating comparison. The
current evidence does not establish that capacity flexibility—rather than the
richer information and recourse embedded in the flexible policy—is what changes
the asymptotic rate. This is a potentially central but plausibly repairable issue.

**Provisional revision scope.** This would require a substantial analytical
revision rather than a cosmetic robustness check. The exact recommendation label
should depend on the target journal and the rest of the manuscript audit; the
fictional excerpt alone is not enough to determine it.

### Motivation–Execution–Insight and first-order assessment

- **Motivation.** Coordinating capacity and inventory under uncertain regional
  demand is plausibly consequential, but the snapshot does not establish the
  operational stakes or rank cross-product flexibility against rival levers such
  as forecast quality, permanent capacity, or emergency sourcing.
- **Execution.** Even taking the two stated rates as correct, the comparison
  changes the system optimum, information set, decision timing, and policy
  construction together. It therefore cannot isolate the mechanism claimed in
  the interpretation.
- **Insight.** The inventory/reallocation decomposition may remain a useful
  structural insight. What remains unresolved is whether physical flexibility
  changes the scaling, or whether the contrast is driven by richer adaptation.
- **First-order object.** For the headline theoretical claim, the candidate
  first-order object is the cross-product feasibility constraint. Its strongest
  rival explanation is the value of post-signal information and a richer feedback
  policy. A matched comparison is needed to separate them.

### M1 — Match the comparison before attributing the rate gain

**Claim under review.** The improvement from `Theta(sqrt(n))` to `O(1)` is caused
by the interaction of flexible capacity and inventory hedging.

**Evidence and test.** The two reported quantities are approximation gaps to two
different system optima, not a matched measure of the economic value of
flexibility. Moreover, `pi_F` uses joint post-signal feedback while `pi_D` is a
separable pre-signal rule. The comparison therefore changes physical feasibility,
information, decision timing, and policy construction together. A contrast
between `G_F` and `G_D` cannot by itself isolate the effect of flexibility.

**Evidence status: not established, not false.** This observation does not show
that flexibility fails to generate the claimed rate gain. It shows that the
present benchmark cannot distinguish that mechanism from the value of additional
information or recourse. If a matched comparison preserves the rate separation,
the manuscript's interpretation would be materially strengthened.

**Publication consequence.** Because the mechanism attribution carries the
paper's claimed insight, this is more than a request for an extra robustness
check. Without parity, readers cannot tell whether the main result is about
flexible capacity, adaptive information, a larger policy class, or their joint
effect. The structural policy result may survive, but the claim to fame and its
position relative to the closest literature remain uncertain.

**Proportionate author request.** First separate policy approximation quality
within each manuscript-specified system from the economic value of flexibility.
For the latter, construct matched optima `C_tilde_D^*(n)` and
`C_tilde_F^*(n)` over the same demand process, cost and capacity scaling,
filtration, decision epochs, and class of state-feedback mappings. The dedicated
feasible-action set should be nested in the flexible set, with cross-product
switching as the only added action. Then measure the value
`C_tilde_D^*(n) - C_tilde_F^*(n)` and identify which analytical term changes the
scaling. If this normalization is infeasible, state the result as a joint value
of flexibility and post-signal adaptation and narrow the abstract, introduction,
and managerial claims.

**Disconfirmation route.** Demote or withdraw M1 if the manuscript already
contains a same-information, same-timing dedicated comparator, distinguishes
approximation gaps from the value of flexibility, and measures both systems under
the same demand, cost, capacity, and policy scaling. In that
case, the review should instead verify the derivation and assess whether the rate
separation is novel relative to the closest matched literature.

### Confirmation gate

At this point the Skill should stop. A concise handoff to the reviewer could be:

> I propose retaining M1 as the controlling major comment, with the status
> **not established** rather than **false**. The structural decomposition remains
> the strongest asset, and the requested response is a matched
> information/recourse comparison or a narrower joint-mechanism claim. Shall I
> draft the report on that basis, or would you like me to test, narrow, or reorder
> M1 first?

No polished referee report should be generated until the reviewer confirms or
revises this substantive plan.

## Stage 2 — Illustrative prose after confirmation

Assume the reviewer replies: `Confirm M1 and keep the structural asset visible.`
Only then might the corresponding passage read:

> The paper's most promising contribution is the structural decomposition behind
> the proposed state-dependent allocation rule. It gives a clear analytical account
> of how pre-positioned inventory can be coordinated with ex-post production, and
> that result may remain valuable even under a narrower interpretation of the
> application.
>
> My central concern is that the current comparison does not yet establish the
> mechanism to which the paper attributes its rate improvement. The flexible
> policy allocates capacity after observing both regional signals and conditions
> jointly on the inventory state, whereas the dedicated benchmark is restricted to
> separable decisions made before those signals. Thus the reported `O(1)` versus
> `Theta(sqrt(n))` contrast compares approximation gaps to different system
> optima while also varying physical feasibility, information, timing, and policy
> construction. I do not read this as evidence that the claimed flexibility
> effect is false; rather, the comparison presently provided does not isolate
> that attribution or measure the economic value of flexibility.
>
> I therefore encourage the authors to separate the approximation guarantee in
> each manuscript-specified system from a matched value of flexibility. Define
> `C_tilde_D^*(n)` and `C_tilde_F^*(n)` over the same demand, costs, normalized
> capacity, filtration, decision epochs, and feedback-policy architecture, with
> dedicated feasible actions nested in flexible feasible actions; then vary only
> cross-product switching. Showing which term changes the scaling of
> `C_tilde_D^*(n) - C_tilde_F^*(n)` would directly support the paper's
> interpretation.
> If such a result is unavailable, the theoretical contribution could still be
> meaningful, but the paper should present the finding as the joint value of
> flexibility and post-signal adaptation and calibrate its broader claims.

Notice what changes between the two stages: the internal fields and status labels
support the decision but disappear from the author-facing prose; the positive
asset remains visible; and the concern is expressed at exactly the strength the
fictional evidence warrants.
