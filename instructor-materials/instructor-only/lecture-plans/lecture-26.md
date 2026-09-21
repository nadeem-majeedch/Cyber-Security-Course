# Lecture 26 — Cloud Security II: Containers, Serverless, and Secrets
**Module M7 · Week 13, Session 2 · 120 min · CLO-7 (primary)**

## Learning Objectives
1. Harden container images and runtimes: minimal bases, non-root users, capability dropping, image scanning gates.
2. Explain container-isolation boundaries and their limits (kernel sharing, escape-class CVEs awareness, runtime options).
3. Secure serverless patterns: event-injection surfaces, over-privileged function roles, cold-start secrets handling.
4. Implement secrets management for cloud workloads: brokered short-lived credentials, no secrets in env-vars-as-config confusion, workload identity.

## Key Concepts
- Image supply chain: base-image provenance, SBOM (revisits L08), signing, admission gates
- Isolation: namespaces/cgroups (concept), what escapes mean, VM-based sandboxing trade-offs
- Kubernetes objects relevant to security: RBAC, NetworkPolicies, Pod Security Standards (awareness level)
- Serverless: per-function roles, event-source trust, dependency layers
- Workload identity: the platform vouches for the workload — no static keys (the L19/L25 secret thread completes)

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L25: escalation-map findings | Q&A |
| 08–30 | Container anatomy: layers, what `docker build` bakes in; instructor hardens a fat root image live (multi-stage, non-root, dropped caps) — size and CVE count drop on screen | Live demo |
| 30–50 | Isolation honesty: what a container shares with the host; escape CVE story (high level); when to demand VM isolation | Discussion |
| 50–60 | Break | — |
| 60–105 | **Lab block (Lab 24):** three-part — (a) harden a provided vulnerable image to pass a scanner gate, (b) fix a K8s pod spec (run-as-non-root, no privilege escalation, NetworkPolicy), (c) replace a function's static cloud key with workload identity | Hands-on |
| 105–115 | Secrets pattern gallery: env-var leak, CI log leak, image-layer archaeology; students map each to the correct control | Pattern gallery |
| 115–120 | Exit ticket; preview L27 (cloud detection) | Q&A |

## Examples
- **CS track:** image-scanner gate in CI: build fails on critical CVE in base; students argue the exception process (no unbounded waivers).
- **DS track:** a training job container with the dataset bucket key baked into the layer — students extract it (lab-safe), then fix with workload identity + scoped role.

## Discussion Questions
1. Minimal images reduce CVEs — what operational friction do they add, and how do teams adapt?
2. "Containers are sandbox for untrusted code" — where does that claim break?
3. Who owns pod-security policy exceptions in a platform team, and how is the request audited?

## Student Activity
Image-hardening to pass a gate; pod-spec fixing; secrets-pattern matching exercise.

## Problem-Solving Scenario
> An ML inference service: `python:latest` base, root user, mounting the Docker socket "for convenience," static bucket key in an env var. Produce: the risk list (each with the incident that would follow), the hardened spec diff, and the rollout order that avoids downtime.

## Summary
Workload security is supply chain + isolation honesty + identity brokering. Bake less, run with less, vouch through the platform rather than copying keys. L27 watches the cloud estate in operation — logging and misconfiguration detection.

## Formative Assessment
1. Name three hardening moves for a container image.
2. What does the Docker socket mount actually grant?
3. Why does workload identity beat static keys?

## Required Resources
- `labs/lab-24-containers/` vulnerable image + pod specs + function sample
- CIS Benchmarks (Docker/K8s, selected items); provider workload-identity docs
- CLO mapping: **CLO-7** (objectives 1–4).
