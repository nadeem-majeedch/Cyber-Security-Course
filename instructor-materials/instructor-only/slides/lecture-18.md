---
marp: true
theme: course
paginate: true
footer: 'Cyber Security · L18 · Module 5 · Week 9'
---

<!-- _class: lead -->
# Lecture 18 — Cryptography II
## PKI, TLS 1.3 & Trust Chains
**Module 5 · Week 9 · 120 min · CLO-5 (primary), CLO-7 (supporting)**

<!--
TIMING: 1 min. Hook: click the padlock in the browser — "this icon is a chain of promises."
-->

---

# Learning Objectives

1. Walk the **TLS 1.3** handshake stages
2. Explain certificates as **identity bindings**
3. Trace a CA chain; explain pinning's tradeoffs
4. Read a TLS capture's metadata (from L13)

<!--
3 min. Lab 16 does the handshake walk live.
-->

---

# TLS 1.3 handshake

```
ClientHello (+key share) ─►
                         ◄─ ServerHello + cert + Finished
Client Finished ─►
[Application data, keys from ephemeral ECDHE + HKDF]
```

*Describe: three-arrow handshake sequence ending in key derivation from ephemeral Diffie-Hellman plus HKDF.*

<!--
1-RTT; forward secrecy BY DEFAULT (checkpoint D item 5). 6 min.
-->

---

# Certificates & chains

```
[leaf: portal.example] ← signs [intermediate CA] ← signs [root CA (trusted store)]
```

*Describe: three-element chain; the browser trusts the root, which vouches for the intermediate, which binds the server name to its key.*

<!--
Certificate = name↔key binding (checkpoint D item 4). Expiry/SAN checks in Lab 16. 5 min.
-->

---

# Pinning & its costs

| Control | Benefit | Cost |
|---|---|---|
| CA pinning | limits who can vouch | ops risk on rotation |
| CT logs | public issuance record | none for clients |

*Describe: two-row control table; pinning narrows trust at operational price, CT adds transparency.*

<!--
Pinning gone wrong = bricked app (misconception: "always pin"). 4 min.
-->

---

# CS example — internal PKI

- Corporate CA + short-lived certs for services; automation owns rotation
- Expiry monitoring is a DETECTIVE control (L04 taxonomy)

<!--
2 min.
-->

---

# DS example — data-plane TLS

- Pipeline-to-warehouse TLS with internal CA; mTLS between microservices
- Same trust-chain reasoning, service names as identities

<!--
2 min.
-->

---

# Lab demo — Lab 16 (PKI & TLS)

- Instructor generates a root + leaf cert (course CA), serves TLS, then breaks trust (untrusted CA) and shows the browser/clap rejection
- **MVO:** chain validated in openssl + one deliberate failure explained
- Sandbox CA only — never import course CA to host trust stores

<!--
DEMO 6 min. The BREAK is the lesson: trust is configured, not magical.
-->

---

# Case session

**CS-046 "Cipher-suite debate"** (Level 3 · Cryptography)

→ which suite arguments survive TLS 1.3's defaults?

<!--
10 min. Model: suite debates mostly dissolve; key management remains.
-->

---

# Wrap-up & exit ticket

- Handshake: ephemeral keys; certs: name↔key; trust: configured chain
- **Exit:** why does TLS 1.3 give forward secrecy by default?

<!--
Close 110. Preview L19: passwords.
-->

---

# References

- RFC 8446 (TLS 1.3); lecture plan lecture-18; Lab 16
