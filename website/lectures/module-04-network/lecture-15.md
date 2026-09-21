# Lecture 15 — IDS/IPS and SIEM: Detection and Alert Triage
**Module 4 · Week 8, Session 1 · 2 hours · CLO-4**

## Learning Objectives
1. Contrast signature-based and anomaly-based detection, including failure modes.
2. Read and author Snort/Suricata-style rules; explain rule anatomy.
3. Triage a SIEM alert queue with enrichment, verdicts, and documentation.
4. Define detection-quality metrics and apply them to a rule set.

## Key Concepts and Definitions

**IDS vs. IPS:** passive detection (a copy of traffic) vs. inline prevention (traffic flows through). Placement decides what you see — an IDS behind the VPN concentrator never sees the internet-side handshake. IPS adds risk: a wrong rule blocks legitimate traffic.

**Signature detection:** known patterns + protocol context. Fails on *novelty*. Its economics: signatures are cheap to run and noisy when poorly scoped.

**Anomaly detection:** baselines of normal, alerts on deviation. Fails on **drift** (normal changes; the baseline rots) and on attacks that *are* small deviations. This is the conceptual on-ramp to Module 6's ML.

**Suricata-style rule anatomy:**

```text
alert http $EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS (msg:".."; content:".."; sid:1000001; rev:1;)
│ action │ proto │ src ──► dst │ options: msg, content, flow, thresholds, sid
```
`sid` = rule identity (local range conventions); `rev` bumps on edits. Rule quality is scoping: narrow `$HOME_NET` beats `any`.

**SIEM pipeline:** log sources → normalization → correlation rules → triage queue. **Enrichment** turns an IP into a decision: asset criticality, user context, threat-intel verdict. Verdicts: **TP** (true positive), **FP** (false positive), **BTP** (benign true positive — the behavior is real and sanctioned).

**Metrics that matter:** TPR/FPR **per rule** (not fleet-wide averages), ATT&CK **coverage** by tactic (what you can even see), and dwell time. Coverage is a *visibility* claim, not a protection claim.

## Conceptual Diagram

```text
logs ──► normalize ──► correlation rules ──► queue ──► analyst
                            ▲                    │ enrich (asset, user, TI)
                 rules from hypotheses (L03)       ▼
                                          TP → incident  FP → tune rule
                                          BTP → document & suppress (justified)
```

## Realistic Examples

- **CS track:** a rule for SSH brute force (**T1110**): threshold on repeated auth failures to one account; the false-positive sources are misconfigured service accounts — students name them before testing.
- **DS track:** the triage queue as a labeled dataset: alert features → disposition; how would an ML classifier pre-sort the queue, and what happens to analyst skill if it silently degrades (the L23/L24 thread begins)?

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "We bought a SIEM, so we detect" | A SIEM is a pipeline; without hypotheses, rules, and tuning it is an expensive log shelf. |
| "More alerts = more security" | Alert budgets are real: unworkable queues hide true positives. |
| "Blocking (IPS) is strictly better" | Wrong inline rules take production down; shadow-mode first, block later. |
| "100% ATT&CK coverage is achievable/meaningful" | Coverage measures visibility per tactic; it says nothing about rule quality or tuning. |

## Classroom Activities

1. **Rule authoring (20 min):** write one rule for the L13 scan pattern; test it against the capture immediately.
2. **Lab 14 (40 min):** SIEM triage simulation — 12 seeded alerts (TP/FP/BTP mix); enrichment; dispositions documented.
3. **Metrics calculation (10 min):** compute the queue's TPR/FPR against the answer sheet; find the coverage gap.

## Discussion Questions

1. Inline IPS blocks — what happens when the rule is wrong? Design the "safe blocking" policy.
2. Your coverage map shows an Exfiltration gap. Do you add log sources, rules, or both — and what does each cost?
3. Auto-closing low-severity alerts: what is gained, what is silently accepted?

## Problem-Solving Exercise

> Monday 08:00 queue: 12 alerts. One host: beacon-45s + new scheduled task + egress spike. Another: a false-positive storm from a misconfigured printer.
> **Deliverable:** triage table (verdict + evidence + action); the one alert that escalates to incident response and why; one rule improvement to kill the printer storm.

## Summary

Detection is a system: rules catch the known, baselines hint at the odd, disciplined triage turns alerts into incidents or evidence-backed silence. This completes the network defense stack; next session consolidates M1–M4 in the midterm.

## Exit Ticket

1. Where does the SID go in a rule, and what convention applies to local rules?
2. Signature vs. anomaly: which fails silently on baseline drift?
3. What enrichment turns an IP alert into a decision?

## References

- OISF, *Suricata documentation — rules*. https://docs.suricata.io
- Bejtlich, R., *The Practice of Network Security Monitoring*.
- MITRE ATT&CK (coverage mapping). https://attack.mitre.org
- NIST SP 800-94, *Guide to Intrusion Detection and Prevention Systems*. https://csrc.nist.gov
