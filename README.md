# Cyber Security Course — BS CS / BS Data Science (7th Semester)

University-level course: **32 lectures × 2 hours = 64 contact hours · 16 weeks · 8 modules**, progressing from security foundations to a defended capstone. Dual-track: Computer Science and Data Science students each lead in parts of the course (M3–M5 CS-intensive, M6 DS-intensive).

> **Status: ✅ content complete — ready for instructor review.** All teaching artifacts exist in both tiers (plans, notes, guides, labs, 100 case studies, assessments, slides, calendar); four repo validators pass. Publication and delivery steps: `docs-meta/handover-guide.md`. Known open items: `docs-meta/findings-register.md`.

## Repository map

| Path | Purpose | Audience |
|---|---|---|
| `syllabus.md` | Course description, CLOs, schedule, assessment strategy, readings | Students + staff |
| `lectures/` | 32 student-facing lecture notes (8 module directories) | Students |
| `labs/` | 14-lab program (8 core graded + enrichment) — worksheets + safe starter code | Students |
| `case-studies/` | 100 **simulated** progressive scenarios (Levels 1–4) with model solutions instructor-side | Students |
| `assessments/student/` | Weekly quiz papers, specimen exams, task briefs, rubric summaries | Students |
| `assessments/instructor-only/` | Question bank, answer keys, live exam papers, moderation guides | **Teaching staff only** |
| `instructor-materials/instructor-only/` | Lecture plans, teaching guides, slide decks with speaker notes, planning calendar | **Teaching staff only** |
| `calendar/` | One-click semester calendar generator + generated views | Students + staff |
| `website/` | GitHub Pages source (student-facing hub) | Public |
| `docs-meta/` | Architecture, roadmap, audit findings, validation reports | Planning |

## Quick navigation

- Course requirements & CLOs → `docs-meta/architecture-and-requirements.md`
- Staged roadmap & quality gates → `docs-meta/implementation-roadmap.md`
- Weekly schedule (dated) → `calendar/generated/student-calendar.md` (regenerate: `python calendar/tools/generate_calendar.py --start YYYY-MM-DD`)
- Instructor handover guide → `docs-meta/handover-guide.md`
- Student usage guide → `docs-meta/student-guide.md`
- Latest audit results → `docs-meta/final-course-audit.md` + `docs-meta/findings-register.md`

## Validators (run before any hand-off)

```bash
python case-studies/tools/validate_cases.py        # 100-case completeness
python assessments/tools/validate_assessments.py   # quiz/exam structure, keys, leakage
python assessments/tools/validate_slides.py        # deck contract + speaker notes
python calendar/tools/generate_calendar.py --validate-only  # 16×32 structure + links
```

## Ethics

All materials teach **authorized, defensive** cybersecurity. Labs use sandboxed, synthetic targets only; every demonstrated weakness is paired with defensive remediation. All 100 case studies are **simulated scenarios** (fictional organizations, clearly labeled) — no real incident is presented as fact. Attacking systems without written authorization is illegal and out of scope of this course.

**Distribution warning:** everything under `instructor-only/` tiers — including live exam papers and answer keys — must move to a private repository or the campus LMS **before term start** if this repository remains public. See `docs-meta/findings-register.md` (C1).
