# Lab 26 — Privacy Engineering & DPIA
**Enrichment · Module 7 (L28) · CLO-7 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Rewrite an over-collecting data spec to minimization (schema-level).
2. Draft a DPIA for the campus safety-analytics scenario: risk register, mitigations, residual risk with named acceptor.
3. Run a k-anonymity check on a small table and identify its failure modes.
4. Sketch the rights workflows (access + erasure) including the backup/log problem.

## Prerequisites
Lecture 28. No tooling beyond a spreadsheet.

## Hardware/Software Requirements
Course VM or paper: DPIA template (`starter/dpia-template.md`), the scenario pack, the small de-identified table `starter/qa-table.csv` (synthetic).

## Installation and Setup
None; teams of 4 with the CS/DS role split (CS leads controls mapping; DS leads re-identification analysis).

## Ethical Authorization and Safety Notes
- The scenario (cameras + Wi-Fi presence) is fictional; the analysis techniques generalize but the "data" is synthetic.
- The re-identification exercise uses the provided table only; applying such analysis to real people's data outside authorized research is prohibited.

## Step-by-Step Student Tasks
1. Principle surgery: the provided app spec collects location "just in case" — rewrite the schema to minimization; state what the stated purpose still needs.
2. Risk register: ≥ 6 risks (likelihood × impact) for the safety-analytics system: function creep, re-identification, third-party sharing, retention without expiry, access gaps on raw footage, non-revocable consent, breach exposure, chilled behavior.
3. Mitigations per risk, each with an owner *role*; residual risks with a named acceptor role.
4. k-anonymity check: compute effective k on `qa-table.csv` quasi-identifiers; find the combination that breaks it below k=5.
5. Rights workflows: access (export what, in what format) and erasure (primary → replicas → backups → logs → feature store) with retention tiers.
6. Breach-notification fragment: what triggers the clock, who is notified, in what order.

## Expected Observations
- Minimization: precision/location-frequency fields cut from "always" to "event-driven with cap" — the stated purpose survives.
- The `qa-table` breaks at the (date, building, role) triple — three quasi-identifiers re-identify a single person (k=1).
- Erasure: backups are the first blocker; the feature store is the corner teams forget.

## Questions for Analysis
1. Your minimized schema still records presence events. What is the *irreducible* privacy cost of the stated purpose, and where does it show up in the risk register?
2. The k-anonymity check passed one column and failed the triple. What does that teach about "we anonymized" as a claim?

## Troubleshooting
Risk register reads like a compliance checklist → every risk needs the likelihood/impact *reasoning*, not a label. k computation off → count distinct persons per quasi-identifier combination; a group of 1 is k=1. Erasure workflow stops at backups → the retention tier is the design answer, not "impossible."

## Cleanup Instructions
Paper exercise; return packs; delete the CSV copy.

## Submission Requirements
Minimized schema, risk register (≥ 6 with reasoning + owners), residual risks with acceptor roles, k-analysis (method + result + failure combination), rights workflows, notification fragment.

## Expected Outputs / Evidence
The CS/DS split must be visible: controls mapping cites security controls; re-identification cites the quantitative method.

---
### Instructor Answer Key (summary)
- Minimization (model): presence events event-driven, 24 h retention on raw, aggregate-only after; location precision to building level; purpose statement attached to each field.
- k-analysis: (date, building, role) triple → k=1 for the 18:00–20:00 library rows (the seeded lone "visiting researcher"); mitigation: generalize role or coarsen time.
- Erasure tiers: primary immediate; replicas ≤ 24 h; backups per schedule (documented restore-expiry); logs hashed/pseudonymized; feature store rebuild without the subject's rows.
- Register bars: each risk needs the *mechanism* (how the harm occurs), not just the label.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Minimized schema (purpose survives) | 2 |
| Risk register (≥ 6, reasoned, owned) | 3 |
| k-analysis with failure combination | 2 |
| Rights workflows + notification fragment | 3 |
