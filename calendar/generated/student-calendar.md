# Semester Calendar — Cyber Security (student view)
**BS CS / BS Data Science · 7th semester · 16 weeks · 32 lectures × 2 h (64 contact hours)**
**Semester start (configurable): 2026-09-07** — sessions are Mondays & Thursdays; regenerate with `python calendar/tools/generate_calendar.py --start YYYY-MM-DD`.

Legend: 🔬 lab · 📝 assessment · 💬 case discussion · 🔗 links go to the live course files.

| Week | Session 1 (Mon) | Session 2 (Thu) |
|---|---|---|
| **W1** | **2026-09-07** · L01 | **2026-09-10** · L02 |
| **W2** | **2026-09-14** · L03 | **2026-09-17** · L04 |
| **W3** | **2026-09-21** · L05 | **2026-09-24** · L06 |
| **W4** | **2026-09-28** · L07 | **2026-10-01** · L08 |
| **W5** | **2026-10-05** · L09 | **2026-10-08** · L10 |
| **W6** | **2026-10-12** · L11 | **2026-10-15** · L12 |
| **W7** | **2026-10-19** · L13 | **2026-10-22** · L14 |
| **W8** | **2026-10-26** · L15 | **2026-10-29** · L16 |
| **W9** | **2026-11-02** · L17 | **2026-11-05** · L18 |
| **W10** | **2026-11-09** · L19 | **2026-11-12** · L20 |
| **W11** | **2026-11-16** · L21 | **2026-11-19** · L22 |
| **W12** | **2026-11-23** · L23 | **2026-11-26** · L24 |
| **W13** | **2026-11-30** · L25 | **2026-12-03** · L26 |
| **W14** | **2026-12-07** · L27 | **2026-12-10** · L28 |
| **W15** | **2026-12-14** · L29 | **2026-12-17** · L30 |
| **W16** | **2026-12-21** · L31 | **2026-12-24** · L32 |

## Week 1 · 2026-09-07 – 2026-09-10
**Due / happen this week:**
- 📝 **Quiz Q1 (specimen)** — [details](../../assessments/student/quizzes/quiz-01.md)
### Lecture 01 — Security Foundations: CIA, Ethics, and the Defender's Mindset
*Mon 07 Sep 2026 · M1 Security Foundations & Threat Modeling · CLO-1*
- Define CIA and classify real failures
- Apply responsible-disclosure rules
- 🔬 [Lab 00](../../labs/lab-00-hardening-baseline/README.md) — Security Baseline & System Hardening **(graded)** · *Lab 00 due W2*
- 💬 Case discussion: [CS-001](../../case-studies/collection/level-1-beginner.md)
- 🔗 [Lecture notes](../../lectures/module-01-fundamentals/lecture-01.md)

### Lecture 02 — Threat Modeling I: STRIDE and Attack Trees
*Thu 10 Sep 2026 · M1 Security Foundations & Threat Modeling · CLO-1*
- Build a STRIDE model (≥ 12 entries)
- Decompose threats with attack trees
- 🔬 [Lab 01](../../labs/lab-01-threat-modeling/README.md) — Threat Modeling: STRIDE & Attack Trees
- 💬 Case discussion: [CS-005](../../case-studies/collection/level-1-beginner.md)
- 🔗 [Lecture notes](../../lectures/module-01-fundamentals/lecture-02.md)

## Week 2 · 2026-09-14 – 2026-09-17
**Due / happen this week:**
- 📝 **Checkpoint A (graded, /10)** — [details](../../assessments/student/quizzes/quiz-02.md)
- 📝 **Lab 00 report due**
### Lecture 03 — Threat Modeling II: Attack Surface and MITRE ATT&CK
*Mon 14 Sep 2026 · M1 Security Foundations & Threat Modeling · CLO-1*
- Enumerate and shrink an attack surface
- Map behaviors to ATT&CK techniques
- 🔬 [Lab 02](../../labs/lab-02-attack-surface/README.md) — Attack Surface & ATT&CK Mapping
- 💬 Case discussion: [CS-020](../../case-studies/collection/level-1-beginner.md)
- 🔗 [Lecture notes](../../lectures/module-01-fundamentals/lecture-03.md)

### Lecture 04 — Defense in Depth, Least Privilege, and Checkpoint A
*Thu 17 Sep 2026 · M1 Security Foundations & Threat Modeling · CLO-1*
- Layer preventive/detective/corrective controls
- Apply least privilege and secure defaults
- 🔬 [Lab 03](../../labs/lab-03-controls-layering/README.md) — Defense-in-Depth Control Plan
- 💬 Case discussion: [CS-006](../../case-studies/collection/level-1-beginner.md)
- 🔗 [Lecture notes](../../lectures/module-01-fundamentals/lecture-04.md)

