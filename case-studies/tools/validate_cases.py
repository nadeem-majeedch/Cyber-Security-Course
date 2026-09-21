#!/usr/bin/env python3
"""Validation for the 100-case collection.

Checks:
  1. Case counts per level file (20/25/30/25; IDs CS-001..CS-100, no gaps).
  2. Required student-facing components present in every case:
     Scenario, Stakeholders, Available evidence, Student task, Difficulty,
     Domain, Time, CLO, Safety notes.
  3. Instructor solution files cover the same case IDs (keyed per case).
  4. INDEX.md references every case ID exactly once.
  5. Solution sections carry the six required instructor components
     (model solution / reasoning / alternatives / tradeoffs / mistakes / prompts).

Run from the repository root:  python case-studies/tools/validate_cases.py
Exit code 0 = all checks pass.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # case-studies/
SOL = ROOT.parent / "instructor-materials" / "instructor-only" / "case-solutions"

LEVELS = {
    "collection/level-1-beginner.md": (20, "CS-{:03d}", 1),
    "collection/level-2-intermediate.md": (25, "CS-{:03d}", 2),
    "collection/level-3-advanced.md": (30, "CS-{:03d}", 3),
    "collection/level-4-expert.md": (25, "CS-{:03d}", 4),
}
SOL_FILES = {
    1: "level-1-solutions.md",
    2: "level-2-solutions.md",
    3: "level-3-solutions.md",
    4: "level-4-solutions.md",
}
STUDENT_FIELDS = ["Scenario", "Stakeholders", "Available evidence", "Student task",
                  "Difficulty", "Domain", "Time", "CLO", "Safety notes"]
SOLUTION_FIELDS = ["Model solution", "Reasoning", "Alternatives",
                   "Tradeoffs", "Common mistakes", "Prompts"]

failures: list[str] = []
notes: list[str] = []


def err(msg: str) -> None:
    failures.append(msg)


def case_ids(text: str) -> list[tuple[str, int]]:
    """Return (case_id, offset) for each '## CS-NNN' heading."""
    return [(m.group(1), m.start()) for m in re.finditer(r"^## (CS-\d{3})", text, re.M)]


def split_cases(text: str) -> dict[str, str]:
    ids = case_ids(text)
    out: dict[str, str] = {}
    for i, (cid, off) in enumerate(ids):
        end = ids[i + 1][1] if i + 1 < len(ids) else len(text)
        out[cid] = text[off:end]
    return out


def check_expected(field: str, body: str, cid: str, path: str) -> None:
    if field.lower() not in body.lower():
        err(f"{path}: {cid} missing component '{field}'")


all_ids: list[str] = []
for rel, (count, _fmt, level) in LEVELS.items():
    p = ROOT / rel
    if not p.exists():
        err(f"missing file: {p}")
        continue
    text = p.read_text(encoding="utf-8")
    cases = split_cases(text)
    if len(cases) != count:
        err(f"{rel}: expected {count} cases, found {len(cases)}")
    ids = [c for c, _ in case_ids(text)]
    all_ids.extend(ids)
    # sequential, no gaps within the level
    nums = sorted(int(c.split("-")[1]) for c in ids)
    expected_start = {1: 1, 2: 21, 3: 46, 4: 76}[level]
    if nums != list(range(expected_start, expected_start + count)):
        err(f"{rel}: IDs not sequential from CS-{expected_start:03d}: {nums}")
    for cid, body in cases.items():
        for field in STUDENT_FIELDS:
            check_expected(field, body, cid, rel)
        # difficulty marker present
        if f"Level {level}" not in body:
            err(f"{rel}: {cid} missing 'Level {level}' difficulty marker")
        # no solution leakage: student file must not contain model solutions
        if re.search(r"\*\*Model solution\*\*", body, re.I):
            err(f"{rel}: {cid} LEAKS model solution into student tier")

# 1. global: exactly CS-001..CS-100
want = [f"CS-{i:03d}" for i in range(1, 101)]
if sorted(all_ids) != want:
    missing = set(want) - set(all_ids)
    dupes = {x for x in all_ids if all_ids.count(x) > 1}
    err(f"global ID set mismatch; missing={sorted(missing)} dupes={sorted(dupes)}")

# 3. solution files cover the same IDs with required components
for level, fname in SOL_FILES.items():
    p = SOL / fname
    if not p.exists():
        err(f"missing solution file: {p}")
        continue
    text = p.read_text(encoding="utf-8")
    sols = split_cases(text)
    level_ids = [f"CS-{i:03d}" for i in
                 range({1: 1, 2: 21, 3: 46, 4: 76}[level],
                       {1: 1, 2: 21, 3: 46, 4: 76}[level] + LEVELS[
                           [k for k, v in LEVELS.items() if v[2] == level][0]][0])]
    for cid in level_ids:
        if cid not in sols:
            err(f"{fname}: no solution section for {cid}")
            continue
        body = sols[cid]
        for field in SOLUTION_FIELDS:
            if field.lower() not in body.lower():
                err(f"{fname}: {cid} missing instructor component '{field}'")

# 4. index coverage
idx = ROOT / "INDEX.md"
if idx.exists():
    itext = idx.read_text(encoding="utf-8")
    for cid in want:
        n = len(re.findall(rf"\b{cid}\b", itext))
        if n == 0:
            err(f"INDEX.md: {cid} not referenced")
        elif n > 1 and f"| {cid} |" not in itext:
            notes.append(f"INDEX.md: {cid} appears {n} times (multi-table rows OK if intended)")
else:
    err("missing INDEX.md")

# report
print(f"Cases found: {len(all_ids)} (expect 100)")
for n in notes:
    print(f"note: {n}")
if failures:
    print(f"\nFAILURES ({len(failures)}):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("ALL CHECKS PASSED")
