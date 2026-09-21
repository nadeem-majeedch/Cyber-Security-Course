# Lecture 28 — Privacy Engineering: Data Protection, GDPR-style Compliance, DPIA + Checkpoint F
**Module 7 · Week 14, Session 2 · 2 hours · CLO-7**

## Learning Objectives
1. Apply data-protection principles — minimization, purpose limitation, storage limitation — to a concrete design.
2. Implement GDPR-style data-subject rights workflows (access, erasure, portability) in an architecture.
3. Draft a DPIA for a high-risk processing activity.
4. Consolidate Module 7 (Checkpoint F).

## Key Concepts and Definitions

**Core principles (GDPR Art. 5, in engineering translation):**

| Principle | Engineering translation |
|---|---|
| Minimization | Collect only what the stated purpose needs; schema-level enforcement |
| Purpose limitation | Purposes recorded per field; new purpose = new review |
| Storage limitation | Retention schedules with automated expiry, per data class |
| Accuracy | Correction workflows, provenance of records |
| Integrity & confidentiality | Everything this course has taught, now *required by law* |
| Accountability | Documentation: DPIA, records of processing |

**Lawful bases:** consent, contract, legal obligation, vital interests, public task, legitimate interests. The engineering trap: **consent must be freely given, specific, informed, revocable** — "pay or consent" and dark patterns fail this bar.

**Pseudonymized vs. anonymized:** pseudonymization (identifiers replaced with keys you still hold) is a *safeguard* — the data remains personal data. True anonymization is effectively irreversible de-identification; *most "anonymized" data isn't*. Re-identification with a few auxiliary data points is a demonstrated research result for location and movie-rating datasets — treat re-identification risk as a design input.

**Subject rights (mechanics):** access (export what you hold, *about them*), erasure ("delete me" vs backups and immutable logs), portability (machine-readable export). Honest answers: backups restore expired erasures unless retention tiers exist; security logs may be exempt where they serve legal obligations — with limits.

**DPIA (Art. 35):** for high-risk processing — systematic monitoring, large-scale special categories. Structure: processing description → necessity/proportionality → risk register (likelihood × impact per risk) → mitigations → **residual risk with a named acceptor** (L04's discipline, formalized).

**Breach notification:** supervisory-authority notification on the 72-hour-style timeline where risk exists; your incident-response runbook (L31) must have this branch.

## Conceptual Diagram

```text
delete-me request ─► primary store ─► replicas ─► backups (retention tier) ─► logs (exempt? limited)
                                   └► feature store (the DS corner everyone forgets)
k-anonymity check: is each "person" indistinguishable from k−1 others on the quasi-identifiers?
   (a check, not a guarantee — auxiliary data defeats small k)
```

## Realistic Examples

- **CS track:** the erasure pipeline diagram: what must change in primary store, replicas, backups, logs, and the ML feature store — the delete-propagation design is the deliverable.
- **DS track:** re-identification risk: a "de-identified" location dataset re-identified with a few spatio-temporal points (cited study in `case-studies/`); students compute the effective k of their lab dataset and its failure modes.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "We anonymize, so GDPR doesn't apply" | Most "anonymized" data is pseudonymized; the test is irreversibility, not intention. |
| "Encryption makes anything compliant" | Encryption is one safeguard (Art. 32-class); minimization and purpose still bind. |
| "Erasure means wiping every copy, always" | There are lawful carve-outs (legal obligations, security logs); the design question is retention tiers, not absolutism. |
| "A DPIA is paperwork after launch" | It is a design gate: risks found before launch cost less and sign-off means something. |

## Classroom Activities

1. **Principle surgery (15 min):** a campus app collecting location "just in case" — rewrite the data spec to minimization.
2. **Checkpoint F (12 min).**
3. **Lab 26 (40 min):** DPIA workshop — the "campus safety analytics" system (cameras + Wi-Fi presence): risk register ≥ 6, mitigations, residual risks; DS students lead re-identification analysis, CS students lead controls mapping.
4. **k-anonymity mini-exercise (8 min):** compute k on a small table; find the quasi-identifier that breaks it.

## Discussion Questions

1. Is "we anonymize" ever fully true? What would you demand before believing it?
2. Security logs conflict with erasure rights — design the compromise (hashing, retention tiers) and state its limits.
3. Who signs the DPIA's residual-risk line, and what does that signature mean legally vs. morally?

## Problem-Solving Exercise

> The safety-analytics system wants 30-day location retention, third-party analytics sharing, and has no deletion path.
> **Deliverable:** DPIA risk register (≥ 6 entries with likelihood/impact); the minimized redesign that still meets the stated purpose; the rights-workflow sketch (access + erasure); the breach-notification plan fragment.

## Summary

Privacy engineering is minimization with receipts: collect less, keep it shorter, prove it with a DPIA, and honor rights in architectures never designed for deletion. Module 7 ends — Module 8 assembles everything into the capstone.

## Exit Ticket

1. Name three GDPR-style principles and their engineering translation.
2. Why is pseudonymized data still personal data?
3. What breaks "delete me" first: backups or logs?

## References

- EU GDPR, Articles 5, 15–22, 32–35. https://gdpr-info.eu (unofficial mirror; official: EUR-Lex)
- NIST Privacy Framework 1.0. https://www.nist.gov/privacy-framework
- de Montjoye, Y.-A. et al., "Unique in the Crowd," *Scientific Reports*, 2013 (re-identification with 4 spatio-temporal points).
- Sweeney, L., "Simple Demographics Often Identify People Uniquely," Carnegie Mellon U., 2000 (k-anonymity lineage).
