# Teaching Guide — Lecture 29 (Capstone Kickoff)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–12 | Briefing + rubric walk | The brief, environment tour, grading bands — no surprises later. |
| 12–25 | Team formation | Balanced CS/DS; roles assigned (lead/scribe/red-note/blue-note). |
| 25–55 | Threat-model sprint | DFD + STRIDE; desk-check boundaries team by team. |
| 55–60 | Break | — |
| 60–90 | Backlog conversion | Score, freeze top-8; contracts drafted. |
| 90–108 | Peer review swap | Teams attack each other's models. |
| 108–120 | Contracts signed + exit ticket | Milestone filing; L30 expectations. |

## Board/Projector Activities

- **Projector:** the scenario environment tour (services, data stores, CI, PII store); the rubric bands.
- **Board:** each team's DFD lives on its own wall section for the whole sprint (photo per team for LMS).

## Speaker Notes (key beats)

1. The scenario spans every module by design — say which module each service stresses (web→M2, CI→M2/M7, analytics→M6, PII store→M5/M7).
2. Constraint culture: three controls per service forces *argument*, and the rubric scores the argument, not the count.
3. Evidence discipline is the rubric's spine: claims must cite artifacts from today onward.
4. Desk-check boundaries: four trust boundaries minimum; the CI pipeline's boundary is the one teams miss.
5. Contracts: specific, dated, demonstrable — "a working X" not "work on X."

## Expected Student Difficulties

- Teams over-model (30 threats, all shallow). Fix: enforce per-element coverage; the backlog conversion will cull.
- Backlog scoring collapses into "everything is high impact." Fix: force-rank — if two items tie, the team must break the tie in one sentence.
- Role assignment drifts to friends' preferences. Fix: assign red-note/blue-note by the L12/L14 discussion performance you have observed.

## Teaching Tips

- Pre-verify the scenario environment before class; kickoff losing 20 minutes to broken infra poisons the capstone.
- The peer-review swap is timed tightly (attack the *model*, not the team); provide the two prompts: "which boundary is missing?" and "which adversary did you not consider?"
- File contracts immediately; L30's desk-checks refer to them.

## Answer Keys **[KEY]**

- Desk-check reference (minimum model): boundaries = internet↔web, web↔data stores, CI↔everything, analytics↔data, (accept cloud control-plane as a fifth). Missed adversary examples: insider labeler (M6), broker-then-affiliate ransomware path (M3), CI-role escalation (M7).
- Rubric bands (summary): integration arc + evidence-cited claims = top; complete-but-disconnected controls = middle; claims without artifacts = bottom regardless of volume.
- Exit ticket: free-text check against the team's filed contract — look for specificity.

## Lab Delivery (Lab 27 / capstone environment)

- Minimum viable outcome: DFD (≥ 4 boundaries) + ≥ 15 STRIDE entries + top-8 backlog + signed contract.
- Expected failure points: shared-board contention — one wall section per team, pre-marked; teams losing work — photos at each phase.

## Discussion Facilitation

Q2 (which module dominates the backlog) is the course's self-portrait — let teams tabulate; the usual answer (M7/M2) opens the "is that the scenario or the discipline?" conversation you want at showcase time. Q3 (evidence-as-you-build) seeds the L30 discipline.

## Accessibility

- Wall-based modeling: provide the same DFD/STRIDE as digital canvas with keyboard navigation; teams choose their medium.
- Contracts: template with pre-labeled fields; large-print versions on request.
- Desk-checks: schedule a seated option for teams with members who cannot stand through the walk-throughs.
