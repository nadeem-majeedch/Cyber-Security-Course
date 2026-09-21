# Teaching Guide — Lecture 14 (Firewalls, Segmentation, Zero Trust)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: one pair presents capture-B evidence | Frame citations required. |
| 08–30 | Zone-map build | Class designs the campus map live on the board. |
| 30–50 | Ruleset workshop + planted shadow | From map to ordered rules; find the dead rule. |
| 50–60 | Break | — |
| 60–105 | Lab 13 (team segmentation + reachability matrix) | Must-work / must-break lists drive design. |
| 105–115 | Zero-trust translation | Rewrite two perimeter rules as identity policies. |
| 115–120 | Exit ticket + preview | Tease L15: "who watches this design?" |

## Board/Projector Activities

- **Board:** the zone map (boxes + trust lines) built by the class; the ordered ruleset beside it.
- **Handout:** reachability-matrix template (must-work / must-break per zone pair).

## Speaker Notes (key beats)

1. East-west vs. north-south: ransomware travels east-west; the perimeter model only guards north-south.
2. Stateful semantics: return traffic rides state; rule order = first match; any-any defeats the policy.
3. Egress: exfiltration is egress — the forgotten half of every firewall policy.
4. Zero trust: per-session verification + identity-based policy (800-207); it *layers*, not replaces.
5. Blast radius: printers-with-cached-credentials example — six rules, one worm path cut.

## Expected Student Difficulties

- Rulesets drift to any-any under time pressure. Fix: the must-work matrix makes each rule's purpose explicit.
- "Zero trust = product." Fix: teach it as the 800-207 policy model; name what changes (decision point, per-session).
- Students segment nothing because "everything talks to everything." Fix: force the must-break list first — design the blast radius before the flows.

## Teaching Tips

- Keep the planted shadow rule subtle (a broader rule *above*, not below); finding it is the audit skill.
- Timebox the zone map (12 min); polish kills momentum.
- The reachability matrix is the artifact that survives into the capstone (L29 reuses it) — say so.

## Answer Keys **[KEY]**

- Planted shadow rule: `allow printers→servers any` earlier in the list shadows the later specific denies — accept "the SMB deny to workstations is unreachable."
- Lab 13 model design: printers/IoT zone (no SMB to workstations), management zone (admin-only, MFA), backup zone (one-way), DMZ (web), internal zones tiered; rules ordered specific→general with explicit deny last.
- Exit ticket: 1 no (state allows return); 2 north-south (perimeter) vs east-west (lateral) — egress is exfiltration; 3 e.g., per-session verification vs. "inside = trusted."

## Lab Delivery (Lab 13)

- Minimum viable outcome: zone map + ordered ruleset + completed reachability matrix.
- Expected failure points: teams forget the backup zone's one-way requirement; the matrix exposes it — good, let the matrix teach.

## Discussion Facilitation

Q2 (egress politics) is the realistic one: universities can't hard-deny student egress; the exception policy (time-boxed, logged, reviewed) is the compromise. Q3 (costs): connect to documentation debt — the service catalog *is* the paydown.

## Accessibility

- Zone maps are spatial: provide the text-equivalent (zone list + allowed flows table) so non-visual learners design the same artifact.
- Ruleset review: line-numbered printouts; the audit works from text alone.
