# Teaching Guide — Lecture 07 (XSS, CSRF, SSRF, IDOR)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: project one parameterized diff | The author explains their fix (1 min). |
| 08–30 | XSS family | Live reflected demo in the sandbox app; then the three-context table. |
| 30–48 | CSRF | The forged-transfer storyboard; GET state-change failure. |
| 48–60 | SSRF + IDOR | URL-fetch demo; invoice enumeration demo. |
| 60–62 | Break | — |
| 62–105 | Lab 06 (four stations) | Rotate; verification exchange at the end (fix a peer's, verify your own). |
| 105–115 | CSP workshop | Write a CSP; inspect report-only violations. |
| 115–120 | Exit ticket + preview | Tease L08: "the pipeline should have caught all four." |

## Board/Projector Activities

- **Board:** the four-flows diagram (who runs the request: victim / victim / server / attacker) — it is the lecture's spine; photograph and post.
- **Projector:** sandbox app comment field (XSS); dev tools showing the forged CSRF request in the lab target.

## Speaker Notes (key beats)

1. The four flaws differ in *whose browser/server sends the request* — that sentence organizes remediation (encode vs token vs allow-list vs ownership check).
2. XSS: one encoder is not enough; contexts differ. Demo the same payload behaving differently in body vs attribute.
3. CSRF: the ambient-credential insight; fix = break the ambient assumption (token) *and* reduce sending (`SameSite`).
4. IDOR: authentication ≠ authorization; the check must be object-level and server-side.
5. CSP: defense in depth, report-only first.

## Expected Student Difficulties

- "Escaped output prevents XSS" (DOM sinks break it). Fix: demo `innerHTML` writing a query-string value in the sandbox page.
- Students conflate CSRF with XSS (both "evil request"). Fix: the who-runs-it diagram; XSS runs *in* the origin, CSRF runs *against* it.
- SSRF feels exotic until the metadata example. Fix: draw the server's vantage point — "your server's permissions are the loot."

## Teaching Tips

- Station rotation needs visible timers; appoint timekeepers (they emerge naturally from Lab 02's role assignment).
- The verification exchange (pairs swap) doubles as peer instruction; keep pairs fixed, swap *builds* not people.
- Keep payloads demonstrative (an alert/visible marker), never destructive, inside the sandbox.

## Answer Keys **[KEY]**

- Station fixes: XSS → context-aware encoding + CSP; CSRF → token + `SameSite=Lax` (origin check acceptable as second); SSRF → egress allow-list + block link-local; IDOR → ownership check in the object-fetch path.
- Regression tests: XSS — re-render stored payload and assert no script execution; CSRF — post without token expecting 403; SSRF — fetch metadata IP expecting rejection; IDOR — other-user object fetch expecting 403/404.
- Exit ticket: 1 DOM-based; 2 token + SameSite (accept origin check); 3 predictability enables enumeration.

## Lab Delivery (Lab 06)

- Minimum viable outcome: two stations completed with verified fixes (stretch: all four).
- Expected failure points: stations share one app instance — reset script per rotation; SSRF station must have real egress disabled (fake-net) to stay sandboxed.

## Discussion Facilitation

Q2 (`SameSite=Strict` everywhere) produces the embedded-flow trade-off; let a student argue the payment-widget case. Q3 (IDOR ownership) seeds the CI-testability discussion that returns in L08 and M8.

## Accessibility

- The four-flows diagram: text transcription is in the student notes; read the four arrows aloud as sentences.
- Stations: large-print station cards; the lab checklist is keyboard-navigable; verification screenshots can be replaced by text transcript for students using assistive tech.
