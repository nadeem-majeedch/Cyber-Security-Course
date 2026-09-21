# Question Bank — Final Exam Items (all CLOs) · ⚠️ INSTRUCTOR-ONLY

Scenario-based and analytical items for the live final (`../final-paper.md`). Duplicate-avoidance: none of these appear in quizzes, specimens, or the midterm bank.

## FE-A (scenario, 8 marks) · CLO-1,4 · Bloom: Analyze · Difficulty: Medium

A university lab network: one flat VLAN, student VMs with host-only internet via NAT, a file server, and an instructor console. Mid-semester, a student VM begins ARP-spoofing to intercept lab traffic.

**(a)** Which MITRE ATT&CK technique describes the ARP spoofing, and which STRIDE elements does it violate? **[2]**
**(b)** Give a segmentation + switching control set that detects and prevents this. **[3]**
**(c)** Which log entries would the control set produce, and where would they flow? **[3]**

**Key:** (a) T1557 (Adversary-in-the-Middle, ARP cache poisoning variant); Spoofing + Information Disclosure (accept Tampering). (b) Dynamic ARP inspection + DHCP snooping + separate instructor VLAN with private VLANs on student ports. (c) DAI drop logs and DHCP-snooping binding violations on the access switch → forwarded to syslog/SIEM with port metadata.

## FE-B (analytical, 10 marks) · CLO-5 · Bloom: Evaluate · Difficulty: Hard

A startup's threat model for customer data at rest: (1) AES-256-GCM volume encryption; (2) keys stored in the same volume's config file; (3) nightly backups copied unencrypted to object storage; (4) passwords hashed with SHA-256.

**(a)** Rank the four risks with justification. **[4]**
**(b)** Redesign: state the correct primitive or control for each and where the key must live. **[4]**
**(c)** One tradeoff the redesign introduces. **[2]**

**Key:** (a) Ranking defensible either way but must justify: (2) key co-location nullifies encryption (catastrophic); (3) unencrypted backup = full-data exposure outside the perimeter; (4) fast hash = credential dump→crack path; (1) GCM is sound. (b) KMS/HSM-held keys with envelope encryption; encrypt backups with independent keys + immutable access policy; Argon2id/bcrypt password storage; keep GCM with proper IVs. (c) KMS/HSM adds operational dependency/cost and latency; key-loss procedures become critical (accept reasoned tradeoffs).

## FE-C (data-driven, 10 marks) · CLO-6 · Bloom: Create · Difficulty: Hard

You are given 30 days of auth logs (synthetic course dataset): 5% labeled incidents. Design the anomaly pipeline end to end: feature engineering (3), model choice and validation protocol (3), precision/recall tradeoff for SOC handoff (2), and the top adversarial weakness (2).

**Key:** Features: per-user/entity login velocity, new-country/new-device flags, hour-of-day profile deviation, failure ratios. Model: isolation forest for unsupervised triage + supervised gradient boosting where labels exist; **time-based split** validation, never random. Tradeoff: threshold set by analyst capacity — maximize recall subject to precision floor (e.g., 0.5); present PR curve, not accuracy. Weakness: concept drift / attackers mimicking normal rhythms — needs drift monitoring + periodic retraining.

## FE-D (governance, 10 marks) · CLO-7,1 · Bloom: Evaluate · Difficulty: Hard

A department plans to adopt a cloud analytics platform processing student learning data (EU-style jurisdiction). Deliver: the DPIA skeleton (necessity, proportionality, risks, mitigations) (5), the shared-responsibility split for the platform (3), and one contractual control plus one technical control protecting the data (2).

**Key:** DPIA: lawful basis, necessity/data minimization, risk register (re-identification, sub-processor access, transfer), mitigations (pseudonymization, retention limits, DPA with sub-processor list, DPIA review trigger). Responsibility: provider = infra/patching/log integrity; department = IAM, data classification, retention, consent/lawful basis. Contractual: DPA with SCCs/audit rights; technical: encryption with department-held keys + access logging.

## FE-E (IR scenario, 10 marks) · CLO-8,3 · Bloom: Evaluate · Difficulty: Hard

Sunday 02:10: backup server shows 90% CPU; encrypted-extension files appear on two file shares; a ransom note names a leak site deadline.

**(a)** First three actions in order, each with the IR phase it belongs to. **[3]**
**(b)** Which evidence must survive your containment, and how? **[3]**
**(c)** The two decisions that must NOT be made by the responders alone. **[2]**
**(d)** One resilience metric to report to the board and how it changes backup design. **[2]**

**Key:** (a) Isolate affected segments (Detection/Containment); preserve volatile + log evidence before changes (Detection & Analysis); activate immutable/offline restore path (Containment→Recovery). (b) Memory images, ransom-note sample, BEC/email logs if phishing entry suspected, PCAP — hashed and logged in custody record. (c) Ransom payment and public disclosure — legal/insurer/executive. (d) RPO/RTO: drives offline-copy frequency and restore-test cadence.

## FE-F (open design, 10 marks) · CLO-8 · Bloom: Create · Difficulty: Expert

Design the detection stack for a 50-person SaaS: pick three detections you would build first, name the telemetry source for each, and defend the ordering against a team that says "buy a SIEM first." Constraints: 2 analysts, 12-month horizon.

**Key:** Full credit for defended ordering, e.g.: (1) identity anomalies (failed/odd-hour logins, MFA fatigue) from IdP logs — highest-frequency vector; (2) egress beacons/DNS anomalies from firewall/DNS logs — maps to C2; (3) cloud control-plane alerts (admin role changes) from audit logs. Argument: telemetry-first means the SIEM lands on curated, tested sources — buy vs build is a false binary; SIEM is the aggregation layer, detections are the content. Accept alternative orderings with equal rigor.

## FE-G (crypto applied, 8 marks) · CLO-5 · Bloom: Analyze · Difficulty: Medium

An API signs request tokens as `HMAC(secret, user_id + timestamp)`; the secret is shared across services; timestamps are not validated.

**(a)** Two exploitation paths enabled by these choices. **[4]**
**(b)** The corrected token design (format and verification steps). **[4]**

**Key:** (a) Replay (no freshness check); forgery/cross-service abuse (one leaked secret = all services; user_id enumeration → brute force). (b) Per-service derived keys (KDF), token = `HMAC(k, nonce || user_id || exp || scope)`, constant-time compare, exp/nonce replay cache, short TTL.

## FE-H (open-ended, 6 marks) · CLO-1 · Bloom: Evaluate · Difficulty: Medium

"Automation removes the need for security analysts." Take a position; support it with two concrete capabilities automation *cannot* replace from this course (name the lectures), and the one role automation most changes.

**Key:** Defensible either way; strongest case: automation scales detection (L15, L21–L24) but cannot replace adversarial reasoning/validation (L09–L10 analysis judgment), incident command/communication (L28, L31–L32), or governance accountability (L04, L28). Role changed: tier-1 triage shrinks; detection engineering grows.
