# Master Course Architecture & Requirements
**Cyber Security — BS Computer Science / BS Data Science · 7th Semester**

- **32 lectures × 2 hours = 64 contact hours**
- **16 weeks × 2 sessions/week** (Weeks 1–15 = 30 lectures + midterm cadence; Week 16 = capstone showcase + final exam)
- **Eight coherent modules**, beginner → advanced
- Audience: CS **and** Data Science students (dual-track examples throughout)

---

## 1. Repository directory architecture (authoritative)

```text
/
├── docs-meta/                      # Planning & governance (meta, not student handouts)
│   ├── architecture-and-requirements.md   ← this file
│   ├── implementation-roadmap.md
│   └── content-inventory.md
├── lectures/                       # STUDENT-FACING lecture shells + content
│   └── module-01-fundamentals … module-08-capstone
│       ├── module-overview.md
│       └── lecture-NN.md           # one file per lecture, NN = 01..32
├── labs/                           # STUDENT-FACING lab worksheets + starter code
│   └── lab-NN-name/
│       ├── README.md               # student worksheet
│       └── starter/                # runnable starter files (safe, synthetic)
├── case-studies/                   # STUDENT-FACING real-world incidents
├── assessments/
│   ├── student/                    # student-facing: task statements, practice quizzes
│   └── instructor-only/            # answer keys, grading rubrics, exam versions
├── instructor-materials/
│   └── instructor-only/            # lecture delivery notes, timing plans, board work
├── website/                        # GitHub Pages source (public-facing course hub)
│   ├── index.md, syllabus.md, lectures/…, assets/
│   └── index-template.md
├── README.md, LICENSE, CODE_OF_CONDUCT.md   # governance (root)
└── .github/workflows/pages.yml     # Pages build/deploy CI
```

### Access-level separation (enforced by convention)

| Tier | Location | Who sees it |
|---|---|---|
| Student | `lectures/`, `labs/`, `case-studies/`, `assessments/student/`, `website/` | All enrolled students |
| Instructor | `assessments/instructor-only/`, `instructor-materials/instructor-only/` | Teaching staff only |

Rule: **nothing under `instructor-only/` may be linked from `website/`**, and no answer keys in student folders. (GitHub branch-protection/PATHS note in §11.)

---

## 2. Program-level Course Learning Outcomes (CLOs)

Upon successful completion, students can:

| CLO | Statement | Bloom level | Assessed by |
|---|---|---|---|
| CLO-1 | Explain core security concepts (CIA triad, threat models, attack surface) and the ethics/legal frame of offensive testing | Understand | Quiz 1, participation |
| CLO-2 | Analyze web application vulnerabilities and produce exploit-free, remediation-focused reports | Analyze | Lab reports, Quiz 2 |
| CLO-3 | Dissect malware behavior in isolated sandboxes and map it to MITRE ATT&CK techniques | Analyze | Malware lab, report |
| CLO-4 | Design defensive network architectures (segmentation, IDS/IPS, firewalls) from packet-level evidence | Apply/Design | Network lab, design review |
| CLO-5 | Apply cryptographic primitives correctly and detect misuse (ECB mode, weak hashing, bad key management) | Apply/Evaluate | Crypto lab, Quiz 3 |
| CLO-6 | Apply data science (ML) to security: anomaly detection, phishing classification; and evaluate ML model attacks (evasion, poisoning) | Apply/Evaluate | ML labs, project milestone |
| CLO-7 | Evaluate cloud/shared-responsibility security and privacy compliance (GDPR-style principles) for a given deployment | Evaluate | Cloud lab, case brief |
| CLO-8 | Synthesize a full defensive assessment (threat model → controls → incident response plan) in the capstone | Create | Capstone report + presentation |

**CLO → lecture mapping** (primary ●, supporting ○):

