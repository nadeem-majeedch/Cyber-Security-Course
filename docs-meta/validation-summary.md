# Validation Summary — What Was Actually Run
**Independent QA audit · Date: 2026-09-19 · Environment: Windows (MSYS bash), Python 3.14, Node v24, OpenSSL 3.5**

## Executed checks [V]

| # | Check | Method | Result |
|---|---|---|---|
| 1 | Case validator | `python case-studies/tools/validate_cases.py` | exit 0 — `ALL CHECKS PASSED` (100/100 cases, components, keys, index) |
| 2 | Assessments validator | `python assessments/tools/validate_assessments.py` | exit 0 — 15 papers, 12 bank files, 0 duplicate stems, no student-tier key leakage |
| 3 | Slides validator | `python assessments/tools/validate_slides.py` | exit 0 — 32 lectures + 2 reviews + 1 template, contract + notes + case-ID checks |
| 4 | Calendar validator | `python calendar/tools/generate_calendar.py --validate-only` | exit 0 — 16 weeks, 32 lectures, Mon/Thu, alignment OK, links resolve |
| 5 | Artifact counts | `ls`/`wc -l` on plans, notes, guides, decks, labs, cases, quizzes | 32/32/32/32, 31 lab dirs, 100 cases, 15 quiz papers |
| 6 | Checkpoint paper↔key comparison | scripted regex item-number diff (papers quiz-02/04/06/10/12/14 vs `checkpoint-keys.md`) | **H1 confirmed**: keys stop at item 6; papers go to 7–8 |
| 7 | Website tree inspection | `os.walk`, `ls`, read attempts | **H2 confirmed**: locked dir `index-template.md`, empty module dirs (7/8), no index, no workflow |
| 8 | Core-lab 16-component check | per-component grep × 8 core labs | 8/8 per component (after fixing two auditor regex false negatives — first pass 0/8 on three components was checker error, recorded as I7) |
| 9 | Notes component scan | `grep -L` for References/CLO/DS content | 0 missing references, 0 missing CLO; L32 only note without DS content (L1) |
| 10 | Per-CLO note tag counts | grep CLO-1..8 across notes | CLO-1:6, 2:5, 3:4, 4:7, 5:4, 6:5, 7:5, 8:7 (thin tags → L2) |
| 11 | Placeholder/encoding scan | repo-wide grep TODO/TBD/FIXME/PLACEHOLDER + U+FFFD/CJK/Arabic char scan | 0 content markers (one self-reference in a prior report), 0 anomalies |
| 12 | WCAG contrast computation | WCAG relative-luminance ratio for theme palette | 18.9 / 11.2 / 10.3 / 7.5 : 1 — all pass AA |
| 13 | Lab 15 starter execution | `--help`, `sha256` path, `aead`, `kdf` subcommands | sha256/hmac work; aead/kdf degrade gracefully with VM instructions (L3) |
| 14 | openssl AEAD claim | `openssl enc -aes-256-gcm` | fails as taught ("AEAD ciphers not supported") — I5 reproduced |
| 15 | Safety pattern scan | repo-wide grep for prohibited technique/tooling terms | 4 hits, all ATT&CK names in defensive context (I4) |
| 16 | Internal-link audit | scripted scan of 232 md files + manual verification of the zero-link convention | 0 internal md links authored (M5); calendar-generated links all resolve (check 4) |
| 17 | Repo link/dot-markup spot audit | `cat -A` byte inspection of syllabus §5 | ●/○ dots intact — a suspected corruption was disproven |
| 18 | Tool availability | `command -v` for marp/tshark/lynis/nmap/john/hashcat | all ABSENT (basis for M1, H3) |
| 19 | Site-build attempt | existence checks for index/workflow | build impossible — H2/I6 |
| 20 | Earlier-session evidence carried forward | `git ls-remote` (public repo), calendar regeneration with second start date | basis for C1; calendar reconfigurability [V] |

## Not run [N] — with reasons

| Check | Reason | Consequence |
|---|---|---|
| Marp HTML/PDF/PPTX rendering | Marp CLI not installed; out of audit scope to install tooling | Rendering quality **unverified** (M1) |
| Lab VM/dataset/capture walkthroughs | Infrastructure artifacts do not exist; VM/tooling absent | Practical instructions remain **unverified** (H3) |
| python-vs-openssl digest cross-check | Failed mid-run: `/tmp` fixture path split under Windows/MSYS broke the test, not the content | Cross-check rests on earlier recorded run (L4) |
| GitHub Pages deployment | No workflow exists; building one is remediation, not audit | Deployment behavior **unverified** (H2) |
| Full LMS JSON import round-trip | No LMS available in environment | JSON well-formed by construction (json.dump); consumer-side behavior unverified |
| HTML rendering of student-calendar.html in a browser | Static file inspection only (print CSS present, structure valid) | Visual print layout **unverified** |

## Honest-summary statement

Every "PASS" in `final-course-audit.md` cites an executed command or direct file inspection from the table above; every "CONDITIONAL" or open finding traces to a numbered register entry. Where the auditor's own tooling errored (regex false negatives, `/tmp` path handling, an initial zero-link false suspicion), the error is recorded rather than smoothed over. No test was claimed that was not run.
