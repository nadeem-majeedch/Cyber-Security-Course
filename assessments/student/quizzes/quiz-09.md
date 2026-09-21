# Quiz 9 — Specimen (Week 9) · Cryptographic Foundations
**Ungraded self-check · 12 marks · ~12 minutes · CLO-5 · Answer key discussed in class; not posted.**

## Part A — Multiple choice (1 mark each)

**1.** The "ECB penguin" failure demonstrates that ECB mode:
- A. Compresses poorly
- B. Leaks plaintext patterns because equal blocks map to equal ciphertext
- C. Is slower than CBC
- D. Needs larger keys

**2.** Reusing the same IV in CBC mode causes:
- A. Key exposure
- B. Identical plaintext prefixes to encrypt identically, enabling inference
- C. MAC failure
- D. A longer ciphertext

**3.** GCM is preferred over plain CBC+HMAC in new designs chiefly because:
- A. It uses smaller keys
- B. It provides authenticated encryption in one operation, preventing tampering
- C. It needs no IV
- D. It is post-quantum secure

**4.** A message encrypted with a recipient's public key can be decrypted only with:
- A. The sender's public key
- B. The recipient's private key
- C. A shared secret
- D. The recipient's public key

**5.** In TLS 1.3, the certificate's job is to:
- A. Encrypt the application data directly
- B. Bind the server's name to its public key, authenticated through the CA chain
- C. Replace the handshake
- D. Compress the session tickets

## Part B — Short answer (7 marks)

**6.** (a) State what "forward secrecy" gives you in one sentence (2).
(b) A classmate proposes hashing passwords with SHA-256 plus a per-user salt. Explain the two weaknesses of this for password storage (3) and name the primitive you would use instead (1).
(c) One sentence: why is encryption of passwords (rather than hashing) a design failure? (1)

---
*Specimen items are contaminated for grading use once shown. Review answers against the in-class key.*
