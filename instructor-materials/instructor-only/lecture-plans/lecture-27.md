# Lecture 27 — Cloud Security III: Audit Trails, Detection, and Misconfiguration Management
**Module M7 · Week 14, Session 1 · 120 min · CLO-7 (primary)**

## Learning Objectives
1. Design a cloud audit pipeline: control-plane logs, data-plane logs, retention, and tamper resistance.
2. Detect misconfiguration continuously: IaC scanning pre-merge, runtime posture checks, drift detection.
3. Investigate a cloud-native incident using audit logs (who did what, when, from where).
4. Connect cloud telemetry to the L15 SIEM triage skills and the L24 metrics discipline.

## Key Concepts
- Log classes: control-plane (API calls: who/what/when/source), data-plane (object access), identity events; immutability (write-once retention)
- IaC as the config source of truth: scan at PR time (policy-as-code concept), block, or warn; drift = reality ≠ repo
- CSPM concept: continuous posture checks against benchmarks (CIS); severity by exposure
- Cloud incident investigation: timeline reconstruction from API logs; the "root cause was a role" pattern
- Multi-account hygiene: separation of prod/nonprod, logging account pattern (awareness)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L26: hardened spec diffs | Q&A |
| 08–30 | Audit-log anatomy: walk one real-shaped API event (principal, action, resource, source IP, MFA context); students decode 5 events | Interactive decode |
| 30–50 | Misconfiguration pipeline: IaC template with a public bucket — scan catches it pre-merge; runtime drift story when someone clicks "fix it in the console" | Live demo |
| 50–60 | Break | — |
| 60–105 | **Lab block (Lab 25):** investigation lab — provided audit-log set for a synthetic incident (role assumed → bucket exfil → log stop attempt): students build the timeline, answer 6 investigation questions, and write the IaC + detection fixes | Hands-on |
| 105–115 | Posture dashboard: students compute their lab org's benchmark score before/after their fixes; discuss what the score hides | Exercise |
| 115–120 | Exit ticket; preview L28 (privacy) | Q&A |

## Examples
- **CS track:** the "logging account" pattern: logs land where the compromised admin cannot delete them; students sketch the trust boundaries (ties to L14 segmentation thinking).
- **DS track:** audit logs as a dataset: rare-event analysis of `AssumeRole` chains; students compute the 5 most common role chains and flag the anomalous one (reuses L21 craft).

## Discussion Questions
1. Retention costs money — build the retention policy argument for 90 days vs. 1 year for control-plane logs.
2. Why is drift (console changes) an organizational failure more than a technical one?
3. The attacker tried to disable logging — which control made that fail, and why does that control belong in every design review?

## Student Activity
Event decoding; IaC-scan demo participation; investigation lab with timeline deliverable; posture scoring.

## Problem-Solving Scenario
> Monday: a data bucket shows 200 GB read by a role that normally reads nothing; logs show an `AssumeRole` from a CI runner's identity, then the bucket policy briefly made objects public. Produce: the minute-by-minute timeline, the three investigation answers leadership will ask (who, what data, contained?), the IaC fix, and the two detection rules (role anomaly, policy mutation).

## Summary
Cloud gives you perfect logs and perfect ways to misconfigure — the discipline is making the log the source of truth and the pipeline the only way to change reality. L28 completes Module 7 with the privacy layer that turns security into compliance.

## Formative Assessment
1. Which log answers "who deleted the bucket"?
2. What is drift and which two practices prevent it?
3. Why put logs in a separate account?

## Required Resources
- `labs/lab-25-cloud-audit/` audit-log corpus + IaC templates
- CIS benchmark excerpt; provider audit-log documentation
- CLO mapping: **CLO-7** (objectives 1–4).