## Week 3 · 2026-09-21 – 2026-09-24
**Due / happen this week:**
- 📝 **Quiz Q3 (specimen)** — [details](../../assessments/student/quizzes/quiz-03.md)
### Lecture 05 — Web Foundations: HTTP, Sessions, and Authentication
*Mon 21 Sep 2026 · M2 Web Application Security · CLO-2*
- Read HTTP requests/responses end to end
- Explain session cookies and their attributes
- 🔬 [Lab 04](../../labs/lab-04-web-foundations/README.md) — Web Auth Flow Review
- 💬 Case discussion: [CS-034](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-02-web/lecture-05.md)

### Lecture 06 — Injection Attacks: SQL, NoSQL, and Command Injection
*Thu 24 Sep 2026 · M2 Web Application Security · CLO-2*
- Demonstrate and remediate injection
- Apply parameterization and least-privilege DB
- 🔬 [Lab 05](../../labs/lab-05-injection/README.md) — Injection: Confirm, Fix, Verify
- 💬 Case discussion: [CS-033](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-02-web/lecture-06.md)

## Week 4 · 2026-09-28 – 2026-10-01
**Due / happen this week:**
- 📝 **Checkpoint B (graded, /10)** — [details](../../assessments/student/quizzes/quiz-04.md)
### Lecture 07 — XSS, CSRF, SSRF, and IDOR
*Mon 28 Sep 2026 · M2 Web Application Security · CLO-2*
- Distinguish the four flaw classes by mechanism
- Apply encoding, tokens, egress, object authz
- 🔬 [Lab 06](../../labs/lab-06-xss-csrf-ssrf-idor/README.md) — Web Flaw Stations
- 💬 Case discussion: [CS-050](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-02-web/lecture-07.md)

### Lecture 08 — Secure SDLC, Dependency Hygiene, Security Headers + Checkpoint B
*Thu 01 Oct 2026 · M2 Web Application Security · CLO-2*
- Place SAST/DAST/SCA in the pipeline
- Configure CSP and HSTS with their limits
- 🔬 [Lab 07](../../labs/lab-07-headers-sdlc/README.md) — Security Headers & Dependency Hygiene
- 💬 Case discussion: [CS-049](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-02-web/lecture-08.md)

## Week 5 · 2026-10-05 – 2026-10-08
**Due / happen this week:**
- 📝 **Quiz Q5 (specimen)** — [details](../../assessments/student/quizzes/quiz-05.md)
### Lecture 09 — Malware Analysis I: Taxonomy and Static Triage
*Mon 05 Oct 2026 · M3 Malware Analysis & Social Engineering · CLO-3*
- Triage samples statically (hashes→imports)
- Justify sandbox isolation controls
- 🔬 [Lab 08](../../labs/lab-08-static-triage/README.md) — Malware Static Triage
- 💬 Case discussion: [CS-042](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-03-malware/lecture-09.md)

### Lecture 10 — Malware Analysis II: Dynamic Analysis, Sandboxes, and IOCs
*Thu 08 Oct 2026 · M3 Malware Analysis & Social Engineering · CLO-3*
- Detonate safely with fake-net isolation
- Extract IOCs and map to ATT&CK
- 🔬 [Lab 09](../../labs/lab-09-dynamic-analysis/README.md) — Dynamic Analysis & IOCs
- 🔬 [Lab 27](../../labs/lab-27-forensics/README.md) — Digital Forensics (instructor artifacts) **(graded)** · *Lab 27 due W9*
- 💬 Case discussion: [CS-016](../../case-studies/collection/level-1-beginner.md)
- 🔗 [Lecture notes](../../lectures/module-03-malware/lecture-10.md)

## Week 6 · 2026-10-12 – 2026-10-15
**Due / happen this week:**
- 📝 **Checkpoint C (graded, /10)** — [details](../../assessments/student/quizzes/quiz-06.md)
### Lecture 11 — Ransomware and Worms: Anatomy and Resilience
*Mon 12 Oct 2026 · M3 Malware Analysis & Social Engineering · CLO-3*
- Walk the ransomware lifecycle
- Design 3-2-1 backup resilience
- 🔬 [Lab 10](../../labs/lab-10-ransomware-resilience/README.md) — Ransomware Resilience Scenario
- 💬 Case discussion: [CS-032](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-03-malware/lecture-11.md)

