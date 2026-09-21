# Teaching Guide — Lecture 05 (HTTP, Sessions, Authentication)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–10 | Hook: live login demo | Dev tools open; students see the cookie appear. |
| 10–35 | HTTP anatomy | Six sanitized captures decoded; students call the relevant header. |
| 35–55 | Cookies/sessions deep dive | Fill the attribute table live; rotation story at login. |
| 55–60 | Break | — |
| 60–100 | Lab 04 (auth-flow inspection) | Pairs; checklist-driven; screenshots required. |
| 100–112 | Auth model decision table | Session vs JWT vs OAuth code+PKCE. |
| 112–120 | Exit ticket + preview | Tease L06: "next we break what flows through sessions." |

## Board/Projector Activities

- **Projector:** dev tools (Network tab) on the demo app login; the `Set-Cookie` header magnified.
- **Board:** the browser↔server login sequence diagram from the student notes, redrawn live.

## Speaker Notes (key beats)

1. HTTP is stateless — say it twice; every cookie mechanism exists *because* of statelessness.
2. Cookie attributes are *controls*, each mapping to an attack; teach the table, not a list.
3. JWT: signed ≠ encrypted — the base64 reveal always lands; do it live (decode a token in dev tools).
4. PKCE: one sentence — "proof key binding so intercepted codes are useless"; details are optional reading.

## Expected Student Difficulties

- Students conflate `Secure` (transport) with `HttpOnly` (JS access). Fix: two-column table, one attack each.
- "Stateless = no revocation" is unintuitive. Fix: ask "if a stateless token leaks, who must forget it?" — nobody has it memorized; hence denylists.
- OAuth flows blur together. Fix: this course teaches *one* grant properly (code+PKCE); others are awareness-level.

## Teaching Tips

- Magnify the dev tools font before class; the back row must read `Set-Cookie`.
- The decision-table activity works printed: three columns (model / best for / revocation story).
- Keep the demo app login deliberately slightly wrong (missing `Secure`) — students should *catch* it; that is the lab seed.

## Answer Keys **[KEY]**

- Checklist weaknesses in Lab 04 (find-four exercise): missing `Secure`; missing `SameSite`; long-lived remember-me; MD5-derived session ID (accept rotation-absence). Keys to the corrected header: `Set-Cookie: sid=<128-bit random>; Secure; HttpOnly; SameSite=Lax; Max-Age=3600` + rotate on login.
- Exit ticket: 1 `HttpOnly`; 2 authorization code + PKCE; 3 possible open redirect/session fixation indicator.

## Lab Delivery (Lab 04)

- Minimum viable outcome: four documented weaknesses with screenshots.
- Expected failure points: dev tools in the wrong tab; HTTPS vs HTTP confusion in the sandbox (use the sandbox's self-signed cert as a teaching moment about trust prompts).

## Discussion Facilitation

Q1 (JWT revocation) pairs with the DS example — dashboards in localStorage. Q3: make students commit to one `SameSite` value per site type; hedging defeats the exercise.

## Accessibility

- Dev-tools demos: provide the "what you would see" transcription (student notes box) before the demo so screen-reader users can follow; then narrate changes as they happen.
- Sequence diagram: read aloud node by node; post the photo.
