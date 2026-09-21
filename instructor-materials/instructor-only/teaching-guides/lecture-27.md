# Teaching Guide — Lecture 27 (Audit Trails, Detection, Misconfiguration Management)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: hardened spec diffs | Quick show-and-tell. |
| 08–30 | Audit-log anatomy | Five API events decoded; class finds the suspicious one. |
| 30–50 | Misconfiguration pipeline | IaC scan catch + console-drift story. |
| 50–60 | Break | — |
| 60–105 | Lab 25 (investigation) | Timeline → six questions → IaC + detection fixes. |
| 105–115 | Posture dashboard | Benchmark score before/after; what it hides. |
| 115–120 | Exit ticket + preview | Tease L28: "privacy turns this into compliance." |

## Board/Projector Activities

- **Projector:** the five API events (rendered as a table); the IaC scan catching the public bucket at PR time.
- **Board:** the timeline reconstruction grid (time × actor × action × evidence) filled by the class during the lab debrief.

## Speaker Notes (key beats)

1. The three log classes answer three questions: control-plane (who did what to infra), data-plane (who touched data), identity (who became whom).
2. Tamper resistance is architectural: the logging-account pattern — evidence lives where the compromised credential cannot reach (L14 segmentation, applied to truth).
3. IaC + policy-as-code + drift detection = the pipeline keeps its monopoly on change; every console click is drift.
4. Retention is a decision, not a default: data-plane logging is often opt-in; say the cost trade-off out loud.
5. Investigation = timeline from the log; the "root cause was a role" pattern.

## Expected Student Difficulties

- Students expect cloud logs to be comprehensive by default. Fix: the opt-in reality — show a service with data-plane logging off.
- The audit corpus is dense; students freeze. Fix: the decoding drill first (five events) — the lab uses the same fields at scale.
- Posture-score worship. Fix: the dashboard exercise — score before/after with the "what it hides" annotation (L24's caveat pattern).

## Teaching Tips

- The lab corpus must include the log-stop *attempt* — the failing attempt is the teaching moment (which control saved the evidence).
- Keep the six investigation questions fixed across terms; comparability helps calibration.
- The role-chain analysis (DS track) reuses L21 craft on cloud telemetry — name the reuse explicitly for track-bridging.

## Answer Keys **[KEY]**

- Decoding drill: suspicious event = role assumed from an unusual source IP without MFA context.
- Lab 25 timeline (model): t0 CI-runner identity compromised/abused → t1 AssumeRole to analytics role → t2 bucket policy mutated to public → t3 200 GB data-plane reads → t4 logging change attempted (fails: cross-account write-once) → t5 present. Leadership answers: who = the CI-runner identity via role assumption; what = the dataset prefix; contained = logging intact, policy reverted, role trust tightened.
- Exit ticket: 1 control-plane; 2 reality ≠ declared state — PR-only changes + policy-as-code/drift detection; 3 the compromised admin cannot erase the evidence.

## Lab Delivery (Lab 25)

- Minimum viable outcome: complete timeline + six answers + IaC fix + two detection rules (role anomaly, policy mutation).
- Expected failure points: students read events chronologically but miss the *identity chain* — prompt with "what did this identity become first?"; timeboxing the six questions (8 min each).

## Discussion Facilitation

Q1 (retention) is an economics argument: control-plane logs are small and high-value (1 year defensible); data-plane logs are large and lower-signal (shorter, sampled) — let them defend a split policy. Q3 (which control saved the logs) should end with the design-review question: "where do the logs go when everything else is compromised?"

## Accessibility

- The audit corpus: CSV/tabular access with column dictionary; the timeline grid exists as a spreadsheet template.
- Event decoding: field-by-field verbal walkthrough; the five events are short enough for full transcription in the notes.
