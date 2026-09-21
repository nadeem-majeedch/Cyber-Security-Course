# Lecture 02 — Threat Modeling I: STRIDE and Attack Trees
**Module 1 · Week 1, Session 2 · 2 hours · CLO-1 (primary), CLO-4 (supporting)**

## Learning Objectives
1. Draw a data-flow diagram (DFD) with correct trust boundaries for a small system.
2. Apply STRIDE per DFD element to enumerate threats.
3. Build an attack tree and derive its minimum-cost cut set.
4. Rank threats by qualitative risk and justify the ranking.

## Key Concepts and Definitions

**Threat modeling** is structured reasoning about how a system can be attacked, performed *before* building defenses. It answers three questions in order: *What are we building? What can go wrong? What do we do about it?*

**Data-flow diagram (DFD):** the "what are we building" artifact. Four element types: **entities** (people/external systems), **processes** (code that transforms data), **data stores**, **data flows**. A **trust boundary** is any line where data crosses between actors/levels with different privilege or control (browser↔server, user↔kernel, campus↔internet). *Fact:* most missed threats in student models trace to a missing boundary.

**STRIDE** (per element, ask each letter):
| Letter | Threat | Property violated | Typical elements |
|---|---|---|---|
| S | Spoofing | Authenticity | entities, processes |
| T | Tampering | Integrity | flows, stores, processes |
| R | Repudiation | Non-repudiation/accountability | any interaction |
| I | Information disclosure | Confidentiality | flows, stores |
| D | Denial of service | Availability | processes, resources |
| E | Elevation of privilege | Authorization | processes, entry points |

**Attack tree:** an OR/AND decomposition of attacker goals. OR nodes: any child suffices; AND nodes: all children required. A **cut set** is a set of leaves whose success achieves the goal; the **minimum-cost cut set** (given leaf costs) is the cheapest complete attack path — it tells you where defense buys the most.

**Risk ranking:** likelihood × impact, argued qualitatively. A ranking you can defend beats a number you cannot.

## Conceptual Diagram

```text
 [Student] ──(job.pdf)──► (Print service) ──► [Print queue store]
      ╲________________trust boundary_______________╱
STRIDE on (Print service): S - fake job owner?  T - alter job?
R - deny printing?  I - read others' jobs?  D - flood queue?
E - print as staff?
```
*What you would see:* the board sketch for the campus printing system, with the boundary drawn between the student laptop and the print server; threats listed per element in a table.

## Realistic Examples

- **CS track:** STRIDE on a Git server: ssh process (S: stolen key; E: shell on the host), repo store (T: history rewrite), webhook flow (I: token leak; D: webhook flood).
- **DS track:** STRIDE on a model-serving API: poisoned training store (T), model theft via queries (I), spoofed API keys (S), repudiation of "who submitted this training job" (R).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "STRIDE is a tool you buy" | It is a mnemonic applied to a model; the DFD quality determines everything. |
| "Trust boundaries are only network edges" | Any privilege/control change is a boundary (user↔kernel, tenant↔tenant, batch job↔interactive). |
| "Attack trees need real probabilities" | Ordinal costs support minimum-cut reasoning; fake precision adds nothing. |
| "Threat modeling happens once, at design" | It is re-run on significant change — the model rots with the system. |

## Classroom Activities

1. **DFD catch-the-error (10 min):** the instructor's printing-system DFD has one deliberately missing boundary; the class finds it.
2. **STRIDE table drill (12 min):** per element of the class DFD, produce one threat per letter where sensible.
3. **Lab 01 part A (30 min):** teams DFD + STRIDE the course vending-box (spec sheet provided); each team posts ≥ 10 threats to the shared board.

## Discussion Questions

1. Why do student DFDs so often miss the browser↔server boundary? What boundary do microservices add?
2. A risk matrix rates a threat "medium." What does that hide, and what would you ask for instead?
3. Which STRIDE letter is hardest to *test* for, and why? (Hint: who keeps the evidence — R.)

## Problem-Solving Exercise

> The vending box: networked card reader, firmware updates over HTTP, local admin app with a default password, telemetry to a vendor cloud.
> **Deliverable:** DFD with ≥ 2 trust boundaries; ≥ 10 STRIDE threats; top-3 ranked with a one-line justification each.

## Summary

Threat modeling is structured pessimism: the DFD shows where the system can be abused, STRIDE tells you what to ask at each element, attack trees tell you what is cheapest for the attacker. Rank, then design controls — next lecture connects those controls to adversary behavior at scale (ATT&CK).

## Exit Ticket

1. Which STRIDE letters typically apply to a data store?
2. Sketch the browser↔server trust boundary for yesterday's demo app.
3. Why is "medium risk" an incomplete statement?

## References

- Shostack, A., *Threats: What Every Engineer Should Learn About Threat Modeling* (selected ch.), Wiley.
- OWASP Cheat Sheet Series, *Threat Modeling*. https://cheatsheetseries.owasp.org
- Microsoft, *Threats — STRIDE* documentation. https://learn.microsoft.com/security
- Salter, C., Saydjari, O. S., Schneier, B., Wallner, J., "Toward a Secure System Engineering Methodology," *New Security Paradigms Workshop*, 1998 (attack-tree origin lineage).
