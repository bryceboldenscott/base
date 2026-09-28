# BASE

**BASE** is the project-tracking system I use to run AI-assisted builds. At its centre is **ExecutionOS**, a methodology for keeping one honest, recoverable record of a project: what it's trying to do, what's actually true, what changed, what evidence backs each claim, and exactly where the next session should start.

It ships as a [Claude Code](https://claude.com/claude-code) skill, `/base`, so an AI pair programmer keeps the record up to date as it works, and any session (or any person) can pick the project back up cold.

> **Showcase repository.** This is the public, sanitized part of a private working environment. Personal context and continuity files are not included.

## Why

Long AI-assisted builds fail in predictable ways. Context gets lost between sessions, "done" gets claimed without evidence, decisions get silently reversed, and nobody can say what the next step is. ExecutionOS turns those into rules:

> Truth before completion. Evidence before assertion. Preserve history. No silent requirement or architecture changes. Planned is not completed. Unknown is acceptable. Every session leaves a recoverable next start.

## What's here

| Path | What it is |
|---|---|
| [`skills/base/SKILL.md`](skills/base/SKILL.md) | The `/base` Claude Code skill: `init`, `update`, `status`, `handoff` |
| [`methodologies/EXECUTION_OS_SANITIZED.md`](methodologies/EXECUTION_OS_SANITIZED.md) | The ExecutionOS specification: layers, evidence classes, registers |
| [`methodologies/MVP_DELIVERY_METHOD.md`](methodologies/MVP_DELIVERY_METHOD.md) | Frame → Research → Architecture → Plan → Build → Test → Evaluate → Freeze |
| [`methodologies/EXECUTION_STATE_TEMPLATE.md`](methodologies/EXECUTION_STATE_TEMPLATE.md) | The per-project state file template |
| [`methodologies/EXECUTION_HANDOFF_TEMPLATE.md`](methodologies/EXECUTION_HANDOFF_TEMPLATE.md) | Point-in-time handoff snapshot template |
| [`examples/base-structure-validator/`](examples/base-structure-validator) | A complete worked project, run end to end under the method |

## How it works

Each project gets one `EXECUTION_STATE.md` and a `handoffs/` folder:

- **Registers with stable IDs:** `D-` decisions, `R-` risks, `I-` issues, `U-` unknowns, `A-` actions, `C-` changes, `DL-` deliverables, `S-` sources
- **Evidence classes on every claim:** Authoritative Source, User-Reported, Project Decision, Assumption, Unknown, and others
- **Versioning rules:** the version only increments on material change, and prior entries are superseded by ID, never silently overwritten
- **Definition of Done:** each item has a Pass / Fail / Not Yet Evaluated status and the evidence behind it
- **Handoffs:** frozen snapshots, so any session can be reconstructed

`/base handoff` writes a snapshot; `/base status` reports where things stand without editing anything.

## Worked example

`examples/base-structure-validator` is a small, read-only Python tool that checks whether a project folder follows the ExecutionOS template. It was built as the first real exercise of the MVP Delivery Method, and its state file, test evidence, freeze manifest and handoff are all included.

```bash
python examples/base-structure-validator/validate_structure.py examples/base-structure-validator/test_fixtures/valid_example
# 21/21 checks passed.   (exit 0)

python examples/base-structure-validator/validate_structure.py examples/base-structure-validator/test_fixtures/invalid_example
# 19/21 checks passed.   (exit 1)
```

BASE also tracked the rebuild of [bryceboldenscott.com](https://bryceboldenscott.com) through 20 versions, from content strategy to production deploy.

## Install the skill

```bash
mkdir -p ~/.claude/skills/base
cp skills/base/SKILL.md ~/.claude/skills/base/
```

Then run `/base init` in any project folder. The skill only ever reads and writes the current directory's state file.

---

Bryce Bolden-Scott · [bryceboldenscott.com](https://bryceboldenscott.com)
