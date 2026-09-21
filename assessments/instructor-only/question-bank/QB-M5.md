# Question Bank — Module 5 (L17–L20) · CLO-5 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q9 (W9), Q11 (W11), and makeup packs. Duplicate-avoidance rule: see `README.md`.

## MCQ-5.1

**Topic:** Block-cipher modes · **CLO-5** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 9
**Used in:** Q9

The failure of ECB mode on images ("ECB penguin") demonstrates that ECB:

- A. Compresses poorly
- B. Leaks plaintext patterns because equal blocks map to equal ciphertext ✔
- C. Is slower than CBC
- D. Requires larger keys

**Explanation:** Deterministic, stateless block encryption reveals structure; identical blocks encrypt identically. Key: B.

## MCQ-5.2

**Topic:** IV usage · **CLO-5** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 9
**Used in:** Q9

Reusing the same IV in CBC mode causes:

- A. Key exposure
- B. Identical plaintext prefixes to encrypt identically, enabling inference ✔
- C. MAC failure
- D. Longer ciphertext

**Explanation:** The IV XORs the first block; repetition makes encryption deterministic across messages — the pattern leak returns. Key: B.

## MCQ-5.3

**Topic:** AEAD · **CLO-5** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 9
**Used in:** Q9

GCM is preferred over plain CBC+HMAC in new designs chiefly because:

- A. It needs smaller keys
- B. It provides authenticated encryption in one operation, preventing tampering ✔
- C. It works without an IV
- D. It is post-quantum

**Explanation:** AEAD couples confidentiality and integrity (tag); composition errors (MAC-then-encrypt) vanish. Key: B.

## MCQ-5.4

**Topic:** Asymmetric roles · **CLO-5** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 9
**Used in:** Q9

A message encrypted with a recipient's public key can be decrypted only with:

- A. The sender's public key
- B. The recipient's private key ✔
- C. A shared secret
- D. The recipient's public key

**Explanation:** Public-key encryption is one-way with the private key; signatures use the inverse operation. Key: B.

## MCQ-5.5

**Topic:** Hash integrity · **CLO-5** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 11
**Used in:** Q11

Why does a checksum alone fail to prove download authenticity?

- A. Checksums are too slow
- B. An attacker who replaces the file can recompute and publish a matching checksum ✔
- C. Checksums expire
- D. Files over 4 GB cannot be hashed

**Explanation:** Integrity without authenticated channel is forgeable; you need a signature or an authenticated (TLS) source. Key: B.

## MCQ-5.6

**Topic:** Password hashing · **CLO-5** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 11
**Used in:** Q11

The correct password-storage choice for a new web app is:

- A. SHA-256 with a per-user salt
- B. Argon2id (or bcrypt) with tuned work factor and per-user salt ✔
- C. AES-256 encryption of passwords
- D. MD5 with pepper

**Explanation:** Password storage needs memory-hard KDFs; raw SHA-256 is fast (GPU-friendly). Encrypting passwords is reversible design failure. Key: B.

## MCQ-5.7

**Topic:** Salting rationale · **CLO-5** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 11
**Used in:** Q11

Per-user salts primarily defeat:

- A. Phishing
- B. Precomputed rainbow-table attacks and cross-user deduplication ✔
- C. Side-channel attacks
- D. Session hijacking

**Explanation:** Salts make each hash unique, invalidating precomputation and revealing equal-password users. Key: B.

## MCQ-5.8

**Topic:** Key management · **CLO-5** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 11
**Used in:** Q11

A backup archive is encrypted, but the key was stored in the same encrypted volume. The design failure is:

- A. Wrong cipher choice
- B. Key and data co-located — no independent protection boundary ✔
- C. Missing HMAC
- D. Weak PRNG

**Explanation:** Key management demands separation and lifecycle control; the strongest cipher cannot protect a key stored beside the data. Key: B.

## SA-5.1 (short answer, 6 marks)

**Topic:** TLS handshake · **CLO-5** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 9
**Used in:** Q9

In TLS 1.3: state the purpose of the certificate (2), how session keys are derived (2), and what "forward secrecy" gives you (2).

**Key:** Certificate binds the server name to its public key, authenticated via the CA chain. Session keys derive from ephemeral (EC)DH shared secret via HKDF — fresh per session. Forward secrecy: later private-key compromise does not decrypt past recorded sessions (ephemeral keys erased).

## SA-5.2 (short answer, 4 marks)

**Topic:** Crypto failure autopsy · **CLO-5** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 11
**Used in:** makeup MT-6 only

A developer stores session tokens as `MD5(user_id + fixed_secret)`. Identify two flaws and give the corrected design.

**Key:** MD5 unsuitability (collision/broken for security purposes) and guessability (small user_id space enables brute force of the whole token space; fixed secret = no per-token entropy). Fix: random 128+ bit tokens from CSPRNG stored hashed server-side; or signed tokens (HMAC) with random IDs — never derived from guessable inputs.
