# Lecture 29 — Capstone Kickoff: Scenario, Threat Model, and Control Backlog
**Module M8 · Week 15, Session 1 · 120 min · CLO-8 (primary)**

## Learning Objectives
1. Scope a defensive assessment from a scenario brief: assets, adversaries, constraints, success criteria.
2. Produce a team threat model (DFD + STRIDE, reusing L02–L03 craft) for the capstone system.
3. Convert the threat model into a prioritized control backlog mapped to ATT&CK and to CLOs 2/6/7 threads.
4. Establish team working agreements: roles, evidence discipline, milestone plan.

## Key Concepts
- Capstone scenario: a fictional department platform (web app + analytics job + cloud storage + CI) — deliberately spanning all modules
- Threat-model-as-backlog: each STRIDE entry → control candidate → effort/impact score → sprint item
- Control selection under constraints (budget, uptime, team skills) — the L04 layering discipline returns
- Evidence discipline: every claim in the final report must carry a lab artifact reference
- Milestone plan: M1 (today: model+backlog), M2 (L30: hardening+monitoring demo), M3 (L31: tabletop + runbooks), M4 (L32: showcase + report)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–12 | Scenario release: the brief, the lab environment tour, grading rubric walk-through | Briefing |
| 12–25 | Team formation (balanced CS/DS), charter + role assignment (lead, scribe, red-note, blue-note) | Team setup |
| 25–55 | Threat-model sprint: DFD on the shared board; STRIDE round-robin; instructor desk-checks each team's boundaries | Team work |
| 55–60 | Break | — |
| 60–90 | Backlog conversion: threats → control candidates with effort/impact scoring; top-8 backlog frozen | Team work |
| 90–108 | Peer review swap: teams attack each other's models (missing boundaries, missing adversaries) | Peer review |
| 108–120 | Milestone contracts signed (what exists by L30, by L31, by L32); exit ticket | Admin |

## Examples
- **CS track:** the CI service role from L25 is in the scenario — teams that remember the escalation path design the fix early; those who don't rediscover it.
- **DS track:** the analytics job is a poisoning entry point (L23) — teams must decide: input validation, provenance checks, or monitoring, and defend the budget call.

## Discussion Questions
1. What makes a threat model "done enough" to build from? Define the team's bar.
2. Which module's lessons map to the most backlog items — and is that a statement about the scenario or the discipline?
3. How will your team capture evidence as you build so the report writes itself?

## Student Activity
Threat-model sprint; backlog scoring; peer-review exchange; milestone contracting.

## Problem-Solving Scenario
> The brief: 5 services, 2 data stores, one CI pipeline, a PII store, and a budget of "3 controls per service." Produce: DFD with ≥ 4 trust boundaries, ≥ 15 STRIDE entries, top-8 backlog with scoring, and the adversary narrative (who attacks, why, with what from ATT&CK).

## Summary
The capstone is the course folded into one system: model it (M1), secure its web surface (M2), assume compromise (M3/M4), protect its data (M5), watch it (M6), place it in the cloud lawfully (M7). Kickoff ends with contracts — L30 is the build sprint.

## Formative Assessment
1. Milestone contract: what exactly must exist by L30?
2. Name the four trust boundaries your team drew.
3. Which backlog item did peer review add to your list?

## Required Resources
- Capstone scenario pack (`labs/lab-27-capstone/` or equivalent environment)
- Rubric + milestone-contract template (in `assessments/student/`)
- All prior lab worksheets as reference library
- CLO mapping: **CLO-8** (objectives 1–4).
