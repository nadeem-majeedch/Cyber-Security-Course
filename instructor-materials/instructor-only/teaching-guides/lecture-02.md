# Teaching Guide — Lecture 02 (Threat Modeling I: STRIDE & Attack Trees)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap via cold-call | Three scenario classifications from L01; volunteers first. |
| 08–30 | DFD workshop (printing system) | Plant the missing boundary; let the class find it — don't point. |
| 30–55 | STRIDE per element | Fill the table live; enforce "one threat per letter where sensible". |
| 55–60 | Break | — |
| 60–90 | Lab 01 part A (vending box) | Teams of 4; scribe posts ≥ 10 threats to shared board. |
| 90–108 | Attack trees | Pre-printed cost table; compute min-cut together. |
| 108–120 | Risk ranking + exit ticket | Each team defends its top-3 out loud (30 s each). |

## Board/Projector Activities

- **Board:** printing-system DFD (entities/processes/stores/flows in one color, boundaries in another). Photo to LMS.
- **Projector:** the STRIDE×element matrix (empty; filled live). The attack-tree cost table.

## Speaker Notes (key beats)

1. "What are we building → what can go wrong → what do we do about it" — say this order explicitly; it structures the whole module.
2. The missing-boundary moment is the lesson: resist pointing it out; ask "where does *control over the data* change hands?"
3. Attack trees: emphasize AND vs OR with the "steal exam paper" example; min-cut = cheapest complete path.
4. Close: STRIDE finds breadth, trees find depth — you need both.

## Expected Student Difficulties

- DFDs drift into flowcharts (decision diamonds). Fix: DFDs have four element types only; redraw.
- "R (repudiation)" is abstract. Fix: ask "who can prove who did it, and where is that evidence?"
- Teams list 30 shallow threats. Fix: require per-element coverage, not volume; dedup on the shared board.

## Teaching Tips

- Timebox the DFD strictly (12 min); model quality beats completeness.
- Assign roles in teams now (lead, scribe, red-note, blue-note) — the capstone reuses them.
- The vending-box spec sheet is deliberately ambiguous in one place (who owns the cloud telemetry?) — ambiguity is realistic; let teams resolve it and compare resolutions.

## Answer Keys **[KEY]**

- Printing-system planted error: the missing boundary is student-laptop ↔ print-server (accept: any privilege-change line missed).
- Attack-tree min-cut (exam paper): physical-key theft path at cost 15 vs. bribe+forge at 40 — accept equivalent readings of the printed table.
- Exit ticket: stores → T, I (accept D for availability of data); "medium risk" hides likelihood/impact reasoning.

## Lab Delivery (Lab 01 part A)

- Minimum viable outcome: one DFD with ≥ 2 boundaries + ≥ 10 deduplicated STRIDE threats per team.
- Expected failure points: teams skip the telemetry flow entirely; prompt "what leaves the box?"

## Discussion Facilitation

Q1: the browser↔server boundary is missed because students draw *deployment*, not *trust*; Q2 (risk matrix) pairs well with a 2×2 grid drawn live; Q3 is a 2-minute teaser for M4/SIEM — park it.

## Accessibility

- DFD shapes carry meaning — pair each shape with a label word and read the diagram aloud element by element.
- Team scribe posts to a shared doc so students who can't see the wall board get the same content in real time.
