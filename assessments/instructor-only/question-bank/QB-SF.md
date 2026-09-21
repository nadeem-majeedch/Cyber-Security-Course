# Question Bank — Specimen Pool: Final Practice (Q15 supplement) · ⚠️ INSTRUCTOR-ONLY

Practice items for the Week 15 pre-final specimen (`../../student/quizzes/quiz-15.md`). These do NOT appear in the live final. Duplicate-avoidance rule applies.

## MCQ (1 mark each)

**SF-1.** **IAM · CLO-7 · Bloom: Apply · Medium**
The strongest control against a leaked long-lived access key:
A. Key rotation every 90 days B. No static keys — role-assumed short-lived credentials ✔ C. Key naming conventions D. Billing alerts
*Elimination beats rotation; a role credential expires before leak-exploitation windows close.*

**SF-2.** **IR phases · CLO-8 · Bloom: Understand · Easy**
Eradication belongs to which NIST 800-61 phase group?
A. Preparation B. Containment/Eradication/Recovery ✔ C. Detection & Analysis D. Post-Incident
*Phase 3 groups containment, eradication, and recovery activities.*

**SF-3.** **Password storage · CLO-5 · Bloom: Apply · Easy**
Which storage leaks the most under a database dump?
A. Argon2id hashes B. bcrypt hashes C. Unsalted MD5 ✔ D. Encrypted passwords with key in app config
*Both C and D are catastrophic; unsalted MD5 enables immediate rainbow-table cracking at scale — accept D with equal justification.*

**SF-4.** **Detection metrics · CLO-6 · Bloom: Analyze · Medium**
A rule with TPR 0.9 and FPR 0.2 on 10k daily events (1% malicious) yields approximately:
A. ~90 true, ~1980 false alerts ✔ B. ~900 true, ~200 false C. ~90 true, ~20 false D. ~500 true, ~500 false
*TP 0.9×100=90; FP 0.2×9900=1980 — precision ≈ 4.3%, unusable without tuning. Tests the arithmetic behind alert fatigue.*

**SF-5.** **Containers · CLO-7 · Bloom: Apply · Medium**
The container control that most reduces escape blast radius:
A. Larger images B. Non-root user + read-only rootfs + dropped capabilities ✔ C. More CPU D. Port 8080 mapping
*Least privilege inside the container bounds what an escapee can leverage.*

**SF-6.** **Forensics · CLO-3,8 · Bloom: Apply · Medium**
The order of volatility (collect first → last):
A. Disk → RAM → logs → archives B. RAM → network state → disk → backups ✔ C. Backups → disk → RAM D. Logs → RAM → disk
*Memory and live network state vanish on power-down; disk persists; archives persist longest.*

**SF-7.** **Privacy · CLO-7 · Bloom: Apply · Easy**
Data minimization obliges collecting:
A. Everything, just in case B. Only what is adequate, relevant, and limited to purpose ✔ C. Anonymized aggregates only D. Data older than 5 years
*GDPR Art. 5(1)(c) framing; purpose limitation drives the scope.*

**SF-8.** **Governance · CLO-8 · Bloom: Evaluate · Medium**
The risk register entry that signals good governance:
A. "Risk closed by ignoring" B. Residual risk documented with owner and review date ✔ C. No risks listed D. All risks marked high
*Honest residual + ownership + review cadence is the maturity marker.*

## Short answers (2 marks each)

**SF-9.** **CLO-5 · Bloom: Analyze** — Why is encryption without key lifecycle management an incomplete control? *Key: keys outlive data protection decisions — rotation, revocation, escrow, and destruction determine whether ciphertext stays protected after compromise or staff change.*

**SF-10.** **CLO-6 · Bloom: Evaluate** — Your detector's F1 dropped after the campus switched SSO providers. First hypothesis and check? *Key: data/schema drift in telemetry (new event format) — inspect raw event distributions before touching the model.*

**SF-11.** **CLO-7 · Bloom: Analyze** — One reason "we're compliant, therefore secure" fails. *Key: compliance is point-in-time minimum baseline against known controls; threat landscapes and misconfigurations evolve continuously (accept: audit scope ≠ threat coverage).*

**SF-12.** **CLO-8 · Bloom: Create** — In one sentence each: the capstone's threat model, control, detection, and IR pieces must connect by what logic? *Key: traceability — each layer addresses a named threat; detection watches for control failure; IR assumes both failed; the chain, not the components, is assessed.*
