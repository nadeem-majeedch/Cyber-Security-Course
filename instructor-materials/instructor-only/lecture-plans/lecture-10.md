# Lecture 10 — Malware Analysis II: Dynamic Analysis, Sandboxes, and IOCs
**Module M3 · Week 5, Session 2 · 120 min · CLO-3 (primary)**

## Learning Objectives
1. Conduct controlled dynamic analysis in a sandbox with fake network services and monitored process/file/registry activity.
2. Extract, curate, and format IOCs (host indicators, domains, mutexes, artifact paths).
3. Map observed behaviors to MITRE ATT&CK techniques with evidence.
4. Document a behavioral report that a defender could act on.

## Key Concepts
- Sandbox instrumentation: process monitor, host-based sensors, fake net (DNS sinkhole, simulated HTTP), network capture
- Behavioral observations: persistence mechanisms (Run keys, scheduled tasks, services), C2 beacons (timing/jitter), staging, credential access
- IOCs vs. TTPs: indicators age fast, behaviors persist; both belong in the report
- Sandbox evasion awareness (awareness level): sleep bombs, VM checks — why automated sandboxes miss things
- Chain of custody and handling notes for evidence discipline

## Detailed Teaching Sequence
| Time | Segment | Method |
|---|---|---|
| 00–08 | Recap L09 verdicts; instructor reveals what the samples actually did (they were tested beforehand) | Reveal |
| 08–30 | Instrumentation tour: Process-Monitor-style view, DNS/HTTP fake services, packet capture — what each layer records | Live demo |
| 30–52 | Guided dynamic run of sample-1 by instructor; class calls out observed behaviors as they appear; build the ATT&CK mapping table together | Interactive demo |
| 52–60 | Break | — |
| 60–105 | **Lab block (Lab 09):** students run samples 2–3, collect IOC lists, map ≥ 6 behaviors to ATT&CK IDs with evidence citations (procmon line / pcap frame) | Hands-on |
| 105–115 | IOC curation workshop: deduplicate, rank, format (STIX-lite table); what makes an IOC high-quality (specificity, observability) | Workshop |
| 115–120 | Exit ticket; preview L11 (ransomware) | Q&A |

## Examples
- **CS track:** sample beacons to a fixed domain every 60s ± jitter — students compute beacon interval from pcap timestamps (a DS-flavored measurement).
- **DS track:** from the class's collected runs, aggregate the behavior-frequency table; discuss how a SOC would build a detection from N runs vs. one run (sample variance).

## Discussion Questions
1. Your sandbox shows nothing. List four evasion explanations and one countermeasure for each.
2. Why is a hardcoded IP a better IOC than a domain? When is it worse?
3. A behavior maps to two ATT&CK techniques. Which do you record, and why does the choice matter for detection engineering?

## Student Activity
Paired dynamic runs with division of labor (one drives, one records); ATT&CK mapping table completion; IOC table curation.

## Problem-Solving Scenario
> Sample-3 shows: writes `C:\Users\...\AppData\Roamed\svchost32.exe`, adds a Run key, resolves a DDNS domain, POSTs small packets every 45s. Produce: the behavior chain diagram, ATT&CK mapping with evidence, five high-quality IOCs, and one detection hypothesis a SOC could deploy.

## Summary
Dynamic analysis converts static hypotheses into observed facts — and observed facts into IOCs and ATT&CK mappings that defenders can act on. L11 examines the most disruptive behavior class in detail: ransomware.

## Formative Assessment
1. Name two persistence mechanisms to watch for.
2. What is the difference between an IOC and a TTP?
3. Why use a fake network instead of letting malware phone home?

## Required Resources
- `labs/lab-09-dynamic-analysis/` samples + sensor VM
- MITRE ATT&CK (Enterprise) pages; STIX overview (1-pager)
- CLO mapping: **CLO-3** (objectives 1–4).
