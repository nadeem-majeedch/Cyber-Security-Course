# Lecture 18 — Asymmetric Cryptography, PKI, and TLS
**Module M5 · Week 9, Session 2 · 120 min · CLO-5 (primary) · CLO-7 (supporting)**

## Learning Objectives
1. Explain asymmetric primitives' roles (key exchange, signatures, encryption at small scale) without descending into math beyond course scope.
2. Walk the TLS 1.3 handshake: certificates, key agreement, and what each side proves.
3. Describe the PKI trust model: roots, intermediates, revocation (CRL/OCSP basics), and CA compromise consequences.
4. Evaluate pinning and certificate-transparency concepts; connect TLS failures to real outages/breaches.

## Key Concepts
- Public/private key pairs; Diffie–Hellman key agreement (conceptual); RSA/ECDSA signatures
- Certificates: subject, SAN, chain of trust; intermediates; expiry automation (ACME)
- TLS 1.3: 1-RTT handshake, forward secrecy by default, cipher-suite hygiene
- Revocation: why browsers mostly soft-fail; CT logs and expectation failures
- Pinning: benefits, operational risk (bricking), modern alternatives

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L17 mode table | Q&A |
| 08–30 | Asymmetric tour: two-key magic in three use cases; DH sketch with colors analogy (no modular arithmetic proofs) | Whiteboard |
| 30–52 | TLS 1.3 handshake walk with a real capture: ClientHello → certificate → key share → finished; students annotate each message's proof | Capture annotation |
| 52–60 | Break | — |
| 60–90 | **Lab block (Lab 16):** OpenSSL certificate inspection lab — inspect a live site's chain, decode a cert, find SAN/expiry/issuer; then the course CA: issue a cert to a lab server and break it deliberately (wrong SAN) to see browser errors | Hands-on |
| 90–105 | Trust-failure case: one CA-mis-issuance story + one expired-cert outage; students map each to PKI concepts | Case discussion |
| 105–115 | Pinning debate: mobile banking app pins — availability vs. security; alternatives (CT monitoring) | Debate |
| 115–120 | Exit ticket; preview L19 (hashing/passwords) | Q&A |

## Examples
- **CS track:** internal service mesh mTLS: students issue client+server certs from the course CA and watch a connection succeed/fail on SAN mismatch.
- **DS track:** data-pipeline TLS: a Spark/warehouse connection using self-signed certs — trust-store hygiene, expiry monitoring as an ops-DS concern; encrypted transport vs. encrypted-at-rest distinction.

## Discussion Questions
1. Why does soft-fail revocation create a gap, and what compensates for it (CT, short-lived certs)?
2. Pinning prevented FIDDLE-class attacks but bricked apps when certs rotated — how would you design the escape hatch?
3. What does forward secrecy protect that plain RSA key transport did not?

## Student Activity
Certificate inspection worksheet; CA lab in pairs; handshake annotation on the provided capture.

## Problem-Solving Scenario
> Internal dashboard shows "certificate will expire in 6 days" and the team cannot reach the vendor. Produce: the risk analysis (what breaks, when), the two interim mitigations, and the long-term fix (ACME automation + monitoring) with the renewal policy.

## Summary
Asymmetric crypto turns secret-sharing into trust delegation: certificates bind keys to names, PKI vouches, TLS does the work. When the vouching fails, everything downstream fails — so expiry, revocation, and transparency are operational security. L19: the other endpoint of the trust chain — the humble password.

## Formative Assessment
1. What does a certificate bind?
2. Name two things TLS 1.3 improves over TLS 1.2.
3. Why is revocation "soft" in browsers?

## Required Resources
- `labs/lab-16-pki-tls/` course CA kit + OpenSSL worksheet
- TLS 1.3 handshake capture (sanitized); Cloudflare/OpenSSL docs
- CLO mapping: **CLO-5** (objectives 1–4); **CLO-7** seed (operational compliance angle).
