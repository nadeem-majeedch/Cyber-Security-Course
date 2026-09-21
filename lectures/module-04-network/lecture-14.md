# Lecture 14 — Network Defense II: Firewalls, Segmentation, Zero Trust
**Module 4 · Week 7, Session 2 · 2 hours · CLO-4**

## Learning Objectives
1. Design a segmented network (zones) that maps to data sensitivity and trust levels.
2. Write least-privilege firewall rulesets and audit one for shadowed rules.
3. Explain zero-trust principles and contrast them with perimeter thinking.
4. Choose and justify a remote-access architecture (VPN vs. ZTNA) for a scenario.

## Key Concepts and Definitions

**Zones and tiers:** DMZ (internet-facing), internal (workstations), management (admin planes), guest, and specialty zones (IoT/printers, backups). **North-south** traffic crosses the perimeter; **east-west** moves laterally inside — the direction ransomware actually travels.

**Stateful firewalls:** the device tracks connections; return traffic is permitted by state, not by rule. Rule properties that cause real incidents: **ordering** (first match wins), **shadowed rules** (a broader earlier rule makes a later one dead), and the **any-any** trap (a rule that defeats the whole policy). **Egress filtering** — controlling what *leaves* — is the forgotten half; exfiltration is egress.

**Blast radius:** pre-positioning containment by design. If printers hold cached domain credentials and share a zone with workstations, one compromise spreads; segment printers, and the worm path dies at the zone edge.

**Zero trust (NIST SP 800-207):** per-session verification, identity- and posture-based policy, assume breach. Contrast: the perimeter model trusted "inside." Zero trust is a *direction of travel* implemented with identity-aware proxies and per-application access — not a product you buy.

**Remote access:** full-tunnel vs. split-tunnel VPN (split gives exfil paths and bypasses perimeter inspection), versus **ZTNA**: per-application brokered access, no network-level trust.

## Conceptual Diagram

```text
                 ┌── DMZ (web) ── internet
internet ────────┤
                 ├── internal (workstations) ── servers (tiered)
                 ├── management (admin only)
                 └── IoT/printers ── no SMB to workstations ← worm path cut
rules: source, destination, port, action — ORDER MATTERS; explicit deny last
```

## Realistic Examples

- **CS track:** printers with cached domain credentials: the six-line ruleset delta (printers ↔ workstations SMB denied) kills a lateral-movement path — segmentation as cheap prevention.
- **DS track:** the analytics cluster needs only the warehouse on 5432: enforce it; then discuss the *egress* paths that remain (package mirrors, telemetry) and who monitors them.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "The firewall is the network's security" | It is one control at one boundary; lateral movement historically rides *inside* trust. |
| "Zero trust means no firewalls" | 800-207 layers policy engines over network controls; they compose. |
| "VPN = secure remote work" | VPN grants network-level reach; ZTNA grants application-level access with less blast radius. |
| "Segmentation means micro-managing every flow forever" | Baseline the must-work matrix, automate exceptions with expiry, review quarterly. |

## Classroom Activities

1. **Zone-map build (15 min):** the class designs the campus zone map live (student Wi-Fi, staff, servers, printers, IoT, backups).
2. **Ruleset audit (10 min):** find the planted shadowed rule in a provided ruleset.
3. **Lab 13 (45 min):** teams design segmentation + ruleset for the department scenario and verify the reachability matrix (what *must* break).

## Discussion Questions

1. "Firewalls are dead; zero trust won." Agree or disagree — what does layering both actually look like?
2. Why is egress filtering politically hard at universities? Design the student-lab exception policy.
3. What does segmentation cost in operations, and how do you pay it down (documentation, service catalogs)?

## Problem-Solving Exercise

> The L11 worm returns with credential reuse: workstation → server via SMB.
> **Deliverable:** which rules stop lateral movement at each step; the single missing rule that failed; the monitoring rule that would have alerted first (join to L15).

## Summary

Segmentation is pre-positioned containment: design the blast radius before the incident. Least-privilege rulesets plus egress discipline make perimeter and interior defensible; zero trust moves the check to identity and session. Next lecture adds the watching layer: detection.

## Exit Ticket

1. Does return traffic need an explicit allow rule on a stateful firewall?
2. Name the two traffic directions and why egress matters.
3. State one zero-trust principle and its perimeter-era contrast.

## References

- NIST SP 800-207, *Zero Trust Architecture*. https://csrc.nist.gov
- NIST SP 800-41 Rev. 1, *Guidelines on Firewalls and Firewall Policy*. https://csrc.nist.gov
- Stallings & Brown, *Computer Security* (network defense chapters).
- CIS Controls (network-related safeguards). https://www.cisecurity.org/controls
