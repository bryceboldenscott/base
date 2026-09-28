# base-structure-validator — ExecutionOS State
Version: v0.2
Last Updated: 2026-09-15

Recordkeeping rules for this file: use stable IDs per register (D-1 Decision Log, R-1 Risk Register, U-1 Unknowns/Questions, I-1 Issue Log, A-1 Action Register, C-1 Change Log, DL-1 Deliverables, AUD-1 Audit Notes, S-1 Source Register...); entry content is immutable once written — only a Status field may transition, and every transition is logged in Change Log; Last Updated changes on every edit, Version increments only for material changes; empty registers are valid and should say so explicitly ("None recorded"), never be invented; never record a fact, decision, risk, or completion claim without genuine evidence. This project's Definition of Done uses the MVP Delivery Method's five-value result vocabulary (Pass; Pass with known limitation; Fail; Not tested; Out of scope), kept local to this project only — the shared ExecutionOS templates are not modified.

## Objective
Provide a small, local, read-only Python tool that checks whether a BASE project folder follows the ExecutionOS structural template, and use building/testing it as the first real exercise of the MVP Delivery Method inside BASE. [User-Reported — Bryce authorized this as the MVP Delivery Method test project]

## Scope
In-scope: structural presence checks (required files/directories/headings/metadata lines) for one target project folder at a time; deterministic PASS/FAIL output; Python standard library only.
Out-of-scope: content-accuracy checking, confidentiality scanning, DoD-completion checking, recovery-quality checking, multi-target checking in one run, any network access, any modification of the target, git-hook integration, general-purpose Markdown linting.

## Authority
Bryce Bolden-Scott approves all material changes to this file. Bryce authorized Build through Evaluate only; Freeze, commit, and a final handoff are explicitly not authorized yet.

## Definition of Done
- DoD-1: Given the valid fixture, the validator reports all checks passed and exit code 0. Status: Pass. Evidence: `TEST_EVIDENCE.md`, Case 1.
- DoD-2: Given the invalid fixture, the validator reports exactly the two intended defects and exit code 1. Status: Pass. Evidence: `TEST_EVIDENCE.md`, Case 2.
- DoD-3: The script runs with no network access and no non-standard-library dependencies. Status: Pass. Evidence: source imports only `sys` and `pathlib`; no third-party package; no network call anywhere in the script.
- DoD-4: Running the script twice against unchanged input produces identical output and exit code. Status: Pass. Evidence: `TEST_EVIDENCE.md`, all four cases, each compared with `diff` and found identical.

