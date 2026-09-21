# Lecture 29 — Capstone Kickoff: Scenario, Threat Model, Control Backlog
**Module 8 · Week 15, Session 1 · 2 hours · CLO-8**

## Learning Objectives
1. Scope a defensive assessment from a scenario brief: assets, adversaries, constraints, success criteria.
2. Produce a team threat model (DFD + STRIDE) for the capstone system.
3. Convert the threat model into a prioritized control backlog mapped to ATT&CK.
4. Establish team working agreements and milestone contracts.

## Key Concepts and Definitions

**The capstone scenario:** a fictional department platform — web app + analytics job + cloud storage + CI pipeline — deliberately spanning every module. The constraints are part of the exercise: **three controls per service** forces the prioritization muscle.

**Threat-model-as-backlog:** each STRIDE entry becomes a control candidate, scored (effort × impact) and frozen into a top-8 backlog. The scoring is argued, not computed — "we picked segmentation over the WAF because east-west spread is our biggest blast radius" is the calibre of reasoning the rubric rewards.

**Evidence discipline (the rubric's spine):** every claim in the final report must reference a lab artifact — a screenshot, a transcript, a test output. Claims without artifacts are opinions.

**Milestone contracts:** written, signed commitments — what exists by L30 (hardening + detection demo), L31 (tabletop + runbooks), L32 (showcase + report). Contracts make scope drift visible *early*.

**Team roles** (from L02, now permanent): lead, scribe, **red-note** (adversary thinking), **blue-note** (defender thinking).

## Conceptual Diagram

```text
scenario brief ─► DFD (≥4 trust boundaries) ─► STRIDE (≥15 entries)
                                    │ score: effort × impact
                                    ▼
                        top-8 control backlog ─► milestone contract (L30/L31/L32)
peer review: another team hunts missing boundaries/agents ─► backlog amended
```

## Realistic Examples

- **CS track:** the CI service role from L25 is in the scenario: teams that remember the escalation path design the fix into the backlog early; teams that don't rediscover it in L30 — the course's modules folding into one system.
- **DS track:** the analytics job is a poisoning entry point (L23): the backlog decision — input validation, provenance checks, or monitoring — is a budget argument, and every option is defensible *if the reasoning is stated*.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "The threat model is a form to finish" | It is the design conversation; the backlog *is* the model, converted. |
| "More backlog items = better" | Eight argued items beat twenty unaudited ones; prioritization is the skill. |
| "Constraints are unfair" | Real budgets are the point — descope decisions come with the course (L30) and are graded on reasoning. |
| "Peer review is adversarial" | It is the purple-team loop (L24): another model on your system finds your blind spots cheaply. |

## Classroom Activities

1. **Scenario briefing + rubric walk (12 min):** the brief, the environment, the grading bands.
2. **Threat-model sprint (30 min):** DFD on the shared board; STRIDE round-robin; instructor desk-checks boundaries.
3. **Backlog conversion + peer review (45 min):** scoring, freezing, then the swap-and-attack.
4. **Milestone contracts (15 min):** written, signed, filed.

## Discussion Questions

1. What makes a threat model "done enough" to build from? Define your team's bar in one sentence.
2. Which module's lessons map to the most backlog items — and is that a statement about the scenario or the discipline?
3. How will your team capture evidence as you build so the report writes itself?

## Problem-Solving Exercise

> The brief: 5 services, 2 data stores, one CI pipeline, a PII store, budget = 3 controls per service.
> **Deliverable:** DFD with ≥ 4 trust boundaries; ≥ 15 STRIDE entries; top-8 backlog with scoring; the adversary narrative (who attacks, why, with what from ATT&CK).

## Summary

The capstone is the course folded into one system: model it (M1), secure its web surface (M2), assume compromise (M3/M4), protect its data (M5), watch it (M6), place it lawfully in the cloud (M7). Kickoff ends with contracts — L30 is the build sprint.

## Exit Ticket

1. What must exist by L30, per your milestone contract?
2. Name the four trust boundaries your team drew.
3. Which backlog item did peer review add?

## References

- Your own course library: L02–L04 notes (modeling), L25 (IAM), L23 (ML attacks), L14 (segmentation).
- NIST SP 800-30 (risk assessment vocabulary, concept level). https://csrc.nist.gov
- OWASP SAMM (assurance-process framing, awareness level). https://owaspsamm.org
- Rubric and milestone-contract template: `assessments/student/`.
