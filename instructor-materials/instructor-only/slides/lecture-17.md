---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L17 · Module 5 · Week 9'
---

<!-- _class: lead -->
# Lecture 17 — Cryptography I
## Symmetric Ciphers, Modes & IVs
**Module 5 · Week 9 · 120 min · CLO-5 (primary)**

<!--
TIMING: 1 min. Hook: "encryption is easy; encryption that SURVIVES its environment is engineering."
-->

---

# Learning Objectives

1. Choose block-cipher **modes** by property
2. Demonstrate **ECB's** structural leak
3. Explain IV randomness requirements
4. Justify **AEAD** for new designs

<!--
Lab 15 uses the ECB-penguin artifact live. 3 min.
-->

---

# Modes at a glance

| Mode | Property | Failure mode |
|---|---|---|
| ECB | deterministic blocks | leaks patterns |
| CBC | chained + random IV | IV reuse = patterns |
| GCM | AEAD (conf + integrity) | nonce reuse catastrophic |

*Describe: three-row mode table; each row pairs the mode's property with its characteristic misuse.*

<!--
The GCM nonce-reuse row is the advanced hook — Lab 18 autopsy. 6 min.
-->

---

# The ECB penguin

```
  plaintext image        ECB-encrypted
  ┌──────────────┐      ┌──────────────┐
  │  [penguin]   │ ──►  │  [penguin]   │  silhouette survives!
  └──────────────┘      └──────────────┘
```

*Describe: two side-by-side boxes; the encrypted image still shows the penguin outline because equal blocks encrypt identically.*

<!--
You cannot hide structure by encrypting blocks independently. MCQ-5.1. 4 min.
-->

---

# IVs — freshness beats secrecy

```
C₁ = E(k, P₁ ⊕ IV)        IV public, RANDOM per message
IV fixed  → identical starts → identical ciphertexts
```

*Describe: the CBC first-block equation plus the consequence line; the IV must be fresh, not secret.*

<!--
MCQ-5.2. Nonce/IV management reappears at GCM. 4 min.
-->

---

# CS example — file-store encryption

- Per-file GCM, unique nonce from counter, keys in KMS
- Integrity comes from the tag, not hope

<!--
2 min.
-->

---

# DS example — encrypted exports

- Dataset export column-level AES-GCM; deterministic encryption ONLY where matching is required — and then know the leak you accepted

<!--
2 min. Deterministic-encryption tradeoff = CS-047.
-->

---

# Lab demo — Lab 15 (crypto operations)

- Instructor runs `crypto_lab.py`: ECB vs CBC image output side by side, then GCM tamper flip
- **MVO:** one tamper attempt detected by the GCM tag
- Starter tested on Python 3.14/OpenSSL 3.5; AEAD paths need `cryptography` on the VM

<!--
DEMO 5 min. Honesty note from lab-validation-report: openssl enc rejects AEAD — route via Python; say it aloud.
-->

---

# Case session

**CS-047 "Deterministic by necessity"** (Level 3 · Cryptography)

→ when does determinism buy queryability, and what leaks?

<!--
10 min. Model names the leak explicitly and prices it.
-->

---

# Wrap-up & exit ticket

- Modes are properties; IVs need freshness; AEAD by default
- **Exit:** why does ECB leak? one sentence

<!--
Close 110. Preview L18: TLS/PKI.
-->

---

# References

- Boneh & Shoup ch. on modes; lecture plan lecture-17; Lab 15
