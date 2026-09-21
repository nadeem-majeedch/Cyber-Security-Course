---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L28 · Module 7 · Week 14'
---

<!-- _class: lead -->
# Lecture 28 — Privacy Engineering
## Minimization, Rights & DPIA — + Checkpoint F
**Module 7 · Week 14 · 120 min · CLO-7 (primary)**

<!--
TIMING: 1 min. Hook: "GDPR-style rules are engineering requirements with legal names." Checkpoint F at min 100.
-->

---

# Learning Objectives

1. Apply **data minimization** & purpose limitation
2. Walk the data-subject **rights** and their blockers
3. Draft a **DPIA** skeleton for a real deployment
4. Demonstrate Module 7 mastery (Checkpoint F)

<!--
The DPIA draft = SA-6 = FE-D rehearsal. 3 min.
-->

---

# Minimization & purpose

```
collect:  adequate · relevant · limited to purpose
retain:   only as long as the purpose lives
share:    only if the purpose survives the move
```

*Describe: three-line discipline; GDPR Art. 5 principles translated into engineering gates.*

<!--
SF-7. Every extra field is a liability with a retention clock. 4 min.
-->

---

# Rights and their blockers

| Right | Engineering blocker |
|---|---|
| access / portability | data spread across stores |
| erasure | backups, logs |
| rectification | denormalized copies everywhere |

*Describe: three-row rights table naming the technical obstacle for each; backups and logs are the classic erasure blockers.*

<!--
Checkpoint F item 6 + FE-B. "Delete me" meets append-only reality. 5 min.
-->

---

# Anonymization is a spectrum

```
pseudonymized:  re-identifiable with extra data → still personal
anonymized:     genuinely non-reversible → out of scope (rare!)
rare combos of quasi-identifiers → re-identification (CS-010)
```

*Describe: three-step spectrum; pseudonymized data remains regulated, true anonymization is harder than claimed.*

<!--
MCQ/checkpoint F item 6. L1's CS-010 "grades by email" echo. 5 min.
-->

---

# The DPIA skeleton (SA-6 template)

```
1 necessity & lawful basis   2 proportionality/minimization
3 risk register              4 mitigations   5 review triggers
```

*Describe: five-part skeleton; the review trigger is what makes it a living document.*

<!--
Walk the campus cloud-analytics example (FE-D). DS students: this is YOUR compliance deliverable in industry. 6 min.
-->

---

# CS example — retention automation

- Lifecycle policies expire logs/backups on schedule — rights compliance by infrastructure, not by memory

<!--
1.5 min.
-->

---

# DS example — privacy budget

- Repeated aggregate queries leak (differencing) — CS-093's "privacy budget exhausted"
- Mitigation: query auditing, noise (DP overview level)

<!--
1.5 min. DS-track flagship topic.
-->

---

# Lab demo — Lab 26 (DPIA workshop)

- Instructor fills the skeleton for the course analytics deployment live; class challenges each row
- **MVO:** completed skeleton with one honestly-accepted residual risk
- Paper exercise — no personal data involved

<!--
DEMO 5 min. Paper lab, still a lab — evidence discipline applies.
-->

---

# Checkpoint F — last 20 minutes

- 8 items: PaaS patching, wildcards, roles, control-plane logs, drift, pseudonymization + 2 scenarios
- From `quizzes/quiz-14.md`

<!--
ADMIN at 100. M7 complete. Preview M8: capstone teams form next week.
-->

---

# Case session (if time)

**CS-094 "Synthetic cover-up"** (Level 4 · Data Science/governance)

→ governance meets ML: what does honest disclosure require?

<!--
Optional 8 min. Strong case-brief candidates take it.
-->

---

# Wrap-up

- Minimization is engineering; rights meet backups; DPIAs live
- **Reading:** L29 notes; form capstone teams

<!--
Close. M7 complete — log checkpoint F; teams announced next session.
-->

---

# References

- GDPR Art. 5, 15–22, 35; lecture plan lecture-28; Lab 26
