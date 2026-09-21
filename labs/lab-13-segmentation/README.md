# Lab 13 — Segmentation & Ruleset Design
**Enrichment · Module 4 (L14) · CLO-4 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Design a zoned network (campus case) with a documented reachability matrix.
2. Write an ordered, least-privilege firewall ruleset from the zone map.
3. Audit a provided ruleset and find the planted shadowed rule.
4. Translate two perimeter rules into identity-based (zero-trust) policies.

## Prerequisites
Lecture 14. Lab 00's least-privilege habits.

## Hardware/Software Requirements
Course VM or paper: zone-map stencils, the department scenario pack, ruleset template, the `ruleset-with-flaw.txt` audit exercise.

## Installation and Setup
None; teams of 4.

## Ethical Authorization and Safety Notes
Design exercise on paper; the scenario is fictional. The "must-break" list is a *design* artifact — nothing is blocked on any real network.

## Step-by-Step Student Tasks
1. Zone map: student Wi-Fi, staff, servers (tiered), management, printers/IoT, backups — with trust directions.
2. Reachability matrix: must-work and must-break lists per zone pair (the design contract).
3. Ruleset: ordered, specific (no any-any), explicit deny last; egress rules included.
4. Audit exercise: find the planted shadowed rule in `ruleset-with-flaw.txt`; explain the failure it permits.
5. Zero-trust translation: rewrite two perimeter rules as identity-based policies (per-session verification).
6. Blast-radius check: the L11 worm scenario — which rule stops lateral movement at each step; which single missing rule fails.

## Expected Observations
Teams' first rulesets allow DNS/NTP everywhere (fine) but forget printers' cached credentials (the SMB must-break item) and egress from servers. The shadowed rule sits two lines above a specific deny.

## Questions for Analysis
1. Your must-break list had an item stakeholders would contest (student Wi-Fi → servers "for printing"). Design the exception policy that is auditable.
2. Which is cheaper in your ruleset: one broad rule + monitoring, or three specific rules? Defend with the audit cost, not just the rule count.

## Troubleshooting
Matrix contradicts the ruleset → the matrix is the contract; fix the rules. Shadow rule hard to find → read top-down; first match wins; look for a broader rule *above* a deny.

## Cleanup Instructions
Paper exercise; return stencils and packs.

## Submission Requirements
Zone map, reachability matrix, ordered ruleset, audit finding (shadowed rule + consequence), two zero-trust translations, blast-radius walk.

## Expected Outputs / Evidence
The ruleset must be machine-checkable in format (line-ordered, action+src+dst+port); the matrix and ruleset must not contradict.

---
### Instructor Answer Key (summary)
- Planted shadowed rule: `allow printers -> servers any` (line 6) above `deny printers -> workstations smb` (line 11) — the deny for printer→workstation SMB is shadowed by nothing *per se*, but the earlier broad printer→servers rule masks the intended narrow printer→servers DNS-only design; consequence: printers reach servers on all ports (worm path).
- Expected zones: 6 with backup zone one-way (no inbound sessions).
- Zero-trust translations (model): "allow staff → HR app:443" → "policy: group hr-staff, device managed, session-scoped to app hr-app"; "allow admin → management:22" → "policy: group netops + PAM session + recorded."
- Blast-radius walk: workstation → SMB → server blocked by zone deny; printer path was the miss.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Zone map + consistent reachability matrix | 3 |
| Ordered ruleset (specific, egress included, deny last) | 3 |
| Shadowed-rule audit with consequence | 2 |
| Zero-trust translations + blast-radius walk | 2 |
