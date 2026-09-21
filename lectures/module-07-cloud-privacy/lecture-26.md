# Lecture 26 — Cloud Security II: Containers, Serverless, and Secrets
**Module 7 · Week 13, Session 2 · 2 hours · CLO-7**

## Learning Objectives
1. Harden container images and runtimes: minimal bases, non-root, capability dropping, scanner gates.
2. Explain container-isolation boundaries and their limits honestly.
3. Secure serverless patterns: event-injection surfaces, per-function roles.
4. Replace static secrets with workload identity and brokered credentials.

## Key Concepts and Definitions

**Image supply chain:** an image is layered filesystem + config; everything in the build is baked in. Hardening moves: **minimal base images** (fewer packages = fewer CVEs), **multi-stage builds** (build tools never ship), **non-root user**, **read-only root filesystem**, **dropped capabilities** (the Linux capability list, not all-or-nothing root), and **scanner gates** in CI (build fails on critical CVEs — with a *bounded* exception process).

**Isolation honesty:** containers share the host kernel; isolation comes from namespaces/cgroups. Stronger isolation (VM-based sandboxes / micro-VMs) trades density for boundaries. Rule of thumb: untrusted code demands harder boundaries than trusted internal workloads — know which you are running.

**Kubernetes objects that matter (awareness level):** RBAC (who may do what to the API), **NetworkPolicies** (pod-to-pod allow-lists — the L14 segmentation idea inside the cluster), Pod Security Standards (run-as-non-root, no privilege escalation).

**Serverless:** functions with **per-function roles** (not one fat role for the app), event-source trust (who can invoke), and dependency layers (the supply chain again — L08).

**Workload identity:** the platform vouches for the workload ("this pod/function is what it claims"), brokering short-lived cloud credentials — no static keys baked anywhere. This completes the L19/L25 secrets thread.

**Secrets pattern gallery (where static secrets leak):** environment variables (visible in configs, dumps, child processes), CI logs (echoed values), **image layers** (a secret in an early layer persists even if "deleted" later — layers are additive).

## Conceptual Diagram

```text
build:  fat base + root + build tools + secret in layer   ✗
        → minimal base + multi-stage + non-root + no secrets + SBOM + scan gate  ✓
run:    read-only rootfs · drop capabilities · NetworkPolicy allow-lists
secrets: workload identity → brokered short-lived creds → vault with access logging
```

## Realistic Examples

- **CS track:** the CI scanner gate: build fails on a critical CVE in the base image; students write the exception policy that doesn't rot ("waivers expire; waivers name an owner").
- **DS track:** a training-job container with the dataset-bucket key baked into an early layer: students extract it (lab-safe), then fix with workload identity + a scoped role — the layer-archaeology lesson lands personally.

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Containers are sandboxes for untrusted code" | They are process isolation on a shared kernel; untrusted code wants VM-level boundaries. |
| "Deleting a secret from a later layer removes it" | Layers are additive; the secret persists in history — rebuild from a clean stage. |
| "One app-wide role is simpler" | It is simpler *to build* and simpler to abuse; per-function roles bound the blast radius. |
| "Scan once at build, safe forever" | New CVEs appear after you ship; scheduled re-scans and base-image updates are the control. |

## Classroom Activities

1. **Live hardening demo (20 min):** fat root image → minimal, non-root, no build tools; watch size and CVE count drop on screen.
2. **Lab 24 (45 min):** (a) harden the provided image to pass the scanner gate, (b) fix the pod spec (non-root, no priv-esc, NetworkPolicy), (c) replace the static key with workload identity.
3. **Secrets pattern gallery (10 min):** map each leak pattern to its control.

## Discussion Questions

1. Minimal images reduce CVEs — what operational friction do they add, and how do teams adapt?
2. "Containers are a sandbox for untrusted code" — where does that claim break?
3. Who owns pod-security exceptions in a platform team, and how is each request audited?

## Problem-Solving Exercise

> An ML inference service: `python:latest` base, root user, Docker socket mounted "for convenience," static bucket key in an env var.
> **Deliverable:** the risk list (each with the incident that would follow); the hardened spec diff; the rollout order that avoids downtime.

## Summary

Workload security is supply chain + isolation honesty + identity brokering: bake less, run with less, and let the platform vouch instead of copying keys. Next lecture watches the estate in operation — audit trails and misconfiguration management.

## Exit Ticket

1. Name three hardening moves for a container image.
2. What does the Docker socket mount actually grant?
3. Why does workload identity beat static keys?

## References

- NIST SP 800-190, *Application Container Security Guide*. https://csrc.nist.gov
- Kubernetes docs, *Pod Security Standards*, *Network Policies*. https://kubernetes.io/docs/
- CIS Benchmarks (Docker/Kubernetes). https://www.cisecurity.org
- CISA/NSA, *Kubernetes Hardening Guidance*. https://www.cisa.gov
