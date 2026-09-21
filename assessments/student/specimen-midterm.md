# Specimen Midterm (Week 8 practice) — Cyber Security
**Practice paper · 90 minutes equivalent · 50 marks · Modules M1–M4 (CLO-1–CLO-4) · Questions only — the live midterm has different items; format and mark allocation match exactly.**

## Section A — Multiple choice (10 × 1 mark)

1. A backup job overwrites good archives with encrypted ones. Which CIA property failed *in the backup system*?
   A. Confidentiality B. Integrity C. Availability D. Non-repudiation

2. STRIDE element most directly countered by server-side session validation:
   A. Spoofing B. Tampering C. Repudiation D. Elevation of privilege

3. In ATT&CK, "Credential Access" is an example of a:
   A. Technique B. Tactic C. Procedure D. Mitigation

4. The control type that *stops* an attack in progress is:
   A. Preventive B. Detective C. Corrective D. Directive

5. Which fix most reduces attack surface?
   A. Adding an IDS B. Disabling an unused public API C. Longer passwords D. A second firewall vendor

6. A query built by string concatenation is fixed by:
   A. Input length limits B. Parameterized statements C. A WAF D. HTTPS

7. SSRF impact is highest when the target is:
   A. An external website B. The cloud metadata service C. The renderer's own cache D. A CDN

8. Static malware triage begins with:
   A. Detonation B. Hashing and threat-intel lookup C. Registry diffs D. Memory capture

9. A ruleset processes top-down; a broad allow above a specific deny results in:
   A. The deny winning B. The allow winning C. A configuration error D. Both logging

10. Anomaly IDS vs signature IDS — the expected tradeoff is:
    A. Fewer false positives, fewer detections B. Novel detection, more false positives C. Perfect detection D. No baseline needed

## Section B — Short scenario answers (2 × 6 marks)

**11.** The registrar's server sits on the campus flat network; a phished staff password lets an attacker enumerate shares. (a) Name the initial-access technique in ATT&CK terms and one likely discovery technique. (b) Propose a containment action that preserves evidence. (c) Name one preventive and one detective control that would have reduced impact.

**12.** Design zone placement and a three-rule summary for: public web tier, internal API, database, admin jump host. Default-deny between zones. Justify the single most important logging point.

## Section C — Scenario analysis (choose 2 of 3 × 8 marks)

**13.** *Code analysis.* Given the excerpt on the answer sheet (a route handler with string-concatenated SQL and user input passed into a template renderer): identify each vulnerability with a CWE, rank by impact, and give the corrected pattern.

**14.** *PCAP analysis.* The capture shows repeated SYNs to port 3389 across 200 hosts, then one host sending 40 MB to a single external IP over 445. Characterize both behaviors, name two corroborating telemetry sources, and give the containment order if the exfil is confirmed.

**15.** *Vendor audit.* A default deployment exposes an admin UI on 8080 with default credentials, verbose errors, and backups to an unprotected share. List five weaknesses, each tagged with the principle it violates and its concrete fix.

## Section D — Synthesis essay (8 marks)

**16.** Budget allows **either** MFA on all student accounts **or** EDR on all lab machines. Take a position; justify it with a risk-based argument; state what you give up; name the residual risk you would formally accept and who should own that acceptance.

---
*Marking guide mirrors the live paper: full marks require named CWEs/principles, ordered response steps, and traceable reasoning — not keywords. Model answers are discussed in the Week 8 tutorial.*
