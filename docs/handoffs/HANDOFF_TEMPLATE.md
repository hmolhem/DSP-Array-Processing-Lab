# Pull Request Handoff Template

## 1. PR Identity

- **PR Number:** `#NNN` — verify after the pull request is opened
- **PR Title:** `PR title`
- **Status:** `In Progress / Open / Merged`
- **Date:** `YYYY-MM-DD`
- **Repository:** `hmolhem/DSP-Array-Processing-Lab`
- **Source Branch:** `branch/name`
- **Base Branch:** `main`
- **Base Commit:** `base commit SHA`
- **Head Commit:** `current or final branch commit SHA`
- **Merge Commit:** `Pending at merge; recoverable from GitHub PR metadata`

### Same-PR Handoff Rule

A PR handoff should normally be created or updated on the same feature branch as the pull request it documents.

Do not create a separate follow-up PR merely to record the previous PR's merge commit or final merge timestamp.

Information that does not exist before merge, especially the final merge commit SHA, may remain marked as pending because GitHub pull-request metadata is the authoritative source for that information.

For retrospective handoffs, replace pending fields with verified historical values when available.
---

## 2. Purpose

Describe the engineering or repository problem addressed by this pull request.

The purpose should explain:

- what needed to change,
- why the change was necessary,
- what scope was intentionally included,
- what scope was intentionally excluded.

---

## 3. Context Before This PR

Describe the relevant repository state before the change.

Include only information needed to understand why this PR exists.

Examples:

- previous implementation state,
- known documentation gap,
- validation deficiency,
- repository infrastructure limitation,
- prior PR dependency,
- unresolved technical issue.

---

## 4. Files Changed

List the important files added, modified, or removed.

Example:

- `path/to/file_a.md` — added technical documentation.
- `path/to/file_b.py` — modified reference implementation.
- `path/to/file_c.png` — generated validated figure.

Do not merely reproduce `git diff --stat`; explain the role of each important file.

---

## 5. Technical Changes

Describe the actual technical work performed.

This section should capture the engineering substance of the PR.

Examples include:

- mathematical-model changes,
- algorithm implementation,
- experiment design,
- numerical correction,
- documentation architecture,
- Git or repository infrastructure,
- encoding or formatting policy,
- test additions,
- visualization improvements,
- computational or hardware-oriented changes.

---

## 6. Design Decisions

Record decisions that future work may depend on.

For each important decision, describe:

### Decision

State the decision.

### Rationale

Explain why it was chosen.

### Alternatives Considered

Record meaningful alternatives when relevant.

### Consequence

Explain what this decision implies for future development.

Repeat this structure for additional decisions when necessary.

---

## 7. Validation Performed

Document how the change was verified.

Possible validation evidence includes:

- analytical checks,
- numerical reference comparisons,
- deterministic test cases,
- Monte Carlo evaluation,
- visual inspection,
- Markdown rendering inspection,
- encoding checks,
- line-ending checks,
- `git diff --check`,
- staged-diff review,
- generated-artifact inspection,
- cross-implementation comparison.

Example:

- `git diff --check` passed.
- `git diff --cached --check` passed.
- Numerical output matched the analytical reference within the stated tolerance.
- Generated figures were visually inspected.
- UTF-8 and line-ending policy were verified.

Validation statements should be specific and reproducible when practical.

---

## 8. Issues Encountered

Record meaningful problems discovered during the work.

Examples:

- incorrect assumptions,
- numerical instability,
- encoding corruption,
- Markdown rendering failure,
- API or library behavior,
- Git workflow issue,
- implementation bug,
- unexpected experimental result.

For each important issue, briefly record:

- symptom,
- cause,
- resolution.

This section may be marked `None` when no meaningful issue occurred.

---

## 9. Known Limitations

Document limitations that remain after merge.

Examples:

- incomplete parameter coverage,
- missing Monte Carlo validation,
- no fixed-point implementation,
- no hardware benchmark,
- limited source models,
- documentation still requiring expansion,
- historical information not yet backfilled.

If no known limitation is relevant, state:

`No material limitations identified for the scope of this PR.`

---

## 10. Curriculum and Lab Mapping

Record repository-learning relationships when relevant.

Example:

- **Engineering Lab:** `Ex02`
- **Curriculum Topics:** `DSP-019` through `DSP-022`
- **Flagship Project Connection:** `PROJECT-01`, if applicable

For infrastructure-only PRs, state:

`Not directly mapped to a DSP curriculum topic.`

---

## 11. Repository State After Merge

Describe the important resulting state.

Include information such as:

- new files now present,
- new standards now enforced,
- completed lab capability,
- updated documentation architecture,
- new validated artifacts,
- expected or completed branch-cleanup status,
- expected or verified synchronization state of `main`,
- final merge metadata when already available; otherwise note that GitHub PR metadata is authoritative.

The purpose is to allow a future session to understand the repository state without reconstructing the full PR history.

---

## 12. Follow-Up Work

List the next technically meaningful tasks created or enabled by this PR.

Separate:

### Required Follow-Up

Work necessary to complete an existing technical objective.

### Optional Follow-Up

Enhancements that may be valuable but do not block progress.

Use `None` when appropriate.

---

## 13. Recommended Next Step

State the single most logical next engineering action after this PR.

This should be specific enough that a new working session can begin without reconstructing the project plan.

---

## 14. Continuity Notes

Record any information that is especially important when transferring the work to:

- a new development session,
- a new ChatGPT chat,
- another engineer,
- a future repository-maintenance task.

Do not duplicate the entire document.

Use this section for details that would otherwise be easy to lose.

---

## 15. Historical Accuracy Rule

For retrospective handoffs:

- use repository history as the primary source,
- distinguish verified facts from reconstructed context,
- do not invent unavailable commit metadata or validation results,
- label uncertain information explicitly when necessary.

For current PRs, create or update the handoff while technical context is still fresh.

---

## 16. Completion Check

Before considering the handoff complete, verify:

- PR identity is correct.
- Branch and commit information is correct.
- Important files are accounted for.
- Technical changes are explained.
- Major design decisions are preserved.
- Validation is recorded.
- Known limitations are explicit.
- Curriculum or lab mapping is included when relevant.
- Repository state after merge is clear.
- The recommended next step is actionable.
