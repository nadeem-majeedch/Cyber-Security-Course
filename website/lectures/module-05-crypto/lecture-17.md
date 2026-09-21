# Lecture 17 — Symmetric Cryptography and Block Cipher Modes
**Module 5 · Week 9, Session 1 · 2 hours · CLO-5**

## Learning Objectives
1. Explain symmetric encryption's roles and its key-distribution problem.
2. Choose block-cipher modes correctly: ECB's leakage, CBC's IV requirements, CTR's nonce discipline, GCM's authenticated encryption.
3. Demonstrate ECB pattern leakage visually and CBC bit-flipping mechanics.
4. Argue why confidentiality without integrity is incomplete.

## Key Concepts and Definitions

**Symmetric encryption:** one shared key both encrypts and decrypts. Fast; used for bulk data. The **key-distribution problem**: both sides need the same secret *before* they can communicate securely — the problem asymmetric crypto solves (L18).

**AES:** the standard block cipher — 128-bit blocks, 128/192/256-bit keys. *Fact:* with a proper mode, AES itself has no publicly known practical break; failures live in *how* it is used.

**Modes — what each one is for:**

| Mode | Idea | Failure if misused |
|---|---|---|
| **ECB** | Each block encrypted independently | Identical plaintext blocks → identical ciphertext: patterns leak (deterministic) |
| **CBC** | Chain blocks with previous ciphertext; needs a **random IV** per message | Predictable/reused IV → tampering (bit-flipping), pattern leaks |
| **CTR** | Encrypt a counter → keystream; nonce+counter must never repeat | **Nonce reuse** → keystream reuse → plaintext recovery |
| **GCM** | CTR + authentication **tag** (AEAD) | Nonce reuse is catastrophic (tag forgery + plaintext exposure) |

**The integrity lesson:** encryption alone answers "can they read it?", never "did they change it?" **AEAD** (authenticated encryption with associated data, e.g., GCM) answers both — it is the default choice until a documented reason says otherwise.

**CBC bit-flipping (the lab):** in CBC, flipping bit *i* of ciphertext block *n* flips bit *i* of plaintext block *n* *and* garbles block *n−1*. If the format tolerates the garble (e.g., a cookie where the flag is in the last block), tampering succeeds without the key.

## Conceptual Diagram

```text
ECB:  P1 P2 P3 P1  →  C1 C2 C3 C1        ← pattern visible (penguin!)
CBC:  IV ⊕ P1 → E → C1;  C1 ⊕ P2 → E → C2   (chaining; IV must be random per message)
CTR:  counter+1 → E(key) → keystream ⊕ P    (nonce reuse = keystream reuse = game over)
GCM:  CTR ciphertext + auth tag             (verify tag BEFORE using plaintext)
```

## Realistic Examples

- **CS track:** a file-encryptor using `AES-256-CBC` with a *hard-coded IV*: three defects (static IV, no MAC, unauthenticated format) — students rewrite with GCM and a per-message random nonce.
- **DS track:** a telemetry archive encrypted per-column with ECB: row patterns leak through ciphertext (same customer, same ciphertext prefix). Fix: AEAD + key-rotation plan for data at rest (ties to L20's migration thinking).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "AES-256 is automatically secure" | The key *size* is the smallest part; mode, IV/nonce discipline, and authentication decide. |
| "ECB is fine for small data" | Small structured data (tokens, flags) is exactly where patterns leak meaning. |
| "Encryption provides integrity" | It does not; bit-flipping and unauthenticated formats exist. AEAD or a MAC is required. |
| "The IV is a secret" | The IV must be *unpredictable/random* per message, not secret — confusing IV with key breaks designs. |

## Classroom Activities

1. **ECB penguin reveal (5 min):** the image lab output; class explains the failure from the picture.
2. **Lab 15 (45 min):** (a) ECB-penguin with the provided image, (b) CBC bit-flip the `role=user` cookie to `role=admin`, (c) switch to GCM, show tampering fails the tag.
3. **Mode decision table (10 min):** six data types → mode → why.

## Discussion Questions

1. Why is "we use AES-256" an incomplete security claim? What is your next question?
2. How do engineers accidentally reuse nonces, and what design prevents it?
3. Where is deterministic encryption genuinely required? (teaser: searchable encryption)

## Problem-Solving Exercise

> A legacy app encrypts session state with AES-128-ECB; the ciphertext is exposed in a URL parameter.
> **Deliverable:** what an attacker learns from ciphertext patterns; the tamper primitive available; the GCM-based fix with key/nonce handling; a migration plan for existing stored ciphertext.

## Summary

Modes are where "we use AES" becomes true or false: ECB leaks, CBC needs random IVs, CTR/GCM demand nonce discipline — and integrity must ride along (AEAD). Next lecture: the trust machinery that distributes keys in the first place.

## Exit Ticket

1. Which mode leaks plaintext patterns?
2. Why does CBC need a random IV?
3. What does the G in GCM buy you?

## References

- NIST SP 800-38A (block-cipher modes) and SP 800-38D (GCM). https://csrc.nist.gov
- Boneh, D. & Shoup, V., *A Graduate Course in Applied Cryptography* (modes chapters), free draft.
- OWASP Cheat Sheet Series, *Cryptographic Storage*. https://cheatsheetseries.owasp.org
- Python `cryptography` library docs (hazmat primitives warnings). https://cryptography.io
