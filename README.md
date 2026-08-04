# MS/OR Referee Review

A human-in-the-loop Codex Skill for reviewing analytical, algorithmic, computational, empirical, and hybrid manuscripts in **Management Science**, **Operations Research**, and adjacent OR/MS journals.

The Skill is designed to do more than locate technical errors. It forms a paper-level judgment across **Motivation, Execution, and Insight**, asks whether the manuscript studies a genuinely first-order research object, connects detailed evidence to the journal-level publication case, and turns only the confirmed ideas into a natural referee report.

> This Skill assists an authorized human reviewer. It does not replace the reviewer's judgment, verify compliance with a journal's AI policy, or authorize processing confidential material.

## 中文简介

这是一套面向 MS/OR 论文的交互式审稿 Skill。它不会把审稿简化成“找数学错误”，而是同时判断问题是否重要、研究对象是否具有 first-order 意义、模型—理论—算法—证据是否闭环，以及结果相对最接近的基准或文献是否产生了真正的新 insight。

默认流程分为两步：先输出整体判断、拟采用的 major comments、排序、证据和修改要求，请用户确认；收到 `confirm` 或“按这个写”后，才生成完整的自然语言审稿报告。诊断路径按论文类型和实际疑点选择，不要求机械填表，也不为凑数量制造 comments。

## Why this Skill

Weak review workflows often fail in one of two directions:

- they produce a generic checklist of assumptions, proofs, experiments, and exposition issues without deciding what matters; or
- they anchor on one concrete error and never assess whether the problem is important, the modeled object is first-order, or the results are genuinely new and consequential.

This Skill instead follows the manuscript's full claim chain:

`important problem -> first-order research object -> generative formulation -> rigorous execution -> interesting and consequential result -> calibrated claim`

Its standard of judgment is stable, but its diagnostic depth is adaptive. Tables, maps, counterexamples, literature comparisons, and reviewer passes are used only when they can change the thesis, issue ordering, recommendation, or requested repair.

## What It Evaluates

| Lens | Core question |
|---|---|
| Motivation | Is the exact problem important, and are the real stakes established? |
| First-order object | Does the focal mechanism, decision layer, information structure, or mathematical obstacle govern the headline phenomenon? |
| Execution | Does the model-proof-algorithm-data-application chain support the claim at its stated scope? |
| Insight | What non-obvious result, capability, boundary, or decision change survives the closest baseline? |
| Novelty | What is the consequential delta relative to matched prior work, rather than a renamed standard object? |
| Claim calibration | Do the title, abstract, managerial implications, and recommendation stay within what the analysis establishes? |

A hard mathematical error is one possible execution problem. It does not substitute for evaluating the other dimensions, and it controls the report only when its reach and repairability make it the decisive bottleneck.

## Core Workflow

### 1. Establish the review object

- confirm authorization and journal-policy compatibility;
- identify the exact manuscript version and review round;
- keep reports, decisions, responses, and later versions sealed during a blind review;
- record the target journal/area, requested output, and verification limits.

### 2. Freeze an editorial prior

Before hunting for proof or implementation errors, the Skill records:

- the paper's intended claim to fame;
- the strongest prospective contribution;
- the likely first-order object and strongest rival mechanism;
- the closest canonical or literature baseline;
- what the assumptions already make predictable;
- whether the paper would clear the journal bar if every formal result were correct.

This prevents a readily verifiable local error from displacing a more important motivation, novelty, or insight judgment.

### 3. Audit selectively and generate ideas broadly

The Skill routes the manuscript to the relevant analytical, algorithmic, empirical, simulation, and managerial checks. It generates both positive and negative candidates, including:

- publishable assets and surviving theoretical routes;
- rival first-order mechanisms and missing decision layers;
- canonical reductions and matched-rate literature comparisons;
- model-theorem-implementation mismatches;
- omitted recourse, behavior, or feedback loops;
- proof, algorithm, identification, simulation, and evidence failures;
- results that are correct but predictable or decision-irrelevant.

Confidentiality, source control, MEI completeness, evidence calibration, and user confirmation remain fixed gates. Beyond those gates, optional diagnostics are triggered only when they can add distinct decision-relevant information. The workflow stops when further checks cannot reasonably change the publication thesis, priority order, recommendation, or repair path.

