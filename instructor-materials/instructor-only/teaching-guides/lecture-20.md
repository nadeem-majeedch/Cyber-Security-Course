# Teaching Guide — Lecture 20 (Crypto Failures in the Wild + Checkpoint D)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap benchmark table | The ladder reads aloud. |
| 08–30 | Case 1: predictable RNG | Failure chain on the board; class writes the design rule. |
| 30–48 | Cases 2–3 pair dissection | Classify + one-line rule each; pairs present. |
| 48–60 | Break | — |
| 60–72 | **Checkpoint D** | 10 min + most-missed recap. |
| 72–95 | Lab 18 (vendor-claim review) | Three fictional pages; challenge questions. |
| 95–110 | Failure-pattern wall | Aggregate all M5 failures into the taxonomy. |
| 110–120 | M5 wrap + M6 preview | Bridge: "now we make the machines watch." |

## Board/Projector Activities

- **Board:** the failure-chain arrow diagram for case 1 (weak seed → predictable key → harvestable traffic); the four-class taxonomy grid filling through the session.
- **Handouts:** the three fictional vendor pages (deliberately plausible, with the red flags listed in the keys).

## Speaker Notes (key beats)

1. Frame the module's arc: primitives (L17) → trust (L18) → storage (L19) → *failures* (today). The taxonomy table is the deliverable.
2. "Don't roll your own" needs the honest version: vetted libraries, public protocols, and verification — someone builds it, you use it correctly.
3. Data-at-rest failures are migrations, not patches — connect to the L17 ECB migration exercise.
4. Vendor-page red flags: proprietary algorithm, unnamed mode, no randomness story, no KMS story, "military-grade."
5. After Checkpoint D: recap the two most-missed items (see keys) before the lab.

## Expected Student Difficulties

- Students hunt for the *algorithm* to be broken. Fix: the taxonomy — usage and key custody fail; primitives rarely do.
- CVE parsing intimidates. Fix: three CWE families cover most entries; read one CVE description together.
- The pattern wall may feel repetitive. Fix: it is deliberate consolidation — students propose each placement.

## Teaching Tips

- Fictional vendor pages: keep them plausible but clearly synthetic; never model them on real products (no defamation risk, no legal exposure).
- Case selection rule: only public write-ups with verifiable citations; no invented incidents, no unverifiable numbers — check links before each term.
- The wall (whiteboard or poster) stays up through the capstone — it is referenced in L29's backlog work.

## Answer Keys **[KEY]**

- Checkpoint D: see `assessments/instructor-only/checkpoint-keys.md` §D.
- Vendor-page red flags (expected finds): Page A "proprietary cipher, no third-party review" → ask for algorithm/mode/analysis; Page B "AES-256" no mode, static key per deployment → ask mode? nonce? key storage?; Page C "military-grade, bank-level" + no KMS → ask randomness, key lifecycle, agility.
- Exit ticket: 1 insufficient randomness; 2 re-encryption migration of stored data vs. code patch; 3 proprietary/secret algorithm with no public analysis.

## Lab Delivery (Lab 18)

- Minimum viable outcome: three challenge-question sets, one per vendor page.
- Expected failure points: questions too vague ("is it secure?") — require the four question slots: algorithm/mode, randomness, keys/lifecycle, agility/migration.

## Discussion Facilitation

Q1 (who builds crypto) is the module's philosophical close: name the real process (open proposals, public analysis, standards bodies) without hero worship. Q2 (data-at-rest vs code) previews migration planning — the DS-track example carries it.

## Accessibility

- Case studies: distribute in accessible formats; the failure-chain diagrams have text equivalents in the notes.
- The pattern wall: paired with the taxonomy table handout so wall-physicality never gates participation.
