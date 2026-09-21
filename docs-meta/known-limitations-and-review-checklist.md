# Known Limitations & Manual Review Checklist
**Handover date: 2026-09-19 · Companion to `handover-validation-report.md`. Items here are honest gaps — not hidden warnings.**

## A. Known limitations (open, with owners-by-role)

| ID | Limitation | Impact | Where tracked |
|---|---|---|---|
| C1 | Instructor-only tiers (live exams, keys, solutions, decks) sit in a **public** repository | Delivery-blocking: students could read every assessment | `findings-register.md` — remediation designed, execution is the owner's (private repo / LMS) |
| H3 | Lab infrastructure not built (VM snapshots, prepared captures, log datasets, evidence packs); instructions untested at delivery fidelity | Labs cannot run as written until built | Acceptance specs inside each core worksheet; first-delivery walkthrough required |
| M1 | Marp rendering never executed (CLI absent in authoring environment) | Slide visual output unverified; Markdown content validated | Pre-term smoke test in `handover-guide.md` §2 |
| L3/L4 | Lab 15 starter aead/kdf paths and the digest cross-check not executed in this environment | Minor; documented degradation behavior | `lab-keys.md` ledger |
| — | Website deployment not executed (requires owner access) | Site is built but not live | `pages-publication.md` steps |
| — | LMS JSON import and browser print layout unverified | Low risk; well-formed by construction | manual checklist B7/B8 |
| — | Textbook editions cited generically; library access unconfirmed | Pre-term administrative task | `handover-guide.md` §2.6 |
| — | Case-study solution scaffolding for L4 cases is facilitation-grade around each reference position | Instructors extend with current-term context | `case-coverage-report.md` §6 |

## B. Manual review checklist (for the instructor, in order)

1. **[C1 — do first]** Move `instructor-materials/instructor-only/` and `assessments/instructor-only/` to a private location; verify no student-facing path links into them (the website build guard covers only `website/`).
2. **[Read-through]** Skim `syllabus.md` end-to-end; confirm department-mandated sections/policies are present and weights match your program's rules.
3. **[Spot-teach]** Pick any two lectures and "dry-run" them from deck + guide + notes; confirm the timing plan and speaker-note beats match your style.
4. **[Keys sanity]** Read `assessments/instructor-only/checkpoint-keys.md` against the six quiz papers; adjust item 7–8 model answers to your context if desired (newly written — H1 fix).
5. **[Marp]** Install Marp, render one deck to HTML + PDF, check pagination/theme; then batch-render all decks.
6. **[Calendar]** Run `python calendar/tools/generate_calendar.py --start YOUR-MONDAY`; check the dated student view and your planning calendar; confirm W16's dates avoid your institution's exam blackout windows.
7. **[LMS]** Import `calendar-semester.json` into the LMS (or hand-enter key dates); adjust.
8. **[Print]** Open `calendar/generated/student-calendar.html` in a browser; print-preview one page range.
9. **[Labs — H3]** Build the infrastructure pack per the worksheets' acceptance criteria; run one core lab end-to-end personally before term.
10. **[Publish]** Follow `pages-publication.md`; verify the deployed URL loads (a green Actions run alone is not verification).
11. **[Safety re-read]** Re-read the responsible-use rules in `labs/README.md` and the safety contract in the L09/L10 materials; confirm they match your institution's lab policy.
12. **[Accessibility]** Spot-check one deck's rendered output at high zoom and one lab handout with a screen reader if possible.

## C. Explicitly not done (to avoid concealing findings)

Nothing was removed, rewritten, or excluded to make the audit findings disappear: H1/H2/M2/M3/M4/M6/L1/L2 were **fixed with content** (see `handover-validation-report.md` §2); H3/M1/publication are **left open with instructions** rather than declared complete; the audit trail (`final-course-audit.md`, `findings-register.md`, `validation-summary.md`) is preserved verbatim with its original severities, including the closed informational items.
