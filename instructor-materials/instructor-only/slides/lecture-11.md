---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L11 · Module 3 · Week 6'
---

<!-- _class: lead -->
# Lecture 11 — Ransomware Anatomy & Resilience
**Module 3 · Week 6 · 120 min · CLO-3 (primary), CLO-4 (supporting)**

<!--
TIMING: 1 min. Hook: the L10 sample was a scout — ransomware is the payroll stage. No invented stats; use the case data only.
-->

---

# Learning Objectives

1. Walk the ransomware **lifecycle** end to end
2. Explain **double extortion** economics
3. Design **3-2-1** backup resilience
4. Draft the restore-first runbook

<!--
Objectives feed Lab 10 and CS-059. 3 min.
-->

---

# Lifecycle — seven stages

```
access ─► escalate ─► move laterally ─► stage
   ─► exfiltrate ─► detonate ─► (leak site)
```

*Describe: seven-stage left-to-right chain; detonation is late — the quiet stages before it are the defender's real window.*

<!--
DETECTION WINDOW: loud at detonation, quiet before — connect to M4 monitoring. 6 min.
-->

---

# Double extortion economics

```
Victim pays for:  keys (restore)  +  silence (no leak)
Defender removes: downtime fear (backups) ── leak fear remains
```

*Describe: two-line ledger — what ransomware monetizes on each side; backups erase the first lever only.*

<!--
Why immutable + tested restores matter even then: leak lever persists. Checkpoint C item 4. 4 min.
-->

---

# 3-2-1 with a modern twist

| Rule | Meaning | Ransomware angle |
|---|---|---|
| 3 copies | primary + 2 backups | one survives deletion |
| 2 media | different systems | one survives platform bugs |
| 1 offline | immutable/off-site | survives admin compromise |

*Describe: three-row table interpreting 3-2-1 against ransomware deletion behavior; the offline copy is the load-bearing one.*

<!--
MISCONCEPTION: "RAID = backup." Replication replicates encryption. MCQ-3.5. 4 min.
-->

---

# CS example — restore-first runbook

- Order: isolate → preserve → restore from immutable → THEN investigate calmly
- RTO/RPO named in the runbook header (recap from L04 governance)

<!--
2 min. Full IR loop is L31 — preview only.
-->

---

# DS example — research data vault

- Immutable snapshot tier for datasets; deletion requires two-person rule
- Ransomware against data ≠ ransomware against availability only — integrity proofs (checksums) matter

<!--
2 min. DS + CS-032 backup-availability case echo.
-->

---

# Lab demo — Lab 10 (ransomware resilience)

- Instructor "detonates" the sandbox encryptor on a throwaway folder, then restores from the immutable tier
- **MVO:** measurable restore time vs RPO/RPO stated in lab sheet
- Simulator script is synthetic; no real ransomware artifacts

<!--
DEMO 5 min. Emphasize the restore clock — that's the metric executives understand.
-->

---

# Case session

**CS-032 "Backup that never restored"** (Level 2 · Cryptography/availability)

→ backup existed; restore failed. Which control was missing?

<!--
10 min. Model: untested restore = no backup (bridge to L31 tabletop).
-->

---

# Wrap-up & exit ticket

- Quiet stages are the window; 3-2-1 with offline is load-bearing
- **Exit:** name the stage you'd instrument first and why

<!--
Close 110. Preview L12: phishing.
-->

---

# References

- CISA #StopRansomware guide (per-term check for updates)
- Lecture plan lecture-11; Lab 10
