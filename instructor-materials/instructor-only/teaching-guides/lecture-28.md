# Teaching Guide — Lecture 28 (Privacy Engineering + Checkpoint F)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: investigation timelines | One team's grid. |
| 08–30 | Principle surgery | The always-on location app rewritten to minimization. |
| 30–48 | Rights mechanics | Erasure vs backups/logs; retention tiers. |
| 48–60 | Break | — |
| 60–72 | **Checkpoint F** | 10 min + most-missed recap. |
| 72–105 | Lab 26 (DPIA workshop) | Campus safety analytics; CS/DS role split. |
| 105–115 | Re-identification teaser | k-anonymity mini-exercise. |
| 115–120 | M7 wrap + capstone logistics | Team formation reminders. |

## Board/Projector Activities

- **Board:** the delete-propagation diagram (primary → replicas → backups → logs → feature store) drawn live; the k-anonymity table.
- **Handout:** DPIA template (sections pre-labeled); the scenario pack.

## Speaker Notes (key beats)

1. Principles → engineering translations: the table is the lecture; minimization is *schema-level*, not aspirational.
2. Consent quality: freely given, specific, revocable — "pay or consent" and dark patterns fail the bar; say it plainly.
3. Pseudonymized ≠ anonymized: the keys you hold keep it personal data; the re-identification studies make the risk concrete.
4. Rights mechanics with honesty: backups restore expired erasures unless retention tiers exist; security logs have lawful carve-outs *with limits*.
5. DPIA: risk register + mitigations + residual risk with a named acceptor — L04's discipline, formalized by law.
6. Breach-notification branch in the IR runbook (L31 callback).

## Expected Student Difficulties

- "GDPR is a legal topic, not mine." Fix: every principle lands as a *schema and pipeline* decision; the DS-track re-identification analysis makes it quantitative.
- Erasure absolutism vs. exemption nihilism. Fix: retention tiers as the design answer — not everything deleted, nothing kept unmanaged.
- The DPIA feels like form-filling. Fix: the risk register is where thinking lives; the form is scaffolding.

## Teaching Tips

- The campus-safety scenario is deliberately uncomfortable (cameras + presence tracking) — that discomfort generates genuine DPIA material.
- Enforce the CS/DS role split in teams; the DPIA is the course's clearest dual-track artifact.
- Checkpoint F recap: the most-missed items historically are pseudonymization status and the delete-me order (backups first).

## Answer Keys **[KEY]**

- Checkpoint F: see `assessments/instructor-only/checkpoint-keys.md` §F.
- DPIA expected risks (≥ 6 of): function-creep beyond stated purpose; re-identification of presence data; third-party sharing without purpose limitation; retention without expiry; access-control gaps on raw footage; consent not revocable; breach exposure of location history; chilled behavior effects.
- Exit ticket: 1 minimization→schema; storage limitation→retention schedules; accountability→documentation (accept others with translation); 2 the mapping keys are retained → re-identifiable → still personal data; 3 backups (then logs).

## Lab Delivery (Lab 26)

- Minimum viable outcome: DPIA with ≥ 6 risks, mitigations, and residual-risk line; rights-workflow sketch.
- Expected failure points: risks without likelihood/impact (add the columns); mitigations without owners (require named roles); teams writing "delete all data" as mitigation — push for tiered retention.

## Discussion Facilitation

Q2 (logs vs erasure) is the honest design compromise: hash identifiers in logs, tier retention, document the legal basis — and state the residual gap in the DPIA rather than pretending it away. Q3 (the signature) separates legal accountability from moral ownership; let that tension stand — it is real.

## Accessibility

- DPIA template: pre-labeled sections, screen-reader navigable; the risk register as a spreadsheet with dropdown scaffolding.
- The k-anonymity table: large-print handout; the computation is arithmetic and works entirely from the table.
