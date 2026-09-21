# Lab 24 — Container & Workload Hardening
**Enrichment · Module 7 (L26) · CLO-7 · Duration: 2 hours · Check-in lab**

## Learning Objectives
1. Harden a provided fat, root-based image to pass a scanner gate (minimal base, multi-stage, non-root, dropped caps).
2. Fix a seeded pod spec (run-as-non-root, no privilege escalation, NetworkPolicy).
3. Replace a static cloud key with workload identity (pre-configured course cluster role).
4. Map the secrets-pattern gallery (env var / CI log / image layer) to controls.

## Prerequisites
Lecture 26. Docker basics from Lab 05/06 usage.

## Hardware/Software Requirements
Course VM: Docker, the provided `ml-infer:weak` image + build kit (`starter/Dockerfile.weak`, `app/`), scanner gate script, the course K8s sandbox (`starter/pod-weak.yaml`, cluster role pre-configured).

## Installation and Setup
```bash
docker images | grep ml-infer          # weak image present
./starter/scan-gate.sh ml-infer:weak   # baseline scan: expect failures
```

## Ethical Authorization and Safety Notes
- The "extracted secret" in the layer-archaeology step is a synthetic classroom key embedded by the course build; extraction is done with the provided `starter/layer-lab.sh` on your own machine.
- The K8s sandbox is course-owned and single-tenant; the NetworkPolicy exercise affects only your own namespace.

## Step-by-Step Student Tasks
1. Baseline: record image size, user, layer count, scanner findings for `ml-infer:weak`.
2. Harden the Dockerfile: minimal base + multi-stage + non-root `USER` + drop capabilities + read-only rootfs; build as `ml-infer:hardened`.
3. Pass the scanner gate (zero critical findings); record new size/user/layer stats.
4. **Layer archaeology:** run `layer-lab.sh` on the weak image; extract the baked key; confirm it is *gone* from the hardened build (rebuild from a clean stage).
5. Pod spec: fix `pod-weak.yaml` (three fields); apply to your sandbox namespace; verify with `kubectl exec` that the container runs as non-root and cannot escalate.
6. Workload identity: replace the static bucket key with the pre-configured cluster role; verify the app still reads its (sandbox) object.
7. Gallery: env-var / CI-log / layer patterns → the control for each.

## Expected Observations
Image shrinks ~5–10×; scanner gate goes red→green; the layer archaeology finds the key in the weak image's early layer *and* confirms absence post-rebuild. Pod: non-root verified; NetworkPolicy blocks the seeded cross-namespace probe.

## Questions for Analysis
1. Your hardened image dropped the shell (minimal base). Name one debugging capability you lost and the platform-native replacement.
2. The static key "worked" until it didn't — state the exact incident it enables, and why workload identity changes the blast radius rather than just the hygiene.

## Troubleshooting
Gate still fails on one finding → the base image's stale CVE; pin the newer base tag listed in the starter README. Pod won't schedule → read-only rootfs needs an emptyDir for `/tmp` (starter comment). `kubectl` auth error → you are out of your namespace; the sandbox prompt shows it.

## Cleanup Instructions
`docker stop $(docker ps -q --filter ancestor=ml-infer:hardened)`; delete weak/hardened images; `kubectl delete -f` your applied resources; remove extracted key files.

## Submission Requirements
Before/after stats table, hardened Dockerfile + gate output, layer-archaeology evidence (found + gone), fixed pod spec + verification, workload-identity switch verification, gallery mapping.

## Expected Outputs / Evidence
The "key found in weak, absent in hardened" pair is the supply-chain lesson's evidence — both halves required.

---
### Instructor Answer Key (summary)
- Weak image: `python:latest`, root, 9 layers, key in layer 2, 4 critical findings. Hardened target: `python:3.12-slim`, non-root, 3 effective layers, 0 critical.
- Pod fields: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, NetworkPolicy egress → broker only.
- Gallery controls: env-var → brokered short-lived creds; CI-log → masked outputs + vault actions; image-layer → build-time secretless + multi-stage.

### Assessment Rubric (10 pts — check-in)
| Criterion | Points |
|---|---|
| Hardened image passes gate + stats table | 3 |
| Layer archaeology (found + gone) | 2 |
| Pod spec fixed + verified | 3 |
| Workload identity switch + gallery | 2 |
