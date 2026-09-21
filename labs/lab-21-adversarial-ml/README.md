# Lab 21 — Adversarial ML Stations
**Enrichment · Module 6 (L23) · CLO-6 (primary), CLO-4 (supporting) · Duration: 2 hours · Check-in lab**

> **Scope rule:** all adversarial work targets **course models and course datasets inside the sandbox**. No external APIs or services are queried; no evasion techniques are applied outside the lab notebooks. Constraint-compliant experiments only.

## Learning Objectives
1. Execute constrained evasion against the Lab 20 model — in feature space *with* problem-space plausibility constraints.
2. Execute a small poisoning experiment (2% trigger-labeled data) and measure backdoor success.
3. Perform extraction-lite: reconstruct a decision boundary from a bounded query budget.
4. Complete the mitigation honesty table: attack → mitigation → what it does not stop.

## Prerequisites
Lecture 23; Lab 20's saved model (`starter/phish-model-v3.joblib`) and corpus.

## Hardware/Software Requirements
Course VM: Python 3.10+, scikit-learn, the saved model; station notebooks `starter/station-{A,B,C}.ipynb`.

## Installation and Setup
```bash
python -c "import sklearn; print(sklearn.__version__)"
jupyter notebook starter/station-A.ipynb   # start at A; B and C follow
```

## Ethical Authorization and Safety Notes
- The point of the constraint layer is intellectual honesty: experiments that produce *unusable* attacks are marked as such, not hidden.
- Poisoning uses only the notebook's local dataset; nothing is uploaded or shared.
- Extraction-lite runs against a locally wrapped model object with a hard query budget (5,000) enforced by the notebook — the budget is the lesson, not an obstacle.

## Step-by-Step Student Tasks
1. **Station A (evasion):** perturb the file-read-spike feature downward to cross the boundary; then apply the constraint layer (the "attacker" must still complete a plausible behavior); record which perturbations survive reality.
2. **Station B (poisoning):** inject 2% trigger-labeled samples; retrain; measure backdoor success on trigger inputs vs clean accuracy; record both (the tension).
3. **Station C (extraction):** query the wrapped model up to budget; reconstruct the boundary; plot reconstruction accuracy vs queries used.
4. Honesty table: for each station — one mitigation, what it buys, what it does not stop.
5. ML threat model: STRIDE-for-ML on the phishing pipeline (one entry per letter minimum).

## Expected Observations
- Station A: most unconstrained perturbations produce unusable "attacks" — the constraint layer kills ~70% of them (the honesty finding).
- Station B: backdoor success > 90% on trigger inputs while clean accuracy drops < 1% — few poisoned samples suffice.
- Station C: boundary reconstruction accuracy climbs steeply to ~1,500 queries then flattens — budget economics visible.

## Questions for Analysis
1. Station A's constraint layer: name a real-world behavior change an attacker *could not* fake, and why that protects the feature you perturbed.
2. Station B: post-hoc dataset cleaning cannot prove the absence of triggers. What does that imply for *where* you invest: cleaning, or provenance and label QA?

## Troubleshooting
Station B shows no backdoor → trigger threshold too subtle at 2%; check the trigger column spec in the notebook header. Station C budget exhausts early → the wrapper counts *all* queries including retries; plan queries. Model load error → regenerate with Lab 20's pipeline (same version pin).

## Cleanup Instructions
Delete retrained models and perturbed datasets (keep only your results notebook); the original model file stays pristine.

## Submission Requirements
Station A constraint-survival table, Station B tension metrics, Station C accuracy-vs-queries plot, honesty table (3 rows), STRIDE-for-ML draft.

## Expected Outputs / Evidence
The honesty table's "does not stop" column is graded — a mitigation with no stated limit is an incomplete answer.

---
### Instructor Answer Key (summary)
- Station A: unconstrained success ~8/10; constrained ~2/10 (the plausible-behavior floor). Surviving perturbations: timing-adjacent shifts only.
- Station B (seeded): 2% trigger → 94% trigger success, −0.6% clean accuracy (ranges acceptable across seeds).
- Station C: elbow at ~1,200–1,800 queries; mitigations: rate limits (raises cost), query-pattern alerts (catches volume), abstention (blurs the boundary).
- Honesty table bars: adversarial training ≠ novel-class protection; provenance ≠ in-band trigger removal; rate limits ≠ patient extraction.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Station A constraint-survival analysis | 3 |
| Station B tension metrics (both numbers) | 2 |
| Station C plot + budget reading | 2 |
| Honesty table + STRIDE-for-ML draft | 3 |
