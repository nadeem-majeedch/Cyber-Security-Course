---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L03 · Module 1 · Week 2'
---

<!-- _class: lead -->
# Lecture 03 — Threat Modeling II
## Attack Surface & MITRE ATT&CK
**Module 1 · Week 2 · 120 min · CLO-1 (primary)**

<!--
TIMING: 1 min. Hook: "ATT&CK is a dictionary of enemy verbs" — open attack.mitre.org live (2 min).
-->

---

# Learning Objectives

1. Enumerate & prioritize an **attack surface** (six categories)
2. Navigate **ATT&CK** tactics vs techniques
3. Map observed behaviors to technique IDs
4. Write a threat-informed defense hypothesis

<!--
Objectives echo the plan; the hypothesis is SA-1.2's skill. 3 min.
-->

---

# Attack surface — six categories

```
NETWORK   CODE     HUMAN
  ┌─────────────────────┐
  │  PHYSICAL · SUPPLY  │
  │      CHAIN · ML     │
  └─────────────────────┘
```

*Describe: six labeled boxes; the first three are classic, the last three (physical, supply chain, ML/data) are the ones teams forget.*

<!--
DRILL: list the portal's surface in 60 s per category (6 min). Surface SHRINKS by removal — recall MCQ-1.7.
-->

---

# ATT&CK structure

| Tactic (the WHY) | Technique (the HOW) |
|---|---|
| Credential Access | T1003 OS Credential Dumping |
| Persistence | T1053 Scheduled Task |
| Defense Evasion | T1036 Masquerading |

*Describe: three tactic-technique pairs; tactics are columns of adversary objectives, techniques are behaviors inside them.*

<!--
MISCONCEPTION: "techniques are tools." They're BEHAVIORS; tools come and go. 4 min.
-->

---

# The defense hypothesis

```
IF technique T1003
THEN telemetry: process opens lsass.exe (Sysmon EID 10)
THEN control: block non-approved callers + alert
```

*Describe: three-line IF/THEN/THEN template converting an ATT&CK technique into telemetry and a control.*

<!--
This is the semester's most reused template — it returns in M4, M6, and the capstone. 5 min, students draft one.
-->

---

# CS example — CI/CD runner

- Surface: build tokens, dependency feeds, runner shell
- ATT&CK: T1552 (unsecured credentials), T1195 (supply chain)
- Hypothesis: IF token in env dump THEN alert on build-log scan

<!--
2 min — previews M7 containers.
-->

---

# DS example — notebook environment

- Surface: shared notebooks, dataset buckets, kernels
- ATT&CK: T1530 (cloud storage), T1078 (valid accounts)
- Hypothesis: IF bucket listed by unusual account THEN alert

<!--
2 min — CS-073 territory; recall in M6.
-->

---

# Lab demo — Lab 02 (attack-surface inventory)

- Instructor inventories the course portal VM: `ss -tulpn`, route list, account list
- **MVO:** mapped inventory with a kill-list of 3 removable items
- Sandbox only — local VM, no external targets

<!--
DEMO 4 min. Pivot if tools missing: /etc/passwd + listening sockets by hand.
-->

---

# Case session

**CS-020 "Startup with no rules"** (Level 1 · Governance)

→ where would an attack-surface inventory have changed the outcome?

<!--
10 min block. Model: inventory → top-3 removals. Links to L04 controls.
-->

---

# Wrap-up & exit ticket

- Surface: enumerate → shrink; ATT&CK: tactic→technique→telemetry
- **Exit:** one hypothesis (technique + telemetry + control)

<!--
Close 110. Preview L04: controls & defense in depth.
-->

---

# References

- MITRE ATT&CK Enterprise (attack.mitre.org)
- Lecture plan lecture-03; Lab 02 worksheet
