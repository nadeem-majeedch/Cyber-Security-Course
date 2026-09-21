# Lecture 14 — Network Defense II: Firewalls, Segmentation, and Zero Trust
**Module M4 · Week 7, Session 2 · 120 min · CLO-4 (primary)**

## Learning Objectives
1. Design a segmented network (zones, VLANs/subnets) that maps to data sensitivity and trust levels.
2. Write least-privilege firewall rulesets (stateful semantics, ordering, explicit deny) and audit one for shadows/redundancy.
3. Explain zero-trust principles (per-session verification, least privilege, assume breach) and contrast with perimeter thinking.
4. Choose and justify remote-access architecture (VPN vs. ZTNA patterns) for a scenario.

## Key Concepts
- Zones and tiers: DMZ, internal, management, guest; east-west vs. north-south traffic
- Stateful inspection; rule ordering, shadowed rules, any-any traps; egress filtering (the forgotten half)
- Segmentation outcomes: blast-radius math (what the L11 worm could have reached)
- Zero trust: identity-centric access, per-application tunnels, policy decision points; NAC awareness
- Remote access: full-tunnel vs. split VPN, ZTNA/broker pattern, device posture (concept)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L13: one pair presents capture-B evidence | Presentation |
| 08–30 | Segmentation design: campus case (student Wi-Fi, staff, servers, printers, IoT, backups) — class builds the zone map together | Board design |
| 30–50 | Ruleset workshop: from zone map to ordered ruleset; instructor plants a shadowed rule, students audit and find it | Exercise |
| 50–60 | Break | — |
| 60–105 | **Lab block (Lab 13):** teams design the segmented network + ruleset for the course "department" scenario; verify reachability matrix against requirements (what MUST break) | Team design |
| 105–115 | Zero-trust translation: rewrite two perimeter rules as identity-based policies; discuss what infrastructure is needed | Discussion |
| 115–120 | Exit ticket; preview L15 (IDS/IPS/SIEM) | Q&A |

## Examples
- **CS track:** printers got domain credentials cached — segment them and cut SMB to workstations; the ruleset delta is 6 lines and kills a worm path.
- **DS track:** analytics cluster talks only to the data warehouse on 5432 — enforce via segmentation; discuss data-exfiltration paths left open (egress) and their monitoring.

## Discussion Questions
1. "Firewalls are dead, zero trust won" — agree or disagree? What does the evidence say about layering both?
2. Why is egress filtering politically hard in universities? Design the student-lab exception policy.
3. What does segmentation cost (ops, troubleshooting) and how do you pay it down (documentation, service catalogs)?

## Student Activity
Team segmentation design with a reachability matrix (must-work / must-break lists); ruleset audit exchange between teams.

## Problem-Solving Scenario
> The L11 worm returns with credential reuse: workstation → server SMB spread. Given the class zone map: (1) which rules stop lateral movement at each step, (2) which single missing rule failed, (3) the monitoring rule that would have alerted first.

## Summary
Segmentation is pre-positioned containment: design the blast radius before the incident. Least-privilege rulesets and egress discipline make the perimeter and the interior both defensible. L15 adds the detection layer that watches the design in operation.

## Formative Assessment
1. Stateful firewall: does return traffic need an explicit allow rule?
2. Name the two traffic directions and why egress matters.
3. Give one zero-trust principle and its perimeter-era contrast.

## Required Resources
- `labs/lab-13-segmentation/` scenario pack + reachability-matrix template
- Zone-map stencils (printed or digital); NIST SP 800-207 zero-trust overview (2-page)
- CLO mapping: **CLO-4** (objectives 1–4).
