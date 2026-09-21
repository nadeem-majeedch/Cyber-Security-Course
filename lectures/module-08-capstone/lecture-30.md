# Lecture 30 — Capstone Build Sprint I: Hardening and Detection
**Module 8 · Week 15, Session 2 · 2 hours · CLO-8**

## Learning Objectives
1. Implement the top-priority backlog controls (configuration, code, or policy).
2. Deploy detection content (rules/dashboards) against the capstone environment.
3. Demonstrate control effectiveness with before/after evidence inside the sandbox.
4. Calibrate progress against the milestone contract; descope explicitly.

## Key Concepts and Definitions

**Sprint discipline:** backlog → task split → time-boxed build → demo checkpoint. The rule of the day: **demo or it didn't happen** — a control you cannot show working is a wish.

**Verification-before/after:** re-run the course's own probes (L06-style injection probes, L13-style scans) against your *fixed* build; the before/after pair is the evidence that the fix holds. This is regression testing, security-edition.

**Detection wiring:** the M4/M6 craft deployed on the capstone environment — SIEM rules with test events, the anomaly dashboard pointed at the environment's auth logs, tuned within an alert budget.

**The descope log:** a visible, running record of what you cut and why. Descope is a *decision* (with a residual-risk line and an acceptor), not a drift. It returns in L31 as the incident path — cut wisely.

**Desk-check protocol:** the instructor reviews progress against the contract mid-sprint; blockers surface early, not in L32.

## Conceptual Diagram

```text
backlog item ─► implement ─► verify: before/after probes ─► evidence captured
detection:    hypothesis ─► rule ─► test event ─► dashboard (budget-fit)
demo checkpoint: one control live-verified + one detection firing — per team
descope log:  item cut + why + residual risk + acceptor
```

## Realistic Examples

- **CS track:** the parameterization fix for the scenario app's search: the L06 probe returns nothing post-fix; the diff + probe output become report evidence.
- **DS track:** the L21 anomaly detector aimed at the capstone's auth logs: the seeded brute-force test alerts; the tuning (threshold, features) is documented as the deliverable.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Implementation = done" | Verified implementation = done; the before/after evidence is the completion criterion. |
| "Descope means failure" | Honest descope with reasoning is high-scoring behavior; silent scope collapse is what fails. |
| "The dashboard is decoration" | It is a *detection* deliverable with an alert budget — it must fire on the test event and stay quiet on noise. |
| "We'll capture evidence at the end" | Evidence captured at the end is reconstructed; capture as you go or lose it. |

## Classroom Activities

1. **Build block 1 (50 min):** implement; instructor desk-checks; mini-lectures on demand.
2. **Build block 2 (35 min):** detection wiring + evidence capture.
3. **Demo checkpoint (12 min):** three-minute stand-ups — one verified control, one firing detection.
4. **Scope adjustment round (8 min):** descope log entries; L31 expectations.

## Discussion Questions

1. Which backlog item did your team descope — and what risk does that accept? Who would sign it?
2. What does "verified" mean for a control you cannot safely test end-to-end? What partial evidence suffices?
3. If the L31 tabletop exposes a gap you cannot fix in time, what does your runbook say instead?

## Problem-Solving Exercise

> Mid-sprint: the scenario's third-party analytics integration cannot be segmented within budget.
> **Deliverable:** two compensating options (egress monitoring; data-minimization via L28 thinking); the evidence you can still capture; the descope-log entry with the residual-risk statement.

## Summary

Build sprints convert models into evidence-bearing artifacts: controls you can probe, detections you can fire, dashboards that show state. The milestone contract holds you to demonstrable progress — L31 stress-tests it all with an incident.

## Exit Ticket

1. Show one before/after probe result from today (name it).
2. What descope did you log, and why?
3. Which detection fired in your demo?

## References

- Your course library: L06 (probes), L13/L15/L24 (detection), L21 (analytics), L25/L26 (cloud hardening).
- Milestone contract + desk-check sheet: `assessments/student/` (rubric summary; full rubric in the instructor tier).
- NIST SP 800-61 Rev. 2 (for the L31 runbook framing). https://csrc.nist.gov