### Lecture 12 — Social Engineering, Phishing & Awareness Programs + Checkpoint C
*Thu 15 Oct 2026 · M3 Malware Analysis & Social Engineering · CLO-3*
- Dissect phishing/BEC anatomy
- Design awareness programs with report-rate metrics
- 🔬 [Lab 11](../../labs/lab-11-awareness-design/README.md) — Awareness Campaign Design
- 💬 Case discussion: [CS-023](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-03-malware/lecture-12.md)

## Week 7 · 2026-10-19 – 2026-10-22
**Due / happen this week:**
- 📝 **Quiz Q7 (specimen)** — [details](../../assessments/student/quizzes/quiz-07.md)
### Lecture 13 — Network Defense I: Packet Analysis with Wireshark
*Mon 19 Oct 2026 · M4 Network Security & Monitoring · CLO-4*
- Read TCP conversations and TLS metadata
- Spot scan/beacon/exfil patterns
- 🔬 [Lab 12](../../labs/lab-12-packet-analysis/README.md) — Network Traffic Analysis (prepared captures) **(graded)** · *Lab 12 due W8*
- 💬 Case discussion: [CS-056](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-04-network/lecture-13.md)

### Lecture 14 — Network Defense II: Firewalls, Segmentation, Zero Trust
*Thu 22 Oct 2026 · M4 Network Security & Monitoring · CLO-4*
- Design default-deny zones
- Write minimal, ordered rulesets
- 🔬 [Lab 13](../../labs/lab-13-segmentation/README.md) — Segmentation & Ruleset Design
- 💬 Case discussion: [CS-025](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-04-network/lecture-14.md)

## Week 8 · 2026-10-26 – 2026-10-29
**Due / happen this week:**
- 📝 **Midterm examination (15%)**
- 📝 **Quiz Q8 pre-midterm (specimen)** — [details](../../assessments/student/quizzes/quiz-08.md)
- 📝 **Lab 12 report due**
### Lecture 15 — IDS/IPS and SIEM: Detection and Alert Triage
*Mon 26 Oct 2026 · M4 Network Security & Monitoring · CLO-4*
- Contrast signature vs anomaly IDS
- Triage a SIEM queue with metrics
- 🔬 [Lab 14](../../labs/lab-14-siem-triage/README.md) — Alert Triage & Correlation
- 🔬 [Lab 29](../../labs/lab-29-vuln-assessment/README.md) — Authorized-Target Vulnerability Assessment **(graded)** · *Lab 29 due W11*
- 💬 Case discussion: [CS-039](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-04-network/lecture-15.md)

### Lecture 16 — Wireless, VPN & Midterm Consolidation
*Thu 29 Oct 2026 · M4 Network Security & Monitoring · CLO-4*
- Assess WPA3 and VPN posture honestly
- Consolidate Modules 1–4 in the midterm
- 🔗 [Lecture notes](../../lectures/module-04-network/lecture-16.md)

## Week 9 · 2026-11-02 – 2026-11-05
**Due / happen this week:**
- 📝 **Quiz Q9 (specimen)** — [details](../../assessments/student/quizzes/quiz-09.md)
- 📝 **Lab 27 report due**
### Lecture 17 — Symmetric Cryptography and Block Cipher Modes
*Mon 02 Nov 2026 · M5 Cryptography & Applied Trust · CLO-5*
- Choose modes by property
- Demonstrate ECB failure; justify AEAD
- 🔬 [Lab 15](../../labs/lab-15-crypto-integrity/README.md) — Cryptographic Operations & Integrity Checks **(graded)** · *Lab 15 due W10*
- 💬 Case discussion: [CS-047](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-05-crypto/lecture-17.md)

### Lecture 18 — Asymmetric Cryptography, PKI, and TLS
*Thu 05 Nov 2026 · M5 Cryptography & Applied Trust · CLO-5*
- Walk the TLS 1.3 handshake
- Explain certificates and trust chains
- 🔬 [Lab 16](../../labs/lab-16-pki-tls/README.md) — Certificates, PKI & TLS Inspection
- 💬 Case discussion: [CS-046](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-05-crypto/lecture-18.md)

