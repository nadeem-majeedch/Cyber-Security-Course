# Lecture 32 — Capstone Showcase and Final Examination
**Module 8 · Week 16, Session 2 · 2 hours · CLO-8 (primary), CLO-1 (supporting)**

## Learning Objectives
1. Present and defend the capstone: threat model, controls, evidence, tabletop findings — under examiner questioning.
2. Critique peer defenses constructively with a rubric-anchored form.
3. Complete the final examination (CLO-1..8 integration, not recall).
4. Close the course: reflection, pathways, ethics recommitment.

## Key Concepts and Definitions

**Defense format:** 6 minutes presentation + 4 minutes questions per team. The rubric's top band rewards **integration**: a single arc that connects modeling → controls → detection → response, all evidence-cited.

**The evidence hierarchy** (how examiners weigh claims):

```text
live demo  >  artifact citation (screenshot/transcript/test output)  >  narrative claim
```
Expect questions aimed at the weakest link — the claims with no artifact. A strong defense *names its own residual risks before the panel does* (L29–L31 trained exactly this honesty).

**Peer review:** rubric-anchored forms — one specific strength, one specific gap, one question the panel should ask. Constructive specificity is the skill; "looks good" is a non-answer.

**The final examination:** 35 minutes, integrated scenario — one incident that crosses modules (map ATT&CK techniques, name two controls per stage with evidence you'd collect, draft the first three IR decisions, note the privacy duty triggered). A/B variants.

**Course synthesis:** security as layered engineering + measurement + ethics — the three threads that ran from L01 to here.

## Realistic Examples

- **Strong defense (illustrative composite, not a real team):** a six-minute arc that opens on the DFD, shows the injection fix with before/after probe screenshots, fires the beacon detection live, then presents the L31 decision log's hardest entry with its trade-off — every claim carries an artifact reference.
- **Weak defense (illustrative):** a slide deck narrating what the team "would have done," with no artifacts and a detection dashboard shown but never demonstrated firing — the panel's probing lands on exactly the evidence-free claims.
- **Exam question example (in the published coverage map's style):** the phish → credential → cloud role → exfiltration scenario — students who traced this class of chain in L11, L25, and L31 recognize it as integration, not novelty.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Long presentation = strong defense" | The rubric scores integration and evidence, not minutes of slides; a tight evidenced arc beats an exhaustive tour. |
| "Admitting a gap weakens the grade" | Unprompted residual-risk disclosure is the top band's marker; the panel finds undisclosed gaps anyway. |
| "The exam is a memory test of 32 lectures" | It is one cross-module scenario; the checkpoints already tested recall — integration is what remains untested. |
| "Peer review is a formality" | Rubric-anchored peer forms are part of the showcase culture; "looks good" helps nobody and scores nowhere. |

## Conceptual Diagram

```text
6-min arc: problem ─► threat model ─► controls (evidence!) ─► detection firing ─► tabletop findings
4-min Q&A: panel probes the weakest evidence link ─► team names residual risks
exam: one cross-module incident ─► ATT&CK map + controls + IR decisions + privacy duty
```

## Classroom Activities

1. **Showcase round (60 min):** ~7 teams × 10 min (6+4); instructor + peer forms scoring.
2. **Final examination (35 min).**
3. **Course retrospective (5 min):** one-minute papers; CLO self-assessment vs. checkpoints.
4. **Close (5 min):** pathways (certifications, CTFs, further reading), ethics recommitment.

## Discussion Questions (during defense Q&A)

1. Which control would you remove if the budget halved — and what compensates?
2. Where does your system still fail? (Every strong answer names a real one.)
3. What would you instrument next, and why?

## Problem-Solving Exercise

The final examination's centerpiece scenario (summary form): phish → credential → cloud role → exfiltration.
- (a) map the ATT&CK techniques per stage;
- (b) two controls per stage, with the evidence you would collect for each;
- (c) the first three IR decisions and their trade-offs;
- (d) the privacy duty triggered and its timeline.
This single item samples CLO-1..8.

## Summary

The showcase is the course's proof: students who can model, build, detect, respond, and account for their choices. The exam checks integration; the reflection checks humility. You leave authorized-minded, defense-focused, and evidence-driven — go defend things that matter, lawfully.

## Exit Ticket

One-minute retrospective: the one thing you are most confident about, and the one you will study next.

## References

- Your own capstone artifacts and course notes (the primary references of record).
- Exam coverage map and study pointers: `assessments/student/`.
- Pathways handout (curated certifications/CTF listings): `assessments/student/`.
- NIST CSF 2.0 (the synthesis frame from L04, one last time). https://www.nist.gov/cyberframework
