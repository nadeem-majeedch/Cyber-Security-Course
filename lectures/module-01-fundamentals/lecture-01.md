# Lecture 01 — Security Foundations: CIA, Ethics, and the Defender's Mindset
**Module 1 · Week 1, Session 1 · 2 hours · CLO-1**

## Learning Objectives
After this lecture you can:
1. Define confidentiality, integrity, and availability (CIA) and classify scenarios by the property primarily at risk.
2. Distinguish security from privacy and from safety, and identify where they conflict.
3. Explain the authorization-first rule and responsible disclosure.
4. Set up the course lab environment safely (VM + snapshot).

## Key Concepts and Definitions

**Security** is the property that a system behaves as its stakeholders intend, despite adversary action. We assess it through three classical properties:

- **Confidentiality (C):** information is disclosed only to those authorized. *Fact:* breaches where customer records leak are primarily confidentiality failures.
- **Integrity (I):** information and processing are not improperly altered. Includes *data integrity* (content) and *system integrity* (behavior).
- **Availability (A):** authorized users can access the system when needed. Ransomware that halts operations is primarily an availability attack.

**Vocabulary used all semester (keep it consistent):**
- **Asset** — something valuable to protect (data, service, reputation).
- **Threat** — a potential cause of harm (actor + action).
- **Vulnerability** — a weakness that a threat can exploit.
- **Control (safeguard)** — a measure that prevents, detects, or corrects harm.
- **Risk** — the combination of likelihood and impact of harm. We treat it qualitatively in this course: *risk = likelihood × impact* is a thinking tool, not arithmetic.

**Security ≠ privacy ≠ safety.** Security protects against deliberate adversaries. Privacy protects individuals' control over their personal data — you can be perfectly secured and still process data unethically. Safety protects against accidental harm (no adversary required). They interact: monitoring employee traffic may increase security while decreasing privacy.

**Authorization-first rule (this course's core ethical rule):** never interact with a system you do not own or lack explicit written permission to test. This is both an ethical rule and, in most jurisdictions, a legal boundary.

**Responsible (coordinated) disclosure:** you report a found vulnerability to the vendor privately, allow a remediation window, and publication is coordinated. The alternative, full disclosure, publishes immediately — historically argued to pressure vendors, at the cost of exposing users to the flaw. **This course requires the coordinated route.**

## Conceptual Diagram

```text
            THREAT (actor + action)
                   │ exploits
                   ▼
ASSET ◄── harms ── VULNERABILITY ── mitigated by ──► CONTROL
   ▲                                                   │
   └────────────────── value to protect ───────────────┘
Risk = likelihood(threat succeeds) × impact(on asset)
```
*What you would see:* the instructor draws this as a triangle on the board and walks a ransomware incident around it (asset: file server; vulnerability: unpatched VPN; threat: ransomware affiliate; control: patching + offline backups).

## Realistic Examples

- **CS track:** a CI/CD pipeline where a dependency update injects code into the build. Asset: released software; property at risk: integrity; control candidates: dependency pinning, signed builds.
- **DS track:** an analytics platform where (a) a training dataset is silently corrupted — integrity, and (b) a dataset of personal records is exposed publicly — confidentiality. Each changes the risk story for the *models* built on that data (garbage-in integrity → wrong decisions; leaked data → privacy harm).
- **Availability anchor:** a hospital's records encrypted by ransomware. With tested offline backups, availability is recoverable; without them, the harm escalates.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Security = confidentiality only" | Availability and integrity failures can be more disruptive than disclosure. |
| "If it's on the public internet, it's fair game to test" | Public exposure ≠ authorization. The authorization-first rule applies regardless of reachability. |
| "Full disclosure is always irresponsible" | It is a contested position with a real history; coordinated disclosure is this course's required practice. |
| "Risk matrices give precise risk" | They order qualitative judgments; the numbers are not measurements. |

## Classroom Activities

1. **Scenario classification (pairs, 8 min):** classify 8 one-line scenarios by primary CIA property. Two examples: "attacker alters transaction amounts" (I); "DNS outage makes the site unreachable" (A).
2. **Triangle debate (5 min):** where do security and privacy genuinely conflict? One concrete campus example.
3. **Lab 00 orientation (35 min):** boot the course VM, take a snapshot, verify isolation settings, complete the environment checklist.

## Discussion Questions

1. A hospital's records are encrypted by ransomware. Which CIA property is most harmed — and does your answer change if backups exist?
2. You find a critical flaw in a company's public website without permission. What are your options, and what does each cost the users?
3. Is "we monitor everything for security" a defensible position for a university? What would you add to the policy to make it defensible?

## Problem-Solving Exercise

> A student-run food-delivery app stores passwords in plaintext, has no backups, and its status page is inaccurate during outages.
> **Deliverable (5 lines):** the three biggest risks each mapped to a CIA property; the likely impact of each; the *first* control you would deploy, with a one-sentence justification.

## Summary

Security work starts from assets and risk, not tools. CIA is the classification lens; threat/vulnerability/control is the working vocabulary; authorization and coordinated disclosure are the ethical frame for everything that follows.

## Exit Ticket (formative, ungraded)

1. "An attacker alters transaction amounts in a database" — C, I, or A?
2. Name the two disclosure routes; which does this course require?
3. One thing that is still unclear about rules of engagement.

## References

- Stallings, W. & Brown, L., *Computer Security: Principles and Practice*, ch. 1 (selected ed. per library).
- NIST, *Cybersecurity Framework (CSF) 2.0* — overview. https://www.nist.gov/cyberframework
- NIST SP 800-12 Rev. 1, *Introduction to Information Security* (glossary definitions). https://csrc.nist.gov
- CISA, *Known Exploited Vulnerabilities Catalog* — motivation for coordinated remediation. https://www.cisa.gov/known-exploited-vulnerabilities-catalog
