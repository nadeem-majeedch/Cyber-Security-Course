# Lecture 04 — Defense in Depth, Least Privilege & Checkpoint A
**Module M1 · Week 2, Session 2 · 120 min · CLO-1 (primary) · CLO-8 (supporting)**

## Learning Objectives
1. Layer preventive, detective, and corrective controls into a defense-in-depth design for a small system.
2. Apply least privilege and secure defaults to accounts, services, and storage.
3. Classify controls (administrative/technical/physical × preventive/detective/corrective) and locate coverage gaps.
4. Present a control set that addresses a given STRIDE threat list (capstone skill preview).

## Key Concepts
- Defense in depth: layered controls, no single point of failure, control diversity
- Least privilege, need-to-know, separation of duties; secure defaults (deny-by-default)
- Control taxonomy matrix; gap analysis against a threat list
- NIST CSF functions (Govern, Identify, Protect, Detect, Respond, Recover) as an organizing frame
- Residual risk and acceptance

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L03: read out two best student detection hypotheses | Showcase |
| 08–35 | Control taxonomy workshop: 20 control cards sorted into the 3×3 matrix on the wall; discuss misplaced cards | Kinesthetic activity |
| 35–55 | Defense-in-depth design of the L03 department app: for its top 5 threats, layer controls; introduce gap analysis | Board work |
| 55–60 | Break | — |
| 60–75 | **Checkpoint A** (10-min quiz, CLO-1 items) + peer self-marking of concept items | Assessment |
| 75–105 | **Lab block (Lab 03):** teams take the vending-box STRIDE list and produce a layered control plan; least-privilege rewrite of a given overly-permissive account/service/storage config | Teams |
| 105–115 | Gallery walk: teams critique each other's control layers for single points of failure | Peer review |
| 115–120 | Module 1 wrap + Module 2 preview (HTTP) | Q&A |

## Examples
- **CS track:** CI pipeline compromise scenario — layering branch protection (prevent), signed builds + provenance (detect/prevent), canary deploy + rollback (correct).
- **DS track:** analytics database — read-only role for analysts (least privilege), query logging with anomaly alerts (detect), immutable backups (correct).

## Discussion Questions
1. Budget allows only three controls for the vending box. Which three and why — how do you justify residual risk?
2. Where does defense in depth actually hurt (complexity, false positives, user workarounds)?
3. Why is "deny-by-default" harder to sell to product teams, and how do you answer their objections?

## Student Activity
Control-card sorting (whole class), then team control-plan authoring with the 3×3 matrix as a checklist; least-privilege rewrite exercise on provided config files.

## Problem-Solving Scenario
> Given: vending-box threat list from L02 (≥ 10 STRIDE threats). Produce: control matrix covering ≥ 8 threats with ≥ 2 layers for each of the top 3; name the residual risks you accept and who would sign off.

## Summary
A control you cannot name is a control you do not have. Layer prevention, detection, correction; enforce least privilege everywhere; document accepted residual risk. Module 1 ends — students can now model, enumerate, and layer. Module 2 applies this to the web, the most exposed surface most organizations run.

## Formative Assessment
1. Classify: WAF rule (prevent/detect? technical?), SOC alert triage, quarterly restore drill.
2. Give one concrete least-privilege fix for "analysts with DB admin rights."
3. What is the difference between risk transfer and risk acceptance?

## Required Resources
- `labs/lab-03-controls-layering/` worksheet + config-file exercise set
- 20 printed control cards; Checkpoint A paper + key (in `assessments/`)
- NIST CSF 2.0 one-pager
- CLO mapping: **CLO-1** (consolidation, objectives 1–3); **CLO-8** seed (control synthesis).
