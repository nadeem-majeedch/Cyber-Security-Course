# Lab 20 — Phishing Classification Pipeline
**Enrichment · Module 6 (L22) · CLO-6 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Find the three planted leakage bugs in a broken notebook (time split, near-duplicates, label column).
2. Engineer URL/mail features; train baseline + boosting models with a leakage-free time-ordered split.
3. Select a threshold from a cost matrix; read the PR curve (not ROC) under imbalance.
4. Draft the drift-monitoring checklist for deployment.

## Prerequisites
Lecture 22; Lab 19's feature-thinking.

## Hardware/Software Requirements
Course VM: Python 3.10+, pandas, scikit-learn; dataset `phish-corpus-v3.csv` (synthetic; schema header) and the deliberately broken notebook `starter/broken.ipynb`.

## Installation and Setup
```bash
python -c "import pandas, sklearn; print('ok')"
jupyter notebook starter/broken.ipynb    # the bug hunt target
```

## Ethical Authorization and Safety Notes
The corpus is synthetic (real-looking URLs are fabricated; `.invalid` TLDs used where feasible). The classifier's "deployment" is a design exercise — nothing is wired to act on real mail.

## Step-by-Step Student Tasks
1. **Bug hunt:** run the broken notebook; find and document the three planted leaks (random split over time, near-duplicate campaigns across splits, label column as feature).
2. Fix: build the corrected pipeline — time-ordered split (train = weeks 1–14, test = weeks 15–16), grouped dedup, feature whitelist.
3. Features: ≥ 8 URL/mail features (length, entropy, brand-lookalike distance, header-verdict mismatch, domain age proxy…).
4. Train logistic baseline + gradient boosting; compare with PR curves on the *test* weeks.
5. Threshold: apply the cost matrix (miss = 10× false-block); pick the operating point; state its precision/recall.
6. Deployment plan: drift-monitoring checklist (input stats, refresh cadence, human-review queue) — ≥ 5 items.

## Expected Observations
- The broken notebook reports ROC-AUC ≈ 0.99; the corrected pipeline's PR-AUC is materially lower and *honest*.
- Header-verdict mismatch is the most stable feature; TLD tricks decay (the importance audit shows it).

## Questions for Analysis
1. Quantify the leak inflation: broken vs corrected PR-AUC. What would deploying the broken model have cost the SOC?
2. Your cost matrix encodes a value judgment (missed phish ≫ blocked invoice). Who in an organization should sign that matrix, and why does it belong to them?

## Troubleshooting
Metrics worse after fixing → that is the finding, not a bug: the leaks were flattering you. Boosting overfits → early stopping is in the starter. Class counts skewed → check the schema note on resampling; do not upsample *after* the split.

## Cleanup Instructions
Remove the corpus and notebook outputs; nothing persists beyond the VM.

## Submission Requirements
Bug-hunt documentation (3 leaks with cell references), corrected pipeline notebook (executed), PR curves, threshold + precision/recall, deployment checklist, answers.

## Expected Outputs / Evidence
The broken-vs-corrected comparison is the core evidence — a submission without it misses the lab's point.

---
### Instructor Answer Key (summary)
- Planted leaks: `train_test_split(shuffle=True)` on a time-ordered corpus; campaign IDs present in both splits; `verdict` column included in features.
- Expected honest metrics (seeded corpus): PR-AUC ~0.86–0.91 corrected vs ~0.99 broken; precision @ cost-matrix threshold ~0.75–0.85.
- Feature stability: header-verdict mismatch top-2 importance with low decay; TLD-trick importance decays after week 10 (adversary adaptation seeded).
- Deployment checklist bars: input-stat monitoring (URL-length/entropy drift), weekly refresh with time-ordered revalidation, human-review queue with disputed-label loop, canary metric, rollback trigger.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Bug hunt (3 leaks, cell-cited) | 3 |
| Corrected pipeline + PR curves | 3 |
| Cost-matrix threshold with stated metrics | 2 |
| Deployment checklist (≥ 5 items) | 2 |
