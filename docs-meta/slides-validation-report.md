# Slides Package — Coverage & Validation Report
**Date: 2026-09-19 · Validator: `assessments/tools/validate_slides.py` (executed; exit 0 — "ALL CHECKS PASSED")**

## 1. Deliverable inventory (36 files)

| Component | Location | Count |
|---|---|---|
| Lecture decks (Marp Markdown) | `instructor-materials/instructor-only/slides/lecture-01..32.md` | 32 |
| Midterm review deck | `slides/midterm-review.md` | 1 |
| Final review deck | `slides/final-review.md` | 1 |
| Case-session template (6-step protocol) | `slides/case-session-template.md` | 1 |
| Marp theme (accessibility baseline) | `slides/theme.css` | 1 |

Format baseline and build instructions: `slides/README.md`. Speaker notes are embedded as Marp HTML comments — one per slide with timing guidance and failure pivots.

## 2. Deck contract (per lecture, machine-verified)

Title · objectives · concept slides · ≥ 1 labeled ASCII diagram with `*Describe:*` text line · CS-track example · DS-track example · misconception/pitfall content · **lab-demo slide with sandbox safety line + MVO** · **case-session slide citing exact case IDs** · wrap-up/exit ticket · references.

## 3. Validation performed (evidence)

1. **Structure:** 32/32 decks exist with Marp front matter; zero placeholder markers (TODO/TBD/PLACEHOLDER).
2. **Contract:** every required component present in every deck per regex checks; lab-demo slides carry MVO lines; every non-title content slide carries speaker notes (References-only slides exempt as bibliographic — documented in the validator).
3. **Case references:** 41 case IDs cited across decks; **all verified against `case-studies/INDEX.md`** (cross-file consistency, no broken references).
4. **Tier separation:** no Marp decks exist in any student-facing tree (`lectures/`, `website/`) — decks embed answer-adjacent speaker notes and stay instructor-only.
5. **Review decks + template:** present, noted, and the template enforces the six-step protocol with the instructor-only solution pointer.
6. **Rendering status (honest):** Marp CLI is **not installed** in this workspace (Node v24 present). All rendering steps (HTML/PDF/PPTX export) are **untested**; decks are authored and validated as Markdown. Pre-term task: `npm install -g @marp-team/marp-cli`, then smoke-test one deck to HTML and PDF. This is flagged in `slides/README.md` and enforced as a README check in the validator.

**Defects caught by validation and fixed:** first run raised 42 findings — two real contract gaps (L30/L31 used non-standard CS/DS heading variants; renamed to the canonical pattern) and validator over-strictness (References slides and exam-day decks L16/L32 flagged for components they legitimately replace: exam administration replaces lab-demo/case-session, mirroring the hour-math precedent documented in the coverage report). All fixes are content or documented exemptions; no check was removed.

## 4. Design-quality notes

- **Slide density:** ≤ 6 bullets/slide, ≤ 12 words/bullet target; tables and fenced diagrams carry the load.
- **Diagrams:** ASCII in versionable fenced blocks — pipeline flows (L09/L10), zone maps (L14), handshake sequences (L18), rollout staircases (L24), lifecycle chains (L11/L20). Each labeled and paired with a `*Describe:*` screen-reader line.
- **Terminology:** locked to syllabus/CLO vocabulary; CWE/ATT&CK/STRIDE spellings consistent across decks, labs, and cases.
- **Accessibility:** ≥ 24 px body via theme, high-contrast palette, text descriptions for every diagram, no color-only meaning — per the approved quality standard.
- **Speaker notes:** every slide has timing beats, misconception callouts, demo pivot plans, and the case-protocol enforcement reminders.

## 5. Known limitations

1. **Rendering untested** (no Marp CLI in workspace) — the only untested step in the pipeline; one-deck smoke test required before term.
2. Deck case-session slides name one case each from the INDEX's per-module suggestions; instructors may substitute any case from the same module's suggested list.
3. L32's deck documents the showcase/exam day shape; per-term room/logistics details live in the exam papers' logistics sections.