| Lecture | Module | CLO coverage | | Lecture | Module | CLO coverage |
|---|---|---|---|---|---|---|
| L01 | M1 | ●1 | | L17 | M5 | ●5 |
| L02 | M1 | ●1 ○4 | | L18 | M5 | ●5 ○7 |
| L03 | M1 | ●1 | | L19 | M5 | ●5 |
| L04 | M1 | ●1 ○8 | | L20 | M5 | ●5 ○6 |
| L05 | M2 | ●2 | | L21 | M6 | ●6 |
| L06 | M2 | ●2 ○8 | | L22 | M6 | ●6 |
| L07 | M2 | ●2 | | L23 | M6 | ●6 ○4 |
| L08 | M2 | ●2 | | L24 | M6 | ●6 ○8 |
| L09 | M3 | ●3 | | L25 | M7 | ●7 |
| L10 | M3 | ●3 | | L26 | M7 | ●7 |
| L11 | M3 | ●3 ○4 | | L27 | M7 | ●7 |
| L12 | M3 | ●3 | | L28 | M7 | ●7 |
| L13 | M4 | ●4 | | L29 | M8 | ●8 |
| L14 | M4 | ●4 | | L30 | M8 | ●8 |
| L15 | M4 | ●4 | | L31 | M8 | ●8 ○1 |
| L16 | M4 | ●4 ○2 | | L32 | M8 | ●8 |

---

## 3. Module boundaries and prerequisites

| # | Module | Lectures | Weeks | Prerequisite |
|---|---|---|---|---|
| M1 | Security Foundations & Threat Modeling | L01–L04 | W1–2 | none |
| M2 | Web Application Security | L05–L08 | W3–4 | M1 |
| M3 | Malware Analysis & Social Engineering | L09–L12 | W5–6 | M1 |
| M4 | Network Security & Monitoring | L13–L16 | W7–8 | M1 (M2/M3 helpful) |
| M5 | Cryptography & Applied Trust | L17–L20 | W9–10 | M1 |
| M6 | Data Science for Security & ML Security | L21–L24 | W11–12 | M1; M4 for anomaly detection |
| M7 | Cloud Security & Privacy/Compliance | L25–L28 | W13–14 | M4; M5 for key/cloud crypto |
| M8 | Capstone: Blue-Team Defense in Depth | L29–L32 | W15–16 | all modules |

Dependency DAG: `M1 → {M2, M3, M4, M5} → {M6, M7} → M8`. M2∥M3∥M4∥M5 are mutually independent, allowing parallel lab tracks.

---

## 4. The 32-lecture plan (all lecture numbers allocated)

Every lecture = 2 h: ~50 min theory, ~50 min guided lab/case work, ~20 min wrap-up + assessment checkpoint.

**M1 — Security Foundations (L01–L04, W1–2)**
- L01 Course orientation; CIA triad; security vs. usability; ethics & responsible disclosure
- L02 Threat modeling I (STRIDE, attack trees)
- L03 Threat modeling II + attack surface mapping; MITRE ATT&CK overview
- L04 Defense in depth, least privilege, secure defaults; **Checkpoint A (diagnostic quiz)**

**M2 — Web Application Security (L05–L08, W3–4)**
- L05 HTTP anatomy for attackers/defenders; cookies, sessions, auth models
- L06 Injection attacks: SQL/NoSQL/command injection — detection & parameterized defenses
- L07 XSS, CSRF, SSRF, IDOR — with secure-coding fixes
- L08 Secure SDLC: dependency hygiene, headers (CSP/HSTS), DAST/SAST basics; **Checkpoint B + lab challenge**

**M3 — Malware Analysis & Social Engineering (L09–L12, W5–6)**
- L09 Malware taxonomy; static analysis in isolated VM (hashes, strings, imports)
- L10 Dynamic analysis & sandboxing; indicators of compromise (IOCs)
- L11 Ransomware & worm case anatomy; backup/restore resilience
- L12 Social engineering, phishing, BEC; awareness program design; **Checkpoint C**

**M4 — Network Security & Monitoring (L13–L16, W7–8)**
- L13 TCP/IP refresher from a defensive lens; packet capture with Wireshark
- L14 Firewall design, segmentation, VLANs, zero-trust principles
- L15 IDS/IPS & SIEM: signature vs. anomaly detection; alert triage lab
- L16 Wireless & VPN security; **Midterm checkpoint (CLO-1..4 consolidated)**

**M5 — Cryptography & Applied Trust (L17–L20, W9–10)**
- L17 Symmetric crypto, block modes; why ECB is dangerous (visual lab)
- L18 Asymmetric crypto, PKI, TLS handshake walk-through; certificate pinning
- L19 Hashing, MACs, passwords (bcrypt/argon2), salt & pepper
- L20 Crypto failures in the wild (case-driven); key management; **Checkpoint D**

**M6 — Data Science for Security & Security of ML (L21–L24, W11–12)**
- L21 Security analytics with ML: log anomaly detection (isolation forest)
- L22 Phishing/malware classification pipelines; feature engineering & drift
- L23 Attacking ML: evasion, poisoning, model extraction (with defensive mitigations)
- L24 SOC-grade detection engineering: evaluation metrics (precision/recall trade-offs); **Checkpoint E**

