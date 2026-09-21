# Lecture 31 — Capstone Build Sprint II: Incident-Response Tabletop
**Module 8 · Week 16, Session 1 · 2 hours · CLO-8**

## Learning Objectives
1. Execute an incident-response tabletop against your own capstone system, following a NIST-800-61-shaped flow.
2. Exercise runbooks under time pressure and record where they fail.
3. Refine controls and runbooks from tabletop findings.
4. Prepare the showcase deliverable structure for L32.

## Key Concepts and Definitions

**Tabletop mechanics:** facilitated incident simulation using **inject cards** (escalating scenario updates); no tools first — *decisions before keystrokes*. Roles: **incident lead** (owns the call), **scribe** (the decision log — the graded artifact), **communications** (what is said, to whom, when), **technical leads** (containment/recovery options).

**The decision log:** every entry = timestamp + decision + options considered + evidence + who decided. It is both the graded artifact and the honest record of how your system *actually* behaves under pressure.

**The NIST 800-61 flow (the tabletop's shape):** detection & analysis → containment → eradication & recovery → post-incident activity. Each phase has an artifact in your log: detection source, containment options *analysis*, recovery order (L11's restore ordering), lessons.

**Injected pressure:** round 2 injects deliberately target **your descope items** — the thing you cut becomes the incident path. This is by design: residual risk you accepted is the risk that arrives.

**Communication discipline:** the regulator-timeline pressure (L28's notification duty) and the exec-demand inject ("is it fixed yet?") test whether the team communicates *status with evidence* or improvises.

## Conceptual Diagram

```text
inject ─► role check ─► options analysis ─► DECISION (logged) ─► next inject
IR flow:  detect/analyze ─► contain ─► eradicate/recover ─► lessons
artifacts: detection source │ containment analysis │ recovery order │ gap→backlog
hot wash: 3 gaps each ─► refinement sprint (patch runbooks/controls, 15 min)
```

## Realistic Examples

- **CS track:** the containment decision — block the C2 domain vs. isolate the host: evidence loss vs. spread; the decision log captures the trade-off reasoning (either is defensible; unlogged decisions are not).
- **DS track:** the detection pipeline becomes the incident's detection source: why did the alert fire late? The fix (feature/threshold change) is committed *tonight* — the lessons-learned loop closing within the session.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Tabletops are theater" | They rehearse *decision-making* — the phase where real incidents are lost; artifacts prove the rehearsal. |
| "Containment first, questions later" | Containment options analysis first: destroying evidence destroys the investigation. |
| "The runbook is for juniors" | Runbooks are how *senior* teams scale under stress; your tabletop failures write their next version. |
| "We'll remember the findings" | You won't; the hot wash and refinement sprint exist because memory fails at hour three of a real incident. |

## Classroom Activities

1. **Tabletop round 1 (40 min):** six injects — phish → credential use → persistence → exfil; decisions logged.
2. **Tabletop round 2 (30 min):** harder injects targeting descope items; regulator-timeline pressure.
3. **Hot wash (10 min):** three gaps per team, written.
4. **Refinement sprint (15 min):** patch runbooks/controls; accepted risks recorded.
5. **Showcase prep (10 min):** structure walkthrough — problem → model → controls → evidence → findings.

## Discussion Questions

1. What did your runbook assume that reality (the inject deck) broke first?
2. Containment vs. evidence preservation — when do they genuinely conflict?
3. Your descope from L30 became the breach path: what does that teach about accepting residual risk?

## Problem-Solving Exercise

> Inject series culminates: attacker in the analytics job (the poisoning entry point), pivoting to the PII store; regulator-timeline pressure active.
> **Deliverable:** the decision log (≥ 10 entries); containment plan with recovery order; the two runbook patches written during the refinement sprint; the notification-draft outline.

## Summary

The tabletop converts the capstone from an architecture into an operable defense: people, decisions, rehearsed failure. Teams leave with patched runbooks and honest accepted risks — everything is on the line at the showcase.

## Exit Ticket

1. What was your costliest decision, and what evidence supported it?
2. Which IR phase consumed most of your time, and why?
3. What did the hot wash add to your backlog?

## References

- NIST SP 800-61 Rev. 2, *Computer Security Incident Handling Guide*. https://csrc.nist.gov
- Your capstone artifacts: milestone contract, descope log, detection dashboards.
- Decision-log template: `assessments/student/`.
