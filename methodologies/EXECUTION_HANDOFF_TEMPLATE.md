<!-- How to use: copy this file to projects/<project-name>/handoffs/<date>-<version>-handoff.md and populate every <placeholder> from the current EXECUTION_STATE.md. Never overwrite an existing handoff file — each one is a permanent snapshot. Always supply the referenced EXECUTION_STATE.md alongside this handoff — this short summary does not reproduce every active action, issue, or governing instruction from the full state file. -->

# Handoff — <Project Name> — <Version>

## Snapshot Identity
This handoff reflects `EXECUTION_STATE.md` as of Version <version>, Last Updated <date>. Commit reference: <hash, if known — omit this line otherwise>. The state file itself is not required to contain its own commit hash. This is a fixed point-in-time record, not a live, evolving one.

## Objective
<copied verbatim from EXECUTION_STATE.md>

## Scope
<copied verbatim>

## Authority
<copied verbatim>

## Status (as of <version>)
- Current Phase: <phase>
- Overall Status: <status>
- Current Priority (recorded in the snapshot): <priority>

## Definition of Done — Status
- <DoD-N>: <Pass/Pending/Fail>. Evidence: <reference, or "Pending">.

## Frozen Decision(s)
<ID> — <decision>. Status: Frozen. (Or: "None recorded." — only decisions actually marked Frozen belong here; open/undecided items do not.)

## Risk(s)
<ID> — <risk>. Likelihood/Impact/Status. (Or: "None recorded.")

## Unknown(s)
<ID> — <unresolved question>. Blocking: <Yes/No>. (Or: "None recorded.")

## Completed Work
- <ID>: <what was done, before/after state if applicable, where the transition is recorded>.

## Evidence References
- <Deliverable ID>: <Progress Status, Verification Status, Acceptance Status, evidence reference, readiness>.
- <Audit ID>: <what it reconciled>.

## Milestone History
- <Change Log ID(s)>: <what each milestone established>.

## Recorded Next Action (from the snapshot — historical record only)
"<the Exact Next Action recorded in the state file at the time of this snapshot>." Preserved verbatim as part of the fixed snapshot.

## Instructions for the Reader (required)
Record the actions already authorized by Bryce and reference the instruction or decision granting that authority. This section documents existing authorization; it cannot create or expand it. If authority is unclear, inspect and report the uncertainty before acting.

## Fixed-Snapshot Notice
The project-state account above represents the state as of the Version/date (and commit, if given) in Snapshot Identity. Any notes added afterward (including this notice and Instructions for the Reader) describe how to use this handoff — they are not changes to that snapshot.
