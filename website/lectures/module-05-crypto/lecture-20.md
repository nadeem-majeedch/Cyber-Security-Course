# Lecture 20 — Cryptographic Failures in the Wild + Checkpoint D
**Module 5 · Week 10, Session 2 · 2 hours · CLO-5 (primary), CLO-6 (supporting)**

## Learning Objectives
1. Dissect named crypto failure classes and classify root causes (mode misuse, randomness, protocol logic, implementation).
2. Extract design rules from failure patterns.
3. Evaluate a vendor's crypto claims from a spec sheet.
4. Consolidate Module 5 (Checkpoint D).

## Key Concepts and Definitions

**Failure taxonomy** (the lecture's organizing table):

| Class | What goes wrong | Representative CWE |
|---|---|---|
| Mode misuse | ECB for structured data; unauthenticated encryption | CWE-327 |
| Randomness | Predictable keys/nonces (weak seeds, entropy starvation) | CWE-330, CWE-338 |
| Protocol logic | Downgrade paths; oracle behaviors (padding-oracle class) | CWE-326/327 family |
| Implementation | Hard-coded keys, home-rolled ciphers, key material in firmware | CWE-798, CWE-327 |

**Case set (each taught from a public write-up; citations in `case-studies/`):**
1. **Predictable RNG → predictable keys:** weak seeding made key generation guessable; design rule: use vetted CSPRNGs, entropy health checks.
2. **Protocol downgrade:** a fallback path let connections degrade to weak parameters; design rule: fail closed, no silent downgrades.
3. **Hard-coded key harvest:** one key in firmware = one key for every device ever shipped; design rule: per-device keys, keys out of code (vaults/HSMs).
4. **Mode misuse at rest:** deterministic encryption leaked record structure; design rule: AEAD defaults; plan re-encryption migrations.

**Crypto agility:** the *design property* that lets you swap algorithms/parameters without re-architecting — what made some of these systems patchable and others recallable.

**Reading CVE entries:** CWE-327 (broken/proprietary crypto), CWE-330 (insufficient randomness), CWE-798 (hard-coded credentials) — three families that cover most of what you will meet.

## Conceptual Diagram

```text
failure classes feed one wall:
  randomness ──┐
  mode misuse ─┼──► design rules:  vetted CSPRNG · AEAD default · fail closed ·
  protocol ────┤                    per-device keys · keys out of code · agility
  implementation ─┘
vendor claim red flags: "proprietary algorithm" · no mode named · "military-grade"
                         · no KMS story · no randomness story
```

## Realistic Examples

- **CS track:** the firmware-signing story: a verification key hard-coded in every device — the harvest campaign writes itself; students map it to CWE-798 and the HSM/per-device fix.
- **DS track:** a telemetry archive encrypted per-record with ECB and a timestamp-derived static key: pattern leakage across records; students design the re-encryption plan (mode fix + key rotation + downtime window).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Don't roll your own crypto means don't touch crypto" | It means: use vetted libraries and protocols; *someone* must build them under public scrutiny — your job is correct use and verification. |
| "A breach of the algorithm means everything breaks" | Almost all real failures are usage and key management, not the primitives. |
| "Hard-coded keys are fine if the binary is obfuscated" | Obfuscation delays, never prevents, extraction. |
| "We'll rotate keys later" | Without agility, later is a recall. Design rotation in. |

## Classroom Activities

1. **Case 1 walk-through (20 min):** the RNG failure chain; class writes the design rule.
2. **Pair dissection (15 min):** cases 2–3; classify root cause; one-line design rule each; pairs present.
3. **Checkpoint D (12 min).**
4. **Lab 18 (25 min):** three fictional vendor crypto pages; students write the challenge questions that unmask the claims.
5. **Failure-pattern wall (10 min):** all Module 5 failures aggregated into the four-class taxonomy.

## Discussion Questions

1. Who *should* build crypto, with what process — and how do the rest of us verify what we use?
2. Which failure class is hardest to patch retroactively (data at rest vs. code) — and what does that imply for migration planning?
3. Which three questions unmask marketing crypto claims fastest?

## Problem-Solving Exercise

> An IoT camera line: "AES-256" in the spec, no mode named, one key string in every firmware image, debug RNG seeded from uptime.
> **Deliverable:** the four defects, each classified in the taxonomy; the exploit narrative a researcher would follow (responsible-disclosure framing); the remediation spec (mode, per-device keys, CSPRNG, KMS) and the OTA-patch strategy.

## Summary

Crypto fails at the seams — randomness, modes, protocol logic, key custody — rarely at the primitive. The design rules on the wall are the module's takeaway: vetted randomness, AEAD defaults, fail closed, keys out of code, agility for the day you must rotate. Module 6 weaponizes data science for defense.

## Exit Ticket

1. CWE-330 covers which failure class?
2. Why is a data-at-rest crypto failure worse to remediate than a code failure?
3. Name the red flag in "proprietary military-grade algorithm."

## References

- MITRE CWE-327, CWE-330, CWE-338, CWE-798. https://cwe.mitre.org
- NIST SP 800-57 Part 1 (key management). https://csrc.nist.gov
- IETF, RFC 8446 §appendix (protocol-failure lessons context). https://datatracker.ietf.org
- Case write-ups used in class: see `case-studies/` (per-term selection with full citations; no invented incidents).
