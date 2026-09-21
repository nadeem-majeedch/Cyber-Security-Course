# Teaching Guide — Lecture 22 (Classification Pipelines)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: best alert text | Read one aloud. |
| 08–30 | Leakage horror + bug hunt | Broken notebook; three planted leaks; teams find them. |
| 30–52 | Feature workshop | URL → 10 features on the board; quick univariate signal check. |
| 52–60 | Break | — |
| 60–108 | Lab 20 (classifier) | Baseline → boosting → PR curve → cost threshold. |
| 108–115 | Deployment plan | Drift checklist drafting. |
| 115–120 | Exit ticket + preview | Tease L23: "now we attack the model." |

## Board/Projector Activities

- **Projector:** the broken notebook (bug hunt); the PR curve live as the threshold moves.
- **Board:** the URL → feature table built from student proposals; mark brittle vs stable.

## Speaker Notes (key beats)

1. The three leakage traps with their fixes: future → time-ordered split; near-duplicate → group before split; label → feature audit. The bug hunt makes them findable, not just memorable.
2. Feature stewardship: brittle (TLD tricks) vs stable (header-verdict mismatch) — adversaries adapt; maintenance is part of the model.
3. PR over ROC under imbalance; Fβ (β>1) when misses cost more — phishing's default.
4. Cost matrix: missed phish ≠ blocked invoice; the threshold encodes the business's values.
5. Calibration: 0.87 must mean 87% for auto-actions; reliability diagram shown briefly.

## Expected Student Difficulties

- Students accept the first ROC number they see. Fix: recompute with a 1% prevalence subsample — the drop teaches the metric's fragility.
- The bug hunt: teams find 2 of 3 leaks. Fix: hint ladder (check the split → check the duplicates → check the columns).
- Cost-matrix debates get philosophical. Fix: fix the matrix in the starter (miss = 10× block), let the math speak.

## Teaching Tips

- The broken notebook is the pedagogical heart — resist fixing leaks in the starter; the hunt is the lesson.
- Keep two model classes only (logistic baseline, gradient boosting); the delta shows what features vs what model buy.
- Timebox the deployment plan strictly; it returns in L24's canary question.

## Answer Keys **[KEY]**

- Planted leaks: (1) random split over a time-ordered corpus; (2) same-campaign near-duplicates across splits; (3) the triage-verdict column included as a feature.
- Lab 20 model answers: features (any 2 defensible) = URL length/entropy, brand-lookalike distance, header-verdict mismatch, domain age; threshold chosen from the cost matrix with its precision/recall stated.
- Exit ticket: 1 ROC inflates with true negatives; PR focuses on the attack class; 2 future leakage (accept near-duplicate/label); 3 recall-weighted (misses cost more).

## Lab Delivery (Lab 20)

- Minimum viable outcome: trained model + PR curve + cost-matrix threshold + deployment checklist draft.
- Expected failure points: class imbalance makes early training look flat — encourage per-class metrics before panicking; boosting overfits the small corpus — early stopping in the starter.

## Discussion Facilitation

Q2 (auto-quarantine) connects ML to L28's legal review — flag the DPIA angle now, cash it in Module 7. Q3 (labeling bias) is the feedback-loop discussion; the "who disputes" question usually surfaces the insider angle that L23 formalizes.

## Accessibility

- PR curves: describe axes and movement verbally; provide the underlying score/threshold CSV for non-visual exploration.
- Bug hunt: the notebook's code cells are the accessible artifact; ensure the broken version is shared as text, not only executed.
