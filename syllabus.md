# Course Syllabus — Cyber Security
**BS Computer Science / BS Data Science · 7th Semester · 16 Weeks · 32 Lectures × 2 h = 64 Contact Hours**

> Document set: this syllabus (student-facing) · `docs-meta/architecture-and-requirements.md` (architecture) · `docs-meta/coverage-report.md` (validation) · detailed lecture plans in `instructor-materials/instructor-only/lecture-plans/` (instructor only).

---

## 1. Course Description

Cyber Security is a 64-hour, semester-long course that takes students from foundational security thinking to a full defensive capstone. The course treats security as an engineering discipline: every attack technique is paired with the control that prevents, detects, or responds to it. Eight modules progress from threat modeling and web application security, through malware analysis and network defense, into cryptography, machine-learning-driven security analytics, and cloud/privacy compliance, culminating in a team capstone that synthesizes threat modeling, hardening, detection engineering, and incident response into one defensible architecture.

The course serves **two audiences simultaneously**. Computer Science students engage with systems programming, protocol internals, and secure coding. Data Science students engage with anomaly detection, classification pipelines, adversarial ML, and security telemetry. Every lecture carries at least one example tuned to each track, and Module 6 is DS-intensive while Modules 3–5 are CS-intensive — so both cohorts lead in some modules and follow in others.

Teaching is 50 minutes of theory, 50 minutes of guided hands-on work in an isolated lab environment, and 20 minutes of consolidation, formative assessment, and preview. All lab work uses sandboxed, synthetic targets; the course teaches authorized, defensive security throughout.

## 2. Prerequisites (formal)

- Data Structures & Algorithms (completed)
- Operating Systems (completed) — processes, memory, file systems
- Computer Networks (completed) — TCP/IP, sockets, HTTP basics
- Databases (completed) — SQL fundamentals
- One of: Statistics & Probability (BS DS) **or** Discrete Mathematics (BS CS)

## 3. Expected Student Background (informal)

Students should be able to: write and debug programs in Python or Java; read TCP/IP packet dumps at a basic level; write SQL SELECT/INSERT statements; explain what an operating system process is; and use the Linux command line for navigation, permissions, and file inspection. No prior security knowledge is assumed. Students who have never used a hypervisor or container will be taught both in Week 1 lab orientation.

## 4. Course Learning Outcomes (CLOs) and Measurable Outcomes

Upon successful completion, students will be able to:

| CLO | Statement | Measurable outcome (evidence) | Bloom |
|---|---|---|---|
| CLO-1 | **Explain** core security concepts — CIA triad, threat models, attack surface — and the ethical/legal frame of security work. | Correctly classify ≥ 90% of concept items on Checkpoint A; produce a STRIDE threat model with ≥ 12 credible entries in Lab 01. | Understand |
| CLO-2 | **Analyze** web application vulnerabilities and produce remediation-focused, exploit-free reports. | Lab reports identify ≥ 8 of 10 seeded flaws with correct CWE IDs and a working fix for each. | Analyze |
| CLO-3 | **Dissect** malware behavior in isolated sandboxes and map observed behavior to MITRE ATT&CK techniques. | Malware lab report maps ≥ 6 behaviors to correct ATT&CK technique IDs with supporting evidence. | Analyze |
| CLO-4 | **Design** defensive network architectures (segmentation, firewalls, IDS/IPS) from packet-level evidence. | Design review passes rubric on segmentation correctness, rule minimality, and detection coverage. | Apply/Design |
| CLO-5 | **Apply** cryptographic primitives correctly and detect misuse (ECB, weak hashing, key-management failures). | Crypto lab detects ≥ 8 of 10 seeded misuse patterns and justifies replacements. | Apply/Evaluate |
| CLO-6 | **Apply** data science to security (anomaly detection, phishing classification) and **evaluate** attacks on ML (evasion, poisoning). | ML lab achieves ≥ 0.90 F1 on the synthetic phishing task AND documents ≥ 3 adversarial failure modes with mitigations. | Apply/Evaluate |
| CLO-7 | **Evaluate** cloud shared-responsibility security and privacy compliance (GDPR-style) for a given deployment. | Cloud lab produces a responsibility matrix and a DPIA skeleton rated ≥ 80% on rubric. | Evaluate |
| CLO-8 | **Synthesize** a complete defensive assessment — threat model → controls → detection → incident response plan — in the capstone. | Capstone report + defense passes rubric ≥ 70%; capstone is non-compensable (≥ 40% floor). | Create |

## 5. CLO-to-Lecture Mapping

Primary ●, supporting ○.

| Lecture | Module | CLOs | | Lecture | Module | CLOs |
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
| L15 | M4 | ●4 | | L31 | M8 | ●8 |
| L16 | M4 | ●4 ○2 | | L32 | M8 | ●8 ○1 |

