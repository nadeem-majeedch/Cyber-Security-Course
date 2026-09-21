# Lab 00 — Security Baseline & System Hardening
**Core Lab 1 · Module 1 (L01, L04) · CLO-1 · Duration: 2 hours · Graded lab**

## 1. Learning Objectives
1. Establish a verifiable security baseline for the course VM (snapshots, isolation, updates).
2. Inspect and harden a deliberately weak configuration (accounts, services, permissions, sharing).
3. Apply least privilege and secure defaults; verify each change with a re-check command.
4. Produce before/after evidence suitable for a hardening report.

## 2. Prerequisites
Lecture 01 (CIA, controls), Lecture 04 (least privilege, secure defaults). No prior hardening experience assumed.

## 3. Hardware/Software Requirements
- Course VM image (Linux) in VirtualBox/VMware/Hyper-V, ≥ 2 CPU, 4 GB RAM.
- Instructor-provided `baseline-check.sh` and `weak-configs/` set (inside the VM image).
- Text editor, terminal.

## 4. Installation and Setup
1. Import the course VM image; do **not** use a personal VM.
2. Take a snapshot named `lab00-before`.
3. Verify isolation: no shared folders, no host USB passthrough, NAT networking only.
4. Run the baseline check and save the "before" report:
   ```bash
   sudo ./baseline-check.sh > before.txt
   ```
   *(Tested command shape on the course VM image; output fields documented in the worksheet handout.)*

## 5. Ethical Authorization and Safety Notes
- All work is on the course VM — a target you own. Never run these checks against another person's machine without their explicit consent, and never against any organizational system.
- No exploitation, no attack tooling, no payloads in this lab: it is pure baseline-and-harden.
- Keep the snapshot: rollback restores a known state.

## 6. Step-by-Step Student Tasks
| # | Task | Verification |
|---|---|---|
| 1 | Run `baseline-check.sh`, read `before.txt` | File exists; ≥ 12 findings listed |
| 2 | Weak accounts: in `weak-configs/users.txt`, identify the account with a blank password and the account with UID 0 that is not root | Two lines cited in report |
| 3 | Fix: lock the blank-password account (`passwd -l`), explain (do not change) why the UID-0 account needs instructor review | `passwd -S <user>` shows `L` |
| 4 | Services: find the listening service on 0.0.0.0:8008 (`ss -tlnp`); decide keep/disable; document the decision | `ss -tlnp` re-run shows desired state |
| 5 | File permissions: `weak-configs/shared/` is world-writable — fix to `750`, owner `svcshare` | `ls -ld` shows the new mode |
| 6 | Sharing: confirm VM shared folders are disabled and note the risk they carry | Checklist line |
| 7 | Updates: apply pending security updates (`apt upgrade` on the image or documented equivalent) | Update log excerpt |
| 8 | Re-run `baseline-check.sh > after.txt`; diff | Findings reduced; explain any that remain |
| 9 | Take snapshot `lab00-after` | Snapshot listed |

## 7. Expected Observations
- `before.txt` flags: a blank-password account, a second UID-0 account, a world-writable shared directory, a service bound to all interfaces, stale packages, shared folders enabled.
- `after.txt` shows all fixable findings cleared; the UID-0 finding remains flagged pending instructor review (an intentional residual).

## 8. Questions for Analysis
1. Which finding was an *integrity* risk, which an *availability* risk, which a *confidentiality* risk — and how do you know?
2. Why is a blank-password account worse than a weak-password account? What does `passwd -l` actually do (and not do)?
3. The service on 0.0.0.0:8008: what changed when you bound it to 127.0.0.1 instead — and what breaks if something must reach it remotely?

## 9. Troubleshooting
- `baseline-check.sh: permission denied` → run with `sudo` as instructed.
- `ss` not installed → use the image's fallback `netstat -tlnp` (documented on the handout).
- Snapshot menu greyed out → the VM must be powered off for some hypervisors; power off, snapshot, restart.

## 10. Cleanup Instructions
- Keep `lab00-after` snapshot (used by later labs).
- Remove working files from `~/` (`before.txt`/`after.txt` are submitted; do not leave copies in shared locations — there should be none).
- Log out of the VM; leave the VM powered off.

## 11. Submission Requirements
- `before.txt` and `after.txt` (your own runs — see integrity policy).
- A ≤ 1-page report: findings table (finding → CIA property → fix applied → verification command), your three analysis-question answers, and the residual-risk note for the UID-0 account.
- Screenshots: the diff between reports and the fixed permission listing.

## 12. Expected Outputs / Evidence
`before.txt`, `after.txt`, report PDF/MD, 2–3 screenshots. Evidence must be personally produced (course integrity policy).

---
### Instructor Answer Key (summary — full version in `assessments/instructor-only/`)
- Findings → CIA: blank password = C (+I via impersonation); world-writable share = I; second UID-0 = EoP risk (all three); stale packages = whichever CVE applies (context-dependent).
- `passwd -l` prefixes the hash with `!` — login denied, but keys/other auth paths may remain: hence "explain, don't fix" for UID-0.
- Bind-to-localhost removes network exposure; anything requiring remote access now needs an explicit allow rule — a segmentation seed (Lab 13).

### Assessment Rubric (20 pts)
| Criterion | Points |
|---|---|
| Correct fixes applied and verified (tasks 2–7) | 8 |
| before/after diff with reduced findings | 4 |
| Analysis answers (quality of reasoning) | 4 |
| Residual-risk note names acceptor role | 2 |
| Evidence is complete and personally produced | 2 |
