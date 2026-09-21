# Teaching Guide — Lecture 01 (Security Foundations)
**Instructor-only. Student notes: `lectures/module-01-fundamentals/lecture-01.md`. Session plan: `lecture-plans/lecture-01.md`.**

## Timing Plan (120 min)

| Time | Segment | Notes for delivery |
|---|---|---|
| 00–05 | Welcome, course contract | Read the ethics paragraph aloud — it sets the tone for 16 weeks. |
| 05–15 | Diagnostic poll | Ungraded; use results to calibrate Lab 00 pacing and the Lab 00 self-study pack. |
| 15–40 | CIA with anchor incidents | The three incidents are *framing devices*, not case studies: keep them generic ("a breach", "a tampering incident") to avoid unverifiable specifics. |
| 40–55 | Security/privacy/safety triangle | Board the triangle; make students place examples on it. |
| 55–60 | Break | — |
| 60–95 | Lab 00 orientation | Minimum viable outcome: every student has a snapshot taken. |
| 95–112 | Ethics: RoE + disclosure | Walk the RoE template line by line; students keep it — it returns in every lab. |
| 112–120 | One-minute paper + preview | Collect exit tickets (paper or form tool). |

## Board/Projector Activities

- **Board:** the asset→vulnerability→control triangle (photograph and post to LMS).
- **Projector:** the 8 classification scenarios (student notes §Classroom Activities); reveal answers one at a time.

## Speaker Notes (key beats)

1. Define each CIA property with one concrete harm each — resist the urge to add AAA/AuthN here; that comes in M2.
2. Risk = likelihood × impact is a *thinking tool*; say explicitly that we never compute precise numbers in this course.
3. The authorization-first rule is non-negotiable: state that any violation ends lab access (policy link).
4. Close the ethics block with the disclosure timeline diagram so the exit ticket's Q2 is answerable.

## Expected Student Difficulties

- **"Integrity vs. confidentiality"** confusion when an attack does both (leak + tamper). Fix: ask which harm *happened first*.
- Students conflate **threat** and **vulnerability**. Fix: the triangle board — threat is the actor-side, vulnerability the system-side.
- Non-coders in DS track may stall in Lab 00. Fix: pair-programming pairing for the orientation only.

## Teaching Tips

- Learn 10 names this session; cold-calling works later only on trust.
- If the diagnostic poll shows >30% without Linux basics, announce the Lab 00 self-study pack deadline (before L05) — do not improvise later.
- Keep the RoE template on one page; students must be able to reproduce its skeleton in the capstone.

## Answer Keys

- Scenario classifications: 1-I, 2-A, 3-C, 4-I, 5-A, 6-C, 7-I, 8-A (adjust to your card set; **[KEY]** — do not project in advance).
- Exit ticket: 1-I; 2 = coordinated/responsible disclosure required; 3 = free text, skim for RoE confusion.

## Lab Delivery (Lab 00 orientation)

- Verify host isolation settings before class (no shared folders, snapshot taken, fake-net configured).
- Minimum viable outcome: snapshot + environment checklist complete.
- Expected failure points: virtualization disabled in BIOS; license/network prompts. Have the troubleshooting card ready.

## Discussion Facilitation

Q1 is the warm-up (most students say availability; the backup twist teaches dependency of harms). Q2 is the ethics one — use think-pair-share, then anchor in the authorization rule. Do not let Q3 run long; park it.

## Accessibility

- The board triangle: describe verbally in full ("three vertices: confidentiality left, integrity top, availability right…") and post the photo.
- Poll tool: enable screen-reader mode; provide a paper alternative.
- Lab VM magnification/keyboard-nav per the manual §6.