Coverage check: CLO-1 primary in L01/L03/L04 + capstone ethics thread; CLO-2 primary L05–L08; CLO-3 primary L09–L12; CLO-4 primary L13–L16; CLO-5 primary L17–L20; CLO-6 primary L21–L24; CLO-7 primary L25–L28; CLO-8 primary L29–L32. Every CLO has ≥ 3 primary lectures and at least one formative assessment touchpoint.

## 6. Weekly Teaching Schedule

| Week | Lectures | Module | Focus | Assessment due |
|---|---|---|---|---|
| 1 | L01, L02 | M1 | Orientation & ethics; threat modeling I | — |
| 2 | L03, L04 | M1 | ATT&CK & attack surface; defense in depth | Checkpoint A; Lab 01 |
| 3 | L05, L06 | M2 | HTTP anatomy; injection attacks | Lab 02 |
| 4 | L07, L08 | M2 | XSS/CSRF/SSRF/IDOR; secure SDLC | Checkpoint B; Lab 03 |
| 5 | L09, L10 | M3 | Malware static analysis; dynamic & sandboxes | Lab 04 |
| 6 | L11, L12 | M3 | Ransomware anatomy; social engineering | Checkpoint C; Lab 05 |
| 7 | L13, L14 | M4 | Packet analysis; firewalls & segmentation | Lab 06 |
| 8 | L15, L16 | M4 | IDS/IPS & SIEM; wireless/VPN + **Midterm** | Lab 07; Midterm |
| 9 | L17, L18 | M5 | Symmetric crypto & modes; PKI & TLS | Lab 08 |
| 10 | L19, L20 | M5 | Hashing & passwords; crypto failures | Checkpoint D; Lab 09 |
| 11 | L21, L22 | M6 | Log anomaly detection; phishing classification | Lab 10 |
| 12 | L23, L24 | M6 | Adversarial ML; detection engineering metrics | Checkpoint E; **Case-study brief** |
| 13 | L25, L26 | M7 | Cloud shared responsibility & IAM; containers | Lab 11 |
| 14 | L27, L28 | M7 | Cloud detection; privacy engineering & DPIA | Checkpoint F; Lab 12 |
| 15 | L29, L30 | M8 | Capstone kickoff & threat-model workshop; build sprint I | Capstone milestone 1 |
| 16 | L31, L32 | M8 | Build sprint II + tabletop; showcase + **Final exam** | Capstone + Final |

## 7. Lecture-by-Lecture Learning Objectives

Each lecture states 3–5 objectives in "students will be able to…" form; the full set is embedded in the 32 lecture plans (`instructor-materials/instructor-only/lecture-plans/lecture-NN.md`). The condensed map:

- **L01** — Define CIA triad; distinguish security from privacy & safety; apply the responsible-disclosure and authorization framing.
- **L02** — Build STRIDE and attack-tree models for a small system; rank threats by risk.
- **L03** — Map an attack surface; navigate MITRE ATT&CK tactics/techniques; write a threat-informed defense hypothesis.
- **L04** — Apply defense-in-depth, least privilege, secure defaults; classify controls (preventive/detective/corrective).
- **L05** — Explain HTTP sessions/cookies/auth flows; identify where session logic fails.
- **L06** — Detect and remediate SQL/NoSQL/command injection; use parameterization and least-privilege DB design.
- **L07** — Distinguish XSS/CSRF/SSRF/IDOR; apply output encoding, CSRF tokens, egress control, object-level authz.
- **L08** — Integrate SAST/DAST/dependency scanning; configure CSP/HSTS; describe a secure SDLC.
- **L09** — Perform static triage (hashes, strings, imports, PE/ELF headers) in a VM; justify sandbox isolation.
- **L10** — Run controlled dynamic analysis; extract IOCs; document behavior safely.
- **L11** — Explain ransomware/worm lifecycles; design backup/restore resilience (3-2-1).
- **L12** — Analyze phishing/BEC anatomy; design an awareness program with measurable indicators.
- **L13** — Read TCP/IP and TLS flows in Wireshark; identify suspicious patterns in captures.
- **L14** — Design segmented, zero-trust-aligned networks; write least-privilege firewall rulesets.
- **L15** — Compare signature vs anomaly IDS; triage alerts in a SIEM pipeline.
- **L16** — Assess wireless & VPN security; consolidate M1–M4 in the midterm.
- **L17** — Choose block-cipher modes correctly; demonstrate ECB failure visually.
- **L18** — Walk the TLS 1.3 handshake; explain PKI trust chains and certificate pinning.
- **L19** — Select password hashing (argon2/bcrypt); explain salt/pepper and KDF work factors.
- **L20** — Dissect real crypto failures; specify key-management lifecycle controls.
- **L21** — Build an isolation-forest log-anomaly detector; tune precision/recall for SOC use.
- **L22** — Engineer a phishing/malware classification pipeline; manage feature drift.
- **L23** — Execute evasion/poisoning/extraction demonstrations in the lab; apply mitigations (adversarial training, sanitization).
- **L24** — Define detection-engineering metrics; write a detection rule with measured FPR/TPR.
- **L25** — Allocate responsibility across cloud models; design least-privilege IAM.
- **L26** — Harden containers/serverless; manage secrets properly.
- **L27** — Build cloud audit/monitoring; run misconfiguration scanning.
- **L28** — Apply data minimization and GDPR-style rights; draft a DPIA.
- **L29** — Scope the capstone scenario; produce a team threat model and control backlog.
- **L30** — Implement priority hardening/detection items; demonstrate desk-check progress.
- **L31** — Execute an incident-response tabletop; refine runbooks from findings.
- **L32** — Present and defend the capstone; complete the final examination.

