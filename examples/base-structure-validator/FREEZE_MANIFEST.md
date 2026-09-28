# Freeze Manifest — base-structure-validator v0.1

Frozen: 2026-09-15. These files must remain byte-for-byte unchanged from
this point forward without an explicit, approved change.

## SHA-256 hashes (frozen script and fixture files)

```
90a2f120e6e439c4e310b0f2f7645b90b173e6d0744e8064f800e152f5440149  validate_structure.py
14e6fd4bf073dac018485d9955ebd521c9b6b69001b753a9b623ed6dc7cd0500  test_fixtures/valid_example/EXECUTION_STATE.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  test_fixtures/valid_example/handoffs/.gitkeep
e03d148da5ae1e7601027fd0a7cf1004f03602344306a08d70e4fd2d55119920  test_fixtures/invalid_example/EXECUTION_STATE.md
```

Note: `test_fixtures/invalid_example/` has no `handoffs/` directory by
design (that absence is one of its two intended defects), so there is no
corresponding hash for it.

## Heading-contract compatibility

`validate_structure.py`'s `REQUIRED_HEADINGS` list is a hardcoded copy of
the sixteen section headings in `methodologies/EXECUTION_STATE_TEMPLATE.md`
as it existed at commit `7608e5e` (the commit that introduced the shared
ExecutionOS templates). This frozen version's contract is tied to that
specific template version. If the shared template's headings are ever
added to, removed, or renamed in a future commit, this validator will not
automatically track that change — it must undergo an explicit compatibility
review before being treated as still accurate, per Risk R-1 in
`EXECUTION_STATE.md`.
