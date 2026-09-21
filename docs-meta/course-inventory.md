# Course Inventory — Actual Repository Counts
**Handover date: 2026-09-19 · Counts taken by direct `ls`/`grep`/`find` execution during the final handover review; every count re-verifiable with the command shown.**

## Teaching content

| Artifact | Count | Location | Verify with |
|---|---|---|---|
| Lecture plans (instructor) | **32** | `instructor-materials/instructor-only/lecture-plans/lecture-01..32.md` | `ls instructor-materials/instructor-only/lecture-plans/lecture-*.md \| wc -l` |
| Student lecture notes | **32** | `lectures/module-0{1..8}-*/lecture-01..32.md` | `ls lectures/module-*/lecture-*.md \| wc -l` |
| Teaching guides (instructor) | **32** | `instructor-materials/instructor-only/teaching-guides/` | `ls instructor-materials/instructor-only/teaching-guides/lecture-*.md \| wc -l` |
| Slide decks | **32** + review decks **2** + case-session template **1** | `instructor-materials/instructor-only/slides/` | `ls instructor-materials/instructor-only/slides/lecture-*.md \| wc -l` |
| Instructor manual | **1** | `instructor-materials/instructor-only/instructor-manual.md` | — |

## Labs

| Item | Count | Detail |
|---|---|---|
| Lab directories | **31** | `labs/lab-00-…` through `labs/lab-30-…` |
| Designated lab program | **14** (8 core graded + 6 enrichment) | per `labs/README.md` crosswalk (authoritative) |
| Core graded labs | **8**: 00, 12, 15, 19, 23, 27, 28, 29 | best 6 of 8 count (30%) |
| Enrichment worksheets | **23** total worksheets incl. consolidated suites | 16-component contract on graded labs |
| Tested starter code | **1** (`labs/lab-15-crypto-integrity/starter/crypto_lab.py` — sha256/hmac paths executed; aead/kdf degrade gracefully) | remaining infrastructure: **not built** (finding H3) |

## Case studies

| Item | Count | Detail |
|---|---|---|
| Cases total | **100** | CS-001..CS-100 |
| Level 1 / 2 / 3 / 4 | **20 / 25 / 30 / 25** | `case-studies/collection/level-{1..4}-*.md` |
| Instructor solution sections | **100** | `instructor-materials/instructor-only/case-solutions/` (six components per case) |
| Domains covered | 18 required domains incl. university + enterprise + DS-specific | `case-studies/INDEX.md` |

## Assessments

| Item | Count | Detail |
|---|---|---|
| Weekly quiz papers (student) | **15** | `assessments/student/quizzes/quiz-01..15.md` — includes Checkpoints A–F at weeks 2/4/6/10/12/14 |
| Weekly assessment units | **16** | week 8 = midterm unit, week 16 = final unit (map: `question-bank/README.md`) |
| Specimen exam papers | **2** | midterm + final (student tier, questions only) |
| Question bank items | **120** | 80 module MCQ+SA + 16 exam + 24 specimen — CLO/Bloom/difficulty tagged |
| Live exam papers + marking schemes | **2** (A/B variants) | `assessments/instructor-only/{midterm,final}-paper.md` |
| Checkpoint key sections | **6**, items 1–8 keyed per checkpoint | `checkpoint-keys.md` (H1 fixed) |
| Short assignments | **6** (SA-1..6) | `assessments/student/short-assignments.md` |
| Rubrics | capstone (report+defense, with mark split), lab ledger, case rubrics, oral defense | student + instructor tiers |

## Calendar & website

| Item | State |
|---|---|
| Calendar generator | `calendar/tools/generate_calendar.py` — one command, configurable start |
| Generated student views | `calendar/generated/student-calendar.md` + `.html` (printable) |
| Generated instructor view | `instructor-materials/instructor-only/calendar/instructor-calendar.md` (M2 fixed) |
| LMS JSON | `calendar/generated/calendar-semester.json` (32 sessions) |
| Website | `website/index.md` + `calendar.md` + **32 mirrored notes** (8 modules) |
| Pages workflow | `.github/workflows/pages.yml` — with instructor-content guard; **deployment not yet run** |

## Validation tooling

| Script | Coverage |
|---|---|
| `case-studies/tools/validate_cases.py` | case counts, components, solutions, index |
| `assessments/tools/validate_assessments.py` | papers, bank keys, leakage, duplicates, mark totals, **checkpoint paper↔key coverage** |
| `assessments/tools/validate_slides.py` | deck contract, speaker notes, case-ID integrity, tier separation |
| `calendar/tools/generate_calendar.py --validate-only` | 16×32 structure, dates, alignment, generated-link resolution |
