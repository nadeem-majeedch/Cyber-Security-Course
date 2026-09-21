# Quiz 10 — Checkpoint D (Week 10, L20) · Module 5: Cryptography
**Graded formative · recorded /10 · 12 minutes · CLO-5 · Closed book.**

1. An "encrypted" scan archive still shows the letterhead and repeated boilerplate in visual patterns when decrypted-viewed with the wrong key. Which block-cipher mode was almost certainly used, and what does it leak? **[1]**

2. Why does CBC require a *random* IV per message? One sentence. **[1]**

3. Name the construction class that provides confidentiality *and* tamper detection in one primitive, and the algorithm the course used for it. **[1]**

4. A certificate is presented during a TLS handshake. What does it bind, and who vouches for that binding? **[1]**

5. TLS 1.3 removed legacy cipher suites and changed the handshake. Give **two** security improvements over TLS 1.2 named in lecture. **[1]**

6. The course flagged CWE-330 in several past audits. What does this CWE describe, and give one concrete way it manifests. **[1]**

7. *(Scenario, 2 marks)* A developer stores session tokens as `MD5(user_id + fixed_secret)`. Identify **two** flaws and state the corrected design in one sentence.

8. *(Scenario, 2 marks)* A backup archive is encrypted, but the decryption key sits in a config file inside the same encrypted volume. Name the design failure and the corrected key-management pattern.

*Scoring: 1 mark per numbered item; recorded as a fraction of 10.*
