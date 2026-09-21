# Teaching Guide — Lecture 31 (Capstone Sprint II: IR Tabletop)
**Instructor-only. You are the tabletop controller.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–10 | Rules + roles | Decision-log template distributed; controller role explained. |
| 10–50 | Round 1 (6 injects) | phish → creds → persistence → exfil; pressure escalates. |
| 50–60 | Break + controller review | Skim round-1 logs; target round 2 at each team's gaps. |
| 60–90 | Round 2 (harder injects) | Descope items become the incident path; regulator pressure. |
| 90–105 | Refinement sprint | Patch runbooks/controls; accepted risks recorded. |
| 105–115 | Showcase prep | Structure walkthrough; rubric reminders. |
| 115–120 | Exit ticket + logistics | L32 order of teams drawn. |

## Board/Projector Activities

- **Projector:** inject cards revealed one at a time (print backup set in hand); countdown timer visible.
- **Board:** the IR flow strip (detect → contain → eradicate/recover → lessons) as the shared map of where teams are.

## Speaker Notes (key beats)

1. Controller discipline: no hints disguised as questions before the hot wash — the struggle *is* the curriculum.
2. The decision log is the graded artifact: timestamp, decision, options considered, evidence, decider.
3. Round 2 personalizes: read each team's descope log during the break and target those exact cuts.
4. Containment vs. evidence: the classic trap; teams must articulate the trade-off before acting.
5. The hot wash converts failure to curriculum: three gaps each, written, then *fixed* in the sprint.

## Expected Student Difficulties

- Teams act without logging (decisions lost). Fix: the scribe role is enforced — controller pauses and asks "log it" as needed.
- Silence under pressure. Fix: roles give everyone a voice; the communications role gets the exec/regulator injects.
- Panic at the regulator inject. Fix: L28's notification duty is a *branch in the runbook* — teams with the branch do fine; that contrast is the lesson.

## Teaching Tips

- Inject deck (instructor-only, `assessments/instructor-only/`): six primary + four escalation cards; each card has the expected decision quality bar (not a single right answer).
- The L30 descope log is your targeting list — read it during the break; this is why descope honesty was graded.
- Time pressure is a tool: the visible countdown creates the stress that reveals runbook gaps; release it at the hot wash.

## Answer Keys **[KEY]**

- Inject quality bars: phish inject → report-path + MFA + session revocation options weighed; credential inject → containment-vs-evidence articulated; persistence inject → the capstone's own detection should be cited; exfil inject → egress analysis + evidence preservation; regulator inject → notification branch exists with 72-hour framing; exec inject → status-with-evidence, not improvisation.
- Decision-log rubric: ≥ 10 entries; each entry complete (5 fields); evidence cited where claims made.
- Exit ticket: free-text — check the hot-wash item became a backlog/runbook change.

## Lab Delivery (capstone environment + inject deck)

- Minimum viable outcome: complete decision log + containment plan with recovery order + two runbook patches.
- Expected failure points: teams using tools despite the no-tools-first rule — allow after the first logged decision (the rule is decisions-first, not never); inject pacing too fast — the bar is decision quality, not card count.

## Discussion Facilitation

The hot wash is *the* facilitation moment: run it team-internal first (3 gaps written), then one gap shared aloud per team. Cross-team learning from shared gaps ("two teams cut the same thing") is the highest-value five minutes of the capstone.

## Accessibility

- Role-based format is inherently accessible: scribes may work from a laptop; standing/moving is optional.
- Inject cards: large-print set available; cards also delivered digitally so screen readers announce them.
- Pressure pacing: teams with accommodations may receive a 90-second extension per inject, announced as a standard allowance.
