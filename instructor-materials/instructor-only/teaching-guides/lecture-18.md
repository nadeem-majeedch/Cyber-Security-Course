# Teaching Guide — Lecture 18 (Asymmetric Crypto, PKI, TLS)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap mode table | Cold-call two rows. |
| 08–30 | Asymmetric tour | Two-key magic; DH colors analogy; no proofs. |
| 30–52 | TLS 1.3 walk | Annotate the capture message by message. |
| 52–60 | Break | — |
| 60–90 | Lab 16 (cert inspection + course CA) | Succeed once, fail on purpose once. |
| 90–105 | Trust-failure cases | One CA mis-issuance story + one expiry outage. |
| 105–115 | Pinning debate | Mobile banking framing; escape-hatch design. |
| 115–120 | Exit ticket + preview | Tease L19: "the other end of trust — passwords." |

## Board/Projector Activities

- **Projector:** the TLS 1.3 capture (ClientHello → certificate → Finished) annotated live; `openssl s_client` output.
- **Board:** the chain-of-trust ladder (root → intermediate → leaf) with the validation checks listed beside each rung.

## Speaker Notes (key beats)

1. Keep math conceptual: two-key magic, DH with the color-mixing analogy — state clearly that proofs exist and are optional reading.
2. The certificate's job: bind a *name* to a *key*, signed by someone your trust store already trusts. Everything else is bookkeeping around that sentence.
3. TLS 1.3: 1-RTT, forward secrecy by default, dead suites gone. Walk what each message *proves* — not what it contains.
4. Revocation is soft-fail in browsers; CT + short-lived certs are the modern compensations. State this as operational reality, not endorsement.
5. Pinning: the escape-hatch design (backup pin, expiry window, kill-switch) is the deliverable of the debate.

## Expected Student Difficulties

- Students want the modular-arithmetic details. Fix: park it; give the optional reading pointer (Boneh & Shoup).
- "Green padlock = safe site." Fix: TLS authenticates the binding, not the behavior; phishing sites have valid TLS.
- CA lab failures frustrate. Fix: the *deliberate* failure (wrong SAN) is part of the lab — reframe errors as curriculum.

## Teaching Tips

- Run `openssl s_client -brief` for the live demo — output is short and readable from the back row.
- The expiry-outage case works best told as operations drama (who gets paged, what the runbook says).
- Keep the pinning debate balanced: 3 minutes per side, then the escape-hatch design as synthesis.

## Answer Keys **[KEY]**

- Handshake annotations (model): ClientHello = offers versions/suites/key share; ServerHello+cert = server identity proof; Finished = key-confirmation; forward secrecy = session keys independent of long-term key later compromise.
- Lab expected errors: SAN mismatch → hostname verification failure; expired cert → date validation failure; untrusted root → trust-store failure. Each error nameable in one line.
- Exit ticket: 1 name (subject/SAN) to public key, signed by issuer; 2 any two of 1-RTT, forward secrecy by default, removed weak suites; 3 responder unavailability must not break the web (accept: latency/reliability trade-offs).

## Lab Delivery (Lab 16)

- Minimum viable outcome: one cert decoded (SAN/expiry/issuer) + one course-CA issuance that succeeds + one deliberate failure explained.
- Expected failure points: clock skew breaks validation (teaching moment); SAN spelling — make them type it wrong on purpose first.

## Discussion Facilitation

Q2 (pinning escape hatch) converges on: backup pin + short validity + remote config update — let teams design, then compare to industry practice. Q3 (forward secrecy) rewards the L17 connection: session keys die with the session.

## Accessibility

- TLS captures: provide the annotated message transcript; visual protocol diagrams get text equivalents.
- OpenSSL output: high-contrast, large-font pre-sets; the transcript file is the accessible artifact.
