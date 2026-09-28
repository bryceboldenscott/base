# Test Evidence — base-structure-validator

All commands below were run from `projects/base-structure-validator/` as the
working directory, using `python validate_structure.py <target>`. Each case
was run twice with no changes to the fixture in between, to test DoD-4
(repeatability). Raw captured output for each run is saved under
`test-output/` in this project. Exit codes were captured immediately after
each run, before any other command.

## Case 1 — Valid fixture
Command: `python validate_structure.py test_fixtures/valid_example`
- Run 1: exit code 0. Output: `test-output/valid1.txt`.
- Run 2: exit code 0. Output: `test-output/valid2.txt`.
- Comparison: `diff test-output/valid1.txt test-output/valid2.txt` produced no
  output (files identical). Exit codes identical (0, 0).
- Result: 21/21 checks passed, matching the expected result for DoD-1.

## Case 2 — Invalid fixture
Command: `python validate_structure.py test_fixtures/invalid_example`
- Run 1: exit code 1. Output: `test-output/invalid1.txt`.
- Run 2: exit code 1. Output: `test-output/invalid2.txt`.
- Comparison: `diff test-output/invalid1.txt test-output/invalid2.txt`
  produced no output (files identical). Exit codes identical (1, 1).
- Result: 19/21 checks passed. Exactly the two intended defects failed —
  `FAIL: handoffs/ is a directory` and `FAIL: heading present: ## Audit
  Notes` — matching the expected result for DoD-2. The fixture's deliberate
  prose mention of the string "## Audit Notes" inside a paragraph did not
  cause a false pass, confirming the validator matches actual heading lines
  only, not incidental mentions in prose.

## Case 3 — Nonexistent target
Command: `python validate_structure.py test_fixtures/does_not_exist`
- Run 1: exit code 2. Output: `test-output/nonexistent1.txt`.
- Run 2: exit code 2. Output: `test-output/nonexistent2.txt`.
- Comparison: outputs identical, exit codes identical (2, 2).
- Result: reported as a usage error, not a structural failure, per the
  contract.

## Case 4 — Regular-file target (not a directory)
Command: `python validate_structure.py validate_structure.py`
- Run 1: exit code 2. Output: `test-output/regularfile1.txt`.
- Run 2: exit code 2. Output: `test-output/regularfile2.txt`.
- Comparison: outputs identical, exit codes identical (2, 2).
- Result: also correctly reported as a usage error, distinguishing "target is
  not a directory" from "target directory exists but lacks required files"
  (Case 2 covers the latter).

## Repeatability conclusion (DoD-4)
All four cases produced byte-identical stdout and identical exit codes
across both runs, verified by direct `diff` comparison, not by inspection
alone. Result: Pass.

## Reproduction (post-Freeze, v0.2)
Performed 2026-09-15 against the frozen files identified in `FREEZE_MANIFEST.md`. All four cases were re-run twice each, with output captured to `reproduction-output/` (kept separate from the pre-freeze `test-output/`), and exit codes captured immediately after each run.

- Valid fixture: exit codes 0, 0.
- Invalid fixture: exit codes 1, 1.
- Nonexistent target: exit codes 2, 2.
- Regular-file target: exit codes 2, 2.

Cross-comparison: each of the eight `reproduction-output/` files was compared via `diff` against its corresponding pre-freeze `test-output/` file. All eight comparisons found no differences — reproduction output is byte-identical to the original evidence.

Hash verification: `sha256sum` was re-run against all four frozen files (`validate_structure.py`, both fixture `EXECUTION_STATE.md` files, and the valid fixture's `handoffs/.gitkeep`) after reproduction completed. All four hashes matched `FREEZE_MANIFEST.md` exactly — the frozen files were not altered by running the validator against them, confirming its read-only behavior.

Result: Reproduction Pass. No failure encountered; Closeout proceeds.

## Limitations of these checks
These are structural checks only. They do not and cannot establish: factual
accuracy of any section's content; confidentiality of the target's contents;
whether a target project is actually complete; or whether a target's handoff
would survive a fresh-session recovery test of the kind used for the
ExecutionOS test project. A target can pass every check here while still
containing false claims, unresolved work, or a handoff that fails recovery.
