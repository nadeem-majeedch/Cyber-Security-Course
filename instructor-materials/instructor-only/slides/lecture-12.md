---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L12 · Module 3 · Week 6'
---

<!-- _class: lead -->
# Lecture 12 — Social Engineering & Awareness
## + Checkpoint C
**Module 3 · Week 6 · 120 min · CLO-3 (primary)**

<!--
TIMING: 1 min. Hook: "the samples were the EASY attack; humans are the cheap one." Checkpoint C at min 100.
-->

---

# Learning Objectives

1. Dissect phishing/BEC anatomy (pretext, urgency, authority)
2. Explain **SPF/DKIM/DMARC** roles
3. Design an awareness program with **report-rate** metrics
4. Demonstrate Module 3 mastery (Checkpoint C)

<!--
3 min. BEC = no payload, pure process abuse — flag the distinction.
-->

---

# Anatomy of a phish

```
Pretext (authority: "CEO")  +  Urgency ("by 3 pm")
  +  Process bypass ("don't call, I'm in a meeting")
  =  the kill chain of trust
```

*Describe: three stacked components summing to social-engineering success; the bypass line is the tell.*

<!--
Strongest red flag = bypass, not cosmetics (MCQ-3.6). 5 min.
-->

---

# Email authentication stack

| Layer | Question it answers |
|---|---|
| SPF | may this IP send for the domain? |
| DKIM | is the message cryptographically signed? |
| DMARC | alignment + what receivers should DO |

*Describe: three-row table; DMARC is policy on top of the other two.*

<!--
MISCONCEPTION: "DMARC blocks phishing." It blocks DOMAIN SPOOFING; lookalikes and compromises sail past. 5 min.
-->

---

# Awareness that changes behavior

```
click-rate   →  measures the trap
report-rate  →  measures the HUMAN sensor network
time-to-report → minutes matter most
```

*Describe: three-metric ladder replacing click-rate with reporting behavior as the true program outcome.*

<!--
MCQ-3.8 / checkpoint C item 3. Reward reporters publicly — blame kills sensors. 4 min.
-->

---

# CS example — pay-divert BEC

- Attacker: real thread hijack, changed bank details
- Control: out-of-band verification for ANY payment change — process, not product

<!--
2 min.
-->

---

# DS example — data-request pretext

- "Urgent: need the raw CSV for the board" — authority + bypass
- Control: data-access workflow with identity checks, not hallway approvals

<!--
2 min. Social engineering targets DS workflows too.
-->

---

# Lab demo — Lab 11 (awareness design)

- Instructor shows the sandbox phish-simulation console: build a campaign, set the report button
- **MVO:** measurable indicators defined before any simulated send
- All simulation mails land in the course tenant only — never off-platform

<!--
DEMO 4 min. Ethics line: simulations measure systems, not punish people.
-->

---

# Checkpoint C — last 20 minutes

- 8 items: DMARC, pretexts, metrics, hashes, persistence, fake-net + scenarios
- From `quizzes/quiz-06.md`

<!--
ADMIN at 100. M3 complete. Preview M4 networking.
-->

---

# Case session (if time)

**CS-023 "CEO's signature style"** (Level 2 · BEC)

→ which process control would have caught it?

<!--
Optional; CS-023 pairs with the CS example.
-->

---

# Wrap-up

- Trust is the attack surface; process controls defend it
- **Reading:** L13 notes; Wireshark installed check

<!--
Close. M3 complete — log checkpoint scores.
-->

---

# References

- NIST SP 800-61r2 (preparation phase); DMARC.org overview
- Lecture plan lecture-12; Lab 11; checkpoint keys (instructor)
