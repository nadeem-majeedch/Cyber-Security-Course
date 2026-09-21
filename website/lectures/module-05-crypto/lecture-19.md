# Lecture 19 — Hashing, Password Storage, and Key Management
**Module 5 · Week 10, Session 1 · 2 hours · CLO-5**

## Learning Objectives
1. Distinguish hash functions, HMACs, and password KDFs; select the right tool per use.
2. Explain password-cracking economics and salt's exact role.
3. Configure modern password storage (argon2id/bcrypt) with defensible parameters.
4. Apply key/secret lifecycle controls: generation, storage, rotation, and the committed-secret leak.

## Key Concepts and Definitions

**Three tools that look alike and are not:**

| Tool | Question it answers | Speed | Password storage? |
|---|---|---|---|
| **Hash** (SHA-256) | "Is this the exact input?" | Millions/s on GPU | **No** — designed to be fast |
| **HMAC** | "Did a key-holder produce this?" | Fast | No (integrity, not slow-by-design) |
| **Password KDF** (argon2id, bcrypt, PBKDF2) | "Can we make guessing expensive?" | Deliberately slow, memory-hard (argon2) | **Yes** |

**Salt:** a unique random value stored *with* each password hash. It defeats precomputation (rainbow tables) and identical-password correlation — it does **not** slow a targeted attack by itself. **Pepper:** a secret value *not* stored in the database (key vault/HSM); it adds defense if the DB leaks alone. *Neither replaces a slow KDF.*

**Cracking economics:** attacker cost = hash rate × work factor. Work factors are chosen so verification ≈ 100–300 ms on your hardware (user patience) while cracking becomes millions of years per attempt-space — parameters must be re-tuned as hardware improves.

**Password policy (NIST SP 800-63B direction):** length over composition-theater; screen against breach corpora; **no forced periodic rotation** without evidence of compromise; rate-limit and monitor authentication.

**Secrets lifecycle (the other half of the lecture):** generate with real randomness (L20 previews failures otherwise); store in vaults/secret managers with access logging; prefer **short-lived credentials**; rotate with a migration window; scan repositories for committed secrets (and revoke, not just delete — history persists).

## Conceptual Diagram

```text
cracking cost ladder (same password, lab hardware, illustrative order of magnitude):
  unsalted MD5      → instant (precomputed/parallel)
  salted fast hash  → parallel per-user guesses (fast hash + cheap salt)
  bcrypt (cost 12)  → ~100 ms × every guess
  argon2id          → ~100 ms AND gigabytes of memory per guess (GPU-unfriendly)

  salt: unique per user, stored with hash  → kills precomputation & cross-user matches
  pepper: secret outside the DB            → leaks of the DB alone are not enough
```

## Realistic Examples

- **CS track:** migration path for a `md5(password)` schema: dual-hash login window → upgrade-on-login to argon2id → forced-reset tail. Students write the algorithm.
- **DS track:** a notebook with an API key committed and forked: takedown order (revoke first, then rewrite history), pre-commit scanning, and short-lived tokens for scheduled jobs.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "SHA-256 is secure for passwords because it's strong" | Strength against *collisions* ≠ resistance to *guessing*; speed is the enemy. |
| "Salting encrypts the password" | Salt is not secret and not encryption; it makes each hash unique and defeats precomputation. |
| "Forcing 90-day rotation improves security" | Rotations push users toward predictable patterns; 800-63B advises against unless compromise is suspected. |
| "Deleted the secret from the repo, so it's safe" | Git history keeps it; revocation is the control, deletion is hygiene. |

## Classroom Activities

1. **Hash-speed benchmark (20 min, Lab 17 part A):** measure MD5/SHA-256/bcrypt/argon2id rates on lab hardware; the table lands the point.
2. **Schema fix (15 min, Lab 17 part B):** migrate the seeded `md5(pass)` store.
3. **Secrets sweep (15 min, Lab 17 part C):** find three committed secrets in the seeded repo; write the revoke-first response.

## Discussion Questions

1. Why does adding a pepper not excuse weak KDF parameters?
2. What evidence changed the guidance against forced rotation, and what replaces it?
3. Secrets in CI variables vs. vaults: which threat does each actually stop?

## Problem-Solving Exercise

> A breach dump (synthetic) contains 1M unsalted MD5 hashes; your app has 50k users on the same scheme.
> **Deliverable:** crack-risk estimate for your users; the migration algorithm with cutover steps; the user-communication plan (what, when); the CI guard that prevents re-introduction.

## Summary

Password security is rate-limiting: slow the guesser (memory-hard KDFs), unique-ify the target (salts), and assume some credentials leak anyway — which is why phishing-resistant MFA (L12) and key/secret hygiene complete the design. Next: reading failures in the wild.

## Exit Ticket

1. Why can't SHA-256 alone store passwords safely?
2. What does a salt accomplish — and what does it not?
3. Name two properties of a well-kept secret.

## References

- NIST SP 800-63B, *Digital Identity Guidelines* (Authentication). https://pages.nist.gov/800-63-3/
- OWASP Cheat Sheet Series, *Password Storage*. https://cheatsheetseries.owasp.org
- RFC 9106 (argon2). https://datatracker.ietf.org
- Bonneau, J. et al., "The Quest to Replace Passwords," *IEEE S&P*, 2012 (foundational survey).
