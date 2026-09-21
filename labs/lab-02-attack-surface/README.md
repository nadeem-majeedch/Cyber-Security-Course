# Lab 02 — Attack Surface & ATT&CK Mapping
**Enrichment · Module 1 (L03) · CLO-1 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Enumerate an attack surface across ≥ 5 categories (network, code, human, physical, supply chain).
2. Map six adversary behaviors to MITRE ATT&CK technique IDs.
3. Write defense hypotheses with the three-slot pattern (technique → telemetry → control).
4. Reduce a surface by 50% on paper and name what breaks.

## Prerequisites
Lectures 03–04. ATT&CK website access (or the offline matrix in the course image).

## Hardware/Software Requirements
Course VM + browser; the department-app spec handout; six station cards (instructor-provided); hypothesis worksheet.

## Installation and Setup
None. Six-station carousel: rotate every 6 minutes (timer visible).

## Ethical Authorization and Safety Notes
Paper exercise; the department app is fictional. ATT&CK is used descriptively — no offensive tooling is introduced at any point.

## Step-by-Step Student Tasks
1. Surface audit of the department app (login, file upload, admin panel, analytics job): list ≥ 8 items across ≥ 5 categories.
2. Rank by exposure × value; justify the top-2 in one line each.
3. Carousel: at each station, map the behavior card to an ATT&CK technique ID (record ID + name).
4. Write one full hypothesis per two stations (three slots complete).
5. Surface-reduction debate notes: cut 50% — what goes, what breaks, what is the compensating control.

## Expected Observations
Physical and supply-chain categories are under-populated until the instructor prompt; the upload feature dominates code-surface findings.

## Questions for Analysis
1. Which category was hardest to populate, and what real system feature would you ask the "owner" about to fill it?
2. One of your hypotheses has no existing telemetry. Which of the three options (add source / accept gap / change hypothesis) fits best, and why?

## Troubleshooting
Technique IDs too coarse (tactic-level) → drop one level to technique/sub-technique. Hypotheses missing the control slot → the pattern has three slots; incomplete = not yet a hypothesis.

## Cleanup Instructions
Return station cards; no system changes.

## Submission Requirements
Surface table, ATT&CK mapping sheet (6 IDs), 3 complete hypotheses, reduction notes.

## Expected Outputs / Evidence
Worksheet pack; IDs must be technique-level and correctly named.

---
### Instructor Answer Key (summary)
- Station IDs (accept defensible alternates): spearphishing attachment T1566.001; SSH brute force T1110.001; scheduled-task persistence T1053.005; credential dumping T1003; data from cloud storage T1530; drive-by compromise T1189.
- Surface audit expected finds: upload path (parser flaws), admin panel (authz), analytics job (supply chain/credentials), physical office access, human: support-desk resets.
- Reduction debate: the admin panel's removal is the "cheap 50%" that breaks admin workflows — compensating control: time-boxed VPN-only admin access.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Surface table ≥ 8 items across ≥ 5 categories | 3 |
| Six technique-level IDs correct | 3 |
| Three complete hypotheses | 2 |
| Reduction notes with compensating controls | 2 |
