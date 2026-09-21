# Assessment Package — Coverage & Validation Report
**Date: 2026-09-19 · Validator: `assessments/tools/validate_assessments.py` (executed; exit 0 — "ALL CHECKS PASSED")**

## 1. Deliverable inventory

| Component | Location | Count |
|---|---|---|
| Weekly quiz papers (student, questions only) | `assessments/student/quizzes/quiz-01..15.md` | 15 |
| Checkpoint papers (student) | Q2/4/6/10/12/14 = Checkpoints A–F | 6 (within the 15) |
| Specimen exam papers (student) | `specimen-midterm.md`, `specimen-final.md` | 2 |
| Question bank files | `instructor-only/question-bank/QB-M1..M8, QB-MT, QB-FE, QB-SM, QB-SF` | 12 |
| Banked items | 80 module MCQ+SA · 16 exam items · 24 specimen items | **120** |
| Live exam papers + marking schemes (A/B variants) | `midterm-paper.md`, `final-paper.md` | 2 |
| Capstone instructions (student) + rubric/moderation (instructor) | `capstone-brief.md`, `capstone-rubric.md` | 2 |
| Practical lab assessment guide | `practical-assessments.md` | 1 |
| Short assignments SA-1…SA-6 | `short-assignments.md` | 6 briefs |
| Case-study activity brief | `case-study-activity.md` | 1 |
| Oral defense & presentation rubric | `oral-defense-rubric.md` | 1 |
| Pre-existing: checkpoint keys, lab keys | unchanged (one pointer sentence added) | 2 |

**16 weekly assessment units:** Weeks 1–15 each carry a quiz unit (six of them are the graded Checkpoints A–F; Week 8's unit is the midterm itself with a pre-midterm specimen); Week 16 is the final-exam unit. Map in `question-bank/README.md`.

## 2. Validation performed (machine-checked)

1. **Structure:** 15 quiz papers present; Q2/4/6/10/12/14 verified as checkpoint papers; no answer-key markers (✔ / Key / Explanation) in any student paper.
2. **Bank integrity:** every MCQ carries a ✔ key, explicit key letter, and explanation; every SA carries a key; CLO + Bloom tags on all items; exam/specimen item blocks all keyed.
3. **Duplicate check:** normalized question stems across quizzes + specimen pools → **0 duplicates**. Bank README documents the standing duplicate-avoidance rule (shown specimens are contaminated for live use; makeup packs MT-1…MT-9 pre-designated).
4. **Leakage scan:** tightened marker set across all student-tier files → 0 hits; answer-key headings → 0. (First run caught the student README naming the instructor-only path — reworded rather than weakened the check; validator false positives on disclaimers were fixed in the validator, documented here.)
5. **CLO coverage:** all eight CLOs present in bank tags.
6. **Mark totals:** bracketed per-item marks reconciled against stated totals (checkpoint papers record /10 by design; one bonus +1 item allowed).

**Defects caught and fixed during validation (honest log):** (1) SM/SF pools lacked explicit `Bloom:` fields → added; (2) README path reference → reworded; (3) validator's own over-matching leakage markers and item-block parser → corrected in the validator; all changes are content/format fixes, none weaken a real check.

## 3. CLO × Bloom coverage (bank-wide)

| CLO | Items | Bloom span | Reaches weekly units |
|---|---|---|---|
| CLO-1 | 18 | Understand→Evaluate | Q1, Q3, Q8, Q15, MT, FE |
| CLO-2 | 15 | Apply→Evaluate | Q1, Q3, Q8, MT, FE |
| CLO-3 | 13 | Apply→Evaluate | Q3, Q5, MT, FE |
| CLO-4 | 15 | Apply→Create | Q5, Q7, Q8, MT, FE |
| CLO-5 | 16 | Understand→Evaluate | Q9, Q11, Q15, FE |
| CLO-6 | 16 | Analyze→Create | Q11, Q13, Q15, FE |
| CLO-7 | 16 | Apply→Evaluate | Q13, Q15, FE |
| CLO-8 | 17 | Understand→Create | Q15, MT(IR), FE |

Every CLO appears in at least one graded (checkpoint/exam) unit and one formative (specimen) unit. Difficulty distribution: Easy 32 · Medium 62 · Hard 28 · Expert 2.

## 4. Consistency with the approved syllabus

- Weights verified against `syllabus.md` §9: labs 30% (best 6 of 8), checkpoints 15% (lowest dropped), midterm 15%, case-study brief 10%, capstone 20% (≥ 40% floor), final 10%. All student-facing documents state these identically; `capstone-rubric.md` enforces the floor at moderation.
- Quiz cadence matches the weekly schedule's assessment-due column (checkpoints at module ends).
- Checkpoint A–F item counts match the pre-existing keys exactly (6–8 items, recorded /10).

## 5. Known limitations

1. Live exam papers assemble from bank + a 10-item MCQ pool embedded in each paper file — final paper assembly per-term is an instructor task; the specimen papers are drawn from different items by construction (validated).
2. Quiz mark-total check tolerates +1 bonus items; check-point /10 recording is accepted by design, not verified arithmetically.
3. The public-repo exposure issue applies with full force to this tier: `midterm-paper.md` and `final-paper.md` are complete live exams in a public repository — moving this tier to a private location before term start is no longer optional, it is required.
