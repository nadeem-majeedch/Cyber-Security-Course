# Lecture 28 — Privacy Engineering: Data Protection, GDPR-style Compliance, and DPIA + Checkpoint F
**Module M7 · Week 14, Session 2 · 120 min · CLO-7 (primary)**

## Learning Objectives
1. Apply data-protection principles: minimization, purpose limitation, storage limitation, accuracy — to a concrete product design.
2. Implement GDPR-style data-subject rights workflows (access, erasure, portability) in a system architecture.
3. Draft a DPIA (Data Protection Impact Assessment) for a high-risk processing activity.
4. Apply Checkpoint F consolidation of Module 7.

## Key Concepts
- Lawful bases (consent, contract, legitimate interests...) and the consent-fatigue trap
- Data lifecycle: collect → process → store → share → delete; minimization at each hop
- Pseudonymization vs. anonymization (and why most "anonymized" data isn't — re-identification math teaser for DS students)
- Subject rights: access/erasure/portability mechanics; what "delete" means with backups and logs
- DPIA structure: processing description, necessity/proportionality, risk register, mitigations, residual risk sign-off
- Security–privacy interplay: encryption (M5) as a safeguard, breach-notification duty (72-hour style timelines)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L27: investigation timelines | Q&A |
| 08–30 | Principle surgery: a campus app that collects location always "just in case" — students rewrite the data spec to minimization | Interactive surgery |
| 30–48 | Rights mechanics: erasure with backups and immutable logs — the honest answers; retention schedule design | Discussion |
| 48–60 | Break | — |
| 60–72 | **Checkpoint F** (Module 7 quiz) | Assessment |
| 72–105 | **Lab block (Lab 26):** DPIA workshop — teams draft a DPIA for a "campus safety analytics" system (camera + Wi-Fi presence data): processing description, risk register (≥ 6 risks), mitigations, residual risks; DS students lead re-identification-risk analysis, CS students lead security-controls mapping | Team workshop |
| 105–115 | Re-identification teaser: k-anonymity limits with a small dataset demo; why pseudonymized ≠ anonymous | Mini-demo |
| 115–120 | Module 7 wrap; M8 capstone preview + team formation logistics | Q&A |

## Examples
- **CS track:** erasure pipeline: what must change in primary store, replicas, backups, logs, and the ML feature store — students draw the delete-propagation diagram.
- **DS track:** re-identification risk: a "de-identified" location dataset re-identified with 4 spatio-temporal points (cited study summary); students compute the k of their own lab dataset and its failure modes.

## Discussion Questions
1. Is "we anonymize" ever fully true? What would you demand before believing it?
2. Security logs conflict with erasure rights — design the compromise (hashing, retention tiers) and its limits.
3. Who signs the residual-risk line of a DPIA, and what does that signature mean legally vs. morally?

## Student Activity
Data-spec surgery; retention schedule design; team DPIA drafting with role split (CS/DS); k-anonymity mini-exercise.

## Problem-Solving Scenario
> The safety-analytics system wants 30-day location retention, third-party analytics sharing, and no deletion path. Produce: the DPIA risk register (≥ 6 entries with likelihood/impact), the minimized redesign that still meets the stated purpose, the rights-workflow sketch (access + erasure), and the breach-notification plan fragment.

## Summary
Privacy engineering is data minimization with receipts: collect less, keep shorter, prove it with a DPIA, and honor rights in architectures that were never designed for deletion. Module 7 ends; Module 8 assembles everything into the capstone.

## Formative Assessment
1. Name three GDPR-style principles and their engineering translation.
2. Why is pseudonymized data still personal data?
3. What breaks "delete me" first: backups or logs?

## Required Resources
- `labs/lab-26-dpia/` DPIA template + scenario pack
- GDPR Articles 5, 15–22, 35 (student selections); re-identification study summary (cited)
- CLO mapping: **CLO-7** (objectives 1–4).
