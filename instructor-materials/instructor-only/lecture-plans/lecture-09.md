# Lecture 09 — Malware Analysis I: Taxonomy and Static Triage
**Module M3 · Week 5, Session 1 · 120 min · CLO-3 (primary)**

## Learning Objectives
1. Apply safe-analysis procedure: isolated VM, no shared folders, snapshot discipline, host hardening.
2. Classify malware families (infostealer, ransomware, worm, trojan, backdoor, rootkit) by behavior and propagation.
3. Perform static triage: hashes, fuzzy hashing (ssdeep concept), strings, imports, PE/ELF headers, packer indicators.
4. Document findings as structured analyst notes.

## Key Concepts
- Analysis environments: isolation layers (VM, snapshot, network control — INetSim-style fake net), why "analysis VM" ≠ "test VM"
- Static indicators: MD5/SHA-256 (identification), imports table (capability hints), strings/UTF-16 strings, section entropy (packing), compiler artifacts
- Packer/crypter concepts; why packing defeats static strings
- Malware taxonomy and naming mess; ATT&CK as the behavior vocabulary (preview of L10)
- Analyst note format: identifiers → capabilities → verdict → confidence

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Module 3 hook: the course uses **synthetic sample binaries built for teaching** — safety contract read aloud | Slides |
| 08–28 | Safe-analysis setup: students boot the analysis VM, take a snapshot, verify no shared folders; instructor demos the wrong way (host-sharing) and consequences | Hands-on |
| 28–50 | Static triage live demo on sample-1: hash → strings → imports → entropy; annotate an analyst note as class watches | Live demo |
| 50–60 | Break | — |
| 60–105 | **Lab block (Lab 08):** students triage samples 2 and 3 (synthetic), produce one analyst note per sample using the template | Hands-on |
| 105–115 | Peer swap: pairs cross-check notes for missed capability hints (imports telling a network story) | Peer review |
| 115–120 | Exit ticket; preview L10 (dynamic) | Q&A |

## Examples
- **CS track:** sample with imports `WSAStartup`, `connect`, `CreateRemoteThread` → backdoor hypothesis; students mark the import groups that justify it.
- **DS track:** static features as a dataset — build the feature table (entropy, import counts, string n-grams) that Module 6's classifier will reuse; discuss sampling bias in malware corpora.

## Discussion Questions
1. Why do we hash before anything else? What does a fuzzy hash add over SHA-256?
2. High section entropy — what are the three explanations, and how would you distinguish them?
3. What can static analysis never tell you? (runtime config, network behavior, unpacked payloads)

## Student Activity
Guided triage of two synthetic samples; each student completes the analyst-note template; cross-check exchange.

## Problem-Solving Scenario
> Sample "invoice.exe": packed sections, two suspicious imports, a URL string. Produce: the identification block (hashes), capability hypotheses with import evidence, entropy measurement with interpretation, and a verdict statement with confidence level — noting what dynamic analysis must confirm.

## Summary
Static triage is cheap, safe, and never sufficient: it turns a binary into hypotheses. Hypotheses get tested dynamically — in a controlled sandbox — in L10.

## Formative Assessment
1. Which hash identifies a file exactly? Which finds near-variants?
2. Name two imports that hint at network capability.
3. Why snapshot before executing?

## Required Resources
- `labs/lab-08-static-triage/` synthetic samples + analyst-note template
- Analysis VM image (no host sharing, fake-net ready); PE/ELF header cheat sheet
- Sikorski & Honig ch. 1–2 (practical basics)
- CLO mapping: **CLO-3** (objectives 1–4).
