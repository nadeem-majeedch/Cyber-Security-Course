# Lecture 17 — Symmetric Cryptography and Block Cipher Modes
**Module M5 · Week 9, Session 1 · 120 min · CLO-5 (primary)**

## Learning Objectives
1. Explain symmetric encryption's roles (bulk data, at-rest protection) and its key-distribution problem.
2. Choose block-cipher modes correctly: why ECB leaks patterns, why CBC needs a random IV, why AEAD modes (GCM) are the modern default.
3. Demonstrate ECB's pattern leakage visually (the classic image lab) and CBC bit-flipping mechanics (concept + lab).
4. Apply authenticated-encryption reasoning: confidentiality without integrity is incomplete.

## Key Concepts
- Block ciphers: AES as the workhorse; key sizes; block size 128-bit
- Modes: ECB (deterministic, pattern-preserving), CBC (IV + chaining, bit-flipping risk), CTR (stream-like, nonce reuse danger), GCM (AEAD: encryption + tag)
- Why integrity must ride with confidentiality; MAC-then-encrypt vs. AEAD
- Key distribution problem → motivates L18 (asymmetric)
- Nonce/IV reuse as the recurring catastrophic failure

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–10 | M5 hook: show ECB "penguin" image; class explains why the mode is broken from the picture alone | Hook |
| 10–30 | Cipher + modes tour: identical plaintext blocks under ECB; CBC chaining diagram; CTR nonce counter; GCM tag | Diagram walk |
| 30–48 | Failure gallery: ECB-encrypted profile avatar (shredder bug story), CBC bit-flip on a cookie flag, GCM nonce reuse consequences | Case slides |
| 48–60 | Break | — |
| 60–105 | **Lab block (Lab 15):** three-part: (a) ECB-penguin with a provided image + OpenSSL/pyca, (b) flip a CBC-encrypted "role=user" cookie to "role=admin" and watch padding/verdict, (c) switch to GCM and show the tamper fails the tag | Hands-on |
| 105–115 | Mode-selection decision table: students fill in (data type → mode → why) for 6 scenarios | Exercise |
| 115–120 | Exit ticket; preview L18 (PKI/TLS) | Q&A |

## Examples
- **CS track:** file-encryptor code review: `AES-256-CBC` with static IV — students list the three defects and rewrite with GCM + random nonce.
- **DS track:** encrypting telemetry at rest — column-level encryption with ECB leaked row patterns in a prior incident; discuss mode choice in analytical stores and key-rotation implications for long datasets.

## Discussion Questions
1. Why is "AES-256" an incomplete security claim? What question do you ask next?
2. GCM nonce reuse breaks catastrophically — how do engineers accidentally reuse nonces, and what design prevents it?
3. Where is deterministic encryption genuinely required (searchable encryption teaser)?

## Student Activity
Three-part crypto lab with a findings sheet; decision-table exercise; one student explains the penguin to the class (Feynman check).

## Problem-Solving Scenario
> A legacy app encrypts session state with AES-128-ECB; users can view their profile JSON in a URL parameter. Produce: what an attacker learns from ciphertext patterns, the tamper primitive available, the GCM-based fix with key/nonce handling, and the migration plan for existing stored ciphertext.

## Summary
Modes are where "we use AES" becomes true or false security. ECB for patterns, CBC for tampering, CTR for reuse — each failure is a design lesson; AEAD (GCM) is the default until proven otherwise. L18 adds the other half of trust: who vouches for keys.

## Formative Assessment
1. Which mode leaks plaintext patterns?
2. Why does CBC need a random IV?
3. What does the G in GCM buy you?

## Required Resources
- `labs/lab-15-modes/` starter scripts (Python `cryptography` lib or OpenSSL)
- Boneh & Shoup ch. on modes (selected); OWASP Cryptographic Storage Cheat Sheet
- CLO mapping: **CLO-5** (objectives 1–4).
