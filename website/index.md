# Cyber Security — BS CS / BS Data Science

**32 lectures × 2 hours = 64 contact hours · 16 weeks · 8 modules · 7th semester**
From security foundations to a defended capstone: threat modeling, web security, malware analysis, network defense, cryptography, ML-driven security analytics, cloud & privacy — culminating in a team defensive architecture you defend orally.

> **Ethics first:** this course teaches *authorized, defensive* security only. All labs run on isolated, sandboxed course targets. Attacking systems without written authorization is illegal and out of scope.

## Start here

| If you are… | Read |
|---|---|
| A student | the [weekly schedule](calendar.md), then your lecture's notes below |
| An instructor | `instructor-materials/` (private distribution — not part of this site) |
| Evaluating the course | `syllabus.md` in the repository root |

## Modules & lectures

### Module 1 — Security Foundations & Threat Modeling
1. [Security Foundations: CIA, Ethics, and the Defender's Mindset](lectures/module-01-fundamentals/lecture-01.md)
2. [Threat Modeling I: STRIDE and Attack Trees](lectures/module-01-fundamentals/lecture-02.md)
3. [Threat Modeling II: Attack Surface and MITRE ATT&CK](lectures/module-01-fundamentals/lecture-03.md)
4. [Defense in Depth, Least Privilege, and Checkpoint A](lectures/module-01-fundamentals/lecture-04.md)

### Module 2 — Web Application Security
5. [Web Foundations: HTTP, Sessions, and Authentication](lectures/module-02-web/lecture-05.md)
6. [Injection Attacks: SQL, NoSQL, and Command Injection](lectures/module-02-web/lecture-06.md)
7. [XSS, CSRF, SSRF, and IDOR](lectures/module-02-web/lecture-07.md)
8. [Secure SDLC, Dependency Hygiene, Security Headers](lectures/module-02-web/lecture-08.md)

### Module 3 — Malware Analysis & Social Engineering
9. [Malware Analysis I: Taxonomy and Static Triage](lectures/module-03-malware/lecture-09.md)
10. [Malware Analysis II: Dynamic Analysis, Sandboxes, and IOCs](lectures/module-03-malware/lecture-10.md)
11. [Ransomware and Worms: Anatomy and Resilience](lectures/module-03-malware/lecture-11.md)
12. [Social Engineering, Phishing & Awareness Programs](lectures/module-03-malware/lecture-12.md)

### Module 4 — Network Security & Monitoring
13. [Network Defense I: Packet Analysis with Wireshark](lectures/module-04-network/lecture-13.md)
14. [Network Defense II: Firewalls, Segmentation, Zero Trust](lectures/module-04-network/lecture-14.md)
15. [IDS/IPS and SIEM: Detection and Alert Triage](lectures/module-04-network/lecture-15.md)
16. [Wireless, VPN & Midterm Consolidation](lectures/module-04-network/lecture-16.md)

### Module 5 — Cryptography & Applied Trust
17. [Symmetric Cryptography and Block Cipher Modes](lectures/module-05-crypto/lecture-17.md)
18. [Asymmetric Cryptography, PKI, and TLS](lectures/module-05-crypto/lecture-18.md)
19. [Hashing, Password Storage, and Key Management](lectures/module-05-crypto/lecture-19.md)
20. [Cryptographic Failures in the Wild](lectures/module-05-crypto/lecture-20.md)

### Module 6 — Data Science for Security & ML Security
21. [Security Analytics I: Anomaly Detection in Logs](lectures/module-06-ml-security/lecture-21.md)
22. [Security Analytics II: Classification Pipelines](lectures/module-06-ml-security/lecture-22.md)
23. [Adversarial Machine Learning: Evasion, Poisoning, Extraction](lectures/module-06-ml-security/lecture-23.md)
24. [Detection Engineering: Metrics, Rules, and the SOC Pipeline](lectures/module-06-ml-security/lecture-24.md)

### Module 7 — Cloud Security & Privacy
25. [Cloud Security I: Shared Responsibility and IAM](lectures/module-07-cloud-privacy/lecture-25.md)
26. [Cloud Security II: Containers, Serverless, and Secrets](lectures/module-07-cloud-privacy/lecture-26.md)
27. [Cloud Security III: Audit Trails, Detection, and Misconfiguration Management](lectures/module-07-cloud-privacy/lecture-27.md)
28. [Privacy Engineering: Data Protection, GDPR-style Compliance, DPIA](lectures/module-07-cloud-privacy/lecture-28.md)

### Module 8 — Capstone
29. [Capstone Kickoff: Scenario, Threat Model, Control Backlog](lectures/module-08-capstone/lecture-29.md)
30. [Capstone Build Sprint I: Hardening and Detection](lectures/module-08-capstone/lecture-30.md)
31. [Capstone Build Sprint II: Incident-Response Tabletop](lectures/module-08-capstone/lecture-31.md)
32. [Capstone Showcase and Final Examination](lectures/module-08-capstone/lecture-32.md)

## Practice materials (in the repository)

- **Labs:** 14-lab program (8 core graded + enrichment) under `labs/` — every worksheet carries authorization and safety rules; all activity is sandbox-only.
- **Case discussions:** 100 progressive simulated scenarios under `case-studies/` (Levels 1–4) used in every lecture.
- **Quizzes & exams:** weekly specimen quizzes and practice papers under `assessments/student/` — answer keys are never published here.

## Schedule

See the [semester calendar](calendar.md) for the week-by-week plan with dates (regenerated per term from `calendar/tools/generate_calendar.py`).
