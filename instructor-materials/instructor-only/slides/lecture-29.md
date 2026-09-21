---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L29 · Module 8 · Week 15'
---

<!-- _class: lead -->
# Lecture 29 — Capstone I
## Scenario Scoping & Threat-Model Workshop
**Module 8 · Week 15 · 120 min · CLO-8 (primary)**

<!--
TIMING: 1 min. Hook: "the last five weeks build ONE artifact you defend in seven days." Teams already formed.
-->

---

# Learning Objectives

1. Scope ONE scenario system with explicit boundaries
2. Produce a team **threat model** (≥ 15 STRIDE entries)
3. Draft the **control backlog** with priorities
4. Assign team accountability areas

<!--
Milestone 1 due end of session. CLO-8's chain starts here. 3 min.
-->

---

# Scope discipline

```
ONE system · explicit boundary · explicit assumptions
"secure everything" = automatic scope failure (MCQ-8.5)
```

*Describe: scope rule with its failure mode; depth-with-traceability beats breadth-without.*

<!--
Show the three scenario options (from capstone-brief); teams commit TODAY. 4 min.
-->

---

# The deliverable chain (rubric preview)

```
threat model ──justifies──► controls ──failure modes──► detections
                     detections ──trigger──► IR runbook
```

*Describe: the four-stage chain with the linking words — justifies, failure modes, trigger; traceability IS the graded skill.*

<!--
Every arrow gets a mark in the rubric — show capstone-brief weights. 5 min.
-->

---

# Workshop mechanics (60 min)

```
15 min: DFD draft          20 min: STRIDE pass per flow
15 min: attack trees ×2    10 min: rank top-5, draft backlog
```

*Describe: four timed workshop blocks; instructor circulates, testing one tree per team.*

<!--
CIRCULATION SCRIPT: for each team, ask "delete this control — what reopens?" — the traceability probe from the rubric. 60 min block.
-->

---

# CS example team — e-commerce scope

- Boundary: checkout flow only; payment gateway = trusted third party (assumption!)
- Top threat: injection → card exfil; tree rooted at DB access

<!--
2 min. One worked example sets the bar.
-->

---

# DS example team — analytics platform scope

- Boundary: ingestion + scoring API; training pipeline out of scope (assumption)
- Top threat: poisoning via feedback loop (L23) → detection on label provenance

<!--
2 min. DS teams get ML-native scopes — allowed, same rigor.
-->

---

# Lab demo — Lab 30 kickoff (capstone working labs)

- Sandbox scenario environments opened; each team verifies access and captures a baseline
- **MVO:** environment reachable + baseline evidence saved
- Sandbox only — capstone ethics statement signed today

<!--
DEMO 5 min. The signed ethics statement is a rubric line item (§5).
-->

---

# Case session

**CS-100 "Capstone dilemma"** (Level 4 · Capstone synthesis)

→ the syllabus's own dilemma, in case form — teams argue scope under pressure.

<!--
15 min for CS-100 — it IS their homework made concrete.
-->

---

# Wrap-up & exit ticket

- Scope, model, backlog — committed before you leave
- **Exit:** team's top-3 backlog items, one line each

<!--
Milestone 1 = DFD + STRIDE + backlog, submitted tonight.
-->

---

# References

- Capstone brief; rubric (instructor); scenario packs; CS-100
