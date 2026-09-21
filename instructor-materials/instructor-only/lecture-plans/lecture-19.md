# Lecture 19 — Hashing, Password Storage, and Key Management
**Module M5 · Week 10, Session 1 · 120 min · CLO-5 (primary)**

## Learning Objectives
1. Distinguish hash functions, HMACs, and password KDFs; select the right tool per use.
2. Explain password-cracking economics: dictionaries, masking, rainbow-table history, salt's exact role.
3. Configure modern password storage: argon2id/bcrypt parameters and work-factor reasoning.
4. Apply key-management lifecycle controls: generation, storage (vaults/HSM concept), rotation, and secrets in code (the classic leak).

## Key Concepts
- Hash properties (preimage, second-preimage, collision) vs. HMAC (keyed integrity) vs. KDFs (slow on purpose: argon2id, bcrypt, PBKDF2 comparison)
- Salt vs. pepper; per-user salts defeat precomputation; work factors vs. GPU farms
- Password policy reality: length > composition; NIST SP 800-63B guidance highlights; breach-corpus checking
- Secrets management: env vars vs. vaults, short-lived credentials, scanning for committed secrets
- Key rotation, key ceremonies (awareness), split knowledge (concept)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L18: cert lab verdicts | Q&A |
| 08–28 | Hash vs. HMAC vs. KDF: three-column comparison; students place 6 use cases in columns | Sorting exercise |
| 28–50 | Cracking economics live: provided leak corpus (synthetic) — instructor cracks unsalted MD5 instantly, salted MD5 slowly, argon2id impractically; timing table on board | Live demo |
| 50–60 | Break | — |
| 60–100 | **Lab block (Lab 17):** (a) measure hashes/sec for MD5/SHA/bcrypt/argon2id on lab hardware, (b) fix a stored-credential schema from `md5(pass)` to argon2id with migration path, (c) secrets-hygiene sweep of a seeded repo — find 3 committed secrets, propose fixes | Hands-on |
| 100–112 | Key-management talk: the vault pattern, rotation without downtime, why "secrets in env vars" persists | Discussion |
| 112–120 | Exit ticket; preview L20 (crypto failures) | Q&A |

## Examples
- **CS track:** migration path design — dual-hash login window, upgrade-on-login, forced reset tail; students write the algorithm.
- **DS track:** a Kaggle-style notebook with an API key committed and forked — the takedown process, secret revocation order, and pre-commit scanning to stop recurrence.

## Discussion Questions
1. Why does adding a pepper not excuse weak KDF parameters?
2. NIST says drop mandatory rotation for passwords — what evidence changed the guidance, and what replaces rotation?
3. Secrets in CI variables vs. vaults: what threat does each actually stop?

## Student Activity
Hash-speed benchmarking with a results table; schema-fix exercise; repo secrets sweep with a findings report.

## Problem-Solving Scenario
> A breach dump (synthetic) contains 1M unsalted MD5 hashes; your app has 50k users on the same scheme. Produce: the crack-risk estimate for your users, the migration algorithm with cutover steps, the communication plan (what do you tell users and when), and the CI guard that prevents re-introduction.

## Summary
Password security is a rate-limiting game: slow the attacker with memory-hard KDFs, unique salts, and sane policies, then assume some credentials leak anyway — which is why MFA from L12 and key hygiene close the loop. L20 audits the catastrophic versions of today's lessons.

## Formative Assessment
1. Why can't you use SHA-256 directly for password storage?
2. What does a salt accomplish, and what does it not?
3. Name two properties of a well-kept secret.

## Required Resources
- `labs/lab-17-password-storage/` benchmark script + seeded repo
- NIST SP 800-63B (selections); OWASP Password Storage Cheat Sheet
- CLO mapping: **CLO-5** (objectives 1–4).
