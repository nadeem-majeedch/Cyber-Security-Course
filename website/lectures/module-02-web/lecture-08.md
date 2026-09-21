# Lecture 08 — Secure SDLC, Dependency Hygiene, Security Headers + Checkpoint B
**Module 2 · Week 4, Session 2 · 2 hours · CLO-2**

## Learning Objectives
1. Place SAST, DAST, and SCA in a CI pipeline and interpret their findings honestly.
2. Configure the core security headers and verify them.
3. Triage vulnerabilities by severity and exploitability; propose patch SLAs.
4. Consolidate Module 2 (Checkpoint B).

## Key Concepts and Definitions

**Secure SDLC:** security activities at defined gates — design review (before code), code review + **SAST** (in PR), **SCA** + dependency policy (in CI), **DAST** (against running staging), release checklist.

**The three scanner families:**

| Type | Sees | Blind to | Typical noise |
|---|---|---|---|
| SAST (source) | Code-level sinks/flows | Runtime config, dependencies | High false positives |
| DAST (running app) | Reachable flaws in *this* build | Code paths you can't reach | Medium |
| SCA (dependencies) | Known-vulnerable versions | Your own code, unpublished CVEs | Low (version truth) |

**Software supply chain:** **SBOM** (a machine-readable inventory of components), **pinning** (exact versions, verified checksums), **provenance** (cryptographic attestation of where a build came). The failure story to know: **dependency confusion** — an internal package name uploaded publicly to a registry gets fetched by your build because the resolver prefers the public name; mitigations: registry scoping, pinning, provenance checks.

**Security headers:**

| Header | Purpose |
|---|---|
| `Content-Security-Policy` | Restricts script/style/media sources (L07) |
| `Strict-Transport-Security` (HSTS) | Forces HTTPS for future visits (needs HTTPS first) |
| `X-Content-Type-Options: nosniff` | Blocks MIME-type guessing (stops some payload injection) |
| `X-Frame-Options` / CSP `frame-ancestors` | Anti-clickjacking framing control |
| `Referrer-Policy` | Limits referrer leakage |

**Triage discipline:** CVSS severity is a *base* signal; your decision adds exploitability (public exploit? internet-exposed?) and compensating controls. Patch SLA policies (e.g., "critical-exposed: 48 h") are organizational commitments, not math.

## Conceptual Diagram

```text
dev PR ──► SAST + SCA ──► CI build ──► staging ──► DAST + header check ──► release
              │fails?                       │fails?
              ▼                             ▼
        fix & re-request             block promotion
```

## Realistic Examples

- **CS track:** a PR adds an unpinned dependency and an `eval()` in a utility: SCA flags the dependency, SAST flags the sink; students write the triage comments that resolve both.
- **DS track:** `requirements.txt` with `pandas` unpinned plus a typosquatted package name in the lockfile: SCA catches both; SBOM generation gives the audit trail the data team lacked.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "The scanner passing means we're secure" | Scanners see categories, not business logic or novel flaws. |
| "False positives mean the tool is bad" | Noise is a tuning problem: baselining and suppression-with-justification are part of operating the tool. |
| "Headers are optional polish" | CSP and HSTS are real exploit-rate reducers; they are controls, not decoration. |
| "Pinning hurts security because you miss updates" | Pin *and* automate updates (renovate-style bots) — controlled change beats drift. |

## Classroom Activities

1. **Pipeline build-out (20 min, Lab 07 part A):** add SCA + SAST jobs to the demo repo; triage five seeded findings.
2. **Headers lab (20 min, Lab 07 part B):** set the header set; verify with a checker; fix one CSP violation.
3. **Checkpoint B (12 min):** Module 2 quiz.

## Discussion Questions

1. SAST reports 400 findings, 380 false positives. What happens to the tool's credibility — and how do you fix the *program* rather than the tool?
2. Which headers are worthless without HTTPS, and why does HSTS deserve a preload discussion?
3. Should a critical CVE in a transitive dependency block release? Write the decision rule.

## Problem-Solving Exercise

> Release is Friday. The scanner shows: a critical RCE in a web framework (public exploit exists), a medium header gap, a license conflict.
> **Deliverable:** triage table (severity, exploitability, exposure); go/no-go recommendation with reasoning; a two-line CI policy that prevents recurrence.

## Summary

Flaws fixed one by one (L05–L07) stay fixed only when the *process* hunts them: scanners with tuned expectations, headers as defaults, dependency hygiene with provenance. Module 3 now follows malicious code onto the endpoint — what it does once inside.

## Exit Ticket

1. Which scanner type finds a vulnerable library version? Which finds a reflected XSS at runtime?
2. What does `nosniff` prevent?
3. Name one CVSS base metric and what it captures.

## References

- OWASP, *Secure Headers Project*. https://owasp.org/www-project-secure-headers/
- FIRST, *CVSS v3.1 Specification* (base metric group). https://www.first.org/cvss/
- CISA, *SBOM* resources. https://www.cisa.gov/sbom
- Ohm, W. et al., "Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks," *DIMVA*, 2020 (dependency-confusion class taxonomy).
