# ⚠️ INSTRUCTOR-ONLY — Lab Keys, Rubric Details & Validation Status

Per-lab answer keys and rubric details are embedded in each lab's README below the `---` divider (marked "Instructor Answer Key"). This file is the index, the validation ledger, and the section-reset procedures.

## 1. Lab key & rubric index

| Lab | Key location in README | Keyed artifacts (instructor-provided) |
|---|---|---|
| 00 hardening | §Key after divider | `baseline-check.sh`, `weak-configs/` in VM image |
| 01 threat modeling | §Key | vending-box spec, attack-tree cost table |
| 02 attack surface | §Key | six station cards |
| 03 controls layering | §Key | control-card deck, `starter/configs/` + checks |
| 04 web foundations | §Key | `webdemo` container (seeded weaknesses) |
| 05 injection | §Key | `vuln-app:weak` + `starter/patches/` |
| 06 web stations | §Key | `webdemo` four seeded stations |
| 07 headers/SDLC | §Key | `webdemo` repo `headers-lab` branch, seeded CI findings |
| 08 static triage | §Key | synthetic `sample-2.bin`, `sample-3.bin` + hash sheet |
| 09 dynamic analysis | §Key | sensor VM image, fake-net config |
| 10 ransomware resilience | §Key | scenario pack (paper) |
| 11 awareness design | §Key | three inert sample mails, BEC storyboard |
| 12 packet analysis | §Key | `capture-A-normal.pcapng`, `capture-B-seeded.pcapng` |
| 13 segmentation | §Key | scenario pack, `ruleset-with-flaw.txt` |
| 14 siem triage | §Key | `alerts-queue.csv`, enrichment sheet, answer sheet |
| 15 crypto | §Key | `manifest.sha256` (seeded mismatch: beta.txt), keys handout |
| 16 PKI/TLS | §Key | course-CA kit, `tlsdemo`, prepared TLS 1.3 capture |
| 17 password storage | §Key | `store-v1.db`, `repo-with-secrets/` (3 secrets, commit `a17f3c9`) |
| 18 crypto failures | §Key | case citation set (links verified per term), vendor pages A–C |
| 19 log anomaly | §Key | `auth-day.csv` + instructor `labels.csv` (seeded chains) |
| 20 phishing classifier | §Key | `phish-corpus-v3.csv`, `broken.ipynb` (3 planted leaks) |
| 21 adversarial ML | §Key | `phish-model-v3.joblib`, station notebooks, query-budget wrapper |
| 22 detection engineering | §Key | `synthetic-day-v2.csv` (chain row ranges), dashboard notebook |
| 23 cloud IAM | §Key | sandbox org seed (6 identities, 10 policies, 3 planted findings) |
| 24 containers | §Key | `ml-infer:weak` + build kit, K8s sandbox, `layer-lab.sh` |
| 25 cloud audit | §Key | `audit-corpus-v2.csv` (chain row ranges) |
| 26 DPIA | §Key | scenario pack, `qa-table.csv` (k=1 triple seeded) |
| 27 forensics | §Key | `evidence-pack-v2.zip` + pack hash sheet |
| 28 IR simulation | §Key | inject deck (sealed), decision-log template, status forms |
| 29 vuln assessment | §Key | `vuln-app:weak`/`:fixed`, patch set, report template |
| 30 capstone | §Key | per-team environment, inject deck, rubric bands |

## 2. Validation ledger (tested vs. untested — recorded honestly)

**Tested on the instructor workstation (2026-09-19; Python 3.14.7, OpenSSL 3.5.7, git 2.55):**
- Lab 15 digest/HMAC command shapes: `python hashlib` and `openssl dgst -sha256` produce identical digests (verified); `openssl dgst -hmac` verified.
- Lab 15 negative result: `openssl enc -aes-256-gcm` **fails by design** ("enc: AEAD ciphers not supported") — worksheets route AEAD through the Python `cryptography` library and teach this as a tooling fact.
- Lab 15 CBC roundtrip via `openssl enc -aes-256-cbc -pbkdf2` verified (encrypt/decrypt roundtrip).
- `crypto_lab.py` CLI paths for `sha256`/`hmac` executed and verified.
- Command *shapes* for Lab 00 (`ss -tlnp`-class checks), Lab 29/23 (docker/aws CLI grammar) verified as syntactically valid and conventionally correct; full execution requires the course images/accounts.

**Untested (documented as such; require course infrastructure):**
- All container images (`webdemo`, `vuln-app`, `tlsdemo`, `ml-infer`), datasets (`auth-day.csv`, `phish-corpus-v3.csv`, `synthetic-day-v2.csv`, `audit-corpus-v2.csv`, evidence pack, samples), the cloud sandbox seed, and the K8s sandbox — these are **course infrastructure to be built per the roadmap**; the worksheets specify their required content and behavior precisely (expected observations sections) so builders can verify against the spec.
- Lab 15's `cryptography`-package paths (GCM/InvalidTag) — API-stable, untested on this workstation (package not installed here); flagged in the starter script itself.
- Lab 19/20/22 notebooks — pandas/sklearn APIs are stable; exact seeded metric values are stated as expectations to verify, not facts.

**Rule for instructors:** anything marked tested was executed; anything marked untested must be walked through before first delivery, and any gap between spec and build is reportable as `content-bug`.

## 3. Section-reset procedures (per lab)

- 04/05/06/07: `docker stop` targets; reset seeded DB volume (05); station reset via `/admin/reset` (06).
- 08/09: restore `lab08-clean`/`lab09-clean` snapshots; wipe `~/samples`.
- 12/27: re-issue capture/evidence packs from the LMS master; verify pack hash.
- 23: instructor resets the sandbox org seed per section (policy rewrites are per-student copies).
- 28: collect sealed inject decks; re-count 13 cards per deck.
- 29: `docker stop vuln-app`; `docker volume rm vulnapp-db` if schema-touched.
- 30: team environments destroyed after grades post (not archived).

## 4. Integrity notes

- Student evidence must be personally produced; the A/B checkpoint variants and per-section seeds (sandbox org, sample hashes, manifest mismatch file) limit copying.
- Per-section variation levers: different manifest mismatch file (15), different seeded chains (19/22), different injected sandbox findings (23), different pack hash (27).
