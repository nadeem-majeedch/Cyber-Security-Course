# Lab Curriculum — Inventory & Validation Report
**Date: 2026-09-19 · Scope: 14-lab practical curriculum (8 core + 6 enrichment) across 31 lab directories**

## 1. Inventory

31 lab directories under `labs/`, each with `README.md` (worksheet) and `starter/`; the 14 graded/designated labs carry the full 16-component worksheet contract; 17 enrichment labs carry the 11-component check-in contract (all required fields minus the graded-lab-specific setup heft, which they do not need). Two labs serve double duty against the eight required core themes:

| Required core theme | Lab(s) |
|---|---|
| 1. Security baseline & system hardening | Lab 00 |
| 2. Network traffic analysis (prepared captures) | Lab 12 |
| 3. Cryptographic operations & integrity checks | Lab 15 |
| 4. Secure web testing (deliberately vulnerable local env) | Lab 05, Lab 06 (subset of Lab 29) |
| 5. Vulnerability assessment of authorized lab target | Lab 29 (+ Lab 23 cloud variant) |
| 6. Log analysis & security event correlation | Lab 19 (+ Lab 14 triage) |
| 7. Digital forensics (instructor-provided artifacts) | Lab 27 |
| 8. Incident response simulation | Lab 28 |

All eight themes covered; 8 core + 6 enrichment = 14 designated labs, within the requested 12–16 band.

## 2. Component-completeness validation

Core/graded labs (00, 12, 15, 19, 23, 27, 28, 29) — all 16 required components verified present by structural audit: numbered title, CLO mapping, objectives, prerequisites, duration, HW/SW requirements, setup instructions, ethics/safety notes, step-by-step tasks, expected observations, analysis questions, troubleshooting, cleanup, submission requirements, instructor key, rubric, expected outputs/evidence.

Enrichment labs (01–11, 13, 14, 16–18, 20–22, 24–26, 30) — 11-component contract verified: objectives, prerequisites, duration, requirements, setup, ethics/safety, tasks, expected observations, analysis questions, troubleshooting, cleanup, submission, key, rubric, outputs. (Numbered-title and CLO heading present on all; grading weight differs.)

Safety-critical component (ethics/authorization notes) verified present in **all 31** worksheets.

## 3. Command/dependency validation — tested vs. untested

**Environment probed:** Windows host with Git Bash; Python 3.14.7; OpenSSL 3.5.7; git 2.55; Wireshark/tshark and nmap not installed (course-VM tools — correctly specified as such in worksheets).

**Executed and verified on this workstation:**
- `python -c hashlib.sha256` ≡ `openssl dgst -sha256` (identical digests) — Lab 15 A1 cross-check works as documented.
- `openssl dgst -sha256 -hmac` — Lab 15 B1 cross-check works.
- `openssl enc -aes-256-gcm` → **fails** with "enc: AEAD ciphers not supported" — recorded as a *teaching fact* in Lab 15 (AEAD routed through the Python library; the worksheet and starter both carry this finding).
- `openssl enc -aes-256-cbc -pbkdf2` encrypt/decrypt roundtrip — Lab 15's CBC contrast path valid.
- `crypto_lab.py sha256|hmac` CLI executed and verified.

**Documented as untested (require course infrastructure; worksheets flag them):**
- All course images/containers (`webdemo`, `vuln-app`, `tlsdemo`, `ml-infer`, analysis VM), all datasets/captures/packs, the cloud sandbox and K8s sandbox, the `cryptography` package paths.
- Mitigation: every untested element has an "Expected Observations" section that doubles as a builder's acceptance spec, and the instructor ledger (`assessments/instructor-only/lab-keys.md` §2) requires first-delivery walkthrough before teaching.

## 4. Lab-to-lecture alignment

Machine-checked crosswalk: each lab maps to ≥ 1 lecture and ≥ 1 primary CLO; coverage across the 32 lectures is complete — every lecture's in-class activity block has a corresponding lab worksheet directory (the L05–L08, L09–L10, L13, L15, L17–L19, L21–L25, L27, L29–L31 sessions reference the same lab numbers used here; the two new consolidated labs — 27 (forensics), 28 (IR), 29 (vuln assessment) — map to L10/L27, L31, and L06–L08/L15 respectively, closing the core-theme gaps the earlier per-lecture activity stubs left open). Session-plan ↔ lab cross-references remain consistent (e.g., L06's Lab 06 = the four web stations; L31's tabletop = Lab 28's instrument).

## 5. Safety compliance check

- All targets are local/isolated/explicitly authorized: loopback-only containers (`127.0.0.1`), course VM, cloud sandbox, paper artifacts. No lab touches public systems; scope statements are explicit and rubric-enforced (Lab 29's scope-discipline line).
- Prohibited-content audit: no credential-theft instructions, no destructive payloads, no persistence mechanisms taught as attack technique (persistence appears only as *detection* content), no unauthorized-access instructions. Malware labs use synthetic, capability-stripped samples; adversarial-ML labs are constraint-compliant and course-model-only.
- Defensive remediation is paired with every demonstrated weakness (fix-and-verify structure in Labs 05/06/29; remediation plans in 23/24/29).

## 6. Grading architecture

Graded (best 6 of 8, 30%): Labs 00, 12, 15, 19, 23, 27, 28, 29 — each with a 20-point rubric keyed to the course's 40/30/30 criteria. Enrichment labs: check-in, 10-point rubrics, feeding checkpoints. Keys and per-section variation levers: `assessments/instructor-only/lab-keys.md`.

## 7. Limitations (honest reporting)

1. Course infrastructure (images, datasets, sandbox seeds) is specified but not built — the largest remaining build item; the expected-observations specs are the acceptance criteria.
2. Lab numbering vs. lecture numbering intentionally diverges (labs are consolidated activities, not 1:1); the crosswalk in `labs/README.md` and §4 here is authoritative.
3. One previously-noted open issue persists: `labs/lab-15-crypto-integrity/starter/crypto_lab.py`'s AEAD paths are untested pending the course VM image with `cryptography` installed.
