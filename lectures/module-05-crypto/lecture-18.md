# Lecture 18 — Asymmetric Cryptography, PKI, and TLS
**Module 5 · Week 9, Session 2 · 2 hours · CLO-5 (primary), CLO-7 (supporting)**

## Learning Objectives
1. Explain asymmetric primitives' roles (key exchange, signatures) at concept level.
2. Walk the TLS 1.3 handshake and state what each message proves.
3. Describe the PKI trust model: chains, revocation basics, certificate transparency.
4. Evaluate pinning trade-offs and design certificate-lifecycle hygiene.

## Key Concepts and Definitions

**Asymmetric pairs:** a **public** key (share freely) and a **private** key (never share). Two jobs: **key agreement** (two parties derive a shared secret over an open channel — Diffie–Hellman family) and **digital signatures** (sign with private, verify with public — RSA/ECDSA family). Encryption-at-scale with public keys is *not* the use case; it is too slow — symmetric keys are exchanged asymmetrically, then bulk data rides symmetrically (L17).

**Certificates bind keys to names:** a certificate = identity (subject/SAN) + public key + issuer's signature, chained up to a **root CA** the OS/browser already trusts. Intermediates sign the leaves; chains are validated path-by-path (expiry, purpose, revocation).

**TLS 1.3 handshake (what each side proves):**

```text
ClientHello: versions, cipher suites, key share          → client offers
ServerHello + {certificate} + Finished                   → server proves identity,
                                                           both derive session keys (1-RTT)
client Finished                                          → client proves possession
Forward secrecy: session keys die with the session even if the long-term key leaks later
```

**Revocation reality:** CRLs (lists) and OCSP (per-cert queries) exist, but browsers mostly **soft-fail** (unreachable responder ⇒ accept). Compensations: **Certificate Transparency** logs (mis-issuance becomes detectable), short-lived certificates, ACME automation.

**Pinning:** hard-coding the expected certificate/key in the client. Benefit: CA compromise can't MITM you. Cost: operational fragility — cert rotation mistakes brick the app. Modern stance: pin *CA-level* or rely on CT + short lifetimes; never pin leaf certs casually.

## Conceptual Diagram

```text
Root CA (in OS/browser trust store)
   └── Intermediate CA (signs leaves)
         └── server cert: CN/SAN = app.example.edu + public key     ← TLS presents this chain

trust question: can I build an unbroken, unexpired, purpose-valid path to a root I already trust?
```

## Realistic Examples

- **CS track:** internal mTLS: students issue client + server certs from the course CA; a SAN mismatch produces the browser/client error — the chain-verification lesson made tangible.
- **DS track:** a data pipeline to a warehouse using self-signed certificates: trust-store hygiene (who imports what), expiry monitoring as an ops duty, and the transport-vs-at-rest encryption distinction (L17).

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "TLS means the site is trustworthy" | TLS authenticates a key↔name binding; it says nothing about the site's *behavior*. |
| "The padlock proves the certificate is valid *and* unrevoked" | Validity checks are local; revocation is mostly soft-fail — hence CT/short-lived certs. |
| "Public-key encryption is how bulk data moves" | It is too slow; it *exchanges* symmetric keys instead. |
| "Pinning is always safer" | Rotation mistakes cause outages; pin conservatively (CA-level) or use CT + automation. |

## Classroom Activities

1. **Certificate inspection (20 min, Lab 16 part A):** inspect a live site's chain; decode a cert (SAN, expiry, issuer); break one deliberately (wrong SAN) and read the error.
2. **Course-CA lab (25 min, Lab 16 part B):** issue a cert to the lab server; succeed and fail on purpose.
3. **Handshake annotation (10 min):** label each TLS 1.3 message with "what is proven here."

## Discussion Questions

1. Why does soft-fail revocation leave a gap, and what compensates (CT, short-lived certs)?
2. Pinning blocks CA-compromise MITM but bricks apps on rotation mistakes — design the escape hatch.
3. What does forward secrecy protect that plain RSA key transport did not?

## Problem-Solving Exercise

> An internal dashboard shows "certificate expires in 6 days"; the vendor's renewal portal is unreachable.
> **Deliverable:** risk analysis (what breaks, when); two interim mitigations; the long-term fix (ACME automation + expiry monitoring) and the renewal policy.

## Summary

Asymmetric crypto turns secret-sharing into trust delegation: certificates bind keys to names, PKI vouches, TLS does the work — and the operational duties (expiry, revocation, transparency) are where trust actually holds or fails. Next: the humble password, the other end of the trust chain.

## Exit Ticket

1. What does a certificate bind?
2. Name two improvements TLS 1.3 has over TLS 1.2.
3. Why is revocation "soft" in browsers?

## References

- RFC 8446 (TLS 1.3). https://datatracker.ietf.org
- NIST SP 800-57 Part 1 (key management recommendations). https://csrc.nist.gov
- Certificate Transparency project. https://certificate.transparency.dev
- Let's Encrypt / ACME documentation. https://letsencrypt.org/docs/
