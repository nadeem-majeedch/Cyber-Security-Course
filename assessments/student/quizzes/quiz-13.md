# Quiz 13 — Specimen (Week 13) · Adversarial ML & Cloud Security
**Ungraded self-check · 13 marks · ~12 minutes · CLO-6, CLO-7 · Answer key discussed in class; not posted.**

## Part A — Multiple choice (1 mark each)

**1.** An attacker appends crafted noise to a malware binary so the classifier flips it to benign. This is:
- A. Poisoning
- B. Evasion
- C. Extraction
- D. Inference

**2.** A threat feed lets the public submit "malicious" URLs used to retrain the corporate classifier. The primary risk:
- A. Storage costs
- B. Poisoning — mislabeled samples shift the decision boundary
- C. Slow retraining
- D. License violations

**3.** A public phishing-scoring API with unlimited queries primarily enables:
- A. Denial of service
- B. Model extraction via a locally trained substitute
- C. SQL injection
- D. Cookie theft

**4.** A detection rule fires 30 times/day with 2 true positives. Before blocking, the correct rollout:
- A. Block immediately — 93% precision is fine
- B. Shadow mode → measure FPR/TPR on live traffic → alert → block
- C. Escalate to the vendor
- D. Lower the threshold

**5.** In IaaS, patching the guest operating system is the responsibility of:
- A. The provider
- B. The customer
- C. The hardware vendor
- D. Nobody — VMs patch themselves

**6.** An IAM policy grants `Action: "*", Resource: "*"`. The immediate risk:
- A. Extra logging
- B. Full administrative compromise if that identity leaks
- C. Slow API responses
- D. Key rotation failures

**7.** The network perimeter is least useful in cloud environments because:
- A. Clouds have no firewalls
- B. Control-plane access is via authenticated APIs — valid credentials are "inside"
- C. VPCs are deprecated
- D. Latency is higher

## Part B — Short answer (6 marks)

**8.** (a) A phishing classifier's F1 drops 30% against slightly reworded URLs. Give two mitigations and one tradeoff of each (4).
(b) One sentence: why does "we're compliant, therefore secure" fail? (2)

---
*Specimen items are contaminated for grading use once shown. Review answers against the in-class key.*
