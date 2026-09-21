# Lecture 01 — Security Foundations: CIA, Ethics, and the Defender's Mindset
**Module M1 · Week 1, Session 1 · 120 min · CLO-1 (primary)**

## Learning Objectives
By the end of this lecture students will be able to:
1. Define confidentiality, integrity, and availability and classify given scenarios by which property is primarily at risk.
2. Distinguish security from privacy and from safety, using concrete examples.
3. Explain the authorization-first rule: why testing requires explicit written permission.
4. Describe responsible disclosure and the typical vulnerability-report lifecycle.

## Key Concepts
- CIA triad; extensions (authenticity, accountability, non-repudiation)
- Security ≠ privacy ≠ safety; the relationship and conflicts between them
- Risk = Likelihood × Impact; asset, threat, vulnerability, control
- Authorization, scope, and rules of engagement (RoE)
- Responsible disclosure (coordinated disclosure) vs. full disclosure
- Hacking legend and computer-misuse law awareness (national + international context)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–05 | Welcome, course contract, syllabus tour | Slides |
| 05–15 | Diagnostic self-check (ungraded poll): 6 prerequisite questions (Linux, Python, TCP, SQL, probability, process model) | Live poll |
| 15–40 | CIA triad with three anchor incidents: a breach (C), a tampering incident (I), a ransomware outage (A). Students classify 8 quick scenarios | Interactive slides |
| 40–55 | Security vs. privacy vs. safety triangle; where they conflict (e.g., monitoring employee traffic) | Guided discussion |
| 55–60 | Break | — |
| 60–95 | **Lab block (Lab 00 orientation):** boot course VM, snapshot, run `lab-00-orientation/` environment check; discuss why we isolate | Hands-on |
| 95–112 | Ethics segment: authorization-first rule; RoE template walk-through; responsible disclosure timeline (report → vendor ack → fix → publication) | Case walk-through |
| 112–120 | Consolidation: one-minute paper + preview of L02 | Q&A |

## Examples
- **CS track:** integrity failure in a CI/CD pipeline where a dependency update injects code — map to CIA.
- **DS track:** data-science example — a training dataset silently corrupted (integrity) and a dataset of personal records exposed (confidentiality); discuss how each changes the "model risk."

## Discussion Questions
1. A hospital's records are encrypted by ransomware. Which CIA property is most harmed, and does the answer change if backups exist?
2. Is it ethical to scan a company's public website without permission if you find a critical flaw? What are your options?
3. Where do privacy and security genuinely conflict, and how would you resolve it as an engineer?

## Student Activity
In pairs, classify 8 scenario cards by primary CIA property and by asset/threat/vulnerability/control; one pair presents their most debatable card.

## Problem-Solving Scenario
> A student-run food-delivery app stores passwords in plaintext, has no backups, and its status page lies during outages. Produce a 5-line risk note: the three biggest risks (mapped to CIA), the likely impact, and the first control you would deploy with a one-sentence justification.

## Summary
Security work starts from assets and risk, not from tools. CIA is the classification lens; authorization and disclosure rules are the ethical frame for everything that follows in this course.

## Formative Assessment (exit ticket)
1. Classify: "an attacker alters transaction amounts in a database" (C/I/A?).
2. Name the two disclosures routes and which one this course requires.
3. One thing you still find unclear about RoE.

## Required Resources
- Course VM image + `labs/lab-00-orientation/` (starter checklist)
- Stallings & Brown ch. 1; NIST CSF 2.0 overview (1-page)
- Slides `L01-slides` source; scenario card deck (printed or in LMS)
- CLO mapping: **CLO-1** (all objectives); supports Lab 00 readiness for CLO-2+.
