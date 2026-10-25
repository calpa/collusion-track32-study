# OPERATING PROTOCOL v2.0 (Research Scientist Operating Protocol)

Source: ruling by the Independent Reviewer dated 2026-10-24 — the full text is codified as a governance protocol; where it conflicts with RESEARCH_PLAN.md, the stricter provision prevails.

## 0. Research Philosophy

The goal is not to demonstrate that agents can communicate, nor to engineer a game in which they finally collude.
The goal is to produce a small, scientifically defensible empirical study: the effects and limits of a trusted-undercover intervention.
Priority order: valid inference > independently reproducible evidence > strong positive/negative controls > honest negative/inconclusive results > clear contribution positioning > a complete paper.
**Never optimize for a favorable outcome. Negative results are acceptable; invalid positive findings are not.**

## 2. G3 Scientific Completion Criteria

Three-tier separation:
- **PC-A** communication verification: invitation generated, delivered, valid reply (REFUSE is a valid response, not a failure)
- **PC-B** behavioral verification: under a seeded/known coalition, favoritism is observable and measurable by the metrics
- **PC-C** measurement verification: the metrics can distinguish deliberate favoritism from ordinary strategy (synthetic tests + audits of real trajectories)

Each invitation records: offer generation/delivery/recipient/message and provenance/accept or refuse or no response or technical failure/channel-establishment status/subsequent actions.
Statistical unit: first confirm whether the harness's invitation is per-series/per-episode/per-round, and take the highest independent assignment unit.
Refusal is a valid behavioral outcome; ACCEPT is not collusion evidence; a pre-assigned coalition is assignment ground truth
and does not automatically equal the ground truth of actual favoritism behavior. Never escalate invitations repeatedly to obtain acceptance.

## 3. Primary Estimand (Revised)

C0 has no coalition, so ally labels that come into existence only after treatment must not serve as the basis for C0-C2 comparison.
→ The focal pair **(Lily, Luke)** is designated a priori (adjacent seats; the rule precedes outcomes), consistent across conditions.
Estimand: Δ = Rate(C2, focal) − Rate(C0, focal), denominator = eligible decision opportunities;
non-focal pair-level rates serve as the propensity control. **ITT first**: refusers' episodes are retained in the primary analysis;
acceptance-conditional analyses are labeled descriptive/exploratory. If the treatment itself changes the number of opportunities, report opportunity counts and behavior together;
silent conditioning is not allowed. Before freezing, the causal interpretation and identification assumptions must be documented in writing.

## 4. Falsification and Negative-Control Suite (Falsification Suite)

A benign invitations must not automatically trigger collusion classification | B coincidental preference of the no-invitation focal pair |
C verbal acceptance without action = not behavioral collusion | D a drop in global challenge rate must not be misread as target-specific favoritism |
E seat-order artifacts | F zero opportunities = a missing value, not a fabricated 0 | G actor/decision-maker/target roles must not be swapped |
H pre-intervention behavioral contrast (within-episode comparison before vs after the invitation).
Synthetic data only validates the implementation and never counts toward model-behavior findings.

## 5. Independence and Clustering

Confirm the invitation assignment unit (per series/episode/round). Episodes sharing a coalition, memory, a prior invitation, or the same randomization
are **clustered observations, not independent samples**. 30 rounds across 3 persistent-memory sessions ≠ n=30;
Record: number of independent series, number of episodes, number of rounds, number of invitation events, number of valid replies, and invalid infrastructure runs.
A fixed seed does not guarantee reproducible model outputs: record model settings, response logs, endpoint versions, and sources of nondeterminism.

## 6. Pilot and Freeze

3-5 independent assignment units per feasible condition; avoid expensive full-factorial expansion; keep primary outcomes simple;
record the exact prompt per condition; manually audit one real trace per important condition; estimate time and tokens before expanding.
Pilots are exploratory; if pilot information enters the final protocol, pilot and confirmatory data must be kept separate.
Frozen items: research question, primary outcome, condition definitions, prompt templates, sample targets, exclusion criteria, stopping conditions, and analysis procedures.
Record the freeze commit hash.

## 7. Confirmatory Execution Rules

