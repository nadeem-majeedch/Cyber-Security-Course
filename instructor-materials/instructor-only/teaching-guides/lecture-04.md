# Teaching Guide — Lecture 04 (Defense in Depth, Least Privilege, Checkpoint A)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: read 2 best hypotheses | Anonymize; praise the three-slot pattern. |
| 08–35 | Control card sort | Wall grid 3×3; whole class; expect 3–4 contested cards. |
| 35–55 | Layering the department app | Fill the prevent/detect/correct rows for top-5 threats. |
| 55–60 | Break | — |
| 60–75 | **Checkpoint A** | 10 min quiz + 5 min self-marking of concept items. |
| 75–105 | Lab 03 (controls layering) | Teams; least-priv rewrite exercise inside. |
| 105–115 | Gallery walk | Teams critique peers for single points of failure. |
| 115–120 | Module 1 wrap + M2 preview | One-sentence bridge to HTTP. |

## Board/Projector Activities

- **Wall:** 3×3 control taxonomy grid (tape labels; cards added by students).
- **Board:** the threat → prevent/detect/correct table for the department app (left partially empty deliberately — gaps are the point).

## Speaker Notes (key beats)

1. The three-column discipline (prevent/detect/correct per threat) is the takeaway; an empty column is a *named* gap, not an oversight.
2. Least privilege: deny-by-default, grant role-shaped, time-bound where possible.
3. Residual risk must have a named acceptor — connect forward to the capstone descope log (L30).
4. After Checkpoint A: spend 5 minutes on the two most-missed items (see keys) before the lab.

## Expected Student Difficulties

- Students file "training" as technical. Fix: the axis is *how* it acts (administrative = people/process), not *what* it protects.
- "More products = more depth." Fix: diversity, not quantity — two controls that fail together are one layer.
- In the least-priv rewrite, students over-revoke and break the app. Fix: the exercise includes a "must still work" list; verification is part of the task.

## Teaching Tips

- Print control cards on card stock; reuse every term.
- The Checkpoint A → lab ordering is deliberate: fresh concept, immediate application.
- During gallery walk, require one *specific* critique per team ("your backup is on the same site" beats "looks good").

## Answer Keys **[KEY]**

- Checkpoint A: see `assessments/instructor-only/checkpoint-keys.md` §A. Most-missed historically: R (repudiation) and the risk-matrix item — recap those two.
- Card sort contested items and their correct cells: WAF rule = technical/preventive; restore drill = technical/corrective (accept detective if argued as testing the control); audit log review = administrative/detective (accept technical/detective with justification).
- Exit ticket: WAF = technical/preventive; triage = detective; restore drill = corrective; least-priv fix = read-only role; transfer = insurance/outsourcing vs. accept = documented decision.

## Lab Delivery (Lab 03)

- Minimum viable outcome: control matrix covering ≥ 8 threats; least-priv rewrite that still passes the "must still work" list.
- Expected failure points: teams layer everything preventive (nothing detects); push one detective control per team minimum.

## Discussion Facilitation

Q1 (three controls only) forces prioritization — make teams commit, don't let them hedge. Q2 (where depth hurts) surfaces FP-fatigue and workaround risk; park the "alert fatigue" thread for L15 where it is taught properly.

## Accessibility

- The wall grid: provide the same grid as a one-page handout so students who cannot reach/see the wall participate fully.
- Checkpoint A: extended-time room per manual §6; large-print version on request; A/B variants already prepared.
- Color-blind note: never mark card cells by color alone — each cell has a label word.
