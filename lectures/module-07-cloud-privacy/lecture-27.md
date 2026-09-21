# Lecture 27 — Cloud Security III: Audit Trails, Detection, and Misconfiguration Management
**Module 7 · Week 14, Session 1 · 2 hours · CLO-7**

## Learning Objectives
1. Design a cloud audit pipeline: log classes, retention, tamper resistance.
2. Detect misconfiguration continuously: IaC scanning at PR time, drift detection, posture benchmarks.
3. Investigate a cloud-native incident using audit logs.
4. Connect cloud telemetry to SIEM triage (L15) and metrics discipline (L24).

## Key Concepts and Definitions

**Log classes:**

| Class | Answers | Examples |
|---|---|---|
| **Control-plane** | "Who did what to the infrastructure?" | API events: principal, action, resource, source, MFA context |
| **Data-plane** | "Who touched the data?" | Object reads/writes, query logs |
| **Identity events** | "Who became whom?" | Role assumptions, key creation, policy changes |

**Tamper resistance:** logs must survive the compromise of the credentials they record — the **separate logging account/pattern**: logs land where a compromised admin *cannot* delete them (cross-account, write-once retention). This is L14's segmentation thinking applied to evidence.

**IaC as the source of truth:** infrastructure declared in code, changed only by pull request. **Policy-as-code** scans templates at PR time (public bucket? blocked). **Drift** = deployed reality ≠ declared state (someone clicked "fix it in the console") — drift is an organizational failure first: the pipeline lost its monopoly on change.

**CSPM (cloud security posture management, concept):** continuous checks of the estate against benchmarks (CIS); severity weighted by exposure (public? internet-reachable?).

**Investigation pattern:** reconstruct the timeline from control-plane logs — who assumed which role, from where, with what MFA state, doing what — the "root cause was a role" pattern.

## Conceptual Diagram

```text
PR ─► policy-as-code scan ─► merge ─► deploy ─┬─► runtime posture checks (CSPM)
                                              └─► drift detector (console change?)
control-plane logs ─► separate logging account (write-once) ─► SIEM (L15 pipeline)
investigation: AssumeRole chain ─► actions ─► data-plane reads ─► timeline
```

## Realistic Examples

- **CS track:** the logging-account pattern sketch: trust boundaries drawn so the compromised admin credential cannot reach the evidence — "who audits the auditors," answered architecturally.
- **DS track:** audit logs as a dataset: rare-event analysis of `AssumeRole` chains — compute the five most common role chains in a month of logs; the anomalous sixth one is the incident (reuses L21's craft on cloud telemetry).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Cloud logs everything by default, forever" | Data-plane and verbose logging are usually *opt-in*; retention is a paid decision you must make. |
| "The console is just for emergencies" | Every console change is drift — undeclared, unreviewed, unscanned. |
| "Posture scores = security" | A benchmark score measures configuration posture, not detection quality or identity hygiene (L24's caveat again). |
| "Logs in the same account are fine" | Compromised admin credentials can then erase the evidence of their own use. |

## Classroom Activities

1. **Event decoding (15 min):** decode five API events (principal/action/resource/source/MFA); students call the suspicious one.
2. **IaC scan demo (10 min):** a public-bucket template caught at PR time; then the console-drift story.
3. **Lab 25 (45 min):** investigation lab — provided audit corpus (role assumed → bucket exfil → log-stop attempt): build the timeline, answer six investigation questions, write the IaC + detection fixes.

## Discussion Questions

1. Retention costs money: build the argument for 90 days vs. 1 year for control-plane logs.
2. Why is drift an organizational failure more than a technical one?
3. The attacker tried to disable logging and failed — which control made that fail, and why does it belong in every design review?

## Problem-Solving Exercise

> Monday: a bucket shows 200 GB read by a role that normally reads nothing; logs show an `AssumeRole` from a CI runner identity, then a brief policy change making objects public.
> **Deliverable:** the minute-by-minute timeline; answers to the three leadership questions (who, what data, contained?); the IaC fix; two detection rules (role anomaly, policy mutation).

## Summary

The cloud gives you perfect logs and perfect ways to misconfigure — the discipline is making the pipeline the only path to change and the log the source of truth, stored where the attacker cannot reach it. Next: the privacy layer that turns security into compliance.

## Exit Ticket

1. Which log class answers "who deleted the bucket"?
2. What is drift, and which two practices prevent it?
3. Why put logs in a separate account?

## References

- NIST SP 800-210 / SP 800-190 (context for cloud access and workload security). https://csrc.nist.gov
- CIS Benchmarks (posture baseline). https://www.cisecurity.org
- Provider documentation: audit-log services (per chosen cloud). 
- NIST SP 800-61 Rev. 2 (investigation flow). https://csrc.nist.gov