## 8. Detailed Lecture Plans

All 32 detailed plans live in `instructor-materials/instructor-only/lecture-plans/` — one file per lecture (`lecture-01.md` … `lecture-32.md`). Every plan contains, in fixed order:

1. Lecture title & metadata (module, week, duration, CLOs)
2. Learning objectives
3. Key concepts
4. Detailed teaching sequence (minute-by-minute for the 2-hour session: theory block, lab block, consolidation block)
5. Worked examples (CS-track and DS-track where relevant)
6. Discussion questions
7. Student activity (in-class)
8. Problem-solving scenario
9. Summary
10. Formative assessment (exit-ticket items)
11. Required resources (lab environment, datasets, tools, references)

The teaching sequence follows the standing pattern: **00–10** recap + hook, **10–60** theory with worked examples, **60–110** guided lab/activity, **110–120** consolidation, exit ticket, and preview. Deviations (midterm L16, showcase L32) are noted in the plans.

## 9. Assessment Strategy

| Instrument | Timing | Weight | CLOs | Notes |
|---|---|---|---|---|
| Lab reports (best 6 of 8) | Weekly | 30% | 2,3,4,5,6 | Rubric: correctness 40%, evidence 30%, remediation quality 30% |
| Checkpoints A–F | Per module | 15% | all | 10-min in-class quizzes; lowest dropped |
| Midterm | Week 8 (L16) | 15% | 1–4 | Closed-book, scenario questions |
| Case-study brief | Week 12 (L24) | 10% | 1,3,7 | 1,500-word structured brief |
| Capstone report + showcase | Week 16 (L32) | 20% | 8 (+2,6,7) | Non-compensable: ≥ 40% floor |
| Final examination | Week 16 (L32) | 10% | all | Mixed format, A/B variants |

Grading notes: pass mark 50% overall with the capstone floor; formative exit tickets are ungraded but tracked for early-warning; academic-integrity policy applies to lab evidence (screenshots must be personally produced).

## 10. Prerequisites and Background

See §2 (formal) and §3 (informal). Bridge material: the first 40 minutes of L01 include a diagnostic self-check; students missing Linux or Python basics receive a self-study pack (Lab 00) due before L05. BS DS students without networking depth get an annotated TCP/IP primer in the same pack; BS CS students without ML depth get a scikit-learn primer before Module 6.

## 11. Recommended Readings and References

**Core texts (both tracks):**
- Stallings & Brown, *Computer Security: Principles and Practice*, 4th/5th ed. — primary text for M1, M4, M7.
- OWASP *OWASP Top 10* (current edition) and *ASVS* — M2 backbone.
- NIST SP 800-61r2 (Incident Handling), SP 800-53 (Controls), CSF 2.0 — governance threads (M1, M8).

**Module-specific:**
- M3: Sikorski & Honig, *Practical Malware Analysis* (selected chapters); MITRE ATT&CK documentation.
- M4: Bejtlich, *The Practice of Network Security Monitoring*; Wireshark official docs.
- M5: Boneh & Shoup, *A Graduate Course in Applied Cryptography* (free draft, selected chapters); Ferguson, Schneier & Kohno, *Cryptography Engineering*.
- M6: Chio & Freeman, *Machine Learning and Security*; Adversarial ML Threat Matrix (MITRE); NIST AI RMF 1.0.
- M7: NIST SP 800-145 (cloud), CIS Benchmarks; EU GDPR text (Articles 5, 15–22, 35).
- Case studies: vendor post-mortems and CISA advisories (cited per case; see `case-studies/`).

**Standards & law:** ISO/IEC 27001:2022 (overview level), GDPR, PCI-DSS (awareness level only).

Reference-recency rule (from the quality standards): prefer sources ≤ 5 years old; classic texts are exempt where foundational. Every lecture plan lists its own readings in "Required resources."

---

*End of syllabus. Validation of lecture counts, hours, progression, and CLO coverage: `docs-meta/coverage-report.md`.*
