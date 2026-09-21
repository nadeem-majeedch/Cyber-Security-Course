# Teaching Guide — Lecture 23 (Adversarial Machine Learning)
**Instructor-only. All adversarial exercises run on course models and datasets inside the sandbox; no external services are targeted.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: model card of the class classifier | Features + threshold recap. |
| 08–30 | Evasion demo | Feature-space perturbation with problem-space constraints; boundary visual. |
| 30–50 | Poisoning storyboard | Backdoor triggers; the "how few" concentration question. |
| 50–60 | Break | — |
| 60–105 | Lab 21 (three stations) | Evasion / poisoning / extraction-lite + mitigation checklists. |
| 105–115 | Honesty table | Attack → mitigation → what-it-doesn't-stop. |
| 115–120 | Exit ticket + preview | Tease L24: "turn model output into engineered detection." |

## Board/Projector Activities

- **Projector:** the decision-boundary plot with a perturbed point crossing it; the backdoor trigger success-rate chart after 2% poisoning.
- **Board:** the pipeline diagram with the three attack-class entry points marked (training data / input / API).

## Speaker Notes (key beats)

1. The three classes map to pipeline stages: poisoning = training, evasion = inference input, extraction = API. Say the mapping; the lab stations follow it.
2. Problem-space constraints: an evasion that produces an unusable phish is a lab artifact, not an attack. This is the intellectual honesty beat of the module.
3. Backdoor concentration: few poisoned samples suffice; therefore *provenance* is the control, not post-hoc cleaning.
4. Extraction is an economics game: rate limits raise cost; watermarking is promising-but-maturing — say so.
5. ATLAS gives the vocabulary; the STRIDE-for-ML mapping gives the structure.

## Expected Student Difficulties

- Students expect dramatic L∞ imagery. Fix: this course's models are tabular — the perturbation story is feature nudges with constraints; scope claims accordingly.
- Poisoning success feels like a magic trick. Fix: show the trigger pattern in the data and its gradient effect; no mystique.
- Mitigation overclaiming. Fix: the honesty table is mandatory in the lab write-up — a mitigation without its failure mode is incomplete.

## Teaching Tips

- Keep extraction "lite": boundary reconstruction from a small query budget, on the course model only.
- The insider-labels scenario (from L22's discussion) now becomes the poisoning vector — call the connection out explicitly.
- Do not publish constraint-free evasion recipes in student materials; the lab notebooks are constrained and sandboxed by design.

## Answer Keys **[KEY]**

- Station A (evasion): perturb file-read-spike feature downward while keeping behavior plausible; mitigation checklist = input validation ranges, adversarial training note, monitoring on feature distributions.
- Station B (poisoning): 2% trigger-labeled samples yield backdoor success on trigger inputs (rate per starter seed); mitigation = provenance, label QA, training-data outlier screen.
- Station C (extraction): decision-boundary reconstruction accuracy rises with query budget; mitigation = rate limits, query-pattern alerts, abstention.
- Exit ticket: 1 poisoning/training, evasion/inference, extraction/API; 2 ignores problem-space usability constraints; 3 rate limiting — cost: latency and legitimate-query friction.

## Lab Delivery (Lab 21)

- Minimum viable outcome: all three stations attempted; two with mitigation checklists completed.
- Expected failure points: poisoning seeds make success rates vary — report ranges, not single numbers; station rotation timing (12 min each) needs the visible timer.

## Discussion Facilitation

Q2 (provenance investment) is the design lesson: cleaning is reactive, provenance is preventive — connect to L25's cloud data governance. Q3 (extraction law): keep it a question, not a ruling — legal frameworks vary and are evolving; the honest answer is "unsettled."

## Accessibility

- Boundary plots: text descriptions of the geometry ("the attack point moves from region A to region B across the decision boundary"); underlying data as CSV.
- Stations: written protocols for each step; keyboard-only paths; no station requires color discrimination (mark shapes/labels).
