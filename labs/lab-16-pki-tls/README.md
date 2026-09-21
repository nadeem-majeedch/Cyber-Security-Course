# Lab 16 — Certificates, PKI & TLS Inspection
**Enrichment · Module 5 (L18) · CLO-5 (primary), CLO-7 (supporting) · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Inspect a live (in-scope) TLS connection: chain, SAN, expiry, issuer.
2. Issue certificates from the course CA; succeed once, fail once on purpose (SAN mismatch).
3. Annotate a TLS 1.3 capture message-by-message (what each side proves).
4. Design the expiry-monitoring fix for the expiring-cert scenario.

## Prerequisites
Lecture 18. Lab 00's verification discipline.

## Hardware/Software Requirements
Course VM: OpenSSL 3.x, Wireshark, the course-CA kit (`starter/course-ca/`), the lab TLS server (`tlsdemo`, loopback-only `https://127.0.0.1:8443`), the prepared TLS 1.3 capture.

## Installation and Setup
```bash
sudo docker start tlsdemo && sudo docker port tlsdemo    # expect 127.0.0.1:8443
openssl s_client -connect 127.0.0.1:8443 -brief < /dev/null
```

## Ethical Authorization and Safety Notes
- The only TLS endpoint inspected is the course's own `tlsdemo` (loopback). Do not run `s_client`/scans against any public host — the "live site" inspection in lecture uses the instructor's projected screen, not yours.
- The course CA is for the lab network only; never add lab CAs to a personal browser's trust store (and remove the lab trust after the session — cleanup step).

## Step-by-Step Student Tasks
1. Chain inspection: `openssl s_client -connect 127.0.0.1:8443 -showcerts` — decode the leaf (subject/SAN/expiry/issuer) with `openssl x509 -text`.
2. **Deliberate failure:** request a cert for `wrong-name.lab` from the course CA; serve it; observe and name the client error.
3. **Deliberate success:** issue for `tlsdemo.lab` with correct SAN; verify the chain builds and the browser/tool accepts.
4. Handshake annotation: open the prepared TLS 1.3 capture; label ClientHello/ServerHello/cert/Finished with "what is proven here" (worksheet table).
5. Forward-secrecy note: identify the key-share in the capture; state in one sentence what FS protects.
6. Scenario: the "cert expires in 6 days" exercise — write the risk analysis, two interim mitigations, and the ACME-automation long-term fix.

## Expected Observations
SAN mismatch → hostname-verification failure (exact error text recorded). Correct SAN → clean chain. The capture shows a 1-RTT handshake with key share (no RSA key transport).

## Questions for Analysis
1. Why does the SAN error appear *before* any application data flows — and what attack does that ordering prevent?
2. Your mitigation list for the expiring cert: why is "buy more time from the vendor" not a mitigation, and what is the difference between mitigating and deferring?

## Troubleshooting
`verify error: self-signed` on the success case → the course CA is not in the VM trust store yet (setup note in `starter/course-ca/README`); use `--cacert` for curl or add per instructions. Handshake capture won't decrypt → expected: TLS 1.3 with (EC)DHE keeps sessions private; annotation works on the *metadata*, which is the lesson.

## Cleanup Instructions
`sudo docker stop tlsdemo`; remove the course CA from any trust store you added it to; delete issued keys/certs from `~/`.

## Submission Requirements
Leaf-certificate decode table, error text from the deliberate failure, success-case chain output, annotation table, FS note, scenario deliverable.

## Expected Outputs / Evidence
The exact error strings (copied, not paraphrased) are the evidence for the failure case.

---
### Instructor Answer Key (summary)
- Failure case expected error: hostname mismatch / `SSL: CERTIFICATE_VERIFY_FAILED` (certificate is valid for `tlsdemo.lab`, requested `wrong-name.lab`).
- Annotation (model): ClientHello = offers versions/suites + key share; ServerHello+cert = server identity proof; Finished = key confirmation both ways; FS = session keys die with the session even on later long-term-key compromise.
- Scenario (model): risk = browser errors at expiry (7×24 app outage); mitigations = temporary internal CA override for *lab* tools only, comms plan; long-term = ACME auto-renewal + expiry monitoring with runbook.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Leaf decode + chain inspection | 3 |
| Deliberate failure (exact error) + deliberate success | 3 |
| Handshake annotation + FS note | 2 |
| Expiring-cert scenario deliverable | 2 |
