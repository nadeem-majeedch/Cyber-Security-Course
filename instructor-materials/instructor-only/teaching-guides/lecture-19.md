# Teaching Guide — Lecture 19 (Hashing, Passwords, Key Management)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap cert lab verdicts | Quick cold-call. |
| 08–28 | Hash vs HMAC vs KDF | Three-column table; students place six use cases. |
| 28–50 | Cracking economics live | MD5 instant → salted slow → argon2 impractical; timing table. |
| 50–60 | Break | — |
| 60–100 | Lab 17 (benchmarks, schema fix, secrets sweep) | Three parts; checkpoints between. |
| 100–112 | Vault pattern + rotation | Short-lived creds; why env-vars persist. |
| 112–120 | Exit ticket + preview | Tease L20: "failures in the wild." |

## Board/Projector Activities

- **Projector:** the live benchmark terminal (hashes/sec counting up per algorithm).
- **Board:** the three-column tool table; the migration ladder (md5 → argon2id) drawn as steps.

## Speaker Notes (key beats)

1. The table is the lecture: hash = fast integrity; HMAC = keyed integrity; KDF = slow-on-purpose. "Password storage?" column decides everything.
2. Salt: unique per user, stored with the hash, kills precomputation and cross-user matching — it does NOT slow a targeted guess. Pepper adds a secret outside the DB.
3. Work factors: 100–300 ms verification on *your* hardware is the tuning target; re-tune as hardware improves.
4. 800-63B: length over composition; breach-corpus checks; no forced rotation without cause.
5. Secrets: generate with CSPRNG, vault them, prefer short-lived, revoke first when leaked (history persists).

## Expected Student Difficulties

- "Strong hash = safe storage" dies hard. Fix: the benchmark table — speed is the vulnerability.
- Salt/pepper conflation. Fix: the storage-location test (in the DB = salt; outside = pepper).
- Secrets sweep: students delete the secret from HEAD and feel done. Fix: the revoke-first rule; git history keeps secrets.

## Teaching Tips

- Run the benchmark before class to know your machine's numbers; the live table should match the handout's order of magnitude.
- The migration exercise has a natural trap (which users get upgraded when?): upgrade-on-login plus a reset tail — let teams discover it.
- Keep NIST guidance quoted precisely ("should" vs "shall") — students will cite it in the capstone.

## Answer Keys **[KEY]**

- Use-case placement: file checksum → hash; API request signing → HMAC; login storage → KDF; token fingerprint → hash; webhook verification → HMAC; key derivation for encryption → KDF (HKDF class, mention-only).
- Migration algorithm: login → compute md5, verify → on success re-hash with argon2id, store, drop md5 → after window, force reset for un-migrated accounts.
- Exit ticket: 1 designed for speed → guessable at GPU rates; 2 unique per user, defeats precomputation (not targeted guessing); 3 e.g., short-lived, access-logged, vault-stored (any two).

## Lab Delivery (Lab 17)

- Minimum viable outcome: benchmark table complete + schema fix committed + ≥ 1 secret found with revoke-first response.
- Expected failure points: argon2 parameters too high for the lab VM (set sane defaults in the starter); secrets sweep spoilers — keep the answer file in the instructor-only tier.

## Discussion Facilitation

Q2 (rotation evidence) rewards nuance: rotation made sense for shared/legacy secrets; for user passwords it degrades choices. Q3 (CI vars vs vaults): CI variables hide from *users*; vaults control access to *machines* — different threats.

## Accessibility

- Benchmark: numbers land on screen fast — provide the final table as a handout; students who can't read the terminal get identical data.
- Lab steps: numbered, keyboard-only paths; no step requires color discrimination.
