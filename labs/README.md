# Labs (student-facing)

Practical curriculum for the 32-lecture course. **14 labs: 8 core + 6 enrichment**, aligned to the eight approved modules and the course CLOs (`syllabus.md` §4).

## Lab inventory

| Lab | Directory | Title | Type | Module / Lectures | Duration |
|---|---|---|---|---|---|
| 00 | `lab-00-hardening-baseline/` | Security Baseline & System Hardening | **Core 1** | M1 · L01, L04 | 2 h |
| 01 | `lab-01-threat-modeling/` | Threat Modeling: STRIDE & Attack Trees | Enrichment | M1 · L02–L04 | 2 h |
| 02 | `lab-02-attack-surface/` | Attack Surface & ATT&CK Mapping | Enrichment | M1 · L03 | 2 h |
| 03 | `lab-03-controls-layering/` | Defense-in-Depth Control Plan | Enrichment | M1 · L04 | 2 h |
| 04 | `lab-04-web-foundations/` | Web Auth Flow Review (demo app) | Enrichment | M2 · L05 | 2 h |
| 05 | `lab-05-injection/` | Injection: Confirm, Fix, Verify (sandboxed) | Enrichment | M2 · L06 | 2 h |
| 06 | `lab-06-xss-csrf-ssrf-idor/` | Web Flaw Stations (sandboxed) | Enrichment | M2 · L07 | 2 h |
| 07 | `lab-07-headers-sdlc/` | Security Headers & Dependency Hygiene | Enrichment | M2 · L08 | 2 h |
| 08 | `lab-08-static-triage/` | Malware Static Triage (synthetic samples) | Enrichment | M3 · L09 | 2 h |
| 09 | `lab-09-dynamic-analysis/` | Dynamic Analysis & IOCs (sandboxed) | Enrichment | M3 · L10 | 2 h |
| 10 | `lab-10-ransomware-resilience/` | Ransomware Resilience Scenario | Enrichment | M3 · L11 | 2 h |
| 11 | `lab-11-awareness-design/` | Awareness Campaign Design | Enrichment | M3 · L12 | 2 h |
| **12** | `lab-12-packet-analysis/` | **Network Traffic Analysis (prepared captures)** | **Core 2** | M4 · L13 | 2 h |
| 13 | `lab-13-segmentation/` | Segmentation & Ruleset Design | Enrichment | M4 · L14 | 2 h |
| 14 | `lab-14-siem-triage/` | Alert Triage & Correlation | Enrichment | M4 · L15 | 2 h |
| **15** | `lab-15-crypto-integrity/` | **Cryptographic Operations & Integrity Checks** | **Core 3** | M5 · L17, L19 | 2 h |
| 16 | `lab-16-pki-tls/` | Certificates, PKI & TLS Inspection | Enrichment | M5 · L18 | 2 h |
| 17 | `lab-17-password-storage/` | Password Storage & Secrets Hygiene | Enrichment | M5 · L19 | 2 h |
| 18 | `lab-18-crypto-failures/` | Crypto Failure Review | Enrichment | M5 · L20 | 2 h |
| **19** | `lab-19-log-anomaly/` | **Log Analysis & Anomaly Detection** | **Core 6** | M6 · L21 | 2 h |
| 20 | `lab-20-phishing-classifier/` | Phishing Classification Pipeline | Enrichment | M6 · L22 | 2 h |
| 21 | `lab-21-adversarial-ml/` | Adversarial ML Stations | Enrichment | M6 · L23 | 2 h |
| 22 | `lab-22-detection-engineering/` | Detection Engineering Pipeline | Enrichment | M6 · L24 | 2 h |
| **23** | `lab-23-cloud-iam/` | **Cloud IAM Least-Privilege Audit** | **Core 5 (vuln assessment)** | M7 · L25 | 2 h |
| 24 | `lab-24-containers/` | Container & Workload Hardening | Enrichment | M7 · L26 | 2 h |
| 25 | `lab-25-cloud-audit/` | Cloud Audit-Trail Investigation | Enrichment | M7 · L27 | 2 h |
| 26 | `lab-26-dpia/` | Privacy Engineering & DPIA | Enrichment | M7 · L28 | 2 h |
| **27** | `lab-27-forensics/` | **Digital Forensics: Instructor-Provided Artifacts** | **Core 7** | M3/M4 · L10, L27 | 2 h |
| **28** | `lab-28-ir-simulation/` | **Incident Response Simulation** | **Core 8** | M8 · L31 | 2 h |
| **29** | `lab-29-vuln-assessment/` | **Authorized Lab-Target Vulnerability Assessment** | **Core 4+5 (secure web testing + vuln assessment)** | M2/M4 · L06–L08, L15 | 2 h |
| 30 | `lab-30-capstone/` | Capstone Working Labs (L29–L31 sessions) | Enrichment | M8 · L29–L32 | 3 × 2 h |

**Core lab themes → labs mapping (assignment requirement):** hardening → Lab 00 · network traffic analysis → Lab 12 · cryptographic operations/integrity → Lab 15 · secure web testing on a deliberately vulnerable local app → Labs 05/06/29 · vulnerability assessment of an authorized lab target → Lab 29 (extends Lab 23's audit) · log analysis & event correlation → Lab 19 (extends Lab 14) · digital forensics with instructor-provided artifacts → Lab 27 · incident response simulation → Lab 28.

## Standing rules (every lab)

> **Responsible use:** All activity is confined to the isolated course environment (course VM, course sandbox targets, instructor-provided artifacts). Scanning or probing public or personal systems is prohibited. No credential theft, destructive payloads, persistence mechanisms, or unauthorized-access techniques are taught or practiced. Every demonstrated weakness is paired with defensive remediation.

## Submission & grading

Graded labs (best 6 of 8 counted, 30% of course grade): **00, 12, 15, 19, 23, 27, 28, 29**. Enrichment labs are checked-in/not-checked-in and feed checkpoints. Rubrics: 40% correctness, 30% evidence quality, 30% analysis/remediation. Instructor keys and rubric detail: `../assessments/instructor-only/` (never distributed).
