# Lab 17 — Password Storage & Secrets Hygiene
**Enrichment · Module 5 (L19) · CLO-5 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Benchmark hash/KDF cost (MD5, SHA-256, bcrypt, argon2id) on the course VM.
2. Migrate a seeded `md5(password)` credential store to argon2id with a dual-hash login window.
3. Find the three committed secrets in the seeded repo; write the revoke-first response.
4. Design the CI guard that prevents re-introduction.

## Prerequisites
Lecture 19. Python 3.10+; `pip install argon2-cffi bcrypt` on the VM.

## Hardware/Software Requirements
Course VM; `starter/store-v1.db` (seeded credential store, synthetic users), `starter/repo-with-secrets/` (seeded), benchmark script `starter/kdf_bench.py`.

## Installation and Setup
```bash
python -m pip install argon2-cffi bcrypt
python starter/kdf_bench.py --quick   # sanity check (~10 s)
```

## Ethical Authorization and Safety Notes
- All credentials are synthetic; the "breach dump" context is fictional. Do not add real passwords to any course store.
- The secrets sweep runs against the seeded repo only. Finding secrets in *other* repositories — including classmates' work — is out of scope; report and look away.
- No cracking is performed or taught here: the benchmark measures *defense cost* (legitimate verification speed), not attack speed.

## Step-by-Step Student Tasks
1. Benchmark: run `kdf_bench.py` full; record hashes/sec (MD5, SHA-256) and verifications/sec (bcrypt cost 12, argon2id default) in a table with your VM's CPU noted.
2. Migration: log in as a seeded user (store v1, md5); apply `starter/migrate_argon2id.py` design — implement the dual-hash window: verify md5 → on success re-hash argon2id → write v2 record → flag migrated.
3. Verify: log in again (argon2id path); check the record's `v` column flipped; a *wrong* password still fails.
4. Secrets sweep: `grep -r` the seeded repo for key-shaped strings; find all three (API key, DB URL with password, private-key block); for each, write the revoke-first response order.
5. CI guard: write a two-line pre-commit/CI rule (secret-pattern scan) that would have caught finding #1.
6. Policy check: against NIST 800-63B highlights in the notes, mark the seeded store's policy fields (length/composition/rotation) as aligned or not.

## Expected Observations
- Benchmark: fast hashes ≥ 10⁶/s vs KDF verifications ≤ 10²/s — a 4-orders-of-magnitude defense gap (your numbers recorded).
- Migration: v1 users flip to v2 on first successful login; users who never log in remain flagged (the reset-tail question).
- Secrets: one in a config file, one in a CI log excerpt, one in git *history* (deleted from HEAD but present in an old commit — `git log -p` finds it).

## Questions for Analysis
1. Your benchmark shows SHA-256 is ~10,000× faster than argon2id verification. Explain why that *exact* speed ratio is the attack economics problem.
2. The history-resident secret: why is `git rm` insufficient, and why is *revocation* the only real fix? What does the history rewrite buy, and at what team cost?

## Troubleshooting
`argon2` import error → pip install per setup; the image's venv may need activation. Benchmark too slow at defaults → the `--quick` flag exists for iteration; full run only for the submission. Migration flips no rows → check you're reading the *same* DB file the login script writes (`starter/store-v1.db`, absolute path).

## Cleanup Instructions
Delete the seeded DB and repo clone; revoke nothing (all keys are synthetic and instructor-managed); clear pip cache if disk-bound.

## Submission Requirements
Benchmark table (with CPU + versions), migration code/diff + before/after login transcript, secrets findings (3) with revoke-first orders, CI guard, policy checklist.

## Expected Outputs / Evidence
The history-resident secret must be cited by commit hash; findings without the commit reference are half-credited.

---
### Instructor Answer Key (summary)
- Seeded secrets: `AKIA...`-shaped API key in `config.ini`, `postgres://user:pw@...` in `ci-log.txt`, RSA private key in commit `a17f3c9` (deleted in `a18f4d0`).
- Migration order: revoke → rotate → rewrite history (optional, team-costly) → CI guard. Revoke-first is the graded ordering.
- Benchmark expectations (course VM class): MD5 ~10⁹/s, SHA-256 ~10⁸–10⁹/s, bcrypt-12 ~10²/s, argon2id ~10²/s with memory cost noted.
- Policy: seeded store enforces 8-char min + rotation 90 d → both misaligned with 800-63B (length ≥ 8 OK but composition/rotation theater misaligned).

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Benchmark table with methodology | 2 |
| Migration implementation + login transcripts | 3 |
| Secrets findings (3) with revoke-first orders (commit-cited) | 3 |
| CI guard + policy checklist | 2 |
