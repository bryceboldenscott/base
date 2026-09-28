---
name: base
description: Manage this project's ExecutionOS state (EXECUTION_STATE.md) and handoffs. Use when the user types /BASE, or asks to initialize, update, check status of, or hand off project tracking. Operates ONLY on the current working directory — never reads or writes another project's state file.
---

# /BASE — per-project ExecutionOS tracking

This Skill manages a single file, `EXECUTION_STATE.md`, and a `handoffs/` folder, both located in the **current working directory** — never anywhere else. It is installed once globally (`~/.claude/skills/base/`) and works identically in any project folder, but its effect is always scoped to whatever directory the session is running in. Never read, write, or reference an `EXECUTION_STATE.md` outside the current working directory, even if one is known from a prior session or another project.

Parse the argument after `/BASE` (`init`, `update`, `status`, `handoff`). No argument: infer intent from the request, or ask.

## Recordkeeping rules (apply to every subcommand)
- Stable IDs per register: `D-` Decision Log, `R-` Risk Register, `U-` Unknowns/Questions, `I-` Issue Log, `A-` Action Register, `C-` Change Log, `DL-` Deliverables, `AUD-` Audit Notes, `S-` Source Register. IDs increment per-register, scoped to this file only.
- Never silently overwrite a prior entry's substance — preserve it and reference it by ID if superseded.
- Status/Result/Evidence/Mitigation/Resolution fields may update as work progresses; log the change and cite the entry ID.
- `Last Updated` changes on every edit, material or not.
- `Version` increments only for **material** changes: Objective/Scope/Authority/DoD changes, new register entries or Status transitions, Deliverable field changes, Unknowns/Parking-Lot additions or resolutions. Typo/formatting fixes are non-material.
- Empty registers are valid: write "None recorded" — never invent content to fill a section.
- Never record a decision, risk, or completion claim without genuine evidence from the conversation.

## `/BASE init`
1. Check the current working directory for an existing `EXECUTION_STATE.md`. If one exists, stop and tell the user — do not overwrite it.
2. Create `EXECUTION_STATE.md` in the current working directory using the template below. Ask the user for Objective, Scope (in/out), Authority, and initial Definition of Done items; fill placeholders with their answers. Set `Version: 0.1`, `Last Updated` to today.
3. Create `handoffs/.gitkeep` in the current working directory.

## `/BASE update`
1. Read `EXECUTION_STATE.md` from the current working directory. If it doesn't exist, tell the user to run `/BASE init` first — do not create one implicitly.
2. Ask what kind of entry: Decision, Risk, Issue, Action, Unknown, Deliverable change, or a Status/Phase change.
3. Assign the next ID in that register, append the entry (never delete or rewrite prior entries), update `Last Updated`, and bump `Version` if the change is material per the rules above. If material, add a `Change Log` entry citing the ID(s) affected.

## `/BASE status`
1. Read `EXECUTION_STATE.md` from the current working directory. If it doesn't exist, say so plainly — do not report on any other project's file.
2. Report: Current Phase, Overall Status, Current Priority, Exact Next Action, any open (non-Closed) Risks/Issues/Unknowns, and any Blocked/Ready Actions.

## `/BASE handoff`
1. Read `EXECUTION_STATE.md` from the current working directory.
2. Create `handoffs/<YYYY-MM-DD>-v<version>-handoff.md` using the handoff template below, populated from the current state file. Never overwrite an existing handoff file — each is a permanent snapshot.

---

## EXECUTION_STATE.md template

```markdown
# <Project Name> — ExecutionOS State
Version: <version>
Last Updated: <date>

## Objective
<One-sentence statement of what this project accomplishes.>

## Scope
In-scope: <bullet list>
Out-of-scope: <bullet list>

## Authority
<Who approves material changes to this file.>

## Definition of Done
- DoD-1: <criterion>. Status: Pending. Evidence: Pending.

## Source Register
- S-1: <source, or "None recorded.">

## Unknowns / Questions
- U-1: <open question>.
  - Blocking: <Yes/No>
  - Resolution: <what would resolve it>

## Phase / Status
- Current Phase: <phase>
- Overall Status: <status>
- Current Priority: <priority>
- Exact Next Action: <exact next action>

## Completed & Active Work
- Completed: <list, or "None yet.">
- Active: <list, or "None yet.">

## Decision Log
- D-1 — <date> — <decision>. Rationale: <why>. Status: <Open/Frozen>.

## Risk Register
- R-1 — <date>
  - Risk: <what could go wrong>
  - Likelihood: <Low/Medium/High>
  - Impact: <Low/Medium/High>
  - Status: <Open/Closed>
  - Mitigation: <plan>

## Issue Log
- I-1 — <issue>. Status: <Open/Closed>. Blocking: <Yes/No>.

## Action Register
- A-1 — <action>.
  - Owner: <who>
  - Status: <Open/Blocked/Ready/Completed>
  - Dependency: <what this depends on>
  - Result: <filled in only once Completed>

## Change Log
- C-1 — <date> — <version> — <material changes, status transitions>.

## Parking Lot / Future Opportunities
- <deliberately parked ideas, or "None recorded.">

## Deliverables
- DL-1 — <deliverable>
  - Progress Status: <Not Started/In Progress/Complete>
  - Verification Status: <Not Verified/Verified/Failed Verification>
  - Acceptance Status: <Not Accepted/Accepted/Rejected>
  - Acceptance/DoD Evidence Reference: <which DoD item(s), and evidence, or "Pending">
  - Communication/Handoff Readiness: <Ready/Not Ready, with reason>

## Audit Notes
- AUD-1 — <date> — <what was reconciled, against what evidence, and the result>.
```

## Handoff template

```markdown
# Handoff — <Project Name> — <Version>

## Snapshot Identity
This handoff reflects `EXECUTION_STATE.md` as of Version <version>, Last Updated <date>. This is a fixed point-in-time record, not a live, evolving one.

## Objective
<copied verbatim from EXECUTION_STATE.md>

## Scope
<copied verbatim>

## Status (as of <version>)
- Current Phase: <phase>
- Overall Status: <status>
- Current Priority: <priority>

## Definition of Done — Status
- <DoD-N>: <Pass/Pending/Fail>. Evidence: <reference, or "Pending">.

## Frozen Decision(s)
<ID> — <decision>. Status: Frozen. (Or: "None recorded.")

## Open Risk(s) / Issue(s) / Unknown(s)
<ID> — <summary>. (Or: "None recorded.")

## Completed Work
- <ID>: <what was done>.

## Recorded Next Action
"<the Exact Next Action recorded in the state file at the time of this snapshot>."
```
