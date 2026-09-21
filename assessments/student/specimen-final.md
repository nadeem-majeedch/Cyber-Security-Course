# Specimen Final (Week 16 practice) — Cyber Security
**Practice paper · 120 minutes equivalent · 60 marks · All modules (CLO-1–CLO-8) · Questions only — the live final has different items; format and mark allocation match exactly.**

## Section A — Multiple choice (10 × 1 mark)

1. In IaaS, patching the guest OS is the responsibility of:
   A. The provider B. The customer C. The hardware vendor D. The regulator

2. Which log answers "who deleted the bucket"?
   A. Flow logs B. Control-plane audit logs C. LB access logs D. DNS logs

3. The strongest control against a leaked long-lived access key:
   A. 90-day rotation B. No static keys — role-assumed short-lived credentials C. Key naming D. Billing alerts

4. The NIST 800-61 phase containing eradication:
   A. Preparation B. Containment/Eradication/Recovery C. Detection & Analysis D. Post-Incident

5. Order of volatility — collect first:
   A. Disk B. RAM C. Backups D. Archives

6. TLS 1.3 session keys derive from:
   A. The certificate B. Ephemeral (EC)DH shared secrets C. The IV D. The MAC

7. GCM is preferred over CBC+HMAC because it:
   A. Uses smaller keys B. Provides authenticated encryption in one operation C. Needs no IV D. Is post-quantum

8. At 0.1% prevalence, the metric most honest for a detector is:
   A. Accuracy B. Precision/recall (PR curve) C. Training loss D. R²

9. Appending crafted noise so a classifier flips a sample to benign is:
   A. Poisoning B. Evasion C. Extraction D. Inference

10. A DPIA is triggered by processing that is:
    A. Cloud-hosted B. Likely high-risk to individuals C. Larger than 1 TB D. Encrypted

## Section B — Short scenario answers (2 × 6 marks)

**11.** A lab VM beacons to one IP every 60 s, creates task `SyncMgr`, and runs `svchost.exe` from `%TEMP%`. Name the ATT&CK techniques, the first artifacts you would collect, and why the VM stays powered but disconnected.

**12.** A user invokes erasure of their data. Name two other rights to verify and the two stores most likely to block compliance; state the practical rule for backups.

## Section C — Scenario analysis (choose 2 of 3 × 10 marks)

**13.** *Crypto redesign.* A startup: AES-GCM volume encryption; keys in a config file on the same volume; unencrypted nightly backups to object storage; SHA-256 password hashing. Rank the four risks with justification, redesign each with the correct primitive/control and key location, and name one tradeoff.

**14.** *IR at 02:10.* The backup server spikes to 90% CPU; encrypted extensions appear on two shares; a ransom note names a leak-site deadline. Give the first three actions with their IR phases, the evidence that must survive containment and how, the two decisions that responders must *not* make alone, and one resilience metric that would have changed the design.

**15.** *Detection pipeline.* Given 30 days of synthetic auth logs (5% labeled incidents): engineer three features, choose a model and validation protocol, set the precision/recall tradeoff for SOC handoff, and name the top adversarial weakness with its mitigation.

## Section D — Synthesis essay (8 marks)

**16.** "Automation removes the need for security analysts." Take a position; support it with two concrete capabilities automation cannot replace (name the course modules), and name the one role automation most changes.

---
*Marking guide mirrors the live paper. Full marks in Section C require ordered response steps, named primitives/phases, and explicit tradeoffs. Model answers are discussed in the Week 16 tutorial before the exam slot.*