## Source Register
- S-1: `methodologies/MVP_DELIVERY_METHOD.md` — ten-phase lifecycle and five DoD result labels. [Authoritative Source — the project's own governing methodology document]
- S-2: `methodologies/EXECUTION_STATE_TEMPLATE.md` — the sixteen required section headings this validator checks for. [Authoritative Source]

## Unknowns / Questions
- U-1: Whether future BASE projects will actually adopt this validator as a routine check, or whether it remains a one-off MVP exercise. [Unknown]
  - Blocking: No
  - Resolution: Requires Bryce's decision, likely after Freeze/Closeout.

## Phase / Status
- Current Phase: Closeout (complete)
- Overall Status: Frozen at v0.2, reproduced, closed out — a completed bounded MVP
- Current Priority: Present the final consolidated report for Bryce's review.
- Exact Next Action: Await Bryce's review; no staging or commit is authorized yet.

## Completed & Active Work
- Completed: Frame, Research (D-1, D-2), Architecture (D-3), Plan (A-1–A-4), Build, Test (`TEST_EVIDENCE.md`), Evaluate (DoD mapping above), Freeze (D-4, `FREEZE_MANIFEST.md`), Reproduce (reproduction results in `TEST_EVIDENCE.md`, hashes verified unchanged), Closeout (AUD-1, project handoff at `handoffs/2026-09-15-v0.2-handoff.md`).
- Active: None — all ten phases of the bounded MVP complete; paused pending Bryce's review. No staging, commit, or further scope is authorized.

## Decision Log
- D-1 — 2026-09-15 — Research: considered substring search versus exact stripped-line match for heading detection; chose exact stripped-line match, since the approved contract requires matching actual heading lines, not incidental mentions in prose. Evidence class: [Project Decision]. Status: Open.
- D-2 — 2026-09-15 — Research: considered requiring Version/Last Updated as strictly the first two lines versus present anywhere in the file; chose "present anywhere," since real project files (including this one) have a title line first. Evidence class: [Project Decision]. Status: Open.
- D-3 — 2026-09-15 — Architecture: chosen design is a single-pass line scan producing a fixed, hardcoded list of 21 checks (file-is-regular, file-is-readable, handoffs-is-directory, Version-present, Last-Updated-present, plus the 16 headings), using only `sys` and `pathlib`, with direct `sys.argv` handling rather than `argparse` for a single positional argument. Rationale: simplest design capable of proving the DoD. Evidence class: [Project Decision]. Status: Open.
- D-4 — 2026-09-15 — Freeze: MVP baseline frozen at v0.2. Accepted scope: structural validator as specified in `README.md`, verified against DoD-1 through DoD-4, all Pass. Known limitations accepted at freeze: cannot establish content accuracy, confidentiality, project completion, or recovery quality (see `README.md`); heading contract is tied to `methodologies/EXECUTION_STATE_TEMPLATE.md` as of commit `7608e5e` and requires explicit compatibility review, not automatic acceptance, if that template changes (see R-1, `FREEZE_MANIFEST.md`). Frozen files and their SHA-256 hashes recorded in `FREEZE_MANIFEST.md`. Evidence class: [Project Decision]. Status: Frozen.

## Risk Register
- R-1 — 2026-09-15
  - Basis: The validator's heading list is a hardcoded copy of the sixteen headings from `methodologies/EXECUTION_STATE_TEMPLATE.md`. [User-Reported]
  - Risk: If the shared template's headings ever change, this validator will silently fall out of sync — nothing re-derives the list from the template at runtime. [Recommendation]
  - Likelihood: Low
  - Impact: Medium
  - Status: Open
  - Mitigation: Not yet decided — could be a documented limitation at Closeout, or a future increment reading the template at runtime. Left open for Bryce's decision.

## Issue Log
- None logged at this stage. (No blockers reaching Evaluate.)
  - Blocking: No

## Action Register
- A-1 — Write `validate_structure.py` implementing the approved contract.
  - Owner: Claude
  - Status: Completed
  - Dependency: Architecture decision D-3.
  - Result: File created; see Build evidence in `TEST_EVIDENCE.md`.
- A-2 — Create two self-contained synthetic fixtures (valid, invalid), not reusing the completed reading-list project.
  - Owner: Claude
  - Status: Completed
  - Dependency: A-1.
  - Result: `test_fixtures/valid_example/` and `test_fixtures/invalid_example/` created.
- A-3 — Run all four test cases (valid, invalid, nonexistent target, regular-file target), twice each, capturing real output and exit codes.
  - Owner: Claude
  - Status: Completed
  - Dependency: A-2.
  - Result: `TEST_EVIDENCE.md` written with real captured evidence; all four cases reproducible.
- A-4 — Map test evidence to each DoD item using the MVP five-value vocabulary.
  - Owner: Claude
  - Status: Completed
  - Dependency: A-3.
  - Result: See Definition of Done section above — all four DoD items Pass.

## Change Log
- C-1 — 2026-09-15 — v0.1 — Project created and carried through Frame, Research, Architecture, Plan, Build, Test, and Evaluate, per Bryce's bounded authorization (Build through Evaluate only). Material content: Objective/Scope/Authority/DoD drafted; three research/architecture decisions (D-1–D-3) recorded; one risk (R-1) recorded; four actions (A-1–A-4) completed; four DoD items evaluated, all Pass.
- C-2 — 2026-09-15 — v0.2 — Freeze, Reproduce, and Closeout authorized and performed. Material content: D-4 (Freeze decision, Status: Frozen) recorded; `FREEZE_MANIFEST.md` created with SHA-256 hashes of the frozen script and fixture files and the commit-`7608e5e` heading-contract compatibility note; reproduction results and Closeout audit to be appended below as each completes.

## Parking Lot / Future Opportunities
- Automatically deriving the required-headings list from `methodologies/EXECUTION_STATE_TEMPLATE.md` at runtime instead of a hardcoded copy (relates to R-1). [Recommendation] — not in scope for this MVP test.

## Deliverables
- DL-1 — `validate_structure.py`
  - Progress Status: Complete
  - Verification Status: Verified — ran successfully against all four test cases, twice each, with correct and reproducible results.
  - Acceptance Status: Not Accepted — acceptance is Bryce's decision, not yet made.
  - Acceptance/DoD Evidence Reference: DoD-1 through DoD-4, all Pass; see `TEST_EVIDENCE.md`.
  - Communication/Handoff Readiness: Ready for review — handoff exists at `handoffs/2026-09-15-v0.2-handoff.md`; not yet staged or committed.
- DL-2 — `README.md`
  - Progress Status: Complete
  - Verification Status: Verified — content checked against actual script behavior and actual test results.
  - Acceptance Status: Not Accepted.
  - Acceptance/DoD Evidence Reference: Supports DoD-3's dependency claim; documents the required limitations.
  - Communication/Handoff Readiness: Ready for review.
- DL-3 — `TEST_EVIDENCE.md`
  - Progress Status: Complete
  - Verification Status: Verified — every line reflects an actual captured run, not a claimed or invented result.
  - Acceptance Status: Not Accepted.
  - Acceptance/DoD Evidence Reference: Primary evidence for DoD-1, DoD-2, and DoD-4.
  - Communication/Handoff Readiness: Ready for review.

## Audit Notes
- AUD-1 — 2026-09-15 — Closeout audit.
  - Outcomes: a frozen (v0.2), reproduced, read-only structural validator exists for ExecutionOS-shaped project folders. All four DoD items (DoD-1 through DoD-4) Pass, with evidence in `TEST_EVIDENCE.md`. Reproduction against the frozen files (`FREEZE_MANIFEST.md`) matched the original evidence exactly, with hashes confirmed unchanged before and after.
  - Lessons: exact stripped-line matching (D-1) was necessary and sufficient to distinguish real headings from incidental prose mentions — confirmed directly by the invalid fixture's deliberate prose test, not merely assumed. Keeping Version/Last Updated detection position-independent (D-2) made the checker robust to real files without cost. A hardcoded heading list (D-3) is simple but creates a genuine, now-documented drift risk (R-1) against the shared template.
  - Recommendations: if this validator is adopted beyond this one bounded MVP, R-1 (heading list drift) should be resolved — either by deriving headings from the template at runtime or by an explicit process tying validator updates to template commits. Not undertaken here — out of the bounded scope authorized.
  - Limitations: as stated in `README.md` — structural checks cannot establish content accuracy, confidentiality, project completion, or recovery quality. This is a completed bounded MVP, not a general-purpose content or security validator, and should not be represented as one.
  - Artifact index (by existing Deliverables ID, not a separate index): DL-1 (`validate_structure.py`), DL-2 (`README.md`), DL-3 (`TEST_EVIDENCE.md`). `FREEZE_MANIFEST.md` and the two `test_fixtures/` folders are supporting artifacts referenced throughout but not separately registered as Deliverables, consistent with the original Plan (A-1 through A-4).
