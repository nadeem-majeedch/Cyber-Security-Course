# Instructor Handover Guide

**Audience:** the instructor (or teaching team) receiving this course package.
**Status at handover:** content complete, validators green, delivery-blocking items flagged below. Full audit trail: `final-course-audit.md`, `findings-register.md`, `validation-summary.md`.

## 1. What you are receiving

| Layer | Where | State |
|---|---|---|
| Syllabus (CLOs, weights, schedule) | `syllabus.md` | Complete |
| 32 lecture plans (minute-by-minute) | `instructor-materials/instructor-only/lecture-plans/` | Complete |
| 32 teaching guides (timing, speaker notes, answer keys, accessibility) | `instructor-materials/instructor-only/teaching-guides/` | Complete |
| 35 slide decks + case-session template (Marp Markdown) | `instructor-materials/instructor-only/slides/` | Complete; rendering untested (M1) |
| Instructor planning calendar | `instructor-materials/instructor-only/calendar/` | Generated per term |
| Question bank (120 items) + exam papers + keys | `assessments/instructor-only/` | Complete; **exposure risk C1** |
| 32 student notes | `lectures/` | Complete |
| 14-lab program (8 graded) | `labs/` | Worksheets complete; **infrastructure missing (H3)** |
| 100 case studies + solutions | `case-studies/` + `instructor-only/case-solutions/` | Complete |
| 16 weekly assessment units | `assessments/student/quizzes/` + papers | Complete |
| Website + Pages workflow | `website/`, `.github/workflows/pages.yml` | Built; **deployment not yet executed** |

## 2. Before term — do these in order

1. **Move the instructor-only tiers private** (finding C1, blocker). Live exam papers and all keys are in a public repo. Options: private companion repo, or campus LMS. Keep the public repo student-only.
2. **Build the lab infrastructure** (H3): VM snapshots, prepared captures, log datasets, evidence packs — each core worksheet lists its acceptance criteria. Then run a first-delivery walkthrough of each core lab and record tested/untested in `assessments/instructor-only/lab-keys.md`.
3. **Install Marp and render one deck** (`npm i -g @marp-team/marp-cli`, then `marp instructor-materials/instructor-only/instructor-only/slides/lecture-01.md -o /tmp/t.html --theme theme.css` from the slides directory) — rendering has never been executed (M1).
4. **Pick your semester start date** and run `python calendar/tools/generate_calendar.py --start YYYY-MM-DD` (Monday). The dated student calendar lands in `calendar/generated/`; your planning calendar in `instructor-materials/instructor-only/calendar/`.
5. **Verify checkpoint item 7–8 marking expectations** (newly keyed — see `checkpoint-keys.md`); adjust wording to your section's context if desired.
6. **Confirm library access** for the core texts; editions are cited generically where the department chooses.
7. **Decide the case-brief registration workflow** (Week 11; see `assessments/student/case-study-activity.md`).

## 3. Operating the semester

- **Weekly rhythm per session:** prep pointers are one row each in your planning calendar (deck + guide + plan). Checkpoint weeks: print the quiz paper, carry the key, 12 minutes, record /10 (A converts — rule stated in the keys file).
- **Case sessions:** run the six-step protocol (`slides/case-session-template.md`); the model solution file stays closed until step 5.
- **Grading:** lab rubric 40/30/30 (correctness/evidence/remediation) with the best 6 of 8 counting; capstone report 70% / defense 30% of the 20% component (arithmetic in `assessments/instructor-only/capstone-rubric.md`).
- **Moderation:** capstone calibration + blind first pass + borderline rule are mandatory per the rubric's moderation section.

## 4. When content changes

Lecture notes, labs, and cases are the source of truth. If you edit a note's title, the calendar generator will refuse to build until the calendar model matches — that is the drift guard working. Re-run all four validators before redistributing anything (commands in the root `README.md`).

## 5. If this repository stays public

Everything under `instructor-only/` is readable by anyone until it moves. The website deploy workflow fails the build if instructor material appears in `website/`, but it cannot protect the rest of the repo. Treat C1 as the first action of the term, not the last.
