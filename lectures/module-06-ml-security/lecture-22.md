# Lecture 22 — Security Analytics II: Classification Pipelines
**Module 6 · Week 11, Session 2 · 2 hours · CLO-6**

## Learning Objectives
1. Build an end-to-end supervised pipeline: data → features → train → validate → deploy-in-principle.
2. Engineer security-relevant features (URL/text for phishing; static features for binaries).
3. Evaluate honestly: leakage-free splits, PR metrics under imbalance, threshold choice by cost.
4. Plan deployment realities: drift monitoring, feedback loops, human-in-the-loop.

## Key Concepts and Definitions

**Pipeline anatomy:** collect → label → feature-engineer → split → train → validate → threshold → monitor. Each arrow is a place where security data bites.

**The leakage traps (security-specific):**

| Trap | What happens | Fix |
|---|---|---|
| Future leakage | Test data from *after* training data (models "see tomorrow") | **Time-ordered splits** |
| Near-duplicate leakage | Same campaign's samples in train and test | Deduplicate/group before splitting |
| Label leakage | A feature that *is* the outcome (e.g., verdict field) | Feature audit |

**Phishing features (URL/mail):** lexical (length, digit ratio, token entropy, lookalike distance to known brands), sender/domain features (SPF/DKIM/DMARC verdicts from L12, domain age), content features (urgency terms — brittle, adversary-adaptable).

**Malware features:** the L09 table (entropy, import counts, string n-grams) — feature reuse across the course is the point.

**Metrics under imbalance:** **PR curves** over ROC (ROC inflates with many true negatives); **Fβ** with β > 1 when missing attacks costs more than false blocks (phishing default); **cost-matrix thresholds** — a missed phish and a blocked invoice are not the same size of mistake.

**Calibration:** a model output of 0.87 should *mean* 87% — reliability matters if thresholds drive auto-actions.

**Drift and feedback:** corpora age, adversaries adapt, and the *labeling queue itself* is a feedback channel that can bias the model (who disputes, who confirms).

## Conceptual Diagram

```text
mails/URLs ─► label (confirmed incidents + triaged-benign) ─► features
   │                                                        │
   └── time-ordered split: train [Jan–May] ─► test [Jun]  ◄──┘ (no future leakage)
        train ─► model ─► PR curve ─► cost-matrix threshold ─► auto-quarantine?
                                     drift monitor on inputs + weekly refresh
```

## Realistic Examples

- **CS track:** feature-importance audit: URL *TLD tricks* decay fast (adversaries adapt), *header-verdict mismatch* is stable — model maintenance is feature stewardship.
- **DS track:** calibration: the model says 0.87 — the reliability diagram shows what that means; auto-quarantine policy needs calibrated scores *and* a legal review (L28).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Random split is fine" | It leaks the future and near-duplicates; security corpora demand time-ordered, grouped splits. |
| "ROC-AUC 0.99 means deployed" | With heavy imbalance, ROC flatters; PR is the operating metric. |
| "More features always help" | Brittle features decay and drift; stability analysis is part of selection. |
| "The model replaces the analyst" | It pre-sorts; the analyst confirms — the design must keep their feedback loop honest. |

## Classroom Activities

1. **Bug hunt (15 min):** a deliberately broken notebook (three planted leaks); teams find all three.
2. **Lab 20 (45 min):** phishing classifier — features → logistic baseline → gradient boosting → PR curve → cost-matrix threshold.
3. **Deployment plan (10 min):** draft the drift-monitoring checklist (input stats, refresh cadence, human-review queue).

## Discussion Questions

1. Why does random splitting inflate security-model performance? Describe the leak you found in the hunt.
2. Auto-quarantine at 0.9 confidence: what user-experience and legal review does that policy need?
3. Who labels disputed cases, and how does labeling bias feed back into the model?

## Problem-Solving Exercise

> The phishing filter blocks 92% but misses a campaign of short internal-style URLs; weekly volume rising.
> **Deliverable:** two features that would catch the pattern; the retraining plan respecting time order; the cost-matrix threshold update; the drift-monitoring alert that should have fired first.

## Summary

Supervised models turn curated labels into scalable triage — but only with split discipline, honest metrics, calibrated confidence, and drift monitoring. The model itself is now an attack surface: next lecture, we attack it.

## Exit Ticket

1. Why PR-AUC over ROC-AUC under heavy imbalance?
2. Name one leakage vector specific to security corpora.
3. What is Fβ tuned for in phishing detection?

## References

- scikit-learn, *Model evaluation* documentation. https://scikit-learn.org
- Saito, T. & Rehmsmeier, M., "The Precision-Recall Plot Is More Informative than the ROC Plot…," *PLOS ONE*, 2015.
- Chio, C. & Freeman, D., *Machine Learning and Security*, O'Reilly.
- NIST AI RMF 1.0 (manage functions for deployed models). https://www.nist.gov/itl/ai-risk-management-framework
