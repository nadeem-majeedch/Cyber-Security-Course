---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L02 · Module 1 · Week 1'
---

<!-- _class: lead -->
# Lecture 02 — Threat Modeling I
## STRIDE, Attack Trees & Risk Ranking
**Module 1 · Week 1 · 120 min · CLO-1 (primary), CLO-4 (supporting)**

<!--
TIMING: 1 min title. Hook: draw the transcript portal on the board and ask "what can go wrong?" — collect 3 answers before showing STRIDE (4 min).
-->

---

# Learning Objectives

1. Build a **STRIDE** model for a small system (≥ 12 entries)
2. Decompose a threat into an **attack tree**
3. Rank threats by likelihood × impact
4. Justify which threat to fix first

<!--
Objectives map to Lab 01 rubric: the ≥12-entry threshold is the CLO-1 evidence line. 3 min.
-->

---

# STRIDE — six letters, six questions

| Letter | Threat | Property violated |
|---|---|---|
| **S** | Spoofing | Authenticity |
| **T** | Tampering | Integrity |
| **R** | Repudiation | Non-repudiation |
| **I** | Info disclosure | Confidentiality |
| **D** | Denial of service | Availability |
| **E** | Elevation of privilege | Authorization |

*Describe: two-column table; each letter pairs a threat class with the security property it breaks.*

<!--
TEACH: one example per letter on the portal (5 min). Keep examples from the plan's table — consistent terminology.
-->

---

# Working the data-flow diagram

```
[Student] --(1 login)--> [Portal] --(2 request)--> [DB]
                             |
                             └--(3 PDF)--> [Student/Registrar]
```

*Describe: three elements (Student, Portal, Database) with numbered flows; every flow gets a STRIDE pass.*

<!--
RULE: threats attach to FLOWS, not boxes. Walk flow 2: T (tamper request), I (read another's PDF), E (role param) — 6 min.
-->

---

# Attack trees — AND vs OR

```
read-another-student's-transcript
├── OR guess-id           (cost 2)
├── OR stolen-session     (cost 6)
└── AND bribe-admin (10) AND avoid-audit (8)   → 18
```

*Describe: root goal with OR branches (cheap single steps) and one AND branch (two steps both required); costs annotate leaves.*

<!--
MIN-CUT: cheapest complete path = guess-id (2). Misconception: students sum OR branches — 3 min drill on the board.
-->

---

# Risk ranking matrix

| | Low impact | High impact |
|---|---|---|
| **Likely** | Fix soon | Fix FIRST |
| **Unlikely** | Accept + document | Plan control |

*Describe: 2×2 likelihood-impact grid; top-right quadrant gets controls first, bottom-left gets documented acceptance.*

<!--
Tie to MCQ-1.5's layered logic: ranking decides ORDER, not WHETHER (2 min).
-->

---

# CS example — API backend

- Flow: client → API → Postgres
- STRIDE hits: replayed JWT (S), JSON tampering (T), verbose errors (I)
- Top risk: replay → short TTL + nonce

<!--
2 min. Keep JWT vocabulary light — deep dive is L07.
-->

---

# DS example — analytics pipeline

- Flow: raw logs → feature store → model
- STRIDE hits: label flipping (T), feature leakage (I), queue flood (D)
- Top risk: silent tampering → checksums on ingest

<!--
DS students: tampering they cannot SEE is the theme of M6 — plant it now (2 min).
-->

---

# Lab demo — Lab 01 (threat model workshop)

- Instructor live-fills 3 STRIDE rows for the portal in the shared editor
- **MVO:** every team leaves with ≥ 12 credible rows drafted
- Template: `labs/lab-01-threat-modeling/README.md`

<!--
DEMO: 5 min. If editor fails: paper handout — same rubric.
-->

---

# Case session

**CS-005 "Printers on the staff network"** (Level 1 · Segmentation)

→ threat-model lens: which STRIDE letters apply to a flat network?

<!--
Run protocol; expect S/I/D answers; model solution connects to L14 segmentation (10 min).
-->

---

# Wrap-up & exit ticket

- STRIDE per flow; trees find paths; ranking decides order
- **Exit:** one STRIDE entry for your own laptop; one min-cut sentence

<!--
Close 110 min. Preview L03: ATT&CK + attack surface.
-->

---

# References

- Shostack, *Threats: What Every Engineer Should Learn* (selected)
- Lecture plan lecture-02; Lab 01 worksheet; case INDEX CS-005
