# Question Bank — Specimen Pool: Midterm Practice (Q8) · ⚠️ INSTRUCTOR-ONLY

Practice items for the Week 8 pre-midterm quiz (`../../student/quizzes/quiz-08.md`). These do NOT appear in the live midterm. Duplicate-avoidance rule applies.

## MCQ (1 mark each)

**SM-1.** **CIA/STRIDE · CLO-1 · Bloom: Understand · Easy**
A database column is readable by an intern whose role does not need it. Violation:
A. Integrity B. Confidentiality ✔ C. Availability D. Repudiation
*Confidentiality = unauthorized reading; role-scoping is the fix (least privilege).*

**SM-2.** **STRIDE · CLO-1 · Bloom: Apply · Easy**
Altering a cookie value from `role=user` to `role=admin` before sending it:
A. Spoofing B. Tampering ✔ C. DoS D. Repudiation
*Modification of data in transit/state = Tampering; the server must treat client data as untrusted.*

**SM-3.** **Injections · CLO-2 · Bloom: Apply · Easy**
The single control that eliminates classic SQL injection:
A. WAF B. Parameterized queries ✔ C. Input length limits D. HTTPS
*Prepared statements separate code from data; WAF/limits are compensating.*

**SM-4.** **Sessions · CLO-2 · Bloom: Apply · Medium**
`SameSite=Strict` primarily mitigates:
A. XSS B. CSRF ✔ C. SSRF D. Clickjacking
*Cross-site requests carry no cookie → forged writes lose their credential.*

**SM-5.** **Static analysis · CLO-3 · Bloom: Understand · Easy**
The safest first artifact to extract from a suspicious document, before any execution:
A. Network traffic B. Embedded macro source (static extraction) ✔ C. Registry hives D. Screenshots
*Static extraction needs no detonation; execution artifacts come later in a sandbox.*

**SM-6.** **Firewall rules · CLO-4 · Bloom: Apply · Medium**
A ruleset lacking an explicit final rule relies on:
A. Implicit default-allow on most platforms — dangerous; write explicit default-deny ✔ B. Implicit deny C. Automatic logging D. Stateful return traffic
*Most legacy ACLs default-allow; explicit deny-last is the auditable posture.*

**SM-7.** **IDS placement · CLO-4 · Bloom: Apply · Medium**
To see east-west (lateral) traffic, sensors must sit:
A. Only at the internet edge B. Inside segments / at inter-zone choke points ✔ C. On the VPN concentrator D. On endpoints only
*Lateral movement crosses internal switches/firewalls; edge sensors never see it.*

**SM-8.** **Defense in depth · CLO-1 · Bloom: Analyze · Medium**
Backups are classified as which pair?
A. Preventive/technical B. Corrective/technical ✔ C. Detective/administrative D. Deterrent/physical
*They restore after failure — corrective; implemented in technology.*

## Short answers (2 marks each)

**SM-9.** **CLO-1 · Bloom: Analyze** — Give one threat to a laptop that STRIDE models poorly, and why. *Key: physical theft/environmental (no interaction with the system's logic); STRIDE presumes a reachable attack surface — physical controls cover the gap.*

**SM-10.** **CLO-2 · Bloom: Analyze** — Why does output encoding fail to prevent command injection? *Key: encoding targets interpreters downstream of the web layer (HTML/JS); the shell parses before that — the fix is argument-list execution, not encoding.*

**SM-11.** **CLO-3 · Bloom: Apply** — One reason a sample's first execution should happen without internet access. *Key: prevent live C2 reach-out/evidence contamination and further compromise; fake-net records the attempts safely.*

**SM-12.** **CLO-4 · Bloom: Analyze** — A rule allows 443 from any → web tier. Name the residual risk and one narrowing change. *Key: any source includes scanners/bots — risk = exposure of app-layer flaws; narrow by geography/ASN/CDN-only origin, or move origin behind CDN allowlist.*
