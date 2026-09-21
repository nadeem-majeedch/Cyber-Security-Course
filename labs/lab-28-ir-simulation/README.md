# Lab 28 — Incident Response Simulation
**Core Lab 8 · Module 8 (L31) · CLO-8 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Execute an incident-response flow (NIST SP 800-61-shaped: detect/analyze → contain → eradicate/recover → lessons) against a simulated incident.
2. Produce a decision log in which every decision records options considered, evidence, and the decider.
3. Exercise communication under pressure (status-with-evidence, not improvisation).
4. Convert lessons into runbook patches and honest residual-risk statements.

## 2. Prerequisites
Lecture 31 (tabletop mechanics, decision log, roles). The capstone environment (or the standalone simulation pack for non-capstone sections). Completion of Lab 27's evidence discipline strongly recommended.

## 3. Hardware/Software Requirements
- Course VM + the instructor-provided **simulation pack** `ir-sim-pack-v1.zip`: inject card deck (sealed), `scenario-brief.pdf`, `decision-log-template.md`, status-report forms.
- Timer (phone is fine); the instructor runs the clock.
- No exploitation tools are needed — **this is a decision exercise, not a hacking exercise.**

## 4. Installation and Setup
1. Unseal the inject deck only when the instructor says "start" (sealed envelope per team).
2. Assign roles before the clock starts: incident lead, scribe (owns the decision log), communications, technical lead.
3. Read the scenario brief (5 minutes, timed); the clock starts after.
   *(Pack composition and inject pacing are instructor-side; team-side setup is deliberately trivial so all time goes to decisions.)*

## 5. Ethical Authorization and Safety Notes
- This is a tabletop simulation on paper artifacts: no system is touched, scanned, or "responded to" outside the fiction of the inject deck.
- Actions in the fiction (e.g., "isolate host") are logged as decisions — never executed on any real machine.
- The injects reference compromise techniques only at the level this course teaches for *detection and response*; they contain no attack instructions.

## 6. Step-by-Step Student Tasks
| # | Task | Notes |
|---|---|---|
| 1 | Roles assigned, log template open, clock confirmed | Pre-flight |
| 2 | **Injects 1–6 (round 1):** for each — read, options analysis (≥ 2 options), decision, log entry | 5 min per inject |
| 3 | Maintain the decision log continuously: timestamp, decision, options, evidence, decider | Scribe |
| 4 | **Inject 7 (pressure):** regulator-timeline question (L28's notification duty) — draft the notification outline | Communications |
| 5 | **Inject 8 (pressure):** executive "is it fixed yet?" — produce a status-with-evidence statement in ≤ 5 sentences | Communications |
| 6 | **Inject 9 (recovery):** decide restore order and justify it | Technical lead |
| 7 | Hot wash: write three gaps in your team's response | 10 min |
| 8 | Refinement: patch two runbook gaps into concrete runbook edits | written |
| 9 | Residual-risk statement: what you accept, who would sign | written |

## 7. Expected Observations
- Round 1 runs smoothly until inject 4–5, when containment-vs-evidence tension appears (blocking the "attacker" loses visibility into what else they touch).
- The regulator inject exposes whether your runbook has a notification branch (teams without one improvise — the lesson).
- Restore-order decisions reproduce Lab 10/L11 reasoning: infrastructure before data, verification before reconnection.
- The hot wash reliably surfaces the same three gaps: no notification branch, no evidence-preservation step in containment, unclear decision authority.

## 8. Questions for Analysis
1. Which decision in your log had the weakest evidence at the time you made it? What would you collect first if you re-ran it?
2. Containment vs. evidence preservation: state the general rule your team will use, and one situation where you would break it.
3. Your notification outline: what triggers the 72-hour-style clock — detection, confirmation, or decision to notify? Defend your reading.

## 9. Troubleshooting
- Team freezes on an inject → controller prompt: "name two options before choosing one" (the log requires it anyway).
- Log falls behind the injects → controller pause; the log *is* the graded artifact, catching up is allowed, skipping is not.
- Role conflict (two people deciding) → the incident lead owns the call; disagreement is logged, not relitigated mid-inject.

## 10. Cleanup Instructions
- Return the inject deck to the sealed envelope; hand it to the instructor (cards are reused across sections).
- Shred/keep your draft notes per instructor instruction; the decision log and runbook patches are submitted, scratch notes are not.

## 11. Submission Requirements
- `decision-log.md` (≥ 10 entries, all five fields per entry).
- `runbook-patches.md` (two concrete edits).
- `notification-outline.md` (the regulator inject answer).
- `residual-risk.md` (accepted risks + named acceptor roles).

## 12. Expected Outputs / Evidence
All four documents from your team's session. Grading is on decision quality and honesty of the log, not on "winning" the simulation — there is no winning.

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Inject deck (order and bars): 1 phish report → report-path + credential reset decision; 2 anomalous sign-in → MFA/session revocation options; 3 persistence indicator (scheduled task) → containment-vs-evidence articulated; 4 egress spike → block vs monitor trade-off; 5 second host → scope expansion decision; 6 ransom-note artifact → recovery planning begins; 7 regulator → notification branch with 72-hour framing; 8 executive → status-with-evidence (≤ 5 sentences, no speculation); 9 restore order → infra → verify → data.
- Strong log entries: two options minimum; evidence cited from prior injects; decider named by role. Weak: "we did X" with no options or evidence.
- Expected hot-wash gaps: notification branch missing; no evidence-preservation step; decision authority unclear. Any two patched concretely = full marks.
- Restore order (model): identity/backup infrastructure → verify integrity → tier-1 data services → general shares → endpoints.

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Decision log completeness (5 fields × ≥ 10 entries) | 6 |
| Options-analysis quality (real trade-offs, not tokens) | 4 |
| Communication injects (status-with-evidence standard) | 4 |
| Runbook patches (concrete, adoptable) | 3 |
| Residual-risk honesty + named acceptors | 3 |