**M7 — Cloud Security & Privacy (L25–L28, W13–14)**
- L25 Cloud shared-responsibility model; IAM least-privilege design
- L26 Container & serverless security; secrets management
- L27 Cloud logging/detection (audit trails, misconfig scanners)
- L28 Privacy engineering: data minimization, GDPR-style rights, DPIA; **Checkpoint F**

**M8 — Capstone (L29–L32, W15–16)**
- L29 Capstone kickoff: scenario briefing, team formation, threat-model workshop
- L30 Build sprint I: hardening & detection implementation; instructor desk-checks
- L31 Build sprint II + incident-response tabletop exercise
- L32 **Capstone showcase + Final examination**

**Quality gate:** 32/32 lecture slots allocated (see §12 verification).

---

## 5. Assessment plan

| Instrument | When | Weight | CLOs |
|---|---|---|---|
| Lab reports (best 6 of 8) | continuous | 30% | 2,3,4,5,6 |
| Checkpoints A–F (in-class quizzes) | per module | 15% | all |
| Midterm (W8, L16) | midterm | 15% | 1–4 |
| Case-study brief | W12 | 10% | 1,3,7 |
| Capstone report + showcase | W16 | 20% | 8 (+2,6,7) |
| Final examination | W16, L32 | 10% | all |

Pass mark: 50% overall with ≥40% on the capstone (capstone is non-compensable).

---

## 6. Quality standards — lectures

1. **Shell contract:** every `lecture-NN.md` must contain: learning outcomes (mapped to CLOs), 2-hour timing plan, theory outline, guided activity, references, and a homework/reading block.
2. **Dual-track relevance:** each lecture carries at least one CS-flavored and one DS-flavored example.
3. **Recency:** references ≤ 5 years old where possible; CWE/OWASP/ATT&CK IDs cited verbatim.
4. **Ethics gate:** offensive content must include the responsible-use statement (template in labs README).
5. No lecture may exceed the 2-hour envelope; overflow material moves to optional "deep dive" boxes.

## 7. Quality standards — labs

1. Every lab runs in a **sandboxed** environment (VM/container); no live third-party systems.
2. Starter code must run with documented commands on the course VM image; CI should smoke-test labs where feasible.
3. Each lab worksheet: objective, preflight checklist, task steps, expected evidence (screenshots/files), submission checklist.
4. Safe-by-construction: any exploit content uses *local vulnerable targets* (e.g., deliberately weak demo apps) and never weaponized tooling.
5. Every offensive lab has a corresponding detection/defense deliverable.

## 8. Quality standards — case studies

1. Facts sourced from public, citable reports (vendor post-mortems, CERT, court documents).
2. Structure: timeline, root cause, impact, controls that would have prevented/detected it, discussion questions.
3. Must map to ≥ 1 CLO and ≥ 1 module; no victim-blaming language; redact personal data.

## 9. Quality standards — assessments & website

**Assessments:** each item tagged to a CLO; answer keys live **only** in `assessments/instructor-only/`; exams have A/B variants; rubrics state criteria + performance levels.

