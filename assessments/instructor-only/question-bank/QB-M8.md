# Question Bank — Module 8 (L29–L32) · CLO-8 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q15 (W15), the pre-final specimen, and makeup packs. Duplicate-avoidance rule: see `README.md`.

## MCQ-8.1

**Topic:** IR lifecycle · **CLO-8** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 15
**Used in:** Q15

The NIST SP 800-61 incident-response phases, in order, are:

- A. Detect → Fix → Report
- B. Preparation → Detection & Analysis → Containment/Eradication/Recovery → Post-Incident ✔
- C. Triage → Backup → Patch → Forget
- D. Identify → Protect → Detect → Respond

**Explanation:** NIST 800-61 four phases; option D is the NIST CSF functions — a deliberate distractor. Key: B.

## MCQ-8.2

**Topic:** Evidence preservation · **CLO-8** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

A compromised host is still encrypting files. The response that balances containment with evidence:

- A. Power off immediately
- B. Isolate from the network (keep powered), then capture volatile data ✔
- C. Reboot into safe mode
- D. Run a full antivirus scan first

**Explanation:** Isolation cuts attacker access without destroying memory; power-off loses volatility. Key: B.

## MCQ-8.3

**Topic:** Chain of custody · **CLO-8** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

A forensic image must be accompanied by:

- A. A screenshot of the desktop
- B. Hashes of image and copy, acquisition time/tool, and collector identity ✔
- C. The antivirus report only
- D. A list of user complaints

**Explanation:** Integrity (hash), provenance (who/when/how) constitute the custody record that makes evidence defensible. Key: B.

## MCQ-8.4

**Topic:** Tabletop exercises · **CLO-8** · **Bloom:** Evaluate · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

The primary output of a tabletop exercise is:

- A. A penalty assessment
- B. Tested gaps in decisions/roles/communications, feeding runbook updates ✔
- C. A press release
- D. A new firewall rule

**Explanation:** Tabletops rehearse decision-making; the deliverable is the improvement list (runbooks, roles, comms). Key: B.

## MCQ-8.5

**Topic:** Capstone scoping · **CLO-8** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

A capstone team proposes "secure everything." The best scoping advice:

- A. Expand the scope
- B. Pick one system, define threat model → controls → detection → IR, and defend tradeoffs ✔
- C. Focus only on firewalls
- D. Copy a vendor whitepaper

**Explanation:** CLO-8 assesses a defensible, complete mini-architecture — depth and traceability beat breadth. Key: B.

## MCQ-8.6

**Topic:** Detection coverage argument · **CLO-8** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 15
**Used in:** Q15

A capstone claims "we monitor everything." The strongest challenge question:

- A. What is your budget?
- B. Which ATT&CK techniques do your rules cover, with what measured FPR/TPR — and what is unmonitored? ✔
- C. Why not buy a SIEM?
- D. Who pays for storage?

**Explanation:** Coverage must be evidenced (mapped techniques + measured performance + honest gaps) — the core defense question. Key: B.

## MCQ-8.7

**Topic:** Governance — risk acceptance · **CLO-8** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 15
**Used in:** Q15

A control is too costly for a small university lab. The governance-correct response is:

- A. Ignore the risk silently
- B. Document a formal risk acceptance with owner, residual risk, and review date ✔
- C. Buy the control anyway
- D. Ask students to be careful

**Explanation:** Risk treatment decisions (accept/transfer/mitigate/avoid) must be explicit, owned, and revisited. Key: B.

## MCQ-8.8

**Topic:** Resilience metrics · **CLO-8** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 15
**Used in:** Q15

RTO and RPO measure, respectively:

- A. Risk trend and occurrence probability
- B. Time to restore service and maximum tolerable data loss ✔
- C. Response team size and operational cost
- D. Recovery cost and outage probability

**Explanation:** Standard BC/DR definitions; students must map them to backup frequency and failover design. Key: B.

## SA-8.1 (short answer, 6 marks)

**Topic:** Capstone synthesis · **CLO-8** · **Bloom:** Create · **Difficulty:** Hard · **Week:** 15
**Used in:** Q15

Given the semester's arc, sketch the skeleton of a defensible defensive assessment for a small e-commerce site: one threat, one control, one detection, one IR step — with the reasoning chain linking them.

**Key:** Threat: card-data theft via injection (STRIDE: Tampering/Info disclosure; ATT&CK: Exploit Public-Facing Application). Control: parameterized queries + least-priv DB. Detection: alert on SQL error bursts/anomalous query latency. IR: isolate DB segment, preserve logs, activate runbook. Chain: threat model justifies control; control failure mode justifies detection; detection triggers IR — traceability is the graded skill.

## SA-8.2 (short answer, 4 marks)

**Topic:** Ethics & disclosure · **CLO-8** · **Bloom:** Evaluate · **Difficulty:** Medium · **Week:** 15
**Used in:** makeup MT-9 only

You find a flaw in your employer's public site outside your assigned scope. State the two professional actions and the one action that violates policy.

**Key:** Report through the responsible channel (security team/program), document without exploiting beyond validation; violate: scanning/exploiting out of scope or publishing details without coordination.