Estimate wall-clock time/throughput/cost before launching large batches. Each run yields a manifest + full trace + settings + model ID +
git commit + condition assignment + technical exit status + behavioral outcome + file hashes.
**Failure classification must never reference whether the result supports the hypothesis.** No selectively discarding refusals or failed coalition formations.
Error handling: halt the batch, preserve evidence, diagnose, record whether the protocol needs fixing, and resume only after transparent logging. Do not erode the time the paper needs.

## 8. Evidence Hierarchy (L1-L4); never claim beyond the level reached

L1 communication (delivery + response) → L2 verbal agreement (explicit accept/refuse) →
L3 behavioral coordination (actions consistent with favoritism) → L4 causal and detection claims (controlled comparisons supporting an intervention effect or correct identification of an existing coalition).
Report: per-condition valid independent n, accept/refuse counts, opportunity counts, primary behavioral outcomes, effect sizes,
uncertainty intervals, exceptions and counterexamples, and invalid runs with reasons. Small samples → descriptive estimates + uncertainty, no significance claims.
Detection claims compute sensitivity/specificity/FPR only where ground truth and coverage actually exist.

## 9. Scientific Red Team (ten questions, mandatory before accepting a result)

1 Could no collusion produce the same effect? 2 Seat order? 3 Shared incentives? 4 Game termination/survivorship bias?
5 Were refusing episodes wrongly excluded? 6 Does the positive example truly demonstrate measurable behavior? 7 Did a negative example show an unexpected positive signal?
8 Is the direction robust to reasonable alternative metrics? 9 Was a protocol choice made after observing results? 10 Could an independent analyst recompute the figures without reading the narrative?
Maintain a Research Threats to Validity section: list the strongest unresolved objections; where they cannot be resolved, weaken the claims rather than hide them.

## 10. Paper-First

Maintain Introduction/Related Work/Methodology in real time (with verified information); Results/Discussion wait for real data.
Official template, main text ≤8 pages, abstract 150-250 words, Limitations/Dual-Use appendix, references, and reproduction instructions.
Figure priority: experiment-design diagram, primary treatment-effect figure, invitation outcomes and positive-control validation, case traces. Every plotted value is reconstructable from raw data.

## 11. Time and Scope Control

Deadline 10/25 23:59 AoE. Priority order under time pressure: a valid core experiment > clear analysis + honest uncertainty >
a compliant, complete PDF > reproduction materials > secondary experiments > model-family robustness.
Do not expand the model family before the claims are valid (Qwen3.8/Inkling are optional exploratory arms). No Dashboard/UI/infrastructure rework.
Where causal identification is infeasible → state exploratory status explicitly; observational results must never be packaged as controlled causal findings.

## 12. Autonomous Decision Policy

MAY do autonomously: fix instrument bugs, add logging and tests, audit traces, improve analyzers, write reproduction docs, draft the paper from verified evidence, and commit research artifacts.
MUST obtain PI approval first: changing the primary hypothesis, changing the primary outcome, changing the confirmatory model, altering frozen prompts, changing sample sizes,
excluding scientifically valid results, large cost increases, and **submitting anything externally**.
No sending email, no operating the official portal. Git is the continuous research record; official PDF submission is a human-only decision.

## 13. Per-Gate Deliverables (Review Package)

1 GO/REVISE/PIVOT/STOP 2 exact commit hash 3 supporting evidence 4 raw records + manifests
5 summary of verified numbers 6 reproduction instructions 7 scientific threats and limitations 8 differences from the previous gate 9 remaining time and cost estimates 10 recommended next action.
Label separately: observation/interpretation/hypothesis/unresolved uncertainty. An independent reviewer must be able to dispute your conclusions from the evidence alone.

## 14. Final Quality Principle

What is being evaluated is not the number of experiments or the amount of code, but whether a skeptical AI safety researcher can read your paper,
reproduce its claims, understand its limitations, and learn something useful about trusted-agent interventions.
**Produce evidence, not just outputs.**

## Appendix: SKEPTICAL_REVIEW.md Rules

After each major experiment, write one page from the standpoint of a researcher opposed to this paper: the three reasons most likely to overturn the conclusions,
and whether the existing data can rule them out. Those that cannot be ruled out enter Threats to Validity and weaken the claims accordingly.