**Website (GitHub Pages requirements — quality gate #4):**
- Source: `website/` directory published via GitHub Actions (`.github/workflows/pages.yml`, `actions/deploy-pages`).
- Pure static (HTML/Markdown + CSS, no server runtime) so it works on Pages.
- `index.md`/`index.html` at site root; relative links only (Pages subpath compatibility).
- No instructor-only content linked from the site.
- Course syllabus, lecture index (all 32), lab index, case-study index, contact/licensing.

## 10. Content preservation rules (standing)

1. Before adding files, re-run the inventory in `content-inventory.md`; if upstream content now exists, extend — never overwrite.
2. Any structural move of existing content requires a migration note in `docs-meta/`.
3. Deletion requires justification recorded in this document's change log.

## 11. Open decisions for the owner

- Whether instructor-only tiers should live in a **private repo** (current repo is public — answer keys in a public repo would leak; **this is an unresolved decision**, flagged in the report).
- Enrollment size & lab environment capacity (affects sandbox choice: local VM vs. cloud lab).
- Grading schema approval by the department (weights in §5 are a proposal).
- Language of instruction (materials drafted in English).

## 12. Quality-gate verification (this document)

- ✅ All 32 lecture numbers planned (§4 lists L01–L32; see roadmap §Verification).
- ✅ Eight modules included with explicit boundaries (§3).
- ✅ Student vs. instructor materials in separate locations (§1 table).
- ✅ GitHub Pages requirements considered (§9).
- ✅ No existing content removed — repo was empty; see `content-inventory.md` §4.

## Change log

| Date | Change |
|---|---|
| 2026-09-19 | Initial architecture; empty-repo baseline documented |
| 2026-09-19 | Syllabus authored (`syllabus.md`); 32 detailed lecture plans written (`instructor-materials/instructor-only/lecture-plans/lecture-01..32.md`); module boundaries and lecture allocations unchanged — §4 lecture titles refined into full teaching titles; coverage evidence in `docs-meta/coverage-report.md` |
| 2026-09-19 | Teaching materials authored: 32 student-facing lecture notes (`lectures/module-0X-*/lecture-NN.md`, 10 required components each incl. diagrams with text equivalents, misconceptions, exit tickets, references) and 32 instructor-only teaching guides (`instructor-materials/instructor-only/teaching-guides/`, 10 required components each incl. timing plans, speaker notes, expected difficulties, answer keys, accessibility) + course-level `instructor-manual.md` + checkpoint keys. Placement note: mission text suggested `teaching/` and `docs/lectures/` trees; per the approved architecture (§1) student notes live in `lectures/` and instructor materials in `instructor-materials/instructor-only/` — duplicate trees intentionally not created to avoid fragmentation |
| 2026-09-19 | Lab curriculum authored: 31 lab directories under `labs/` covering a 14-lab program (8 core + 6 enrichment) mapped to the eight required core themes; 16-component worksheets for graded labs, keys/rubrics embedded instructor-side (`assessments/instructor-only/lab-keys.md` with tested-vs-untested validation ledger); validation report `docs-meta/lab-validation-report.md` (command-level testing performed: sha256/hmac/CBC verified; `openssl enc` AEAD limitation recorded as a teaching fact; course-infrastructure items flagged untested with acceptance specs) |
| 2026-09-19 | Case studies | 100-case progressive collection authored (L1 20 / L2 25 / L3 30 / L4 25; IDs CS-001..CS-100): student collections in `case-studies/collection/`, model solutions in `instructor-materials/instructor-only/case-solutions/`, index + rubrics + validation script (`case-studies/tools/validate_cases.py`), CLO coverage report (`docs-meta/case-coverage-report.md`). All cases labeled simulated; no real incidents fabricated; data-driven DS cases included at every level. |
| 2026-09-19 | Assessments | Full assessment package: 120-item question bank (CLO/Bloom/difficulty-tagged; 80 module MCQ+SA + 16 exam + 24 specimen items) with duplicate-avoidance rule; 15 weekly quiz papers + 2 specimen exam papers (student tier, questions only; checkpoints A–F aligned to the pre-existing keys); live midterm/final papers with marking schemes and A/B variants; capstone rubric + moderation guide; practical-lab grading guide; SA-1…6 briefs; case-study activity; oral-defense rubric; validator `assessments/tools/validate_assessments.py` (exit 0); coverage report `docs-meta/assessment-coverage-report.md`. Weekly-unit map: Q2/4/6/10/12/14 = Checkpoints A–F; Week 8 = midterm; Week 16 = final. |
| 2026-09-19 | Slides | Presentation resources authored (instructor-only, Marp Markdown): 32 lecture decks (objectives, diagrams with text descriptions, CS+DS examples, lab-demo slides with safety/MVO, case-session slides with INDEX-verified case IDs, embedded speaker notes with timing), midterm + final review decks, six-step case-session template, accessibility-first theme, format baseline README. Validator `assessments/tools/validate_slides.py` exit 0; rendering via Marp CLI flagged **untested** (CLI absent in workspace) — see `docs-meta/slides-validation-report.md`. |
| 2026-09-19 | Calendar | One-click semester calendar: `calendar/tools/generate_calendar.py` generates student (MD + printable HTML), instructor-only planning view, and LMS JSON from configurable `--start` date (Mon/Thu × 16). Generated from the repository's actual content — live lecture titles verified at build time (generation aborts on drift), labs per the authoritative crosswalk with staggered graded-lab due weeks, 16 weekly assessment units, per-lecture case sessions. Built-in validation: 16 weeks / 32 lectures / no gaps, Mon–Thu cadence, graded-lab + checkpoint alignment, all generated links resolve. Documented in `calendar/README.md`. |
