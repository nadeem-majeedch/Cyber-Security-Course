---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L01 · Module 1 · Week 1'
---

<!-- _class: lead -->
# Cyber Security — Lecture 01
## Security Foundations: CIA, Ethics & Responsible Disclosure
**Module 1 · Week 1 · 120 min · CLO-1 (primary)**

<!--
TIMING: title 1 min. Hook: "you have all been attackers this week — password guesses, ad blockers" (2 min). Course contract: read §8 pattern aloud once (2 min).
-->

---

# Learning Objectives

By the end you can:
1. Define **CIA** and map failures to the right property
2. Distinguish security vs **privacy** vs **safety**
3. Apply **responsible disclosure** rules to a real finding
4. State the course's authorization boundary in one sentence

<!--
READ VERBATIM OBJECTIVES from lecture plan §2. Tell students these exact objectives are the exit ticket (4 min total for objectives + mapping).
-->

---

# The CIA Triad

| Property | Question it answers | Example failure |
|---|---|---|
| **C**onfidentiality | Who can *read*? | Stolen transcript PDF |
| **I**ntegrity | Who can *change*? | Altered payroll export |
| **A**vailability | Can it be *used*? | Ransomware-encrypted shares |

*Describe: three-column table mapping property → question → failure.*

<!--
TEACH: ask class to classify 3 one-liners (2 min). Emphasize: "most breaches violate more than one — name the PRIMARY."
-->

---

# Security ≠ Privacy ≠ Safety

```
   SECURITY                    PRIVACY                SAFETY
 controls against     |    control over personal   |  harm to people/
 adversarial intent   |    data & its lifecycle    |  systems (no intent)
```

*Describe: three boxes side by side — security fights adversaries; privacy governs personal-data use even with no attacker; safety concerns unintentional harm.*

<!--
MISCONCEPTION: "privacy = security." Counter-example: a company can secure data perfectly and still violate privacy by selling it (3 min).
-->

---

# Example — CS track

**Scenario:** your web app leaks session tokens in referrer headers.

- Confidentiality failure → token theft → account takeover
- Fix: `Referrer-Policy: no-referrer`, `Secure` cookies

<!--
CS students: show the header flow on the board. 2 min.
-->

---

# Example — Data Science track

**Scenario:** an "anonymized" dataset of lab logins still re-identifies students from timestamps.

- Confidentiality holds; **privacy** fails via inference
- Fix: k-anonymity / aggregation before release

<!--
DS students: this is Lecture 28's seed — recall it there. 2 min.
-->

---

# Authorization: the course's bright line

> **No system outside the course sandbox. Ever.**

- Lab VMs, course datasets, designated training targets — that is the whole world
- Real systems → **responsible disclosure** only: report, don't probe

<!--
READ the authorization line verbatim; it reappears in every lab worksheet. 3 min incl. one-word-sign acknowledgment from class.
-->

---

# Responsible disclosure flow

```
[Researcher] --find--> [Private report] --fix window--> [Patch]
     |                                            |
     └── no exploit sale, no public detail ───────┘
```

*Describe: four-stage flow from finding to patch, with the constraint that details stay private during the fix window.*

<!--
Contrast full disclosure briefly (1 min). Point to CS-020 as preview.
-->

---

# Lab demo preview — Lab 00 (baseline)

- Instructor shows: VM snapshot → baseline scan (`lynis audit system` output) → snapshot revert
- **Minimum viable outcome:** students see a before/after hardening delta
- Sandbox only; screenshot policy from `practical-assessments.md`

<!--
DEMO: 4 min. If lynis missing: show `ss -tulpn` port inventory instead — pivot noted in teaching guide lecture-01.
-->

---

# Case session — 5 minutes

**CS-001 "Club committee password"** (Level 1 · Password & authentication)

Propose → groups explain → model reveal → tradeoffs

<!--
PROTOCOL: projector on scenario only. 5 min proposal, 2 groups explain, reveal model solution from case-solutions level-1. Discussion: shared vs individual accounts (10 min total for the block).
-->

---

# Wrap-up & exit ticket

- CIA → classify failures; privacy is not security; authorization is non-negotiable
- **Exit ticket:** 1) name the CIA property in today's case; 2) one sentence: why is selling "anonymized" data a privacy issue?

<!--
Close at 110 min. Preview L02: STRIDE. Collect tickets for early-warning tracker.
-->

---

# References

- Stallings & Brown, *Computer Security: Principles and Practice*, ch. 1
- NIST CSF 2.0 (functions overview)
- Course syllabus §4 (CLO-1), Lab 00 worksheet
