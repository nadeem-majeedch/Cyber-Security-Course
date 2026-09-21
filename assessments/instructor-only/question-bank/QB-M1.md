# Question Bank — Module 1 (L01–L04) · CLO-1 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q1 (W1), Q3 (W3), and makeup packs. No item may appear in both a graded paper and a live specimen without replacement — see `README.md` (duplicate-avoidance rule).

## MCQ-1.1

**Topic:** CIA triad · **CLO-1** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 1
**Used in:** Q1

During monthly reconciliation, a finance clerk discovers that salary figures in the payroll export no longer match the approved budget file, although the export was never edited locally. Which CIA property was violated?

- A. Confidentiality
- B. Integrity ✔
- C. Availability
- D. Non-repudiation

**Explanation:** The data was altered between approval and use — a classic integrity failure. Confidentiality (unauthorized reading) and availability (denial of use) are not implicated. Key: B.

## MCQ-1.2

**Topic:** Security vs. privacy vs. safety · **CLO-1** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 1
**Used in:** Q1

A smart-doorbell vendor ships cameras with a default password. Attackers view strangers' living rooms. Which pair of properties is most directly violated?

- A. Safety and availability
- B. Confidentiality and privacy ✔
- C. Integrity and non-repudiation
- D. Availability and integrity

**Explanation:** Unauthorized viewing is a confidentiality breach of personal data — a privacy violation. The system still works (availability intact) and data was not altered. Key: B.

## MCQ-1.3

**Topic:** STRIDE · **CLO-1** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 2
**Used in:** Q3

An attacker replays a captured request token and the server accepts it as a valid user. Which STRIDE element, and which property, does this violate?

- A. Repudiation — accountability
- B. Spoofing — authenticity ✔
- C. Tampering — integrity
- D. Elevation of privilege — authorization

**Explanation:** Replay impersonates a legitimate principal: spoofing, violating authenticity. Repudiation concerns denying actions; no data was altered. Key: B.

## MCQ-1.4

**Topic:** MITRE ATT&CK · **CLO-1** · **Bloom:** Understand · **Difficulty:** Medium · **Week:** 2
**Used in:** Q3

In ATT&CK Enterprise, tactics and techniques are best described as:

- A. Tool names and malware family names
- B. The adversary's tactical goals and the means of achieving them ✔
- C. Vulnerability identifiers and patch levels
- D. Vendor detection product categories

**Explanation:** Tactics = the "why" (objectives such as Credential Access); techniques = the "how" (behaviors such as OS Credential Dumping). ATT&CK is vendor-neutral behavior taxonomy, not CVE or product data. Key: B.

## MCQ-1.5

**Topic:** Defense in depth · **CLO-1** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 2
**Used in:** Q3

A web server has a WAF, input validation, parameterized queries, and daily backups. A single SQL-injection bypasses the WAF. Which layer stops data loss, and which principle explains why multiple layers matter?

- A. Backups; single point of failure avoidance ✔
- B. Input validation; least privilege
- C. Parameterized queries; economies of scale
- D. Backups; separation of duties

**Explanation:** Even if prevention layers fall, the corrective backup layer limits impact — the point of defense in depth is that no single control is load-bearing. Key: A.

## MCQ-1.6

**Topic:** Control classification · **CLO-1** · **Bloom:** Apply · **Difficulty:** Easy · **Week:** 2
**Used in:** Q3

A SIEM alert page that wakes an on-call analyst is best classified as:

- A. Preventive control
- B. Detective control with corrective follow-up ✔
- C. Deterrent control only
- D. Compensating control only

**Explanation:** The alert detects; the human response corrects. It does not stop the initial action, so it is not preventive. Key: B.

## MCQ-1.7

**Topic:** Attack surface · **CLO-1** · **Bloom:** Analyze · **Difficulty:** Hard · **Week:** 2
**Used in:** Q3

Which change *reduces* attack surface most reliably?

- A. Adding a second firewall vendor
- B. Disabling an unused admin API on the public interface ✔
- C. Requiring longer passwords on the VPN
- D. Adding an IDS behind the firewall

**Explanation:** Removing an exposed function eliminates whole attack paths. The others add detection or harden one door while leaving the API open. Key: B.

## MCQ-1.8

**Topic:** Least privilege & secure defaults · **CLO-1** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3 · makeup MT-2

A new internal tool ships with `admin`/`admin` enabled "for easy first login." The most standards-aligned fix is:

- A. Document the default password in the manual
- B. Force a random per-install password on first boot and disable admin until set ✔
- C. Rate-limit logins with the default password
- D. Move the tool behind the VPN

**Explanation:** Secure defaults remove the unsafe state entirely (CIS-style benchmark practice); rate limits or VPNs add friction but keep the default alive. Key: B.

## SA-1.1 (short answer, 4 marks)

**Topic:** Threat modeling · **CLO-1** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 2
**Used in:** Q3

Apply STRIDE to a university online-transcript portal (login, request transcript, registrar approval, PDF download). Identify **one** credible threat per STRIDE letter (5 marks) and name **one** control for the two threats you rate highest (2 marks). **Total: 7 marks — rescore /5 for quiz use (drop the control marks or scale).**

**Key:** S: stolen session cookie impersonates a student. T: altered approval flag before PDF generation. R: student denies requesting a transcript that was sent to a third party. I: transcript PDF readable by another student via predictable URL. D: script floods transcript requests, exhausting the queue. E: parameter tampering sets `role=registrar`. Controls (top two): per-object access check for I; server-side session + audit trail for S/R.

## SA-1.2 (short answer, 6 marks)

**Topic:** ATT&CK + defense hypothesis · **CLO-1** · **Bloom:** Create · **Difficulty:** Hard · **Week:** 2
**Used in:** makeup MT-1 only (do not reuse in live quizzes)

Write one threat-informed defense hypothesis for credential dumping on Windows workstations: the technique (name or ID), the telemetry you would collect, and the analytic that would fire.

**Key:** Technique: OS Credential Dumping (T1003). Telemetry: process-access events to `lsass.exe` from non-system tools; Sysmon EID 10. Analytic: alert when a process outside a known-good list requests lsass access. Credit any coherent technique→telemetry→analytic chain.
