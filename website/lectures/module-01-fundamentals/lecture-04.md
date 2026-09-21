# Lecture 04 — Defense in Depth, Least Privilege, and Checkpoint A
**Module 1 · Week 2, Session 2 · 2 hours · CLO-1 (primary), CLO-8 (supporting)**

## Learning Objectives
1. Layer preventive, detective, and corrective controls into a defense-in-depth design.
2. Apply least privilege and secure defaults to accounts, services, and storage.
3. Classify controls on two axes (administrative/technical/physical × preventive/detective/corrective) and find gaps.
4. Present a control set that addresses a STRIDE threat list.

## Key Concepts and Definitions

**Defense in depth:** multiple, diverse controls so no single failure is fatal. A useful discipline: for each priority threat, name a **preventive** control (stops it), a **detective** control (reveals it), and a **corrective** control (recovers from it). If any column is empty, you have a gap.

**Least privilege:** every account, process, and service gets the minimum rights needed — and no more. Corollaries: **need-to-know**, **separation of duties** (two people for dangerous actions), **deny-by-default** (allow-list what you must).

**Secure defaults:** the shipped configuration is the safe one; changing it should require deliberate action, not the reverse.

**Control taxonomy:**

| | Preventive | Detective | Corrective |
|---|---|---|---|
| **Technical** | WAF rule, encryption | SIEM alert, IDS | Restore from backup |
| **Administrative** | Policy, training | Audit, review | Incident response plan |
| **Physical** | Lock, mantrap | Camera | Site failover |

**Residual risk:** what remains after controls. It must be *named and accepted* by someone with authority — unnamed residual risk is how organizations get surprised.

**NIST CSF 2.0 functions** (Govern, Identify, Protect, Detect, Respond, Recover) are a useful checklist for asking "which function does this control serve?"

## Conceptual Diagram

```text
Threat: "attacker gets user shell via web app"
  Prevent: input validation, WAF, patched stack, least-priv service account
  Detect:  web shell indicators → SIEM, egress anomaly alert
  Correct: snapshot rollback, credential rotation runbook
                 │
   any empty cell = a documented GAP
```

## Realistic Examples

- **CS track:** a CI pipeline compromise: branch protection (prevent), signed builds/provenance (detect/prevent tampering), canary deploy + rollback (correct).
- **DS track:** an analytics database: read-only analyst role (least privilege), query logging with anomaly alerts (detect), immutable backups (correct).
- **Layering drill:** the vending-box threats from L02 get controls in all three columns; the class finds the cheapest threat that still has an empty column.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Defense in depth = buy more products" | Layers must be *diverse* (fail differently), not numerous. |
| "Least privilege means users can't work" | It means the *default* can't work; you then grant what is needed, ideally role-shaped and time-bound. |
| "Passing the audit = secure" | Compliance samples controls at a point in time; adversaries work continuously. |
| "Someone will accept the risk later" | Residual risk without a named acceptor is an unmanaged liability. |

## Classroom Activities

1. **Control card sort (15 min):** 20 control cards into the 3×3 taxonomy wall grid; debate the misfiled ones.
2. **Checkpoint A (10 min):** six-item quiz on Module 1 concepts (CLO-1).
3. **Lab 03 (35 min):** teams layer controls for the vending-box threat list; least-privilege rewrite of an over-permissive config set.

## Discussion Questions

1. Budget allows three controls for the vending box. Which three, and how do you justify the residual risk?
2. Where does defense in depth *hurt* (complexity, false positives, workarounds) — and how do you pay those costs down?
3. Why is deny-by-default harder to sell to product teams? Build the counter-argument.

## Problem-Solving Exercise

> Input: the ≥ 10 STRIDE threats from L02.
> **Deliverable:** control matrix covering ≥ 8 threats, ≥ 2 layers for each of the top 3; named residual risks with the (fictional) acceptor role; one gap you refuse to leave unmitigated and why.

## Summary

A control you cannot name is a control you do not have. Layer prevention, detection, correction; keep privileges minimal; accept residual risk explicitly. Module 1 gave you the modeling toolkit; Module 2 applies it to the web — the most exposed surface most organizations run.

## Exit Ticket

1. Classify: WAF rule, SOC alert triage, quarterly restore drill (which cells of the matrix?).
2. Give one concrete least-privilege fix for "analysts have DB admin rights."
3. Risk *transfer* vs. risk *acceptance* — one sentence each.

## References

- NIST, *Cybersecurity Framework 2.0*. https://www.nist.gov/cyberframework
- NIST SP 800-53 Rev. 5, *Security and Privacy Controls* (control families). https://csrc.nist.gov
- Stallings & Brown, *Computer Security* (access control and trusted systems chapters).
- Saltzer, J. & Schroeder, M., "The Protection of Information in Computer Systems," *Proceedings of the IEEE*, 1975 (least privilege and complete mediation — foundational).
