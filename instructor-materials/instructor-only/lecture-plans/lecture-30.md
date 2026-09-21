# Lecture 30 — Capstone Build Sprint I: Hardening and Detection Implementation
**Module M8 · Week 15, Session 2 · 120 min · CLO-8 (primary)**

## Learning Objectives
1. Implement the top-priority controls from the team backlog (configuration, code, or policy changes).
2. Deploy detection content (rules/dashboards from M4/M6 craft) against the capstone environment.
3. Demonstrate control effectiveness with evidence (before/after probes inside the sandbox).
4. Calibrate progress against the milestone contract; adjust scope explicitly.

## Key Concepts
- Sprint discipline: backlog → task split → time-boxed build → demo checkpoint
- Verification-before/after: re-running L05–L07-style probes to show fixes hold (regression evidence)
- Detection wiring: SIEM rules + the L24 test-event habit; dashboard for the system's key signals
- Scope honesty: descoping is a decision, not a drift — record it with justification
- Desk-check protocol: instructor reviews progress against the contract, flags blockers early

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–10 | Sprint rules: time-boxes, demo-or-it-didn't-happen, descope log on the board | Briefing |
| 10–60 | **Build block 1:** teams implement (instructor floats for desk-checks; targeted mini-lectures on demand — e.g., "your CSP breaks X, here's why") | Team build |
| 60–65 | Break | — |
| 65–100 | **Build block 2:** detection wiring + evidence capture (before/after probe runs, screenshots, rule tests) | Team build |
| 100–112 | Demo checkpoint: 3-minute stand-up demos per team — one control live-verified, one detection firing | Demos |
| 112–120 | Scope adjustment round; L31 expectations (tabletop prep); exit ticket | Admin |

## Examples
- **CS track:** parameterization fix for the scenario app's search + proof: the L06 probe no longer yields data; the diff and the probe output become report evidence.
- **DS track:** anomaly detector (L21 features) pointed at the capstone's auth logs; dashboard shows the seeded brute-force test alerting — tuning documented.

## Discussion Questions
1. Which backlog item did your team descope, and what risk does that accept — who would sign it?
2. What does "verified" mean for a control you cannot safely test end-to-end? Partial evidence?
3. If the tabletop (L31) exposes a gap you cannot fix in time, what does your runbook say instead?

## Student Activity
Time-boxed build blocks with floating desk-checks; stand-up demos; descope logging.

## Problem-Solving Scenario
> Mid-sprint: the scenario's "third-party analytics" integration cannot be segmented within budget. Produce: the two compensating options (egress monitor + data-minimization via L28 thinking), the evidence you can still capture, and the descope-log entry with the residual-risk statement.

## Summary
Build sprints convert models into evidence-bearing artifacts: controls you can probe, detections you can fire, dashboards that show state. The milestone contract holds teams to demonstrable progress — L31 stress-tests it all with an incident.

## Formative Assessment
1. Show one before/after probe result from today.
2. What descope did you log and why?
3. Which detection fired in the demo?

## Required Resources
- Capstone environment (continued); desk-check sheet (instructor-only)
- Prior lab starter repos as fix-pattern library
- CLO mapping: **CLO-8** (objectives 1–4).
