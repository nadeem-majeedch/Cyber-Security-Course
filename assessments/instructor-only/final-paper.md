# ⚠️ INSTRUCTOR-ONLY — Final Paper (Week 16, L32)

**120 minutes · 60 marks · 10% of course grade · all CLOs · Closed book · Variant B swaps marked items.**
Assemble from `question-bank/QB-FE.md` + the MCQ pool below. No item may repeat quizzes, specimens, or the midterm.

## Paper structure

| Section | Items | Marks | CLO |
|---|---|---|---|
| A — MCQ | 10 × 1 | 10 | all |
| B — Short scenario | FE-A, FE-G | 14 | 1,4,5 |
| C — Scenario analysis (choose 2 of 3) | FE-B, FE-C, FE-E (Variant B: FE-C → FE-F) | 20 | 5,6,7,8 |
| D — Synthesis | FE-D and FE-H (both, short-form) | 16 | 7,1,8 |
| **Total** | | **60** | |

## Section A MCQ pool (10 to be drawn; keys inline)

1. Responsibility for guest-OS patching in IaaS — **customer** (B).
2. Log answering "who deleted the bucket" — **control-plane audit** (B).
3. Strongest anti-leak control for access keys — **no static keys** (C).
4. NIST 800-61 phase with eradication — **Containment/Eradication/Recovery** (B).
5. Order of volatility, first collect — **RAM** (B).
6. TLS 1.3 session keys derive from — **ephemeral (EC)DH** (B).
7. AEAD advantage of GCM — **authenticated encryption in one op** (C).
8. Honest detector metric at 0.1% prevalence — **precision/recall** (B).
9. Crafted noise flipping a classifier — **evasion** (B).
10. DPIA trigger — **likely high risk to individuals** (C).

## Marking scheme (Sections B–D)

- **FE-A (8):** technique 2, control set 3 (detect + prevent required), logs/flow 3.
- **FE-G (8):** (a) 4 (replay 2, cross-service forgery/enumeration 2), (b) 4 (per-service keys, freshness, constant-time compare, short TTL — 1 each).
- **FE-B (10):** (a) 4 — any defensible ranking with justification; co-location must rank top-tier, (b) 4 — KMS/HSM envelope, encrypted backups + immutability, Argon2id/bcrypt, keep GCM (1 each), (c) 2 — operational dependency/latency/key-loss procedure.
- **FE-C (10):** features 3 (1 each, windows required), model + **time-based split** 3, threshold/SOC tradeoff 2 (PR curve argument), adversarial weakness 2 (drift/mimicry).
- **FE-E (10):** (a) 3 (1 per action, phase named), (b) 3 (memory/notes/PCAP with hashing + custody), (c) 2 (ransom + disclosure — legal/insurer/exec), (d) 2 (RPO/RTO → offline-copy cadence).
- **FE-F (10):** three detections 3 (telemetry named), ordering defense 4, buy-vs-build reasoning 2, constraints respected 1.
- **FE-D (10):** DPIA skeleton 5 (necessity, proportionality, risks, mitigations — 1.25 each or holistically), responsibility split 3, contractual + technical control 2.
- **FE-H (6):** position 1, two non-replaceable capabilities with module references 2×1.5, changed role 2. Accept either stance; mark the argument.

## Variant B assembly

Swap FE-C → FE-F in Section C (detection-stack design). Everything else identical; mark schemes unchanged.

## Logistics

- Same seating/invigilation rules as the midterm; the capstone showcase is the same day — schedule the exam slot first, defenses after, per the L32 plan.
- Scripted announcement: Section C choose-two rule; D requires **both** items.
- Grade-board bundle: item analysis, capstone floor flags (see `capstone-rubric.md` §Moderation), and integrity referrals.
