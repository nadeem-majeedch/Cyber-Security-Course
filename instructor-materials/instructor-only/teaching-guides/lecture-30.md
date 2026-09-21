# Teaching Guide — Lecture 30 (Capstone Build Sprint I)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–10 | Sprint rules | Demo-or-it-didn't-happen; descope log visible. |
| 10–60 | Build block 1 | Implement; floating desk-checks; on-demand mini-lectures. |
| 60–65 | Break | — |
| 65–100 | Build block 2 | Detection wiring + evidence capture. |
| 100–112 | Demo checkpoint | 3-min stand-ups; one control + one detection each. |
| 112–120 | Scope adjustment | Descope log; L31 expectations. |

## Board/Projector Activities

- **Board:** the descope log (public, running); the desk-check schedule (teams × times).
- **Projector:** reserved for the demo checkpoint (team laptops to main screen).

## Speaker Notes (key beats)

1. The completion criterion is *verified implementation* — before/after probes, not "it compiles."
2. Evidence capture as-you-go: screenshots with visible clock, transcripts saved, test outputs filed. Reconstructed evidence is worthless.
3. Desk-checks: compare against the filed contract; blockers surfaced now are recoverable, blockers in L32 are not.
4. Descope = decision + residual risk + acceptor. The log is public — that visibility is the integrity mechanism.
5. Mini-lectures on demand: the CSP-breaks-X and IAM-too-narrow moments are teachable to the whole class when they arise naturally.

## Expected Student Difficulties

- Teams rabbit-hole on one hardening item. Fix: desk-check asks "show me two items progressing, not one perfect."
- Detection dashboards stay silent. Fix: the test-event habit (L24) — fire a synthetic event to prove the wire works.
- Evidence chaos by week's end. Fix: a shared evidence folder per team with a naming convention (contract attachment).

## Teaching Tips

- Float with the rubric in hand; verbal desk-check notes recorded immediately (memory fails by the third team).
- The seeded brute-force test event exists in the environment for the DS detection demo — tell one team member per team where it is.
- Watch for over-helping: guide questions ("what would verify this?") rather than solutions.

## Answer Keys **[KEY]**

- Expected demo pairs: CS — injection probe fails post-fix (before/after screenshots); DS — brute-force test event alerts on the auth-log dashboard (threshold documented).
- Desk-check sheet criteria: contract item → evidence artifact → verification method → blocker (if any). Two items progressing = on track.
- Descope-log model entry: item, reason (budget/technical), residual risk one-liner, acceptor role, compensating option.

## Lab Delivery (capstone environment)

- Minimum viable outcome: one verified control + one firing detection per team + descope log started.
- Expected failure points: environment capacity (teams × services) — pre-provision; credential resets mid-sprint — reset tokens staged.

## Discussion Facilitation

Q2 (verification for untestable controls) is the honest-evidence conversation: partial artifacts (config diff + unit-level test + rationale) beat fake end-to-end claims; name the standard now so L32 defenses meet it.

## Accessibility

- Stand-up demos: teams may present seated or from their own laptop screens; no requirement to use the projector.
- Desk-checks: written feedback copy to each team (not verbal only) — helps all, essential for some.
- Sprint timing: the contract's extended-time provisions apply; teams with accommodations may shift block boundaries.
