# Quiz 11 — Specimen (Week 11) · Applied Crypto Failures & ML Detection
**Ungraded self-check · 13 marks · ~12 minutes · CLO-5, CLO-6 · Answer key discussed in class; not posted.**

## Part A — Multiple choice (1 mark each)

**1.** A checksum alone fails to prove a download is authentic because:
- A. Checksums are slow to compute
- B. An attacker who replaces the file can recompute and publish a matching checksum
- C. Checksums expire
- D. Large files cannot be hashed

**2.** The correct password-storage choice for a new web app:
- A. SHA-256 with a per-user salt
- B. Argon2id (or bcrypt) with a tuned work factor and per-user salt
- C. AES-256 encryption of the password
- D. MD5 with a pepper

**3.** Per-user salts primarily defeat:
- A. Phishing
- B. Precomputed rainbow-table attacks and cross-user password deduplication
- C. Side-channel attacks
- D. Session hijacking

**4.** A model reports 99.9% accuracy where attacks are 0.1% of rows. The correct interpretation:
- A. The model is production-ready
- B. Accuracy is misleading; the model may detect nothing — inspect precision/recall
- C. The dataset is too large
- D. The model overfit

**5.** In an isolation forest, anomalies score highly because they:
- A. Have the most features
- B. Are isolated by few random splits (short average path length)
- C. Appear most often in training
- D. Form the largest clusters

**6.** Random train/test splits on time-ordered logs corrupt evaluation because:
- A. Logs are too big
- B. Near-duplicate and temporal events leak across the split, inflating scores
- C. Trees cannot parse timestamps
- D. SHAP values turn negative

## Part B — Short answer (7 marks)

**7.** Design a brute-force detector for SSH logins:
- (a) Two features you would engineer (2)
- (b) Why precision matters for this detector specifically (2)
- (c) One adversarial behavior it must survive and the feature change that addresses it (2)
- (d) One sentence: why not optimize accuracy? (1)

---
*Specimen items are contaminated for grading use once shown. Review answers against the in-class key.*