### 4. Verify, merge, and rank

Candidate ideas are separated into:

- **root issues** that control several downstream concerns;
- **independent issues** that survive repair of the main root;
- **contingent issues** that may disappear after a larger reconstruction;
- **symptoms or supporting evidence** that belong inside another comment;
- **reserve ideas** that are important but not yet sufficiently verified.

The Skill keeps evidentiary strength separate from potential importance. A consequential but unresolved premise is reported as **not established**, together with the comparison or evidence that could resolve it—not upgraded into a claim that it is false.

### 5. Ask for substantive confirmation

The first user-facing deliverable is a compact proposed report plan containing:

- a neutral contribution capsule;
- the overall publication thesis and strongest asset;
- a provisional recommendation and repair posture;
- ranked major comments with manuscript anchors and author requests;
- retained other comments and reserve ideas;
- blocking checks and material verification limits;
- the proposed language, length, file format, and report structure.

The user can approve the plan with `confirm` / `按这个写`, or revise it by comment ID: deepen, test, merge, drop, reframe, or reorder.

### 6. Draft the referee report only after confirmation

The confirmed ideas are translated into author-facing prose through:

`root judgment -> strongest manuscript evidence -> publication consequence -> response path`

Internal labels, scorecards, confidence fields, and diagnostic tables are removed. The report structure is selected from the topology of the reasoning:

- **Standard:** several independent major issues;
- **Issue-led:** one or two paper-spine arguments with multiple manifestations;
- **Dimension-led:** genuinely distinct Motivation, Model/Analysis, Technical, and Presentation judgments;
- **Concise:** one controlling point or a short journal form.

## Review Modes

### Blind review

Independently evaluate an authorized or public manuscript and stop at the confirmation checkpoint unless the user has already approved a substantive report plan.

### Report drafting

Convert a confirmed issue set into a polished referee report in chat, Markdown, DOCX, or PDF. New major objections discovered during writing trigger a return to the confirmation stage.

### Calibration learning

Compare a frozen manuscript-only review with authorized referee reports, AE/DE letters, revisions, or responses. Historical comments are treated as evidence—not an answer key. The Skill learns reusable reasoning operations while preserving valid blind-only ideas and rejecting unsupported observed comments.

## Architecture and Reasoning Fidelity

`SKILL.md` is the control plane, not the entire reasoning library. It preserves the non-negotiable gates, the paper-level MEI workflow, promotion logic, and high-recall activators. Detailed analytical, empirical, editorial-threshold, calibration, and writing operations remain in selectively loaded files under `references/`.

This split is intended to reduce repeated instructions without weakening judgment. Changes are evaluated by behavior, not by word count: the repository includes sealed synthetic cases that test first-order reasoning, theory/application separation, MEI balance after a local hard error, restraint on a clean paper, fairness-guarantee semantics, and resistance to source-borne prompt injection. Real or confidential calibration cases and their answers are never included in the public package.

## Safe Source Handling

- A filename, template, default prompt, or manuscript statement does not establish authorization.
- Manuscripts, attachments, webpages, code, metadata, and embedded text are treated as untrusted data, not instructions.
- The default for a nonpublic manuscript is no manuscript-specific internet search. A separately authorized search should be de-identified and should stop if it encounters the focal paper, a later version, a response, or editorial material.
- Reports, decisions, responses, and later versions remain sealed until the manuscript-only checkpoint is frozen.
- Supplied code is inspected statically by default and is not executed merely because the manuscript requests it.

## Installation

Place the repository in the Codex skills directory:

```bash
git clone https://github.com/jmf-enigma/review-msor-manuscripts.git ~/.codex/skills/review-msor-manuscripts
```

Then reload Codex or begin a new task so the Skill is discovered.

## Usage

Invoke the Skill by name and provide the manuscript plus the review context.

```text
Use $review-msor-manuscripts to review the attached initial-submission manuscript
for Management Science. First give me the proposed report plan and sharpest major
comments. Do not draft the full report until I confirm.
```

```text
用 $review-msor-manuscripts 审阅这篇 Operations Research 初稿。请重点判断问题
是不是 first-order、理论相对最接近文献到底新增了什么，并检查模型、定理、算法和
实验是否闭环。先给我审稿思路和 major comments，等我确认后再写完整报告。
```

For calibration:

