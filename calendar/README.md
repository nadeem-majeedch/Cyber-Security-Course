# Semester Calendar — one-click generation

A calendar for the finalized course that is **generated from the repository's actual content**, never hand-maintained: lecture titles are verified against the live student notes at build time, labs follow the authoritative crosswalk in `../labs/README.md`, assessments mirror `../assessments/student/` and the syllabus weights, and case sessions mirror the instructor decks' case map.

## One-click generation

```bash
python calendar/tools/generate_calendar.py --start 2026-09-07
```

- `--start` = semester start date; **must be a Monday** (the course runs Monday + Thursday sessions, 2 h each — matching the syllabus' two-lectures-per-week structure).
- `--outdir` = output directory (default `calendar/generated/`).
- `--validate-only` = re-run all checks against existing output without regenerating.

Regenerate whenever course content changes; the generator refuses to build if any lecture title drifts from the actual notes.

## Outputs

| File | Audience | Format |
|---|---|---|
| `generated/student-calendar.md` | students | Markdown — week-per-section view with dates, outcomes, lab/assessment/case links |
| `generated/student-calendar.html` | students | **Printable** A4-styled HTML (print CSS embedded; `@media print` hides nav links and avoids page-breaks inside cards) |
| `generated/instructor-calendar.md` | **instructor-only** | planning table: per-session objectives, labs with type/due, assessments, cases, prep links to decks/guides/plans + logistics notes |
| `generated/calendar-semester.json` | LMS/tooling | machine-readable sessions (dates, CLOs, labs, assessments, cases) |

## Generation documentation (how the calendar is built)

1. **Titles** — parsed from `lectures/module-*/lecture-NN.md` H1 lines at build time and compared against the calendar model; any mismatch aborts generation ("calendar matches the actual course content" is enforced, not asserted).
2. **Weeks/sessions** — 16 weeks × 2 sessions = 32 sessions; session 1 = Monday, session 2 = Thursday of the same week, dated from `--start`.
3. **Labs** — per-session assignments from the `labs/README.md` crosswalk (authoritative for lab↔lecture alignment); the eight graded labs carry staggered due weeks (W2, W8, W9, W10, W11, W12, W14, W16 — best 6 of 8 count).
4. **Assessments** — the 16 weekly units from the question-bank map: six Checkpoints (W2/4/6/10/12/14), midterm W8, final W16, specimen quizzes otherwise, case brief W12, capstone milestone W15 + defense W16.
5. **Case studies** — one per lecture (except exam days), mirroring the case-session slides in the instructor decks.
6. **Validation** (runs automatically after generation; exit non-zero on any failure):
   - exactly 16 weeks, exactly 32 lectures, numbering 1–32 with no gaps
   - every session date is a Monday or Thursday
   - graded-lab set equals the 8 core labs; every Checkpoint letter appears in its assigned week
   - every assessment reference resolves to an existing file in `assessments/student/`
   - **every relative link in the generated Markdown/HTML resolves on disk** (labs, cases, quizzes, lecture notes, instructor prep links)

## Notes

- The instructor view lives under `../instructor-materials/` distribution rules — never publish it.
- To change the cadence (e.g., Tue/Fri), edit `session_dates()` in `calendar/tools/generate_calendar.py`; the validators adapt automatically.
- Default start `2026-09-07` is illustrative; departments regenerate with their own date.