## Week 10 · 2026-11-09 – 2026-11-12
**Due / happen this week:**
- 📝 **Checkpoint D (graded, /10)** — [details](../../assessments/student/quizzes/quiz-10.md)
- 📝 **Lab 15 report due**
### Lecture 19 — Hashing, Password Storage, and Key Management
*Mon 09 Nov 2026 · M5 Cryptography & Applied Trust · CLO-5*
- Select Argon2id/bcrypt with tuned work factors
- Explain salt and cracking economics
- 🔬 [Lab 17](../../labs/lab-17-password-storage/README.md) — Password Storage & Secrets Hygiene
- 💬 Case discussion: [CS-021](../../case-studies/collection/level-2-intermediate.md)
- 🔗 [Lecture notes](../../lectures/module-05-crypto/lecture-19.md)

### Lecture 20 — Cryptographic Failures in the Wild + Checkpoint D
*Thu 12 Nov 2026 · M5 Cryptography & Applied Trust · CLO-5*
- Autopsy misuse patterns (ECB, IV reuse, key co-location)
- Specify a key-management lifecycle
- 🔬 [Lab 18](../../labs/lab-18-crypto-failures/README.md) — Crypto Failure Review
- 💬 Case discussion: [CS-011](../../case-studies/collection/level-1-beginner.md)
- 🔗 [Lecture notes](../../lectures/module-05-crypto/lecture-20.md)

## Week 11 · 2026-11-16 – 2026-11-19
**Due / happen this week:**
- 📝 **Quiz Q11 (specimen)** — [details](../../assessments/student/quizzes/quiz-11.md)
- 📝 **Lab 29 report due**
- 🗓 **Register case-brief case** — [task](../../assessments/student/case-study-activity.md)
### Lecture 21 — Security Analytics I: Anomaly Detection in Logs
*Mon 16 Nov 2026 · M6 Data Science for Security & ML Security · CLO-6*
- Engineer features from auth logs
- Tune isolation forests by SOC capacity
- 🔬 [Lab 19](../../labs/lab-19-log-anomaly/README.md) — Log Analysis & Anomaly Detection **(graded)** · *Lab 19 due W12*
- 💬 Case discussion: [CS-055](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-06-ml-security/lecture-21.md)

### Lecture 22 — Security Analytics II: Classification Pipelines
*Thu 19 Nov 2026 · M6 Data Science for Security & ML Security · CLO-6*
- Build phishing classifiers that survive rewording
- Manage feature drift and label quality
- 🔬 [Lab 20](../../labs/lab-20-phishing-classifier/README.md) — Phishing Classification Pipeline
- 💬 Case discussion: [CS-068](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-06-ml-security/lecture-22.md)

## Week 12 · 2026-11-23 – 2026-11-26
**Due / happen this week:**
- 📝 **Checkpoint E (graded, /10)** — [details](../../assessments/student/quizzes/quiz-12.md)
- 📝 **Case-study brief due (10%)** — [details](../../assessments/student/case-study-activity.md)
- 📝 **Lab 19 report due**
### Lecture 23 — Adversarial Machine Learning: Evasion, Poisoning, Extraction
*Mon 23 Nov 2026 · M6 Data Science for Security & ML Security · CLO-6*
- Execute sandbox adversarial demos
- Apply mitigations with named costs
- 🔬 [Lab 21](../../labs/lab-21-adversarial-ml/README.md) — Adversarial ML Stations
- 💬 Case discussion: [CS-067](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-06-ml-security/lecture-23.md)

### Lecture 24 — Detection Engineering: Metrics, Rules, and the SOC Pipeline + Checkpoint E
*Thu 26 Nov 2026 · M6 Data Science for Security & ML Security · CLO-6*
- Take a rule through shadow→alert→block
- Write coverage statements with measured FPR/TPR
- 🔬 [Lab 22](../../labs/lab-22-detection-engineering/README.md) — Detection Engineering Pipeline
- 💬 Case discussion: [CS-085](../../case-studies/collection/level-4-expert.md)
- 🔗 [Lecture notes](../../lectures/module-06-ml-security/lecture-24.md)

## Week 13 · 2026-11-30 – 2026-12-03
**Due / happen this week:**
- 📝 **Quiz Q13 (specimen)** — [details](../../assessments/student/quizzes/quiz-13.md)
### Lecture 25 — Cloud Security I: Shared Responsibility and IAM
*Mon 30 Nov 2026 · M7 Cloud Security & Privacy · CLO-7*
- Allocate responsibility across service models
- Design least-privilege IAM with roles
- 🔬 [Lab 23](../../labs/lab-23-cloud-iam/README.md) — Cloud IAM Least-Privilege Audit **(graded)** · *Lab 23 due W14*
- 💬 Case discussion: [CS-062](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-07-cloud-privacy/lecture-25.md)

