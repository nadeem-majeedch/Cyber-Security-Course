# Slide Decks — Instructor Presentation Resources (⚠️ instructor-only)

Marp-compatible Markdown decks, one per lecture, plus review decks and a case-session template. **They embed speaker notes → instructor-only tier.** Student summaries live in `../../lectures/`; do not publish decks as-is.

## Format decision

- **Marp (Markdown → HTML/PDF/PPTX)** — matches the repo's all-Markdown authoring model; decks remain fully readable as plain Markdown even without the renderer.
- **Rendering availability (honest status):** `marp` CLI is **not installed** in the authoring workspace (Node v24 is present). Rendering steps are therefore **untested**; install with `npm install -g @marp-team/marp-cli` (or use the VS Code Marp extension) and do a one-deck smoke test before term.
- Build: `marp lecture-01.md -o lecture-01.html --theme theme.css` (add `--pdf` or `--pptx` as needed).

## Deck contract (validated by `../../tools/validate_slides.py` via repo script)

Every lecture deck (`lecture-01.md` … `lecture-32.md`) contains, in order:
1. Title slide (lecture code, module, week, CLOs)
2. Objectives slide (3–5, verbatim-aligned with the lecture plan)
3. Concept slides (≤ 6 bullets, ≤ 12 words per bullet target)
4. At least one ASCII diagram slide (labeled; text description for screen readers)
5. CS-track + DS-track example slides (one each minimum)
6. Misconception or pitfall slide
7. Lab-demo slide(s) — what the instructor shows, sandbox-only, with the demo's minimum viable outcome
8. Case-session slide — cites exact case IDs/titles from `../../../case-studies/INDEX.md`
9. Wrap-up + exit-ticket slide (mirrors the lecture plan's formative items)
10. Speaker notes as Marp HTML comments (`<!-- ... -->`) on **every** content slide, including timing beats and the in-class pivot if the demo fails

`midterm-review.md` and `final-review.md` cover exam-format walkthrough and item-strategy; `case-session-template.md` runs the 6-step case protocol (projector → 5-minute proposal → group reasoning → discussion → model reveal → tradeoffs).

## Visual style & accessibility rules (theme.css)

- ≥ 24 px body text, high-contrast palette (#111 on #fff; headings #0b3d66; emphasis #7a1f1f) — checked ratios for WCAG AA.
- Diagrams are ASCII in fenced blocks (versionable, no image dependencies) + a `*Describe:*` line so screen readers/alt-text get the same content.
- No color-only meaning; no timing under 30 s per slide; every demo slide carries the sandbox safety line.
- Terminology locked to the syllabus glossary (CWE/ATT&CK/STRIDE spellings).

## Files

`lecture-01..32.md` · `midterm-review.md` · `final-review.md` · `case-session-template.md` · `theme.css`
