# Lecture 03 — Threat Modeling II: Attack Surface and MITRE ATT&CK
**Module 1 · Week 2, Session 1 · 2 hours · CLO-1**

## Learning Objectives
1. Enumerate and prioritize a system's attack surface across network, code, human, physical, supply-chain, and ML-specific categories.
2. Navigate MITRE ATT&CK and map adversary behaviors to tactics/techniques (with IDs).
3. Write a threat-informed defense hypothesis: *if technique X, then telemetry Y, then control Z*.
4. Re-scope an attack surface after a design change.

## Key Concepts and Definitions

**Attack surface:** the set of points where an adversary can interact with a system — network endpoints, code paths that consume input, **human** interactions (support desks, phishing), **physical** access, the **supply chain** (dependencies, build systems), and for ML systems the **data/label pipeline**. Surface *reduction* removes or gates these points.

**MITRE ATT&CK** (adversarial tactics, techniques & common knowledge) is a curated knowledge base of adversary behavior. **Tactics** are the *why* (Initial Access, Persistence, Lateral Movement…). **Techniques/sub-techniques** are the *how*, each with a stable ID. Canonical examples used all semester: **T1566** Phishing, **T1110** Brute Force, **T1059** Command and Scripting Interpreter, **T1078** Valid Accounts. ATT&CK for Enterprise is the focus; Mobile/ICS variants exist.

**Defense hypothesis:** a testable statement tying adversary behavior to the telemetry that would reveal it and the control that would stop or slow it — the bridge from threat modeling (M1) to detection engineering (M6).

**Fact vs. framing note:** ATT&CK is descriptive (what adversaries have been observed doing), not a guarantee of what your adversary will do. Use it with, not instead of, your DFD/STRIDE model.

## Conceptual Diagram

```text
ATTACK SURFACE (what can be touched)          ATT&CK (what they do with it)
  network endpoints  ─┐                        Initial Access → Execution →
  code input paths    ├─ each point answers  →  Persistence → Lateral Movement →
  humans              │   "how would they       Exfiltration / Impact
  physical            │    get in & move?"
  supply chain        │
  data/label pipeline ┘        DEFENSE HYPOTHESIS: if T1110, then many failed
                               auth events for one account, then rate-limit + MFA
```

## Realistic Examples

- **CS track:** a new backup bucket opened to the office IP range: the surface delta includes public-read misconfiguration, credential reuse, and exposed snapshots; the ATT&CK path begins with **T1078** (valid accounts) or **T1530** (data from cloud storage).
- **DS track:** JupyterHub exposed to the campus network: notebook kernels are code execution (**T1059.007** JavaScript/JScript is not the right one — use **T1059** generally), credentials in notebooks (**T1552.001** credentials in files), model exfiltration by queries.
- **Feature-change drill:** a "resume PDF feedback" feature adds upload → convert → return; new surface: upload path (malicious file handling), converter (document parser vulnerabilities), return path (content-type confusion).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "The attack surface is the public endpoints" | Humans, physical access, and the supply chain are equally real entry points. |
| "ATT&CK tells me my adversary's next step" | It catalogs observed behavior classes; your scenario and model decide relevance. |
| "More surface = more features = better product, security is the trade-off" | Some exposure is intentional (that is the point of a service); the discipline is *deciding* it. |
| "If I can't name a technique ID, it isn't real" | The ID is a label, not a requirement; describe behavior first, then map. |

## Classroom Activities

1. **Surface audit (12 min):** list and rank the surfaces of a fictional department web app (login, upload, admin panel, analytics job) by exposure × value.
2. **ATT&CK navigation tour (15 min):** follow one ransomware path through the ATT&CK site live; each student records 3 technique IDs.
3. **Lab 02 (35 min):** six-station carousel of adversary behaviors → ATT&CK IDs → one defense hypothesis per station.

## Discussion Questions

1. Which produces better defenses: attacker-driven (ATT&CK) or asset-driven (DFD/STRIDE) enumeration — and when do you use each?
2. Your detection hypothesis needs telemetry that does not exist. What are your three options and their costs?
3. Is reduced attack surface always better? Give one case where exposure is intentional and necessary.

## Problem-Solving Exercise

> The department app ships "resume PDF feedback" (upload → convert → return).
> **Deliverable:** ≥ 8 new surface items across at least three categories; 3 plausible adversary behaviors mapped to ATT&CK IDs; one complete defense hypothesis (technique → telemetry → control).

## Summary

Attack surface answers *where can they touch us*; ATT&CK answers *what will they do once they do*. Together they convert vague worry into testable defense hypotheses — which the next lecture turns into layered controls.

## Exit Ticket

1. Give the ATT&CK ID for spearphishing attachment.
2. Name two surface categories students commonly forget.
3. Write a one-sentence defense hypothesis for T1110.

## References

- MITRE ATT&CK for Enterprise. https://attack.mitre.org
- Shostack, A., *Threats* (attack-surface chapters).
- McGraw, G., *Software Security: Building Security In* (risk/surface management perspective), Addison-Wesley.
- CISA, *Attacks on Critical Infrastructure* advisories (technique-mapping examples). https://www.cisa.gov
