# Implementation Roadmap — Cyber Security Course
**Companion to `architecture-and-requirements.md` · Baseline date 2026-09-19**

## Stage 0 — Governance & scaffolding ✅ (this task)

- [x] Inventory empty repo, document baseline (`content-inventory.md`)
- [x] Master requirements, CLOs, module map, 32-lecture plan (`architecture-and-requirements.md`)
- [x] Directory skeleton created (student/instructor tiers, website, labs, case studies, assessments)
- [x] Roadmap (this file)
- [ ] Governance files: `README.md`, `LICENSE` (recommend MIT or CC BY-SA for materials), `CODE_OF_CONDUCT.md`, `.gitignore` (exclude `.freebuff/`, sandbox artifacts)
- [ ] Pages CI skeleton (`.github/workflows/pages.yml`) — must not deploy until Stage 2 content exists

## Stage 1 — Module M1 content sprint (Weeks 1–2 of delivery)
1. Write `lectures/module-01-fundamentals/` L01–L04 per the lecture shell contract (§6 of the requirements doc).
2. Module overview for M1; diagnostic Checkpoint A into `assessments/student/` + key into `assessments/instructor-only/`.
3. Instructor delivery notes for L01–L04 in `instructor-materials/instructor-only/`.
4. First two student labs (`labs/lab-01-threat-modeling/`, `labs/lab-02-attack-surface/`).
5. **Gate G1:** 4 lectures × shell contract, 2 labs runnable, 1 quiz with separated key.

## Stage 2 — Website goes live
1. Build `website/index.md`, `syllabus.md`, lecture index listing all 32 entries (placeholder for future lectures is allowed but every slot must appear).
2. `pages.yml` deploys from `website/` on push to `main`; verify the live URL renders.
3. **Gate G2:** Pages site live, 32 lecture slots visible, zero instructor-only links.

## Stage 3 — Modules M2–M5 sprints (Weeks 3–10 of delivery, one module per sprint)
Repeatable sprint recipe per module:
- 4 lectures (dual-track examples), module overview
- 2 labs (offensive-lab + defensive deliverable)
- 1 checkpoint quiz (student + instructor-only key)
- 1 case study mapped to the module
- Website index updated in the same PR
**Gates G3–G6** = per-module checklist: lectures done, labs tested on the course VM, key separation verified.

## Stage 4 — Modules M6–M7 sprints (DS-heavy; Weeks 11–14)
- Notebooks/datasets policy: synthetic or license-safe datasets only; datasets ≤ 50 MB (GitHub limit) or fetched via script.
- Include model-evaluation deliverable (precision/recall on the lab dataset).
- **Gates G7–G8** as Stage 3.

## Stage 5 — Capstone & finalization (Weeks 15–16)
1. Capstone brief, rubric, team charter template in `assessments/student/`; grading rubric + desk-check sheets in `assessments/instructor-only/`.
2. Final exam A/B versions + keys (instructor-only).
3. Incident-response tabletop script for L31.
4. **Gate G9:** capstone package complete; exam versions sealed in instructor tier.

## Stage 6 — Course closeout & continuous improvement
- Post-semester: anonymized outcome data review, CLO attainment mapping, revision backlog in GitHub issues.
- Archive term artifacts under `website/archive/` (student-facing summaries only).

## Cross-cutting quality gates (verification checklist)

| Gate | Check | Evidence |
|---|---|---|
| Q1 | 32/32 lecture files exist with shell contract | glob `lectures/**/lecture-*.md` = 32 |
| Q2 | 8 module overviews exist | glob `lectures/**/module-overview.md` = 8 |
| Q3 | Student vs instructor separation | answer keys only under `*-instructor-only*` |
| Q4 | Pages readiness | `website/` static + CI present + index lists 32 lectures |
| Q5 | No deletions of existing content | git diff shows only additions |

## Milestone calendar (proposal)

| Week (term) | Stage | Deliverable due |
|---|---|---|
| Pre-term | 0, 2 | governance + live site |
| W1–2 | 1 | M1 complete (G1) |
| W3–10 | 3 | M2–M5 (G3–G6) |
| W11–14 | 4 | M6–M7 (G7–G8) |
| W15–16 | 5 | capstone + finals (G9) |
| Post | 6 | CLO review |

## Risk register (top items)

| Risk | Mitigation |
|---|---|
| Public repo + answer keys leak | Route instructor-only tier to private repo (owner decision §11) or scramble/hide until exam day |
| Lab sandbox escape / abuse | VM isolation, no live-target tools, responsible-use statement, campus AUP reference |
| Dataset licensing for DS labs | Synthetic-first policy; script-fetched public data only |
| Content drift (CVEs age) | Annual revision backlog; version lecture references by year |
