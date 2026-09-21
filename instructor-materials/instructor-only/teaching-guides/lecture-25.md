# Teaching Guide — Lecture 25 (Shared Responsibility & IAM)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–10 | Hook: misconfiguration headline set | Real, citable headline themes; no invented numbers. |
| 10–30 | Responsibility matrix build | Students fill IaaS/PaaS rows; boundary failures highlighted. |
| 30–52 | IAM workshop | Policy JSON anatomy; least-priv vs wildcard twin diffed live. |
| 52–60 | Break | — |
| 60–105 | Lab 23 (sandbox org audit) | Map → escalate-paths → rewrite → verify. |
| 105–115 | Incident replay | The cited case mapped to today's concepts. |
| 115–120 | Exit ticket + preview | Tease L26: "the compute itself." |

## Board/Projector Activities

- **Projector:** the sandbox org's policy list (six identities, ten policies); the can-I-do-X script output.
- **Board:** the escalation map drawn as a graph (identities → assumable roles → modifiable policies).

## Speaker Notes (key beats)

1. The boundary moves with the service model — teach the matrix by *building* it, not presenting it.
2. The empirical pattern: public incidents are customer-side configuration failures; the provider's layer is rarely the story.
3. Policies are JSON sentences; wildcards on wildcard = everything. The twin-diff demo makes least privilege concrete.
4. Escalation thinking: the audit question is "what can this identity *become*?" — roles, self-modification, credential-bearing buckets.
5. Roles over static keys: short-lived, revocable, assumable — the L19 secrets thread concludes here.

## Expected Student Difficulties

- Students think cloud = "secure by default." Fix: the headline hook + the matrix — your rows are your incidents.
- Policy JSON syntax slows non-cloud students. Fix: the starter's policy templates are commented; syntax is copy-adapt, not write-from-memory.
- Escalation paths are missed without a method. Fix: the three-question walk (what can it assume? what can it change? what does it hold?).

## Teaching Tips

- Choose a post-mortem with a verifiable public timeline for the replay; verify links each term (reference-recency rule).
- The can-I-do-X verification script turns "I think it's fixed" into evidence — teach the script before the lab.
- Keep SSO concentration discussion short; it returns properly in L27's logging-account pattern.

## Answer Keys **[KEY]**

- Sandbox org escalation paths (expected): notebook role `s3:*` (data path); CI role assumable-by-user (pipeline→prod path); contractor's static keys never rotated (staleness path). Rewrites: prefix/action-scoped policies, trust conditions on assume-role, rotation+short-lived tokens.
- Exit ticket: 1 the provider; 2 every action on every resource — copy-paste/console defaults; 3 short-lived, revocable (accept: assumable, auditable).

## Lab Delivery (Lab 23)

- Minimum viable outcome: who-can-do-what map + ≥ 3 escalation paths + 2 rewritten policies verified by script.
- Expected failure points: sandbox credentials expiry mid-lab (refresh script provided); students rewrite policies but skip verification — the script run is the deliverable.

## Discussion Facilitation

Q2 (SSO trade-off) previews the logging-account answer: concentration is acceptable *when detection and recovery are designed for it*. Q3 (who audits the auditors) is a governance seed — collect answers; L27 gives the architectural one.

## Accessibility

- Policy JSON: syntax-highlighted printouts with line numbers; the audit works from text.
- The matrix: provided as a fillable table (CSV/spreadsheet) with the same rows/columns as the board version.
