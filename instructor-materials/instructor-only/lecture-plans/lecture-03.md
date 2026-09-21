# Lecture 03 — Threat Modeling II: Attack Surface & MITRE ATT&CK
**Module M1 · Week 2, Session 1 · 120 min · CLO-1 (primary)**

## Learning Objectives
1. Enumerate and prioritize an attack surface (network, code, human, physical, supply chain, ML/DS-specific surfaces).
2. Navigate MITRE ATT&CK Enterprise tactics and techniques; map adversary behaviors to them.
3. Write a threat-informed defense hypothesis: "if technique X, then telemetry Y, then control Z."
4. Re-scope an attack surface after a design change (feature added, service exposed).

## Key Concepts
- Attack surface categories and reduction (minimize exposed endpoints, secrets, privileges)
- MITRE ATT&CK structure: tactics (the why) vs. techniques/sub-techniques (the how); example IDs: T1566 Phishing, T1110 Brute Force, T1059 Command & Scripting Interpreter, T1078 Valid Accounts
- Detection hypotheses as engineering artifacts; telemetry inventory
- ATT&CK for Enterprise vs. Mobile vs. ICS (awareness); ATT&CK-driven purple teaming

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L02: one team presents its vending-box top threat | Presentation |
| 08–30 | Attack surface audit method: walk a fictional department web app (login, file upload, admin panel, analytics job); students list surfaces, then rank by exposure×value | Interactive slides |
| 30–50 | ATT&CK navigation tour: pick Initial Access → Lateral Movement path for a ransomware scenario; read 3 technique pages live | Live demo |
| 50–60 | Break | — |
| 60–95 | **Lab block (Lab 02):** teams map 6 given adversary behaviors to ATT&CK IDs, then write one detection hypothesis each with required telemetry | Teams |
| 95–110 | Surface-reduction debate: given the department app, cut the surface by 50% — what do you remove, what breaks? | Structured debate |
| 110–120 | Exit ticket + preview (defense in depth next) | Q&A |

## Examples
- **CS track:** new S3-compatible backup bucket opened to the office IP range — enumerate the delta surface (public read misconfig, credential reuse, exposed snapshots).
- **DS track:** JupyterHub exposed to campus network — kernel execution as a foothold (T1059), data-store credentials in notebooks (T1552), model exfiltration.

## Discussion Questions
1. Which produces better defenses: attacker-driven (ATT&CK) or asset-driven (DFD/STRIDE) enumeration? When do you use each?
2. Your detection hypothesis has no existing telemetry source. What are your three options and their costs?
3. Is a reduced attack surface always better? Give a case where exposure is intentional.

## Student Activity
Six-station carousel: each station has one adversary behavior description; teams rotate, assign ATT&CK IDs, and accumulate a defense-hypothesis sheet.

## Problem-Solving Scenario
> The department app team ships a "resume PDF feedback" feature: upload → convert → return. Enumerate the new attack surface (≥ 8 items across network/code/human/supply-chain), map 3 plausible adversary behaviors to ATT&CK IDs, and write one complete detection hypothesis.

## Summary
Attack surface answers "where can they touch us"; ATT&CK answers "what will they do once they do." Both feed the defense-in-depth design that L04 builds into layered controls.

## Formative Assessment
1. Give the ATT&CK ID for spearphishing attachment.
2. Name two surface categories students usually forget (physical, supply chain).
3. Write a one-sentence detection hypothesis for T1110.

## Required Resources
- `labs/lab-02-attack-surface/` worksheet; ATT&CK website access
- Department app spec handout; hypothesis template
- CLO mapping: **CLO-1** (objectives 1–4); seeds CLO-4 detection thinking.
