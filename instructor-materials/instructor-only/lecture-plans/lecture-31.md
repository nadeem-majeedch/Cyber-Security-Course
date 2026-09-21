# Lecture 31 — Capstone Build Sprint II: Incident-Response Tabletop Exercise
**Module M8 · Week 16, Session 1 · 120 min · CLO-8 (primary)**

## Learning Objectives
1. Execute an incident-response tabletop against the team's own capstone system, following a NIST-800-61-shaped flow (detect → analyze → contain → eradicate → recover → lessons).
2. Exercise the team's runbooks under time pressure and record where they fail.
3. Refine controls/runbooks from tabletop findings (the final build adjustment).
4. Prepare the showcase deliverable structure for L32.

## Key Concepts
- Tabletop mechanics: inject cards, decision log, controller role, no-tool-first thinking (decisions before keystrokes)
- Roles: incident lead, scribe, communications, technical leads; the decision log as the graded artifact
- IR phases and their artifacts: detection source, containment options analysis, recovery order (ties to L11 restore ordering)
- Lessons-learned loop: every gap → backlog item or accepted-risk note
- Communication discipline: what you say, to whom, when (breach-notification tie-in from L28)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–10 | Tabletop rules + role assignment; inject deck explained; decision-log template distributed | Briefing |
| 10–50 | **Tabletop round 1** (6 injects): phish → credential use → persistence → exfil; teams decide per inject, controller escalates pressure (media query, exec demand) | Tabletop |
| 50–60 | Break + controller review of round-1 logs | — |
| 60–90 | **Tabletop round 2** (harder injects: the team's own descope items come back as the incident path) + hot wash: 3 gaps each | Tabletop + hot wash |
| 90–105 | Refinement sprint: patch runbooks/control gaps found; record accepted risks with sign-off line | Team work |
| 105–115 | Showcase prep: structure walkthrough (problem → model → controls → evidence → tabletop findings), rubric reminders | Briefing |
| 115–120 | Exit ticket; final logistics for L32 | Admin |

## Examples
- **CS track:** containment decision: block the C2 domain vs. isolate the host — teams must weigh evidence loss against spread; the decision log captures the trade-off reasoning.
- **DS track:** the detection pipeline (L21–L24) becomes the incident's detection source; teams analyze why the alert fired late and what feature/threshold change they commit tonight.

## Discussion Questions
1. What did your runbook assume that reality (the inject deck) broke first?
2. Containment vs. evidence preservation — when do they genuinely conflict?
3. Your descope from L30 became the breach path: what does that teach about accepting residual risk?

## Student Activity
Role-played tabletop with decision logs; hot wash; refinement sprint; showcase prep.

## Problem-Solving Scenario
> Inject series culminates: attacker in the analytics job (the DS poisoning entry point), pivoting to the PII store; regulator timeline pressure (L28's notification duty). Produce: the decision log (≥ 10 entries), containment plan with recovery order, the two runbook patches written during the refinement sprint, and the notification-draft outline.

## Summary
The tabletop converts the capstone from an architecture into an operable defense: people, decisions, and rehearsed failure. Teams leave with patched runbooks and honest accepted risks — everything is now on the line at the showcase.

## Formative Assessment
1. Decision log: what was your costliest decision and its evidence?
2. Which IR phase consumed most of your time and why?
3. What did the hot wash add to your backlog?

## Required Resources
- Inject deck (instructor-only) + decision-log template (student)
- NIST SP 800-61 phase diagram (1-page handout)
- CLO mapping: **CLO-8** (objectives 1–4).
