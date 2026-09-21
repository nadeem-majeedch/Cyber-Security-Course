# Quiz 15 — Specimen (Week 15) · Cloud Ops, Privacy, IR & Capstone Readiness
**Ungraded self-check · 15 marks · ~15 minutes · CLO-5, CLO-7, CLO-8 · Answer key discussed in class; not posted.**
*These practice items do not appear on the final itself — they sample the same skills.*

## Part A — Multiple choice (1 mark each)

**1.** The strongest control against a leaked long-lived access key:
- A. Rotating the key every 90 days
- B. No static keys — role-assumed, short-lived credentials
- C. Key naming conventions
- D. Billing alerts

**2.** "Who deleted this bucket?" is answered by:
- A. Flow logs
- B. Control-plane (management) audit logs
- C. Load-balancer access logs
- D. DNS query logs

**3.** An IaC template that passed review still deploys a public bucket. The systemic fix:
- A. Ask reviewers to look harder
- B. Policy-as-code scanning enforced in CI before deploy
- C. An annual audit
- D. A manual console check

**4.** Container escape severity is highest when:
- A. Images are large
- B. The runtime is privileged or mounts the host docker socket
- C. The app is written in Python
- D. Logs go to stdout

**5.** A DPIA is required before processing that:
- A. Uses any database
- B. Is likely to result in high risk to individuals (systematic monitoring, sensitive categories)
- C. Runs in the cloud
- D. Stores fewer than 100 rows

**6.** The NIST SP 800-61 phases, in order:
- A. Detect → Fix → Report
- B. Preparation → Detection & Analysis → Containment/Eradication/Recovery → Post-Incident
- C. Triage → Backup → Patch → Forget
- D. Identify → Protect → Detect → Respond

**7.** A compromised host is still encrypting files. The response balancing containment with evidence:
- A. Power off immediately
- B. Isolate from the network (keep powered), then capture volatile data
- C. Reboot into safe mode
- D. Run a full antivirus scan first

**8.** RTO and RPO measure, respectively:
- A. Risk trend and probability
- B. Time to restore service and maximum tolerable data loss
- C. Team size and cost
- D. Recovery cost and outage likelihood

## Part B — Short answer (7 marks)

**9.** (a) Why is encryption without key lifecycle management an incomplete control? (2)
(b) Your detector's F1 dropped after the campus switched SSO providers. State the first hypothesis and how you would check it. (2)
(c) In one sentence each: what must connect the capstone's threat model → control → detection → IR layers? (3: one per link — the graded word is *traceability*.)

---
*Specimen items are contaminated for grading use once shown. Review answers against the in-class key. Final format guide: Section A MCQs (10 × 1), Section B short scenario answers (2 × 6), Section C scenario analysis (choose 2 of 3 × 10), Section D synthesis essay (8).*
