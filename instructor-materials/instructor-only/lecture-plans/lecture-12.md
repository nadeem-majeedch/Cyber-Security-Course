# Lecture 12 — Social Engineering, Phishing & Awareness Programs + Checkpoint C
**Module M3 · Week 6, Session 2 · 120 min · CLO-3 (primary)**

## Learning Objectives
1. Deconstruct a phishing email (headers, sender spoofing, lookalike domains, payload, lure) and a BEC scheme.
2. Explain why pretexting works (authority, urgency, social proof) and where it crosses legal lines.
3. Design a measurable awareness program: baseline, simulations-with-consent, metrics, escalation paths.
4. Apply Checkpoint C consolidation of Module 3.

## Key Concepts
- Email authentication: SPF, DKIM, DMARC — what each proves and the failure modes
- Phishing anatomy: lure, pretexts (authority/urgency/scarcity), payload types (credential harvest, macro, link), lookalike/homoglyph domains
- BEC: no payload, pure pretext; invoice fraud, CEO fraud; why technical controls miss it
- Awareness program design: consent + ethics for simulations; metrics beyond click rate (report rate, time-to-report); positive reinforcement
- Human firewall limits: MFA as the compensating control for the click that will happen

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L11 restore plans | Q&A |
| 08–30 | Phishing dissection: three real-architecture samples (rendered inert, synthetic), header walk: SPF/DKIM/DMARC verdicts | Interactive dissection |
| 30–48 | BEC storyboard: the invoice-fraud thread; students spot the pretext markers; why no payload = no scanner hit | Storyboard |
| 48–60 | Break | — |
| 60–72 | **Checkpoint C** (Module 3 quiz) | Assessment |
| 72–100 | **Lab block (Lab 11):** teams design an awareness campaign for the university: audience segments, one simulated-phish policy (with consent + ethics review), 3 metrics with target values, escalation path for reported mails | Team design |
| 100–112 | MFA spot-stat: walk through why phishing-resistant MFA (FIDO2) beats OTP push-bombing; students map compensating controls for each lure type | Discussion |
| 112–120 | Module 3 wrap; M4 preview (network security) | Q&A |

## Examples
- **CS track:** DMARC alignment failure — `From:` says university.edu, envelope and DKIM domain don't; students write the header verdict and the receiver's correct action.
- **DS track:** awareness metrics as a dashboard: click-rate, report-rate, time-to-report distributions by department; discuss Simpson's-paradox style pitfalls when comparing departments.

## Discussion Questions
1. Click simulations shame users — what does psychology research say happens to reporting culture instead?
2. Is a BEC "hack"? Legally, technically — what changed for the victim, and why does the distinction matter for insurance and law enforcement?
3. Where is the ethical line for simulations? Design the consent paragraph for our university campaign.

## Student Activity
Email dissection in pairs; awareness-campaign design with a metrics table; class votes which campaign would actually change behavior.

## Problem-Solving Scenario
> Finance received "invoice update" mail from a real vendor's compromised mailbox; payment details changed; DMARC passes (attacker used the real mailbox). Produce: the deception map (pretext markers), the three controls that would have caught it (one technical, one process, one human), and the verification process for payment-detail changes.

## Summary
Technical controls filter most phishing; the rest is economics and psychology. Defense = authentication (SPF/DKIM/DMARC) + phishing-resistant MFA + a reporting culture that rewards speed over purity. Module 4 moves to the wire: seeing what attackers do on the network.

## Formative Assessment
1. Which mail-auth record does the receiver query for policy? (DMARC)
2. Name two pretext categories used in BEC.
3. What metric beats click rate for program health?

## Required Resources
- `labs/lab-11-awareness-design/` worksheet + three inert sample mails
- SPF/DKIM/DMARC quick-reference card; university AUP excerpt (for consent policy)
- CLO mapping: **CLO-3** (objectives 1–4).
