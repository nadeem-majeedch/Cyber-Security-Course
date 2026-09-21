# Capstone Security Project (20% of final grade · non-compensable: ≥ 40% floor)

Teams of 3–4. One deliverable: a **defensive assessment and design for one assigned scenario system**, defended orally in Week 16.

## The four-stage deliverable

Your report (≤ 5,000 words + appendices) must present a **traceable chain** — every later stage references the earlier stage that justifies it:

### Stage 1 — Threat model (L29 milestone)
- Scope statement: one system, explicit boundaries, explicit assumptions.
- STRIDE table (≥ 15 entries) with data-flow diagram; attack trees for the top 2 threats.
- Risk-ranked threat register (top 5) with likelihood/impact rationale.

### Stage 2 — Control design (L30 milestone)
- For each top-5 threat: the preventive/detective/corrective control set that addresses it.
- Least-privilege account/permission design; defense-in-depth map for the highest-risk flow.
- **Cost/friction acknowledgment** for every control — no unpriced controls.

### Stage 3 — Detection engineering (L30–L31)
- 3 detections minimum: each with telemetry source, detection logic, and **measured** FPR/TPR from the course dataset or lab telemetry.
- ATT&CK technique coverage statement — including what you do *not* cover.

### Stage 4 — Incident response plan (L31)
- Runbook for the top threat scenario (roles, first three actions, evidence handling).
- Tabletop finding → runbook update loop demonstrated (from the L31 session).

## Report structure & mark weight (see the published rubric)

| Section | Marks |
|---|---|
| 1. Scope, assumptions, threat model | 20 |
| 2. Control design + traceability | 25 |
| 3. Detection engineering with measured metrics | 20 |
| 4. IR plan + tabletop integration | 15 |
| 5. Ethics, governance & residual risk acceptance | 10 |
| 6. Writing quality & structure | 10 |

## How the 20% breaks down

- **Report: 70% of the component** (14 of the 20 course points) — the 100-point marking sheet.
- **Oral defense: 30% of the component** (6 of the 20 course points) — the 20-point defense rubric, scaled ×1.5.
- The Week 15 milestone is assessed inside report section 1 (threat model) — it is not a separate mark.

## Rules and integrity

- All technical work uses the **course sandbox targets and datasets** — no real-system scanning, no unauthorized testing. The ethics section (marks above) requires a signed team responsibility statement.
- Evidence must be personally/team produced; datasets cited by version.
- Milestones: Week 15 threat model + backlog (10% of capstone, inside the report marks); Week 16 report + defense.

## The defense

20 minutes per team: 10-minute presentation, 10-minute questions. Questions come from the rubric dimensions — expect "why this control," "what does your detection miss," and "who accepts this residual risk." Every team member must answer at least one question alone.
