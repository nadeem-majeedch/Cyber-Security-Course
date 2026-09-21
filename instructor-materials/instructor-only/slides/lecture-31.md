---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L31 · Module 8 · Week 16'
---

<!-- _class: lead -->
# Lecture 31 — Capstone III
## Incident-Response Tabletop & Build Sprint II
**Module 8 · Week 16 · 120 min · CLO-8 (primary)**

<!--
TIMING: 1 min. Hook: "you wrote runbooks; today the runbooks bleed."
-->

---

# Learning Objectives

1. Execute a tabletop against YOUR scenario system
2. Decide under incomplete information, out loud
3. Update runbooks from tabletop findings
4. Prep the defense (question rehearsal)

<!--
Tabletop = FE-E rehearsal + capstone §4 evidence. 3 min.
-->

---

# Tabletop mechanics

```
inject (scenario card) ─► decide (roles, out loud)
   ─► consequences (instructor) ─► next inject ─► findings list
```

*Describe: the inject-decide-consequence loop; the deliverable is the findings list, not a win.*

<!--
MCQ-8.4: output = tested gaps. Facilitation rules: no re-rolls, decisions are binding in-scenario. 5 min.
-->

---

# Injects for the course scenario

```
T+0:    ransom note on file shares        (recall L11/L20)
T+30:   backup job "succeeds" — or does it?
T+2h:   leak-site deadline email arrives  (decision discipline!)
```

*Describe: three timed injects escalating from detection through verification to extortion pressure.*

<!--
T+2h forces the ransom/disclosure boundary: responders DON'T decide that (FE-E). 40 min tabletop.
-->

---

# Findings → runbook (the graded loop)

```
finding: "who can approve offline restore?" — unclear
   → runbook update: named roles + contact chain
   → capstone §4: BEFORE/AFTER version pair
```

*Describe: one finding traced to a runbook change and a before/after version pair; this trace is the capstone evidence.*

<!--
MCQ-8.4's "tested gaps feed runbook updates" — made concrete. 5 min.
-->

---

# Defense prep — the question bank

```
why THIS control?          (traceability probe)
what does your detection MISS?      (coverage probe)
who accepts the residual risk?      (governance probe)
```

*Describe: the three defense question families; each maps to a rubric dimension.*

<!--
10 min rehearsal: each team answers all three out loud, rotating speakers (oral-defense rubric: solo answers required). 20 min.
-->

---

# CS example — team checkpoint

- Runbook now names evidence handling (hash + custody) — tabletop exposed "backup server = evidence?" gap
- Detection metrics re-measured post-changes

<!--
2 min.
-->

---

# DS example — team checkpoint

- Tabletop injected a poisoned-feedback event — runbook now has a provenance hold procedure
- Residual risk: detection blind to novel evasion — documented with owner

<!--
2 min.
-->

---

# Lab demo — Lab 30 (tabletop support)

- Instructor runs the inject deck from the tabletop console; timing visible so teams pace decisions
- **MVO:** findings list produced BEFORE session end
- Discussion exercise — no systems touched

<!--
DEMO 5 min. Injects are scripted in the plan appendix; keep pacing visible.
-->

---

# Case session

**CS-058 "Friday 17:00 incident"** (Level 3 · Incident response)

→ weekendIR: staffing and authority gaps — the tabletop's favorite finding.

<!--
10 min. Directly comparable to today's findings.
-->

---

# Wrap-up & exit ticket

- Decisions out loud; findings become versions; defense is rehearsed
- **Exit:** your team's #1 runbook change from today

<!--
Close. Next session: showcase + FINAL. Report due before showcase.
-->

---

# References

- NIST SP 800-61r2; capstone brief §4; inject deck (plan appendix); CS-058
