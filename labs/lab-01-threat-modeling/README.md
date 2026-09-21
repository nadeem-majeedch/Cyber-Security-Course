# Lab 01 — Threat Modeling: STRIDE & Attack Trees
**Enrichment · Module 1 (L02–L04) · CLO-1 (primary), CLO-4 (supporting) · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Build a DFD with correct trust boundaries for a provided system spec.
2. Enumerate threats with STRIDE per element (≥ 10).
3. Build an attack tree and compute the minimum-cost cut with a printed cost table.
4. Rank the top 3 threats with justified risk reasoning.

## Prerequisites
Lectures 02–04 (DFD, STRIDE, attack trees, controls). No tooling needed — this is a modeling lab.

## Hardware/Software Requirements
Course VM or paper: the `vending-box-spec.pdf` handout, attack-tree cost table, worksheet. Optional: any diagramming tool (draw.io/diagrams.net offline in the image).

## Installation and Setup
None beyond the handouts. Teams of 4; roles from the course convention (lead, scribe, red-note, blue-note).

## Ethical Authorization and Safety Notes
Pure modeling: no systems are touched. The vending-box is fictional; treat ambiguity in the spec as realistic — resolve it and *document your assumption*.

## Step-by-Step Student Tasks
1. Read the spec; list assets and actors.
2. Draw the DFD (entities/processes/stores/flows); mark **≥ 2 trust boundaries**.
3. STRIDE per element; deduplicate into ≥ 10 threats.
4. Attack tree for "obtain free products or cash": AND/OR structure; min-cut from the cost table.
5. Rank top-3 (likelihood × impact) with one-line justifications.
6. Map one control per top-3 threat (L04 columns: prevent/detect/correct).

## Expected Observations
Teams reliably miss the telemetry-to-cloud flow's boundary at first; the HTTP firmware-update path dominates the tree's cheap paths.

## Questions for Analysis
1. Which boundary did your team add last, and what threat only became visible after it existed?
2. Where do STRIDE and the attack tree disagree about what matters most — and which do you trust for *prioritization*?

## Troubleshooting
Threat list stuck at 6–7 → return to the DFD and force one letter per element type. Model quality low → check that stores and flows (not just processes) got STRIDE letters.

## Cleanup Instructions
No system changes; photograph/keep the board; return printed cost tables.

## Submission Requirements
DFD photo/diagram, threat table (≥ 10), attack-tree photo with min-cut marked, top-3 ranking, control mapping.

## Expected Outputs / Evidence
One worksheet pack per team; all names present; assumptions documented.

---
### Instructor Answer Key (summary)
- Planted ambiguity: telemetry ownership (vendor vs. university) — both resolutions defensible; different threat lists follow.
- Expected boundary set: card-reader↔vend-controller, controller↔cloud-telemetry, admin-app↔controller.
- Attack-tree min-cut: HTTP firmware update (cost 15) beats the bribe+forge path (40) — the tree teaches that the cheap path is often the "boring" one.
- Common miss: repudiation on the telemetry flow (who can prove which machine sent what?).

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| DFD with ≥ 2 correct boundaries | 3 |
| ≥ 10 deduplicated STRIDE threats | 3 |
| Attack-tree min-cut correct | 2 |
| Ranked top-3 with justification | 2 |