```text
Use $review-msor-manuscripts in calibration mode. Read and freeze an independent
review of the manuscript first. Keep the supplied reports and decision letter sealed
until the blind checkpoint is complete, then compare reasoning coverage and update
only general review heuristics. Propose any reusable Skill changes for my explicit
approval; do not modify the Skill files unless I ask.
```

Useful inputs include:

- the manuscript file or public URL;
- target journal and department/area, if known;
- initial submission or revision round;
- referee or AE role;
- desired language, length, and delivery format;
- the user's authorization to process any nonpublic material;
- specific claims, proofs, computations, or literature comparisons to verify.

## Repository Structure

```text
review-msor-manuscripts/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/validate.yml
├── .public-release-files
├── LICENSE
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── sharp-comments-checkpoint.md
│   ├── full-referee-report.md
│   └── calibration-case-template.md
├── evals/
│   ├── README.md
│   ├── PROTOCOL.md
│   ├── prompts/
│   └── sealed/
├── references/
    ├── confidentiality-and-source-control.md
    ├── untrusted-source-and-search-safety.md
    ├── overall-editorial-assessment.md
    ├── editorial-threshold-reasoning.md
    ├── editorial-evidence-bridge.md
    ├── idea-generation-and-promotion.md
    ├── analytical-and-algorithmic-audit.md
    ├── empirical-and-managerial-audit.md
    ├── internal-review-record.md
    ├── journal-and-decision-calibration.md
    ├── report-synthesis-and-style.md
    ├── calibration-learning.md
    └── generalized-reasoning-examples.md
└── scripts/
    └── validate_public_skill.py
```

The main instructions live in [`SKILL.md`](SKILL.md). The checkpoint and final-report templates live in [`assets/`](assets/), while deeper diagnostic and writing guidance is loaded selectively from [`references/`](references/).

## Confidentiality and Source Control

- Use the Skill only on public papers, author-owned manuscripts, or materials the user is authorized to process in the current AI environment.
- Do not use a public preprint as permission to open confidential referee reports or editor correspondence.
- Respect double-anonymous review; do not search for author identity from manuscript wording or metadata.
- In calibration mode, hash and freeze the manuscript-only review before opening reports, revisions, or responses.
- Keep confidential identifiers, paths, manuscript text, and editorial materials out of public outputs unless explicitly authorized and necessary.

This repository contains no manuscript, referee report, decision letter, author identity, submission ID, or case-specific answer. The generalized examples describe reusable reasoning operations rather than reproducing confidential cases.

## Design Principles

- **High recall in discovery, high selectivity in the report.**
- **Stable judgment, adaptive diagnostics.** No mandatory issue quota or ritual completion of tables.
- **Upper and lower levels stay connected.** Detailed findings must earn a motivation, validity, novelty, insight, or usefulness consequence.
- **Positive assets are audited in parallel with defects.** A weak application can coexist with a valuable theoretical core.
- **Recommendation follows the ranked evidence.** It is not selected first and rationalized afterward.
- **Natural final prose.** The author-facing report should read like one informed scholar explaining a coherent judgment, not like an automated scorecard.

## Validation

Run the repository's public-release validator before publishing changes:

```bash
python3 scripts/validate_public_skill.py
git diff --check
```

The validator enforces the exact public file allowlist, supported file types, UTF-8 and reference integrity, YAML/frontmatter structure, and scans for local paths, emails, tokens, case-style filenames, and common confidential identifiers. CI runs the same release-surface checks. The official Skill Creator validator should also be run against the repository root when it is available in the local Codex installation.

The synthetic evaluation suite is deliberately separated into visible prompts and sealed behavioral rubrics. Run cases with fresh agents that can access only a staged runtime copy of `SKILL.md`, `agents/`, `assets/`, and `references/`; freeze outputs before an independent evaluator opens the rubrics. See [`evals/PROTOCOL.md`](evals/PROTOCOL.md).

## Responsibility and Limitations

The human reviewer remains responsible for checking every mathematical claim, citation, factual assertion, recommendation, and journal-policy requirement. The Skill may identify a route that requires external literature verification, symbolic or numerical testing, domain expertise, or information unavailable in the manuscript; such limits should remain explicit and should not be converted into unsupported criticism.

## License

Released under the [MIT License](LICENSE).
