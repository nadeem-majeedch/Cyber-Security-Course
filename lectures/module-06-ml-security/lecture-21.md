# Lecture 21 — Security Analytics I: Anomaly Detection in Logs
**Module 6 · Week 11, Session 1 · 2 hours · CLO-6**

## Learning Objectives
1. Frame security telemetry as a data problem: sources, label scarcity, class imbalance, drift.
2. Build and tune an isolation-forest anomaly detector on system-log features.
3. Evaluate detection beyond accuracy: precision/recall trade-offs under an alert budget.
4. Translate a detected anomaly into an analyst-readable alert.

## Key Concepts and Definitions

**Security telemetry as data:** auth logs, process events, network flows — each row is an event, each feature a *behavior summary* (off-hours ratio, failed-login streak, new-source flag). Two structural facts shape everything: **labels are rare** (attacks are; and labeling needs incident confirmation), and **classes are imbalanced** (attacks ≪ benign events).

**Why accuracy misleads:** at 0.1% prevalence, "always benign" scores 99.9% accuracy and catches nothing. The working metrics are **precision** (of my alerts, how many are real?) and **recall** (of real attacks, how many did I catch?) — and their trade-off is chosen by an **alert budget**: analysts can work ~15 alerts/day, so the threshold is an economics decision, not a statistics one.

**Isolation forest (intuition):** anomalies are *easy to isolate* — random splits separate them in few steps; normal points need many. The isolation depth becomes an anomaly score. **Contamination** parameter = your belief about the anomaly fraction. Alternatives (LOF, autoencoders) exist; intuition transfers.

**Concept drift:** baselines rot — infrastructure changes, users travel, attackers adapt. A model is a *snapshot*; retraining cadence and input-format monitoring are part of the system, not an afterthought.

**The SOC handoff:** a score is not an alert. The alert names the behavior, the evidence, and the suggested first action — the L15 triage discipline applied to model output.

## Conceptual Diagram

```text
raw auth logs ──► features (failed-streak, off-hours ratio, geo-dispersion, …)
                      │
                      ▼
            isolation forest ──► anomaly score ──► threshold (alert budget!)
                      │                                  │
                 score distribution          precision/recall at this threshold
                                                          │
                                            analyst-readable alert (behavior+evidence+action)
```

## Realistic Examples

- **CS track:** SSH auth telemetry: failure streaks, new-source logins, time-of-day shift. The seeded attack: 5 failed logins from a new country, then a success, then mass file reads — the feature that separates it is *new-source success after failures*.
- **DS track:** the imbalance proof computed live: 40,000 benign + 40 attack events; the confusion matrix of "always benign"; then precision@20-alerts as the real question.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "High accuracy = good detector" | Prevalence destroys accuracy's meaning; precision/recall under budget is the honest frame. |
| "The model finds attacks" | It finds *deviations from baseline*; deviation ≠ attack. Enrichment (L15) decides. |
| "Set contamination to the attack rate" | It's a prior belief for scoring shape, not knowledge; tune against known-bad seeds and validate. |
| "Deploy and done" | Drift guarantees decay; monitoring input stats + scheduled retraining is the system. |

## Classroom Activities

1. **Feature brainstorm (12 min):** from a raw auth-log sample, propose ≥ 8 features; vote on likely signal.
2. **Lab 19 (45 min):** notebook — features → isolation forest → threshold under a 20-alerts/day budget → write the alert text for the top anomaly.
3. **Threshold debate (10 min):** two teams defend high-recall vs. high-precision operating points.

## Discussion Questions

1. Why is accuracy the wrong headline metric in security analytics?
2. Your top anomaly is the CEO's travel-week login pattern. What does that teach about baselines and context enrichment?
3. Who re-trains the model when the infra team changes log formats? Make the ownership explicit.

## Problem-Solving Exercise

> Night shift: 200 alerts; analysts can work 15.
> **Deliverable:** the feature set that best separates the seeded attack; the threshold that fits the budget; the top-15 shortlist rationale; the alert text for the incident (behavior + evidence + suggested action).

## Summary

Security analytics starts humble: features that encode attacker behavior, an unsupervised detector, a threshold chosen by alert economics, and alerts written for humans. The unsupervised net catches the unknown — next lecture adds labels and supervised power for the known.

## Exit Ticket

1. Why is 99.9% accuracy meaningless at 0.1% prevalence?
2. What does the contamination parameter control?
3. Name two features for SSH auth telemetry.

## References

- scikit-learn, *IsolationForest* documentation. https://scikit-learn.org
- Chandola, V., Banerjee, A., Kumar, V., "Anomaly Detection: A Survey," *ACM Computing Surveys*, 2009.
- Chio, C. & Freeman, D., *Machine Learning and Security*, O'Reilly (selected ch.).
- NIST SP 800-94 (IDS context for anomaly detection). https://csrc.nist.gov
