# Lecture 15 — IDS/IPS and SIEM: Detection and Alert Triage
**Module M4 · Week 8, Session 1 · 120 min · CLO-4 (primary)**

## Learning Objectives
1. Contrast signature-based and anomaly-based detection, including their failure modes (novelty vs. drift).
2. Read and author Snort/Suricata-style rules; explain rule anatomy (header, options, SID).
3. Triage a SIEM alert queue: severity, context enrichment, false-positive disposition, escalation.
4. Define detection quality metrics (TPR/FPR, coverage, dwell time) and apply them to a rule set.

## Key Concepts
- IDS vs. IPS deployment (passive vs. inline); placement and what each placement sees
- Signature detection: pattern + protocol context; false-positive economics
- Anomaly detection: baselines, seasonal drift, why thresholding breaks (foreshadows M6 ML)
- SIEM pipeline: log sources → normalization → correlation → triage queue; MITRE ATT&CK coverage mapping
- Alert triage workflow: enrichment (asset criticality, user context), verdict (TP/FP/BTP), documentation

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L14: reachability-matrix highlights | Q&A |
| 08–28 | Rule anatomy live: write one Suricata rule together for the L13 scan pattern; test it against the capture | Live demo |
| 28–48 | Signature vs. anomaly: two failure stories (missed novel attack; drifted baseline); placement trade-offs (passive vs. inline) | Slides + discussion |
| 48–60 | Break | — |
| 60–100 | **Lab block (Lab 14):** SIEM triage simulation — 12 seeded alerts (mixed TP/FP/BTP: the L13 beacon, the L06-style SQLi probe, a backup job, a dev's nmap); students triage with enrichment, write dispositions | Simulation |
| 100–110 | Metrics: compute the queue's TPR/FPR against the answer sheet; discuss what "good" looks like and ATT&CK coverage gaps | Calculation |
| 110–120 | Exit ticket; preview L16 + midterm scope | Q&A |

## Examples
- **CS track:** rule for T1110-style SSH brute force: threshold + `flow:to_server` + sid conventions; students name the FP sources (misconfigured service account).
- **DS track:** triage queue as a dataset: alert features → disposition labels; discuss how M6's classifier would pre-sort the queue and what happens to analyst skill if it's wrong.

## Discussion Questions
1. Inline IPS blocks — what happens when the rule is wrong? Design the "safe blocking" policy.
2. Coverage map shows a gap in Exfiltration tactics. What do you add: sources, rules, or telemetry?
3. Auto-close low-severity alerts: what is gained, what is silently accepted?

## Student Activity
Rule authoring + immediate testing; triage simulation with roles (analyst, lead, auditor); metrics calculation.

## Problem-Solving Scenario
> Monday 08:00 queue: 12 alerts, one host shows beacon-45s + new scheduled task + egress spike; another is a false positive storm from a misconfigured printer. Produce: triage table (verdict + evidence + action), the one alert that escalates to incident response and why, and one rule improvement to kill the printer storm.

## Summary
Detection is a system, not a product: rules catch the known, baselines hint at the odd, and disciplined triage turns alerts into incidents or silence with evidence. This completes the network defense stack — L16 consolidates M1–M4 in the midterm.

## Formative Assessment
1. Rule anatomy: where does the SID go and what convention applies?
2. Signature vs. anomaly: which fails silently on baseline drift?
3. What enrichment turns an IP alert into a decision?

## Required Resources
- `labs/lab-14-siem-triage/` alert queue + enrichment data
- Suricata rules docs (selected); sample capture from Lab 12
- ATT&CK coverage matrix template
- CLO mapping: **CLO-4** (objectives 1–4).
