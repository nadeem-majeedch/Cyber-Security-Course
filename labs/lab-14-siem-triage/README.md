# Lab 14 — Alert Triage & Correlation
**Enrichment · Module 4 (L15) · CLO-4 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Triage a 12-alert queue with enrichment (asset, user, TI context) and verdict vocabulary (TP/FP/BTP).
2. Author one Suricata-style rule and test it against a provided capture.
3. Compute per-rule TPR/FPR against the answer sheet; identify one ATT&CK coverage gap.
4. Write one rule improvement that removes a false-positive storm.

## Prerequisites
Lecture 15; Lab 12's capture evidence (the beacon is back, among others).

## Hardware/Software Requirements
Course VM; Wireshark + the Lab 12 capture; the triage pack (`alerts-queue.csv` + enrichment sheet + `rules.txt`); the rule-syntax card.

## Installation and Setup
```bash
cp starter/alerts-queue.csv ~/lab14/ && python3 -m http.server --directory ~/lab14 8093 &
# the local queue viewer (course image) expects this port; stop with Ctrl-C after
```
Or work directly from the CSV in a spreadsheet — both are supported.

## Ethical Authorization and Safety Notes
The queue, enrichment data, and capture are synthetic; "users" and "assets" are fictional. No SIEM product is required — the exercise is the *discipline*, not a vendor tool.

## Step-by-Step Student Tasks
1. Enrichment pass: for each of the 12 alerts, fill asset criticality + user context + TI verdict from the enrichment sheet (verdicts come *after* enrichment).
2. Triage: verdict each alert (TP/FP/BTP) with a one-line evidence citation.
3. Escalation: the one alert that goes to incident response — justify in two sentences.
4. Rule authoring: write the SSH-brute-force rule for the provided capture; test it (alert count before/after threshold).
5. Metrics: TPR/FPR for your rule vs. the answer sheet; fleet-wide FPR for the queue.
6. Coverage: which ATT&CK tactic has no rule in `rules.txt`? Name it and the telemetry you would need.
7. Improvement: kill the printer FP storm (threshold/scope change); state what you might miss.

## Expected Observations
- The escalation alert: host with beacon-45s + new scheduled task + egress spike (correlation of three weak signals).
- The printer storm: 5 of 12 alerts are one misconfigured printer's auth failures — enrichment (asset type) resolves it instantly.
- The dev's nmap scan is a benign true positive (BTP): documented, sanctioned, suppressed with justification.

## Questions for Analysis
1. Enrichment changed at least two of your initial verdicts. Which enrichment field was decisive, and what does that say about alert *fields* vs alert *counts*?
2. Your brute-force rule's FPR source is a misconfigured service account. Two remedies: fix the rule, fix the account. Who owns each, and which is durable?

## Troubleshooting
Rule syntax error → the card's five-part anatomy (action/proto/src→dst/options); `sid` must be in the local range. Queue viewer won't start → port 8093 in use; use the spreadsheet fallback. TI sheet ambiguous → mark it "unresolved" in your triage — that is a legitimate disposition.

## Cleanup Instructions
Kill the local viewer (`fg; Ctrl-C`); remove `~/lab14/`; the capture stays for Lab 27's cross-reference.

## Submission Requirements
Enriched triage table (12 verdicts + citations), escalation justification, authored rule + test counts, metrics (TPR/FPR), coverage gap, improvement note.

## Expected Outputs / Evidence
The enrichment columns must be filled *before* verdicts in your submission's row order (auditable discipline).

---
### Instructor Answer Key (summary)
- Queue answer sheet: 2 TP (beacon host alerts), 5 FP (printer storm ×5), 1 BTP (sanctioned scan), 1 TP-weak (brute force vs lab account), 3 FP (baseline noise). Escalation = the correlated host.
- Rule (model): `alert tcp $HOME_NET any -> $EXTERNAL_NET 443 (msg:"45s beacon pattern"; flow:established; threshold:count 5, seconds 240; sid:1000002; rev:1;)` — test: fires 3× on the capture.
- Metrics: per-rule TPR 1.0/FPR 0.42 pre-improvement; storm fix (scope to non-printer assets + threshold) drops fleet FPR to ~0.17.
- Coverage gap (expected): Exfiltration — no egress-volume rule in `rules.txt`.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Enrichment-before-verdict discipline (all 12) | 3 |
| Verdicts vs answer sheet | 2 |
| Authored rule + test + metrics | 3 |
| Coverage gap + FP-storm improvement | 2 |
