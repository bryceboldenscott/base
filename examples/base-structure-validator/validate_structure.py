#!/usr/bin/env python3
"""Structural validator for ExecutionOS-shaped project folders.

Checks structure only. Does NOT establish factual accuracy, confidentiality,
project completion, or recovery quality — see README.md. Read-only: never
modifies the target.
"""
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "## Objective",
    "## Scope",
    "## Authority",
    "## Definition of Done",
    "## Source Register",
    "## Unknowns / Questions",
    "## Phase / Status",
    "## Completed & Active Work",
    "## Decision Log",
    "## Risk Register",
    "## Issue Log",
    "## Action Register",
    "## Change Log",
    "## Parking Lot / Future Opportunities",
    "## Deliverables",
    "## Audit Notes",
]


def run_checks(target: Path):
    results = []

    state_file = target / "EXECUTION_STATE.md"
    state_is_regular_file = state_file.is_file()
    results.append(("EXECUTION_STATE.md is a regular file", state_is_regular_file))

    lines = []
    state_readable = False
    if state_is_regular_file:
        try:
            lines = state_file.read_text(encoding="utf-8").splitlines()
            state_readable = True
        except OSError:
            state_readable = False
    results.append(("EXECUTION_STATE.md is readable", state_readable))

    handoffs_dir = target / "handoffs"
    results.append(("handoffs/ is a directory", handoffs_dir.is_dir()))

    has_version = any(line.startswith("Version:") for line in lines)
    results.append(("Version: line present", has_version))

    has_last_updated = any(line.startswith("Last Updated:") for line in lines)
    results.append(("Last Updated: line present", has_last_updated))

    # Exact stripped-line match only, so a heading mentioned inside a
    # paragraph does not count as the heading itself being present.
    stripped_lines = {line.strip() for line in lines}
    for heading in REQUIRED_HEADINGS:
        results.append((f"heading present: {heading}", heading in stripped_lines))

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_structure.py <target-project-path>")
        sys.exit(2)

    target = Path(sys.argv[1])
    if not target.is_dir():
        print(f"FAIL: target path does not exist or is not a directory: {target}")
        sys.exit(2)

    results = run_checks(target)
    passed = 0
    for description, ok in results:
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"{status}: {description}")

    total = len(results)
    print(f"{passed}/{total} checks passed.")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
