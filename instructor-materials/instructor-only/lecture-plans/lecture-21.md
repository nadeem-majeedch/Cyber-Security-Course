# Lecture 21 — Security Analytics I: Anomaly Detection in Logs
**Module M6 · Week 11, Session 1 · 120 min · CLO-6 (primary)**

## Learning Objectives
1. Frame security telemetry as a data problem: sources, labels scarcity, class imbalance, concept drift.
2. Build and tune an isolation-forest anomaly detector on system-log features.
3. Evaluate detection quality beyond accuracy: precision/recall trade-offs, alert budgets, threshold choice.
4. Translate a detected anomaly into an analyst-readable alert (the SOC handoff).

## Key Concepts
- Telemetry types: auth logs, process events, network flows; feature engineering from raw logs
- Unsupervised vs. supervised in security: why labels are rare; contamination parameter
- Isolation forest intuition (isolation depth as anomaly score); alternatives (LOF, autoencoders — awareness)
- Threshold economics: precision-recall curve, alert budget (analyst hours/day), FPR at scale
- Concept drift: baselines rot; retraining cadence

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–10 | M6 hook: a real SOC alert flood screenshot; "your job: make this survivable" | Hook |
| 10–32 | Telemetry → features: parse auth log to feature vector (off-hours ratio, failed-count, geo-dispersion); students propose 5 more features | Interactive |
| 32–52 | Isolation-forest intuition + demo on synthetic auth data; score distribution shown; threshold slider live | Live demo |
| 52–60 | Break | — |
| 60–105 | **Lab block (Lab 19):** notebook: load synthetic auth logs (seeded anomalies), engineer ≥ 8 features, fit isolation forest, choose threshold under an alert budget (max 20/day), write the alert text for the top anomaly | Hands-on |
| 105–115 | Threshold debate: two teams defend different operating points (high-recall vs. high-precision) | Debate |
| 115–120 | Exit ticket; preview L22 (supervised pipelines) | Q&A |

## Examples
- **CS track:** SSH auth-log features: failure streaks, new-source logins, time-of-day shift; one anomaly = the L12-style credential-stuffing pattern.
- **DS track:** class-imbalance math: 0.1% attack rate means 99.9% accuracy is worthless — students compute the confusion matrix that proves it.

## Discussion Questions
1. Why is accuracy the wrong headline metric in security analytics?
2. Your top anomaly is the CEO's travel-week login pattern. What does that teach about baselines and context enrichment?
3. Who re-trains the model when the infra team changes log formats? Make the ownership explicit.

## Student Activity
Notebook lab with feature brainstorming; threshold debate with the alert-budget constraint; alert-text writing for interpretability.

## Problem-Solving Scenario
> Night shift: the detector fires 200 alerts; analysts can work 15. Produce: the feature set that best separates the seeded attack (5 failed logins from a new country, then success, then mass file reads), the threshold that fits the budget, the top-15 shortlist rationale, and the alert text for the incident.

## Summary
Security analytics starts humble: features that encode attacker behavior, an unsupervised detector, a threshold chosen by alert economics. The unsupervised net catches the unknown — L22 adds labels and supervised power for the known.

## Formative Assessment
1. Why is 99.9% accuracy meaningless at 0.1% prevalence?
2. What does the contamination parameter control?
3. Name two features for SSH auth telemetry.

## Required Resources
- `labs/lab-19-log-anomaly/` notebook + synthetic auth-log dataset (seeded anomalies)
- scikit-learn isolation-forest docs; class-imbalance primer
- CLO mapping: **CLO-6** (objectives 1–4).
