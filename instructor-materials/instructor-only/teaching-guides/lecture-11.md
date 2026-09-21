# Teaching Guide — Lecture 11 (Ransomware & Worms: Anatomy and Resilience)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: best IOC table | Read two curated entries; praise the culling. |
| 08–32 | Kill-chain walk on the cited post-mortem | Stage-by-stage; class marks detection points. |
| 32–50 | Extortion economics + ecosystem | RaaS roles; why exfil changed backups. |
| 50–60 | Break | — |
| 60–72 | Backup-design surgery | Fix the flawed design; pairs. |
| 72–105 | Lab 10 (resilience scenario) | Reconstruct → containment → restore order. |
| 105–115 | Worm containment debate | Random side assignment; 2 min per side. |
| 115–120 | Exit ticket + preview | Tease L12: "the credential that started all this." |

## Board/Projector Activities

- **Board:** the kill-chain arrow strip with detection-point markers added live as the class spots them.
- **Projector:** the cited post-mortem (from `case-studies/`) — read only the timeline section; the rest is homework.

## Speaker Notes (key beats)

1. The kill chain is a *detectability map*: at each stage ask "what telemetry exists here?"
2. Exfiltration changes everything: the second lever (leak) is independent of restore success — that's why 3-2-1-1.
3. Immutability is about *credential reach*: if stolen admin can delete it, it is not immutable.
4. Restore rehearsal: an untested backup is a hypothesis. Tie to the L04 corrective-control column.
5. Worm containment ordering: segmentation → credentials → patching → takedown. Justify the order by blast-radius math.

## Expected Student Difficulties

- "Just pay" intuitions. Fix: present the three argument families (legal, ethical, strategic) evenhandedly, then the design conclusion: remove the coercion.
- Students conflate immutable with offsite. Fix: the credential-reach test as a decision rule.
- In the lab, restore-order answers are random. Fix: give the dependency rule (identity/backup infrastructure before user data).

## Teaching Tips

- The cited post-mortem must be one with a public, verifiable timeline — verify the link each term before class (reference-recency rule).
- Keep victim-organization names factual and neutral; no speculation beyond the published report (no invented statistics — quote only what the source says).
- The debate works because sides are random; force the strongest student to argue the side they dislike.

## Answer Keys **[KEY]**

- Backup-surgery expected fixes: separate backup credentials; offline/immutable copy; restore rehearsal cadence; monitoring on backup-store access.
- Lab 10 restore order (model answer): backup/identity infrastructure → domain-critical services → finance/regulatory systems → general file shares → endpoint re-imaging; accept defensible orderings with justification.
- Exit ticket: 1 T1490; 2 3 copies / 2 media / 1 offsite (+immutable/offline); 3 exfiltration creates disclosure harm independent of restore.

## Lab Delivery (Lab 10)

- Minimum viable outcome: kill-chain reconstruction with ATT&CK IDs + restore-order list with justification.
- Expected failure points: teams freeze on the "next 60 minutes" decisions — prompt with the three questions (contain spread? preserve evidence? communicate?).

## Discussion Facilitation

Q2 (who holds immutability credentials) is the plan-deciding question; make teams answer with a *role*, not a person. Q3 (payment) — cap at 8 minutes; the parking lot takes the overflow.

## Accessibility

- Post-mortem reading: distribute the timeline excerpt in advance in accessible formats (tagged PDF/plain text).
- The kill-chain strip: paired with the stage table in the student notes (text equivalent).
- Debate: allow written opening statements for students who prefer composed arguments.
