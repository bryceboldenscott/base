# ExecutionOS --- Sanitized Portable Specification

## Purpose

A generalized project operating methodology answering: \> What am I
trying to accomplish, what is true, what changed, what evidence do I
have, where does the project stand, and what should happen next?

## Constitution

Truth before completion. Evidence before assertion. Preserve history. No
silent requirement/architecture changes. Planned is not completed.
Separate facts, recommendations, assumptions and unknowns. Unknown is
acceptable. External authority outranks the OS. Every session leaves a
recoverable next start. Reduce cognitive load.

## Layers

-   **CORE:** objective, scope, authority, Definition of Done,
    version/change rules.
-   **KNOWLEDGE:** sources, verified facts, research, assumptions,
    corrections, unknowns.
-   **OPERATIONS:** phase, completed/active work, actions, blockers,
    risks, issues, decisions, changes.
-   **DELIVERY:** deliverables, documentation, acceptance evidence,
    communication, handoff readiness.
-   **CONTINUITY:** persistent state, session handoff, exact next start,
    recovery prompt.
-   **ARCHIVE:** revisions, superseded records, milestone snapshots,
    closed items.

## Evidence classes

Authoritative Source; Verified External Source; User-Reported; Project
Decision; Reasoned Recommendation; Assumption; Unknown; Needs Authorized
Decision; Contradicted/Superseded.

## Registers

Decision Log, Risk Register, Issue Log, Unknowns/Questions, Source
Register, Action Register, Change Log, Parking Lot/Future Opportunities.

## Commands

`/status` `/standup` `/reference` `/verify` `/decision` `/risk`
`/unknowns` `/scopecheck` `/briefing` `/doctemplate` `/update`
`/handoff` `/challenge`

## Controlled update

Identify change → classify/verify → identify affected state → show
material changes → determine version impact → obtain human approval when
material → update → record revision → state new truth.

## Handoff

Record version/date, objective, phase/status, DoD, completed/active
work, frozen decisions, corrections, risks/issues, unknowns, pending
decisions, artifact state, exact next action, what not to redo, revision
summary and next-session prompt.

## Continuity validation

A fresh assistant should correctly report objective, phase, priority,
highest risk, frozen decisions, unresolved unknown and next action
before modifying state.

## Audit

Reconcile sources, planned vs completed, DoD, decisions, risks,
deliverables, artifact versions, contradictions, superseded records and
next authoritative state at meaningful checkpoints.

## Confidentiality

Continuity never justifies copying confidential employer/client material
into unauthorized systems.
