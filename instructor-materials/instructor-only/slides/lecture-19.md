---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L19 · Module 5 · Week 10'
---

<!-- _class: lead -->
# Lecture 19 — Cryptography III
## Hashing & Password Storage
**Module 5 · Week 10 · 120 min · CLO-5 (primary)**

<!--
TIMING: 1 min. Hook: "your database WILL leak; the only question is what the passwords are worth inside it."
-->

---

# Learning Objectives

1. Distinguish integrity hashes from password KDFs
2. Explain **salt** and **work factor**
3. Select Argon2id/bcrypt parameters defensibly
4. Design login rate-limiting that survives evasion

<!--
Objectives = Lab 17 + checkpoint D. 3 min.
-->

---

# Fast hash ≠ password hash

```
SHA-256:  GPU: billions/s   → meant for integrity
Argon2id: memory-hard KDF   → meant to be SLOW
```

*Describe: two-line contrast; password hashing must be expensive on attack hardware, which integrity hashing must not be.*

<!--
MISCONCEPTION: "salt makes SHA-256 safe." Salt kills precomputation, not SPEED (MCQ-5.7). 5 min.
-->

---

# Salt, pepper, work factor

| Ingredient | Stored where? | Purpose |
|---|---|---|
| salt | with the hash | unique per user; kills rainbow tables |
| pepper | secret store | extra defense-in-depth |
| work factor | tunable | grows as hardware does |

*Describe: three-row table; salt is per-user and public, pepper is a secret, work factor is the adjustable cost.*

<!--
Checkpoint D territory. Tuning: log₂ iterations / memory target. 5 min.
-->

---

# Cracking economics (defensive)

```
attacker cost ∝ work factor × password entropy
defender controls:  KDF params, breach-corpus checks, MFA
```

*Describe: cost equation sketch — defenders raise the first term; policy raises the second.*

<!--
Breach-corpus checks (CS-021) beat composition rules — NIST 800-63B framing. 4 min.
-->

---

# CS example — login endpoint

- Argon2id (m=64 MiB, t=3), per-user salt, constant-time verify
- Rate limit by (account, source) aggregates — recall L15 loop

<!--
2 min.
-->

---

# DS example — study participant accounts

- Same KDF discipline in research apps; never export raw password hashes into analytics datasets

<!--
2 min. CS-073 echo: datasets inherit storage sins.
-->

---

# Lab demo — Lab 17 (password storage)

- Instructor benchmarks SHA-256 vs Argon2id on the VM — shows the wall-clock gap, then cracks the unsalted list offline
- **MVO:** tuned KDF + justification in writing
- Synthetic corpus only

<!--
DEMO 6 min. The wall-clock gap is the visceral lesson.
-->

---

# Case session

**CS-021 "Breach-corpus check"** (Level 2 · Password & authentication)

→ what does corpus-checking replace, and what does it miss?

<!--
10 min. Model: replaces composition rules; misses targeted attacks — MFA covers that.
-->

---

# Wrap-up & exit ticket

- KDFs are slow on purpose; salts unique; work factors grow
- **Exit:** order these: MD5, SHA-256+salt, Argon2id — best to worst for passwords

<!--
Close 110. Preview L20: failures & key management.
-->

---

# References

- NIST SP 800-63B (authenticator guidance); RFC 9106 (Argon2)
- Lecture plan lecture-19; Lab 17
