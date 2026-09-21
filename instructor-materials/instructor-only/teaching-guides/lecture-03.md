# Teaching Guide — Lecture 03 (Attack Surface & MITRE ATT&CK)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Team showcase | One team presents its vending-box top threat — praise specificity. |
| 08–30 | Surface audit method | Department app walked live; students rank surfaces before you reveal your ranking. |
| 30–50 | ATT&CK tour | Live site navigation; students record 3 IDs each; keep the pace brisk. |
| 50–60 | Break | — |
| 60–95 | Lab 02 (six stations) | Rotate every 6 min; timer visible. |
| 95–110 | Surface-reduction debate | "Cut 50% — what breaks?" Structured: 2 min per side. |
| 110–120 | Exit ticket + preview | Tease L04 with "you have threats — next: controls." |

## Board/Projector Activities

- **Board:** surface inventory with exposure×value ranking (two-axis grid drawn live).
- **Projector:** MITRE ATT&CK site (Enterprise matrix); the six station behavior cards are printed, one per table.

## Speaker Notes (key beats)

1. Surface = "where can they touch us" — include humans, physical, supply chain *by name*; students reliably forget these three.
2. ATT&CK: tactics = why, techniques = how; IDs are labels for stable communication, not magic.
3. The defense-hypothesis sentence pattern (if-then-then) is the deliverable of the lab; read one exemplar aloud before the carousel.
4. End on the honest framing: ATT&CK is descriptive, your scenario decides relevance.

## Expected Student Difficulties

- Students map behaviors to tactics (too coarse) instead of techniques. Fix: require the technique-level ID.
- Hypotheses come back as "we will monitor better." Fix: the pattern has three slots — technique, telemetry, control — reject any missing slot.
- DS students may see ATT&CK as "not my area." Fix: the JupyterHub example lands this — the data pipeline *is* an attack surface.

## Teaching Tips

- Print the station cards; screens at stations slow rotation.
- During the carousel, listen for wrong IDs and collect them — open the debrief with the two most instructive misses (no names).
- The reduction debate works best if you pre-assign the "product owner" role to a confident volunteer.

## Answer Keys **[KEY]**

- Station IDs (accept defensible alternatives): spearphishing attachment T1566.001; SSH brute force T1110.001; cloud storage discovery T1580 (accept T1619); scheduled task persistence T1053.005; credential dumping T1003; data from cloud storage T1530.
- Exit ticket: T1566.001; two of {physical, supply chain, human}; T1110 hypothesis must include rate-limiting/MFA or lockout control.

## Lab Delivery (Lab 02)

- Minimum viable outcome: every student has ≥ 3 correct technique mappings and one complete hypothesis.
- Expected failure points: stations without printed cards; rotation chaos — appoint a timekeeper per team.

## Discussion Facilitation

Q2 (missing telemetry) is the richest: surface the three options (add source, accept gap, change hypothesis) and their costs. Q3: the intentional-exposure case (a public API *is* the product) reframes surface reduction as decisions, not minimization-at-all-costs.

## Accessibility

- ATT&CK site navigation: describe matrix layout verbally (rows = tactics, columns = techniques) for screen-reader parity; the printed matrix handout is the accessible equivalent.
- Station carousel: ensure stations are wheelchair-reachable and cards are large-print on request.
