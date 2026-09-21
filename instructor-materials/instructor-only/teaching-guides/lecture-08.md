# Teaching Guide — Lecture 08 (Secure SDLC, Dependencies, Headers + Checkpoint B)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: class votes on best CSP | Read the winner aloud; note why it works. |
| 08–30 | SDLC map | Pipeline diagram; place each control at its gate. |
| 30–50 | Live pipeline build | Add SCA+SAST jobs; run; triage 5 seeded findings. |
| 50–60 | Break | — |
| 60–72 | **Checkpoint B** | 10 min + 2 min collection. |
| 72–100 | Lab 07 (headers) | Set headers; verify; fix one CSP violation. |
| 100–112 | Dependency-confusion case | The resolver-prefers-public-name story; mitigations. |
| 112–120 | M2 wrap + M3 preview | Bridge: "flaws become incidents when code runs elsewhere." |

## Board/Projector Activities

- **Projector:** CI run live (the seeded findings appear); the header checker result for the demo app.
- **Board:** SDLC gates timeline (design → PR → CI → staging → release) with control stickers.

## Speaker Notes (key beats)

1. The scanner table (sees / blind to / noise) is the lecture's core model — teach triage as a *skill*, not a checkbox.
2. Dependency confusion: narrate the resolver's decision; mitigations are registry scoping, pinning, provenance.
3. Headers: each maps to an attack class; CSP rollout is report-only first — reuse L07's example.
4. Triage: CVSS is a base signal; exploitability and exposure decide SLAs.

## Expected Student Difficulties

- "High count = bad tool." Fix: the noise column of the table; baselining is normal.
- Students set HSTS without HTTPS and break the lab app. Fix: the lab checklist orders HTTPS first.
- SBOM feels bureaucratic. Fix: the audit-trail framing — "who could tell the regulator what you ran?"

## Teaching Tips

- Run the CI live once *before* class; seeded findings should take <3 min to appear.
- After Checkpoint B, spend 4 minutes on the most-missed items (see keys) before the lab.
- The go/no-go exercise needs a roleplay: security engineer vs product owner; assign roles to force the negotiation.

## Answer Keys **[KEY]**

- Checkpoint B: see `assessments/instructor-only/checkpoint-keys.md` §B.
- Seeded triage table (expected): framework RCE — critical, public exploit, exposed → blocks release; header gap — medium → schedule; license conflict — legal review, not security block.
- Exit ticket: 1 SCA / DAST; 2 MIME-sniffing attacks; 3 e.g., attack vector/impact/exploitability metrics.

## Lab Delivery (Lab 07)

- Minimum viable outcome: header set verified on the demo app + one CSP violation fixed.
- Expected failure points: CI minutes/quota; header checker unreachable from sandbox — use the offline checklist fallback.

## Discussion Facilitation

Q1 (400 findings) is about program credibility — steer to baselining and suppression-with-justification, not tool abandonment. Q3 (block release?) produces the SLA decision rule; capture two team rules on the board and compare.

## Accessibility

- CI run: pair the visual run with a pasted text log in the LMS for screen-reader parity.
- Roleplay: offer the product-owner script card in advance for students who need preparation time.
