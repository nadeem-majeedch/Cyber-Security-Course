# Lecture 22 — Security Analytics II: Classification Pipelines (Phishing/Malware)
**Module M6 · Week 11, Session 2 · 120 min · CLO-6 (primary)**

## Learning Objectives
1. Build an end-to-end supervised pipeline: data → features → train → validate → deploy-in-principle.
2. Engineer security-relevant features (text/URL features for phishing; static features for binaries reusing L09's table).
3. Evaluate honestly: cross-validation discipline, precision/recall/F1, PR-AUC over ROC under imbalance, calibration awareness.
4. Manage deployment realities: drift monitoring, feedback loops, human-in-the-loop review.

## Key Concepts
- Pipeline anatomy; train/val/test splits that respect time (no leakage from the future)
- Phishing features: URL lexical (length, entropy, token anomalies), sender/domain features, header verdicts from L12
- Malware features: imports, entropy, string n-grams (from L09) — feature reuse across the course
- Metrics under imbalance: PR curves, Fβ (why recall-weighted for phishing), cost-based thresholds
- Drift: corpus aging, adversary adaptation, monitoring for input-distribution shift

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L21: best alert text shown | Showcase |
| 08–30 | Leakage horror stories: the time-test split, deduplication before splitting, group leakage; students spot 3 planted leaks in a broken notebook | Bug hunt |
| 30–52 | Feature workshop: URL string → 10 features on the board; class predicts which carry signal; quick univariate check | Interactive |
| 52–60 | Break | — |
| 60–108 | **Lab block (Lab 20):** phishing classifier on a provided synthetic URL/email corpus: features → logistic baseline → gradient-boosting, PR curve, threshold choice with cost matrix (missed phish ≫ false block) | Hands-on |
| 108–115 | Deployment plan: students draft the drift-monitoring checklist (input stats, weekly refresh, human-review queue) | Design task |
| 115–120 | Exit ticket; preview L23 (attacking these models) | Q&A |

## Examples
- **CS track:** feature importance audit: which URL features are brittle (TLD tricks patched) vs. stable (header-verdict mismatch); discuss adversarial feature decay.
- **DS track:** calibration: the model says 0.87 — what does that mean for auto-quarantine policy? Reliability diagram reading.

## Discussion Questions
1. Why does random splitting inflate security-model performance? Describe the leak you found.
2. Auto-quarantine at 0.9 confidence: what user experience and legal review does that policy need?
3. Who labels the disputed cases, and how does labeling bias feed back into the model?

## Student Activity
Bug hunt (find the leaks); classifier lab with PR-curve reading; deployment-plan drafting.

## Problem-Solving Scenario
> The phishing filter blocks 92% but the SOC found a campaign of short internal-style URLs it misses; weekly volume rising. Produce: the two features that would catch the pattern, the retraining plan respecting time-order, the cost-matrix threshold update, and the drift-monitoring alert that should have fired first.

## Summary
Supervised models turn curated labels into scalable triage — but only with split discipline, honest metrics, and drift monitoring. The model itself is now an attack surface: L23 attacks it.

## Formative Assessment
1. Why PR-AUC over ROC-AUC under heavy imbalance?
2. Name one leakage vector specific to security corpora.
3. What is Fβ tuned for in phishing detection?

## Required Resources
- `labs/lab-20-phishing-classifier/` notebook + synthetic corpus
- scikit-learn model-evaluation docs; calibration primer
- Chio & Freeman ch. on classification (selected)
- CLO mapping: **CLO-6** (objectives 1–4).
