# Student Usage Guide

**How to use the course materials, week by week.** (Your instructor publishes dated versions of the schedule; the fixed structure is on the course website's [schedule page](../website/calendar.md) or in `calendar/generated/student-calendar.md`.)

## A normal week

1. **Before the first session:** skim the two lecture notes for the week (start at the course website index or `lectures/module-0X-*/`). Each note lists its learning objectives at the top — those objectives are what the exit ticket and checkpoint will ask about.
2. **In the sessions:** you'll see a case study projected in the first or second hour — spend the five-minute proposal window actually proposing, with reasons. Cases are simulated scenarios; the point is your reasoning, not the "right answer."
3. **Lab time:** every session includes guided lab work on the isolated course environment. Your worksheet is in `labs/lab-NN-…/README.md`. Read the responsible-use rules at the top before touching anything — they are enforced, not decorative.
4. **Consolidation (last 10 minutes):** exit ticket. Ungraded, but tracked — it's how the teaching team spots trouble early.

## Assessments, honestly

- **Checkpoints A–F** (weeks 2, 4, 6, 10, 12, 14): 12-minute closed-book quizzes, 1 mark per concept item, 2 marks per scenario item. Your lowest checkpoint is dropped at term end.
- **Specimen quizzes** (other weeks): ungraded self-checks. Do them — they are the checkpoint question style with training wheels.
- **Lab reports:** best 6 of 8 count (30% of the course). Evidence must be produced by you, in your VM — shared screenshots are treated as collusion. Each lab names its minimum viable outcome; hitting it anchors you at the 70% band.
- **Midterm (week 8) and final (week 16):** format is public (`assessments/student/specimen-midterm.md` / `specimen-final.md`); the live papers use different items. Answer keys are never posted — specimen answers are discussed in tutorials.
- **Case-study brief** (week 12, 10%): pick a Level 3+ case, register it in week 11, write the four-part brief.
- **Capstone** (weeks 15–16, 20%, non-compensable ≥ 40% floor): one system, one traceable chain — threat model → controls → detections → IR runbook — defended orally. The defense rubric rewards honest residual-risk statements, not bravado.

## Where things live

| You want… | Go to |
|---|---|
| Lecture notes | `lectures/module-0X-*/lecture-NN.md` or the website |
| Lab worksheets | `labs/` |
| Case scenarios | `case-studies/collection/level-N-….md` |
| Quiz papers & specimen exams | `assessments/student/` |
| Task briefs (assignments, capstone, case activity) | `assessments/student/*.md` |
| Dated schedule | `calendar/generated/student-calendar.md` |

## Integrity, in one paragraph

Screenshots and outputs must come from your own environment and your own runs. Datasets are cited by version. Cases are simulated — treat fictional organizations as fiction, and never present a case's contents as a real incident. And the course bright line: **no system outside the course sandbox, ever** — report real-world findings through responsible disclosure, don't probe them.
