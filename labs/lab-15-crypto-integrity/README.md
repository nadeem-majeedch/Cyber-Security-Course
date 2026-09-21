# Lab 15 — Cryptographic Operations & Integrity Checks
**Core Lab 3 · Module 5 (L17, L19) · CLO-5 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Produce and verify file digests; use digests for integrity verification.
2. Compute HMACs and explain the difference between a plain hash and a keyed hash.
3. Encrypt with a KDF-derived key and observe tamper detection with AEAD (GCM).
4. Benchmark password-KDF cost and connect it to cracking economics.

## 2. Prerequisites
Lectures 17 and 19 (modes, AEAD, KDFs, salts). Starter script `starter/crypto_lab.py`.

## 3. Hardware/Software Requirements
- Course VM (Linux) with Python 3.10+ and OpenSSL 3.x.
- Python package `cryptography` (Part C/D on the VM): `python -m pip install cryptography`.
- Provided files: `starter/files/alpha.txt`, `beta.txt`, and the instructor's `manifest.sha256`.

## 4. Installation and Setup
1. Verify the toolchain on the course VM:
   ```bash
   python --version && openssl version
   ```
2. Install the AEAD library:
   ```bash
   python -m pip install cryptography
   python -c "from cryptography.hazmat.primitives.ciphers.aead import AESGCM; print('AESGCM OK')"
   ```
3. Smoke-test the starter (digest path):
   ```bash
   python crypto_lab.py sha256 files/alpha.txt
   ```
   > **Tested vs. untested (recorded honestly):** the digest/HMAC command shapes and the `crypto_lab.py` digest/HMAC paths were executed and verified on the instructor workstation (Python 3.14 + OpenSSL 3.5) before publication, including the finding that `openssl enc` **does not support AEAD ciphers** (it prints `enc: AEAD ciphers not supported`). The `cryptography`-package paths (GCM, tamper step) follow the library's stable API but are **untested on the course VM image** — if they fail, that is reportable, expected friction, and part of your troubleshooting write-up.

## 5. Ethical Authorization and Safety Notes
- You are hashing and encrypting *your own* course files on *your own* VM. Nothing here attacks anything.
- Do not encrypt anything you do not own; do not use course keys for personal files; the lab's keys are intentionally disposable.
- Password-cracking is out of scope: you measure KDF *cost* (the defense), you do not crack anything.

## 6. Step-by-Step Student Tasks
| # | Task | Command shape |
|---|---|---|
| A1 | Digest all three provided files (two commands: python and openssl) and cross-check they agree | `python crypto_lab.py sha256 files/alpha.txt`; `openssl dgst -sha256 files/alpha.txt` |
| A2 | Verify the instructor's manifest; identify the one file whose digest does **not** match | `sha256sum -c manifest.sha256` |
| A3 | Flip one byte in the mismatched file (`printf 'x' >> files/beta.txt`), re-digest, then restore from the pristine copy | digest before/after |
| B1 | HMAC the file with the course key | `python crypto_lab.py hmac files/alpha.txt --key course-lab-key`; cross-check `openssl dgst -sha256 -hmac course-lab-key files/alpha.txt` |
| B2 | Change the key; observe the HMAC changes while the plain digest does not | two runs |
| B3 | KDF timing: derive a key from `password` + provided salt at 100k and 600k iterations; record both wall-clock times | `python -c` snippet in worksheet handout |
| C1 | AEAD encrypt a file (key + nonce from the handout format) | `crypto_lab.py aead` path on VM, or the notebook snippet |
| C2 | Tamper: flip one ciphertext byte; attempt decrypt; record the exact error class | decrypt run |
| C3 | Explain in two sentences why the CBC path cannot offer this detection (from L17) | written answer |

## 7. Expected Observations
- Python `hashlib` and `openssl dgst` produce **identical** digests (verified: both output the same hex for the same file on the tested toolchain).
- Exactly one manifest entry fails; appending one byte changes the digest completely (avalanche).
- HMAC: same file, different key → different tag; plain digest unchanged.
- KDF timing scales ~linearly with iterations (roughly 6× from 100k → 600k; your VM's absolute numbers go in the report).
- GCM: one flipped byte → decrypt fails with an authentication/InvalidTag-class error, not garbage output.

## 8. Questions for Analysis
1. The manifest caught a tampered file — but a plain digest is unkeyed. What attack does an HMAC defend against that a published digest does not?
2. Why did `openssl enc -aes-256-gcm` fail on this toolchain, and what does that failure teach about "AES-256" as a security claim?
3. Your KDF benchmark: if verification must stay ≤ 300 ms on the lab VM, what is the maximum iteration count you measured, and why does that number not transfer to a phone?

## 9. Troubleshooting
- `enc: AEAD ciphers not supported` → expected: use the Python path (Part C) for GCM; openssl stays on digests/HMAC/CBC.
- `ModuleNotFoundError: cryptography` → run the setup step 4.2; on offline VMs use the course wheel share.
- Digest mismatch you didn't expect → check line endings (`file alpha.txt`); CRLF vs LF changes bytes and therefore the digest.
- HMAC mismatch across tools → both tools HMAC the *raw bytes*; quoting differences in the key argument are the usual cause.

## 10. Cleanup Instructions
- Delete generated ciphertext/keystream files and restored-file copies.
- Keep your report; do not submit the provided keys as if they were secrets (they are classroom keys and publicly meaningless — note this fact in your report as a key-management observation).

## 11. Submission Requirements
- `results.md`: digest cross-check table, manifest verdict, HMAC comparison table, KDF timing table, GCM tamper transcript (the exact error text), answers to the three questions, and the key-management observation.
- Terminal transcript (text, not screenshots-only).

## 12. Expected Outputs / Evidence
Executed commands with outputs for every task row; personally produced; the mismatched-file identification must match the instructor's seeded file.

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Seeded manifest mismatch: `beta.txt` (one byte flipped from `b` to `c` in the distributed copy). A3's append changes the digest again — both changes must be reported.
- HMAC vs digest: keyed = only key-holders can produce/verify; unkeyed digests can be recomputed by anyone (so an attacker who modifies content can re-digest it).
- GCM error class: `InvalidTag` (cryptography) — tamper detection by authentication, exactly the L17 lesson.
- KDF: 600k iterations ≈ 6× the 100k time on same hardware; the ≤ 300 ms budget lands around 300–600k on the course VM (measure, don't assert).
- Key-management observation expected: course keys are public in the repo → they provide workflow realism, zero confidentiality; production keys live in vaults (L19/L25).

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Digest cross-check + manifest verdict correct | 5 |
| HMAC comparison + keyed-vs-plain reasoning | 4 |
| KDF benchmark with methodology (iterations, hardware, times) | 4 |
| GCM tamper transcript + CBC contrast | 4 |
| Analysis answers + key-management observation | 3 |
