# ⚠️ INSTRUCTOR-ONLY — Midterm Paper (Week 8, L16)

**90 minutes · 50 marks · 15% of course grade · CLO-1–CLO-4 · Closed book · Variant B swaps marked items.**
Assemble the paper from `question-bank/QB-MT.md` + the MCQ pool below. Do not source any item from the Q8 specimen or weekly quizzes.

## Paper structure

| Section | Items | Marks | CLO |
|---|---|---|---|
| A — MCQ | 10 × 1 | 10 | 1–4 |
| B — Short scenario | MT-A, MT-B (or MT-F) | 12 | 1, 4, 2 |
| C — Scenario analysis (choose 2 of 3) | MT-C, MT-E, MT-G (Variant B swaps per bank table) | 16 | 2, 3, 4 |
| D — Synthesis | MT-H (or Variant B dilemma) | 8 | 1 |
| **Total** | | **46** | + 4 marks for Section A quality |

## Section A MCQ pool (10 to be drawn; keys inline)

1. Which CIA property does a MAC (message authentication code) primarily assure? — **Integrity/authenticity** (C).
2. STRIDE element countered by rate-limiting a login endpoint — **DoS** (D).
3. ATT&CK "Procedure" vs "Technique" — a specific actor's implementation of a technique — (B).
4. Control type of a bollard — **Preventive/physical** (A).
5. Biggest attack-surface reducer — **removing the feature** (C).
6. Fix for `f"SELECT … {uid}"` — **parameterization** (B).
7. `HttpOnly` mitigates — **token theft via XSS** (A).
8. First static triage artifact — **hash + TI lookup** (D).
9. First-match rule processing → order rules — **specific before general** (C).
10. Sensor placement for lateral movement — **inter-zone choke points** (B).

Distractors reused from the misconception bank in each module's teaching guide.

## Marking scheme (Sections B–D)

- **MT-A (6):** (a) 2 (technique + discovery), (b) 2 (isolation that preserves memory; accept switch-port shutdown), (c) 2 (preventive + detective, each mapped to a STRIDE element).
- **MT-B (6):** zones 1, rules 3 (1 each, must be least-privilege), logging point + justification 2.
- **MT-C (8):** 2 per flaw — 1 CWE + 1 fix; ranking 2 embedded (any defensible order with justification). *Half marks for correct CWE with wrong fix.*
- **MT-E (6):** (a) 3 (1 per technique), (b) 2 (memory + persistence config, accept PCAP), (c) 1.
- **MT-F (6):** send-vs-read distinction 3, CORS irrelevance 1, two defenses 2.
- **MT-G (8):** (a) 4 (characterization + cited evidence), (b) 2, (c) 2 (order matters: isolate → block → preserve).
- **MT-H (8):** rubric-scored: risk-based argument 3, forgone benefit named 2, formal residual acceptance 2, quality 1. **Accept either position** — mark the reasoning.

## Variant B assembly

Per the swap table in `QB-MT.md`: replace MT-C with the NoSQL/command-injection excerpt, MT-G with the DNS-tunneling capture, MT-H with the backups-vs-segmentation dilemma. Same marks; mark schemes transfer 1:1.

## Logistics

- Seating plan with empty seats between students; two invigilators per 60 students.
- Equation-free paper; calculators unnecessary; no devices.
- Scripted announcement: "choose TWO of three in Section C — mark all three and only the first two count."
- Item analysis: record per-item facility (p-value) and discrimination for the three lowest items to feed next-term's bank review.
