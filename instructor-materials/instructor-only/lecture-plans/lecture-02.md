# Lecture 02 — Threat Modeling I: STRIDE and Attack Trees
**Module M1 · Week 1, Session 2 · 120 min · CLO-1 (primary) · CLO-4 (supporting)**

## Learning Objectives
1. Build a data-flow diagram (DFD) for a small system with correct trust boundaries.
2. Apply STRIDE per DFD element to enumerate threats.
3. Construct an attack tree and derive the minimum-cost cut set.
4. Rank threats by risk (likelihood × impact) and justify the ranking.

## Key Concepts
- DFDs: entities, processes, data stores, data flows, trust boundaries
- STRIDE: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege — mapped to the property violated
- Attack trees: AND/OR nodes, cut sets, cost-based pruning
- Risk matrices and their traps (ordinal math, false precision)
- Threat modeling cadence: model early, re-model on change

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L01 via 3 scenario classifications (cold call) | Q&A |
| 08–30 | DFD workshop: draw the campus printing system live; insert one deliberate boundary mistake, class catches it | Board work |
| 30–55 | STRIDE per element: derive 12+ threats on the printing DFD; table of element-type → typical STRIDE letters | Interactive slides |
| 55–60 | Break | — |
| 60–90 | **Lab block (Lab 01 part A):** teams DFD + STRIDE the course coffee-vending IoT box (spec sheet provided) | Teams |
| 90–108 | Attack trees: build "steal exam paper" tree; compute min-cut with printed costs; compare to intuition | Board work |
| 108–120 | Risk ranking exercise + exit ticket | Individual |

## Examples
- **CS track:** STRIDE on a Git server (ssh process, repo store, CI webhook flow).
- **DS track:** STRIDE on a model-serving API: poisoning the training store (T), querying to exfiltrate the model (I), spoofed API keys (S).

## Discussion Questions
1. Why do most student DFDs miss trust boundaries between browser and server? What boundary do microservices add?
2. A risk matrix rates a threat "medium." What information does that hide, and what would you ask for instead?
3. Which STRIDE letter is hardest to test for, and why (hint: repudiation)?

## Student Activity
Team DFD+STRIDE on the vending-box spec; each team posts 10 threats to the shared board, class deduplicates into a master list.

## Problem-Solving Scenario
> The vending box: card reader (network), firmware update over HTTP, local admin app with default password, telemetry to vendor cloud. Produce: DFD with ≥ 2 trust boundaries, ≥ 10 STRIDE threats, top-3 ranked with one-line justification each.

## Summary
Threat modeling is structured pessimism: DFDs show where the system can be abused; STRIDE tells you what to ask; attack trees tell you what is cheapest for the attacker. Rank, then design controls — L03 connects those controls to ATT&CK.

## Formative Assessment
1. Which STRIDE letters typically apply to a data store?
2. Draw the trust boundary between browser and server on the whiteboard sketch.
3. Why is "medium risk" an incomplete statement?

## Required Resources
- `labs/lab-01-threat-modeling/` worksheet + vending-box spec sheet
- OWASP Threat Modeling cheat sheet; Microsoft STRIDE reference pages
- Printed attack-tree cost table
- CLO mapping: **CLO-1** (objectives 1–2, 4); **CLO-4** seed (control thinking).
