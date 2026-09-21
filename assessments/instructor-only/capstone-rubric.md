# ⚠️ INSTRUCTOR-ONLY — Capstone Rubric & Moderation Guide

Mirrors the student brief (`../../student/capstone-brief.md`); this file adds anchors, common failure modes, and moderation procedure. **Never distribute.**

## Marking sheet (100 points, scaled to the 20% component)

### 1. Scope, assumptions, threat model — 20

| Band | Anchor |
|---|---|
| 17–20 | DFD + STRIDE ≥ 15 entries, all credible; attack trees decompose to leaf actions; risk ranking argued from likelihood AND impact; assumptions stated and revisited |
| 12–16 | Model mostly credible; some entries generic ("XSS" without location); ranking partly justified |
| 0–11 | Inventory without modeling; no ranking logic; scope drifts |

**Common failure:** threats listed per component rather than per data flow — reward flow-level thinking.

### 2. Control design + traceability — 25

| Band | Anchor |
|---|---|
| 20–25 | Every top-5 threat has a control set with preventive/detective/corrective spread; each control names its cost/friction; least-priv design is concrete (accounts, scopes) |
| 13–19 | Controls present, traceability patchy; costs named for some |
| 0–12 | Control catalogue disconnected from threats; no pricing of friction |

**Probe at defense:** "delete control X — what attack reopens?" A team that can answer instantly has real traceability.

### 3. Detection engineering — 20

| Band | Anchor |
|---|---|
| 16–20 | ≥ 3 detections with telemetry source, logic, and measured FPR/TPR on course data; explicit non-coverage statement |
| 10–15 | Detections plausible; metrics estimated rather than measured |
| 0–9 | Rules without telemetry or numbers; "we monitor everything" |

**Hard rule:** unmeasured FPR/TPR caps this section at 15/20.

### 4. IR plan + tabletop — 15

| Band | Anchor |
|---|---|
| 12–15 | Runbook for top threat with roles, ordered first actions, evidence handling; tabletop finding demonstrably changed the runbook |
| 8–11 | Generic runbook; tabletop mentioned but no visible update |
| 0–7 | No roles; actions unordered; evidence handling absent |

### 5. Ethics, governance & residual risk — 10

| Band | Anchor |
|---|---|
| 8–10 | Signed responsibility statement; residual risks named with owner + review date; scope discipline evident |
| 5–7 | Statement signed; residual risks listed without owners |
| 0–4 | Missing statement or no residual-risk honesty |

### 6. Writing quality — 10

Structure, concision, citation of datasets by version. 7–10 = reads like a deliverable, not a transcript.

## Oral defense scoring

Use the published defense rubric (student-facing `../../student/oral-defense-rubric.md`) — 20 points, scaled ×1.5 into the capstone's defense component per the syllabus weighting. Panels record one mark sheet per student (Individual accountability is per-student, not per-team).

### Final composition of the 20% capstone component (state to students)

- **Report: 70%** of the component → the 100-point marking sheet above ÷ 10 → out of 14 course points.
- **Defense: 30%** of the component → the 20-point defense rubric × 1.5 = 30 → ÷ 10 → out of 6 course points.
- Milestone 1 (threat model, Week 15) is assessed inside report §1 — no separate double-counting.
- Example: report 82/100 → 11.5/14; defense 15/20 → 22.5 → 2.3/6 (record to one decimal); capstone component 13.8/20.
- Round only at the final course-grade step, per faculty policy.

## Moderation procedure

1. **Calibration:** before marking, all markers score the same sample report (kept from last term or pre-built); discuss until within ±5.
2. **Blind first pass:** reports marked without seeing defense scores; defense marked without report scores; reconcile after.
3. **Borderline band:** any report within 3 points of a grade boundary gets a second marker; the higher of the two defensible readings stands only with written justification.
4. **Floor enforcement:** capstone < 40% is recorded as the course outcome per the non-compensable rule regardless of total; flag these for the exam board with the §1/§2 scores.
5. **Integrity referrals:** evidence that cannot have been produced in the sandbox → zero on affected section + referral; do not negotiate at the defense.