### Lecture 26 — Cloud Security II: Containers, Serverless, and Secrets
*Thu 03 Dec 2026 · M7 Cloud Security & Privacy · CLO-7*
- Harden images and runtime surfaces
- Manage secrets without env-as-vault
- 🔬 [Lab 24](../../labs/lab-24-containers/README.md) — Container & Workload Hardening
- 💬 Case discussion: [CS-064](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-07-cloud-privacy/lecture-26.md)

## Week 14 · 2026-12-07 – 2026-12-10
**Due / happen this week:**
- 📝 **Checkpoint F (graded, /10)** — [details](../../assessments/student/quizzes/quiz-14.md)
- 📝 **Lab 23 report due**
### Lecture 27 — Cloud Security III: Audit Trails, Detection, and Misconfiguration Management
*Mon 07 Dec 2026 · M7 Cloud Security & Privacy · CLO-7*
- Distinguish control- vs data-plane telemetry
- Run policy-as-code and drift detection
- 🔬 [Lab 25](../../labs/lab-25-cloud-audit/README.md) — Cloud Audit-Trail Investigation
- 💬 Case discussion: [CS-063](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-07-cloud-privacy/lecture-27.md)

### Lecture 28 — Privacy Engineering: Data Protection, GDPR-style Compliance, DPIA + Checkpoint F
*Thu 10 Dec 2026 · M7 Cloud Security & Privacy · CLO-7*
- Apply minimization and data-subject rights
- Draft a DPIA skeleton
- 🔬 [Lab 26](../../labs/lab-26-dpia/README.md) — Privacy Engineering & DPIA
- 💬 Case discussion: [CS-094](../../case-studies/collection/level-4-expert.md)
- 🔗 [Lecture notes](../../lectures/module-07-cloud-privacy/lecture-28.md)

## Week 15 · 2026-12-14 – 2026-12-17
**Due / happen this week:**
- 📝 **Quiz Q15 pre-final (specimen)** — [details](../../assessments/student/quizzes/quiz-15.md)
- 📝 **Capstone milestone 1 (threat model)** — [details](../../assessments/student/capstone-brief.md)
### Lecture 29 — Capstone Kickoff: Scenario, Threat Model, Control Backlog
*Mon 14 Dec 2026 · M8 Capstone · CLO-8*
- Scope one system with explicit boundaries
- Produce a team threat model and backlog
- 🔬 [Lab 30](../../labs/lab-30-capstone/README.md) — Capstone Working Labs (1/3)
- 💬 Case discussion: [CS-100](../../case-studies/collection/level-4-expert.md)
- 🔗 [Lecture notes](../../lectures/module-08-capstone/lecture-29.md)

### Lecture 30 — Capstone Build Sprint I: Hardening and Detection
*Thu 17 Dec 2026 · M8 Capstone · CLO-8*
- Implement priority controls with fix-verify
- Build one detection with measured metrics
- 🔬 [Lab 30](../../labs/lab-30-capstone/README.md) — Capstone Working Labs (2/3)
- 💬 Case discussion: [CS-083](../../case-studies/collection/level-4-expert.md)
- 🔗 [Lecture notes](../../lectures/module-08-capstone/lecture-30.md)

## Week 16 · 2026-12-21 – 2026-12-24
**Due / happen this week:**
- 📝 **Capstone report + showcase defense (20%)** — [details](../../assessments/student/capstone-brief.md)
- 📝 **Final examination (10%)** — [details](../../assessments/student/specimen-final.md)
- 📝 **Lab 28 report due**
### Lecture 31 — Capstone Build Sprint II: Incident-Response Tabletop
*Mon 21 Dec 2026 · M8 Capstone · CLO-8*
- Run a tabletop against your own design
- Update runbooks from findings
- 🔬 [Lab 28](../../labs/lab-28-ir-simulation/README.md) — Incident Response Simulation **(graded)** · *Lab 28 due W16*
- 🔬 [Lab 30](../../labs/lab-30-capstone/README.md) — Capstone Working Labs (3/3)
- 💬 Case discussion: [CS-058](../../case-studies/collection/level-3-advanced.md)
- 🔗 [Lecture notes](../../lectures/module-08-capstone/lecture-31.md)

### Lecture 32 — Capstone Showcase and Final Examination
*Thu 24 Dec 2026 · M8 Capstone · CLO-8*
- Defend the capstone chain under questioning
- Complete the final examination
- 🔗 [Lecture notes](../../lectures/module-08-capstone/lecture-32.md)

---
*Generated from the repository's actual content — do not hand-edit; regenerate instead (`calendar/tools/generate_calendar.py`). Answer keys are never linked here.*
