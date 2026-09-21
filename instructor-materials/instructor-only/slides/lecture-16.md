---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L16 · Module 4 · Week 8'
---

<!-- _class: lead -->
# Lecture 16 — Wireless & VPN Security
## + Midterm Review & Midterm
**Module 4 · Week 8 · 120 min · CLO-4 (primary), CLO-2 (supporting)**

<!--
TIMING: 1 min. Format: 45 min wireless/VPN content, 25 min review, 10 min break/setup, 90... wait — session is 120 min: 40 content, 20 review, 60 midterm (per plan §timing). Checkpoint-style discipline.
-->

---

# Learning Objectives

1. Compare WPA2/WPA3 handshake security
2. Explain captive-portal exposure
3. Debunk "VPN = secure"
4. Consolidate M1–M4 in the midterm

<!--
Midterm is the assessment unit for Week 8 (Q16). 2 min.
-->

---

# Wi-Fi evolution

| Standard | Handshake | Weakness |
|---|---|---|
| Open/captive | none | readable, spoofable |
| WPA2-PSK | PSK | offline dictionary on capture |
| WPA3-SAE | dragonfly | resists offline guessing |

*Describe: three-row evolution table; SAE's gain is resisting offline PSK guessing.*

<!--
MCQ-4.6/4.7. WPA3 ≠ invincible — transition modes downgrade. 5 min.
-->

---

# VPN — what it does and doesn't buy

```
VPN grants: network PRESENCE inside the perimeter
VPN does NOT grant: endpoint health, least privilege, behavior
```

*Describe: two-line ledger; presence is not safety — zero-trust posture still applies.*

<!--
Recall L14 identity-perimeter. Rogue AP geometry preview: CS-091. 4 min.
-->

---

# Midterm review — the shape of the paper

```
A: 10 × MCQ (1)      B: 2 × scenario (6)
C: choose 2 of 3 × 8 D: synthesis (8)      = 50
```

*Describe: four-section mark map; strategy — Section C rewards ordering and evidence, D rewards argued positions.*

<!--
STRATEGY (10 min): MCQ pass fast; C: read all three, pick two BEFORE writing; D: state position, cost, residual — the L04-MT-H rubric. Specimen paper (specimen-midterm.md) was practice; today's paper is different items.
-->

---

# CS example — campus Wi-Fi redesign

- WPA3-Enterprise + separate guest SSID + 802.1X — identity joins the air
- Sensor: rogue-AP detection on legitimate APs

<!--
2 min.
-->

---

# DS example — VPN telemetry

- VPN logs carry posture + location features — good detection fuel
- BUT VPN concentration = single log source — availability & privacy tradeoffs

<!--
2 min.
-->

---

# MIDTERM — administration

- 90 minutes from distribution; sections A–D; choose-two rule in C
- Closed book, no devices; papers counted before/after

<!--
ADMIN: seating plan, scripted announcement of the choose-two rule (from midterm-paper.md logistics). After exam: 2-min M5 preview, reading for L17.
-->

---

# Wrap-up

- M1–M4 consolidated; cryptography next — bring the Lab 15 starter questions

<!--
Post-exam: collect papers, note Section C selection balance for item analysis.
-->

---

# References

- Wi-Fi Alliance WPA3 overview; lecture plan lecture-16; midterm paper (instructor-only)
