---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L30 · Module 8 · Week 15'
---

<!-- _class: lead -->
# Lecture 30 — Capstone II
## Build Sprint I & Desk-Check Clinic
**Module 8 · Week 15 · 120 min · CLO-8 (primary)**

<!--
TIMING: 1 min. Hook: "controls and detections today — defense is where claims meet evidence."
-->

---

# Learning Objectives

1. Implement priority control items from the backlog
2. Build one detection **with measured FPR/TPR**
3. Desk-check another team's chain (traceability)
4. Update runbooks from desk-check findings

<!--
Peer desk-check = calibration before MY grading. 3 min.
-->

---

# Sprint board

```
backlog ──► implement (top 3) ──► verify (fix-verify pairs)
        ──► measure (one detection on class traffic)
```

*Describe: sprint pipeline from backlog through implementation, verification, and measurement; the measured detection is the hard deliverable.*

<!--
Hard rule from the rubric: unmeasured FPR/TPR caps detection marks. 4 min.
-->

---

# Desk-check protocol (30 min)

```
1. read the other team's chain (5 min)
2. probe: "delete control X — what reopens?" (10 min)
3. probe: "which ATT&CK technique is UNcovered?" (10 min)
4. written findings to the team (5 min)
```

*Describe: four-step peer-review protocol with two named probe questions and a time budget.*

<!--
The two probes ARE the defense's first questions — practicing in the light. 30 min block, instructor floats.
-->

---

# Evidence discipline for the report

```
every claim needs: artifact + method + version
datasets cited by version (course packs are versioned!)
screenshots: your own VM, timestamped
```

*Describe: three-line evidence rules; provenance is enforced by the integrity policy.*

<!--
Recall practical-assessments.md: evidence that cannot have been produced by their VM = referral. 3 min.
-->

---

# CS example — team milestone: control implementation

- Parameterized queries land; least-priv DB role live; WAF in shadow
- Verification: replay the L06 exploit → it fails; show it

<!--
2 min.
-->

---

# DS example — team milestone: detection implementation

- Label-provenance detector in shadow mode on class feed; FPR/TPR measured (L24 method)
- Runbook draft started for poisoning scenario

<!--
2 min.
-->

---

# Lab demo — Lab 30 sprint support

- Instructor desk-checks ONE team live on the projector using the protocol — students see the standard
- **MVO:** every team observed one desk-check before doing their own

<!--
DEMO 8 min. The live desk-check sets the quality bar better than any rubric handout.
-->

---

# Case session

**CS-083 "Prioritization under protest"** (Level 4 · Vulnerability prioritization)

→ backlog fights: practice saying "no, because…" with evidence.

<!--
10 min. Teams will hit this EXACT conflict in their sprints.
-->

---

# Wrap-up & exit ticket

- Implement, verify, measure, desk-check, iterate
- **Exit:** desk-check's single most useful finding your team received

<!--
Milestone 2 check next session: working controls + measured detection.
-->

---

# References

- Capstone brief §2–3; desk-check protocol; CS-083
