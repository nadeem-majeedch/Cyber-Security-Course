# Question Bank — Module 6 (L21–L24) · CLO-6 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q11 (W11), Q13 (W13), and makeup packs. Duplicate-avoidance rule: see `README.md`.

## MCQ-6.1

**Topic:** Class imbalance · **CLO-6** · **Bloom:** Analyze · **Difficulty:** Easy · **Week:** 11
**Used in:** Q11

A model reports 99.9% accuracy on network logs where attacks are 0.1% of rows. The correct interpretation:

- A. The model is production-ready
- B. Accuracy is misleading; the model may detect nothing — use precision/recall ✔
- C. The dataset is too large
- D. The model overfit the test set

**Explanation:** The majority-class baseline dominates accuracy; recall on the attack class is the real question. Key: B.

## MCQ-6.2

**Topic:** Isolation forest · **CLO-6** · **Bloom:** Understand · **Difficulty:** Medium · **Week:** 11
**Used in:** Q11

In an isolation forest, anomalies score highly because they:

- A. Have the most features
- B. Are isolated by few random splits (short average path length) ✔
- C. Appear most often in training
- D. Have the largest clusters

**Explanation:** Outliers separate quickly in random partitioning; the `contamination` parameter sets expected anomaly share. Key: B.

## MCQ-6.3

**Topic:** Phishing features · **CLO-6** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 11
**Used in:** Q11

Which feature pair is most robust for phishing URL classification?

- A. Total URL length and count of `@` — combine with age of domain registration ✔
- B. Presence of the word "login" only
- C. HTML color count
- D. Random email body words

**Explanation:** Structural + registration-age features generalize; lexical hints alone are trivially changed by attackers. Key: A.

## MCQ-6.4

**Topic:** Data leakage · **CLO-6** · **Bloom:** Analyze · **Difficulty:** Hard · **Week:** 11
**Used in:** Q11

Random train/test splits on time-ordered security logs corrupt evaluation because:

- A. Logs are too big
- B. Near-duplicate and temporal events leak across the split, inflating scores ✔
- C. Trees cannot handle timestamps
- D. SHAP values become negative

**Explanation:** Temporal leakage: future-pattern training on past-labeled duplicates gives unrealistically high F1 — split by time. Key: B.

## MCQ-6.5

**Topic:** Evasion · **CLO-6** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 13
**Used in:** Q13

An attacker appends carefully crafted noise to a malware binary so the classifier flips to benign. This is:

- A. Poisoning
- B. Evasion ✔
- C. Extraction
- D. Inference

**Explanation:** Evasion = perturb input at inference; poisoning = corrupt training data. Key: B.

## MCQ-6.6

**Topic:** Poisoning · **CLO-6** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 13
**Used in:** Q13

A threat feed lets the public submit "malicious" URLs for retraining the corporate classifier. The primary risk:

- A. Storage costs
- B. Poisoning — attackers inject mislabeled samples to shift the decision boundary ✔
- C. Slow retraining
- D. License violations

**Explanation:** Unvetted crowd labels are an untrusted training-data channel; validate and weight sources. Key: B.

## MCQ-6.7

**Topic:** Model theft · **CLO-6** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 13
**Used in:** Q13

A public phishing-scoring API with unlimited queries primarily enables:

- A. DoS
- B. Model extraction — training a local substitute from API outputs ✔
- C. SQL injection
- D. Cookie theft

**Explanation:** Query access allows boundary reconstruction; rate-limiting and output-noise mitigate. Key: B.

## MCQ-6.8

**Topic:** Detection engineering · **CLO-6** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 13
**Used in:** Q13

A detection rule fires 30 times/day with 2 true. Before blocking, the correct rollout is:

- A. Block immediately — 93% precision
- B. Shadow mode, measure FPR/TPR on live telemetry, then alert, then block ✔
- C. Send to vendor
- D. Lower the threshold

**Explanation:** Staged rollout quantifies risk on real traffic before enforcement. Key: B.

## SA-6.1 (short answer, 6 marks)

**Topic:** SOC detector design · **CLO-6** · **Bloom:** Create · **Difficulty:** Medium · **Week:** 11
**Used in:** Q11

Design a brute-force detector: features (2), why precision matters here (2), one adversarial response it must survive (2).

**Key:** Features: failed-login counts per (user, source) in windows, time-of-day deviation, distinct usernames per source. Precision matters: analyst trust erodes and accounts lock out users on FPs. Adversarial response: slow-distributed attempts across IPs/hours — needs aggregate + velocity features, not per-attempt rules.

## SA-6.2 (short answer, 4 marks)

**Topic:** Adversarial ML mitigations · **CLO-6** · **Bloom:** Evaluate · **Difficulty:** Hard · **Week:** 13
**Used in:** makeup MT-7 only

A phishing classifier's F1 drops 30% against slightly reworded URLs. Give two mitigations and the tradeoff of each.

**Key:** Adversarial training with perturbed samples (costs retraining cycles; raises robustness on known perturbation families); feature hardening toward structural/behavioral signals (loses some lexical signal, resists trivial rewording); accept input sanitization/normalization with drift monitoring.
