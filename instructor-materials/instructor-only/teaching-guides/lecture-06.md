# Teaching Guide — Lecture 06 (Injection Attacks)
**Instructor-only. Safety note: all exploitation practice is confined to the sandboxed course target; say this aloud at the start and at the break.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap exit ticket | Answers on board; credit the HTTP sequence diagram. |
| 08–35 | Teaching demo | Vulnerable vs parameterized login side by side; walk the taint path in code. |
| 35–55 | Injection family tour | One slide per family with its CWE; keep payload theory brief. |
| 55–60 | Break | Repeat the sandbox-only rule here. |
| 60–105 | Lab 05 (confirm → fix → verify) | Pairs; each pair owns one seeded sink. |
| 105–115 | Code review | Project two student fixes; class hunts residual sink paths. |
| 115–120 | Exit ticket + preview | Tease L07: "input can also become markup, requests, URLs, identity." |

## Board/Projector Activities

- **Projector:** the side-by-side query demo (concatenated vs prepared) run against the lab target only.
- **Board:** taint-flow diagram drawn for the first sink; students redraw it for their own sink in the lab.

## Speaker Notes (key beats)

1. The single sentence that organizes the lecture: *injection is data interpreted as code*.
2. Parameterization wins because it separates structure from data *at the protocol level* — not because it filters characters.
3. Demo the boolean-blind pattern conceptually (page answers yes/no); do not teach extraction tooling — detection and defense are the course's business.
4. Command injection: the fix is API shape (`shell=False`, list args), then allow-lists; least-privilege DB/shell accounts limit blast radius.

## Expected Student Difficulties

- Students want to run scanners before understanding taint flow. Fix: the lab requires the drawn taint path before any probing step.
- "ORM = safe." Fix: show the raw-query escape hatch in the lab repo.
- DS students may feel this is "not their topic." Fix: the notebook `pip install` example is deliberately theirs — say so.

## Teaching Tips

- Keep payload discussion at pattern level (this keeps the course defensive and reduces notes-as-weaponization risk).
- The verify step (fix blocks the original probe) is the pedagogical core — do not let pairs skip it when time is short; cut the third sink instead.
- During code review, pick one *good* fix and one *almost-right* fix; kindness keeps volunteers coming.

## Answer Keys **[KEY]**

- Seeded sinks: search (string-concat LIKE), login (boolean-blind), export filename (shell). Fixes: prepared statement ×2; list-form subprocess + allow-listed filename pattern.
- Expected probe log line: repeated requests with `' OR` patterns to the search param — accept equivalent signatures.
- Exit ticket: 1 CWE-89 / CWE-78; 2 metacharacter interpretation; 3 least-privilege account (accept error hygiene).

## Lab Delivery (Lab 05)

- Minimum viable outcome: one sink confirmed → fixed → verified with screenshots.
- Expected failure points: students test against production URLs by habit — stop it immediately and re-anchor the sandbox rule; DB reset needed if someone breaks the schema (reset script in `starter/`).

## Discussion Facilitation

Q2 (ORM escape hatches) is the misconception-killer — have the lab repo's raw-query line ready to show. Q3 (WAF last): use the encoding-variant point, not vendor talk.

## Accessibility

- Live-coding demo: share the final code file after class (screen-reader friendly) rather than only board photos.
- Boolean-blind explanation: pair the behavioral description with a written truth-table example for students who can't follow the rapid page changes.
