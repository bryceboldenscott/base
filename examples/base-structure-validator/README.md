# base-structure-validator

A read-only, standard-library-only Python script that checks whether a
project folder follows the ExecutionOS structural template (as extracted
from the tested `personal-it-reading-list-test` project into
`methodologies/EXECUTION_STATE_TEMPLATE.md`).

## Usage

```
python validate_structure.py <target-project-path>
```

`<target-project-path>` is a folder expected to contain `EXECUTION_STATE.md`
and a `handoffs/` directory (e.g. `projects/<name>/`).

## What it checks

- `EXECUTION_STATE.md` exists as a regular file and is readable.
- `handoffs/` exists as a directory.
- The file contains a line starting with `Version:` and a line starting
  with `Last Updated:`.
- All sixteen required section headings are present as exact heading lines
  (e.g. `## Objective`) — a heading name mentioned inside a paragraph does
  not count.

Checks run in one fixed order every time, so output is deterministic.

## Output format

One `PASS:` or `FAIL:` line per check, naming exactly what was checked, then
a summary line: `N/21 checks passed.`

## Exit codes

- `0` — every check passed.
- `1` — at least one structural check failed.
- `2` — the target path does not exist, or is not a directory (a usage
  error, distinct from a structural failure).

## Limitations

This script performs structural checks only. It cannot and does not
establish:
- **Factual accuracy** — a heading can exist while the content beneath it is
  wrong, fabricated, or contradicts other sections.
- **Confidentiality** — nothing here scans for or rules out
  employer-confidential, proprietary, or NDA-covered content.
- **Project completion** — a `Definition of Done` heading existing says
  nothing about whether any DoD item is actually met.
- **Recovery quality** — passing every check here implies nothing about
  whether the target project's handoff would survive a genuine
  fresh-session recovery test, of the kind performed for the ExecutionOS
  test project (`projects/personal-it-reading-list-test/`).

See `TEST_EVIDENCE.md` for the actual test runs and repeatability evidence.
