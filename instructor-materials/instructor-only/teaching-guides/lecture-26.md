# Teaching Guide — Lecture 26 (Containers, Serverless, Secrets)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–08 | Recap: escalation maps | Two teams present one path each. |
| 08–30 | Live hardening demo | Fat root image → minimal/non-root; size + CVE counts drop. |
| 30–50 | Isolation honesty + K8s objects | Shared-kernel truth; RBAC/NetworkPolicy/PSS awareness. |
| 50–60 | Break | — |
| 60–105 | Lab 24 (image, pod spec, workload identity) | Three parts. |
| 105–115 | Secrets pattern gallery | env-var / CI-log / layer-archaeology → controls. |
| 115–120 | Exit ticket + preview | Tease L27: "watching the estate." |

## Board/Projector Activities

- **Projector:** the hardening demo terminal (image size + scanner output before/after); the layer-archaeology extraction of the baked secret (lab-safe).
- **Board:** the hardening checklist (base/user/stages/caps/rootfs) as a wall list students tick in the lab.

## Speaker Notes (key beats)

1. "Bake less, run with less, vouch through the platform" — the lecture in three clauses.
2. Isolation honesty: shared kernel = namespaces/cgroups; untrusted code wants micro-VM boundaries. Know which you run.
3. Layers are additive: deleting a secret in a later layer leaves it in history — rebuild from a clean stage.
4. Per-function roles, not one fat app role: blast radius is the design variable.
5. Workload identity completes the secrets arc (L19 → L25 → here): the platform vouches; keys stop being copied.

## Expected Student Difficulties

- Students equate "container" with "sandbox." Fix: the shared-kernel sentence + the micro-VM contrast; name the trust decision explicitly.
- K8s YAML volume is intimidating. Fix: the pod-spec exercise changes three fields in a provided spec — surgical, not authoring.
- The scanner gate feels like friction. Fix: the exception policy design (expiring, owned waivers) is part of the lab — process, not just tooling.

## Teaching Tips

- Pre-pull all images before class; registry latency kills the demo window.
- The layer-archaeology demo is the memorable one: extract the baked secret live, then fix it — the arc from exploit to control in five minutes.
- Keep the CIS/K8s hardening references at awareness level; the course's depth stays at design decisions, not operator certification.

## Answer Keys **[KEY]**

- Lab 24 expected fixes: image → minimal base + multi-stage + non-root + dropped caps + read-only rootfs; pod spec → runAsNonRoot, allowPrivilegeEscalation false, NetworkPolicy egress to broker only; secrets → workload identity, scoped role, no static key.
- Risk list for the scenario: Docker-socket mount = host-root-equivalent compromise; `latest` base = drifting supply chain; root + secrets = fast path from RCE to data; static key = unrevocable access.
- Exit ticket: 1 minimal base / non-root / drop caps (accept multi-stage, read-only rootfs); 2 root-equivalent access to the host daemon; 3 short-lived, revocable, platform-vouched.

## Lab Delivery (Lab 24)

- Minimum viable outcome: image passes scanner gate + pod spec fixed + static key replaced.
- Expected failure points: scanner gate blocks *everything* initially — the bounded-waiver exercise is the intended path; workload-identity setup is provider-specific — use the course's pre-configured cluster role.

## Discussion Facilitation

Q1 (minimal-image friction) rewards honesty: debugging without shells, smaller package ecosystems — teams name the cost, then the adaptation (ephemeral debug containers). Q3 (exception ownership) previews platform-team governance in the capstone.

## Accessibility

- Terminal demos: outputs mirrored to a text file shared in the LMS; the hardening diff is a readable patch file.
- YAML exercises: starter files annotated with "change only these lines" comments — reduces cognitive load for screen-reader navigation too.
