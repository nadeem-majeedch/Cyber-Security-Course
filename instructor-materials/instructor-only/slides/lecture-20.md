---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L20 · Module 5 · Week 10'
---

<!-- _class: lead -->
# Lecture 20 — Cryptography IV
## Failure Autopsies & Key Management
## + Checkpoint D
**Module 5 · Week 10 · 120 min · CLO-5 (primary), CLO-6 (supporting)**

<!--
TIMING: 1 min. Hook: "nobody breaks AES; they break the stuff around it." Checkpoint D at min 100.
-->

---

# Learning Objectives

1. Autopsy real crypto **misuse patterns** (not broken math)
2. Specify a key-management lifecycle
3. Map failures to CWEs (330, 321…)
4. Demonstrate Module 5 mastery (Checkpoint D)

<!--
3 min.
-->

---

# The misuse hall of fame

```
ECB on structured data      ── patterns leak
IV/nonce reuse              ── deterministic ciphertext
key beside the data         ── one theft steals both
entropy from time/PID       ── guessable keys (CWE-330)
```

*Describe: four one-line failure patterns; all are configuration/design choices, not broken primitives.*

<!--
MCQ-5.8 (key co-location), CWE-330 (checkpoint D item 6). 6 min.
-->

---

# Key-management lifecycle

```
generate (CSPRNG) ─► store (KMS/HSM) ─► rotate ─► revoke ─► destroy
        every arrow needs an OWNER and a PROCEDURE
```

*Describe: five-stage lifecycle chain; each stage requires a named owner and written procedure.*

<!--
SF-9's answer: without lifecycle, encryption is incomplete. 5 min.
-->

---

# Autopsy discipline (method, not gossip)

| Step | Question |
|---|---|
| observable | what did the system do wrong? |
| primitive | was the math itself broken? (usually NO) |
| control | which lifecycle/control was missing? |

*Describe: three-row autopsy table separating observation, primitive health, and missing controls.*

<!--
RULE: no invented incidents in class — use documented post-mortems cited in case-studies/. 4 min.
-->

---

# CS example — backup encryption done right

- Independent key, KMS-held, envelope-encrypted archive; restore drill proves it (CS-032 echo)

<!--
2 min.
-->

---

# DS example — model artifact signing

- Sign model binaries; verify at load — integrity + provenance
- Keys for signing: same lifecycle, separate from TLS material

<!--
2 min.
-->

---

# Lab demo — Lab 18 (crypto failures)

- Instructor runs the failure sandbox: ECB image, reused IV, hardcoded key — each fixed live
- **MVO:** three fix-verify pairs demonstrated
- Synthetic artifacts only

<!--
DEMO 5 min. This lab IS the checkpoint review — sequence them same week.
-->

---

# Checkpoint D — last 20 minutes

- 8 items: modes, IV, AEAD, certs, TLS 1.3, CWE-330 + 2 scenarios
- From `quizzes/quiz-10.md`

<!--
ADMIN at 100. M5 complete. Preview M6: bring Lab 20 dataset questions.
-->

---

# Case session (if time)

**CS-011 "Password on the router"** (Level 1 · Secrets handling)

→ co-location pattern in miniature.

<!--
Optional 8 min.
-->

---

# Wrap-up

- Math holds; engineering fails; lifecycle owns the keys
- **Reading:** L21 notes; sklearn check for M6

<!--
Close. Log checkpoint D scores.
-->

---

# References

- Ferguson, Schneier & Kohno, *Cryptography Engineering* (selected)
- Lecture plan lecture-20; Lab 18; checkpoint keys (instructor)
