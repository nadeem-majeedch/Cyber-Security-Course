# Teaching Guide — Lecture 12 (Phishing, Social Engineering, Awareness + Checkpoint C)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap restore plans | Two teams read their restore order. |
| 08–30 | Phishing dissection | Three synthetic mails; SPF/DKIM/DMARC verdict columns. |
| 30–48 | BEC storyboard | Annotate pretext markers; no-payload insight. |
| 48–60 | Break | — |
| 60–72 | **Checkpoint C** | 10 min + recap of most-missed. |
| 72–100 | Lab 11 (awareness campaign) | Team design; metrics table with targets. |
| 100–112 | MFA spot-stat | Why phishing-resistant beats OTP/push; compensating controls per lure. |
| 112–120 | M3 wrap + M4 preview | Bridge: "next we watch the wire these attacks traverse." |

## Board/Projector Activities

- **Projector:** the three sample mails (rendered inert — links point to a sandbox explanation page, attachments are text files).
- **Board:** the SPF/DKIM/DMARC three-column "what it proves / fails when" table, filled live.

## Speaker Notes (key beats)

1. The three mechanisms prove *different things*; the alignment failure (From vs. DKIM domain) is the classic spoof tell.
2. The killer insight: authentication proves the envelope, not the content — BEC rides real mailboxes and passes everything.
3. Metrics: click rate is the vanity metric; report rate and time-to-report measure the culture you need.
4. Phishing-resistant MFA binds to origin; push-bombing is the failure mode of naive approval prompts.
5. Consent and ethics for simulations: draft the consent paragraph *in class* (lab seed).

## Expected Student Difficulties

- Students over-trust "green checkmark" authentication indicators. Fix: the compromised-mailbox case — everything checks and it is still fraud.
- "Delete the phish = handled." Fix: report rate/time-to-report framing — the *system* learns from reports.
- Checkpoint C: commonly missed is the mail-auth policy record (DMARC) — recap with the table.

## Teaching Tips

- Render all sample mails inert before class (link-rewrite + attachment neutering); verify twice.
- The consent-paragraph drafting is delicate: let students propose, then show a model consent text (in the lab starter) — never mock real consent documents.
- Keep the BEC storyboard factual: no real company names; the pattern is the lesson.

## Answer Keys **[KEY]**

- Mail verdicts (expected): Mail 1 — SPF pass/DKIM fail, From/envelope mismatch → spoof tell; Mail 2 — all pass but homoglyph lookalike domain → infrastructure tell; Mail 3 — all pass, real compromised mailbox → content/process tell (BEC).
- Checkpoint C: see `assessments/instructor-only/checkpoint-keys.md` §C.
- Exit ticket: 1 DMARC; 2 any two of authority/urgency/scarcity/social proof; 3 report rate (accept time-to-report).

## Lab Delivery (Lab 11)

- Minimum viable outcome: campaign design with ≥ 3 metrics (≥ 2 beyond click rate) and a consent/ethics paragraph.
- Expected failure points: teams propose shaming leaderboards — redirect via the reporting-culture evidence; escalation path often missing — require the "who reads reported mails within X minutes" line.

## Discussion Facilitation

Q1 (shaming → reporting) works with a think-pair-share: predict the effect, then give the counter-intuition. Q3 (consent line): students write first, discuss after — owning the line matters more than getting it "right."

## Accessibility

- Sample mails: provide plain-text transcriptions alongside rendered images.
- The three-column auth table: high-contrast handout; read column headers aloud.
- Campaign design: offer a structured template (sections pre-labeled) so executive-function load stays on content, not formatting.
