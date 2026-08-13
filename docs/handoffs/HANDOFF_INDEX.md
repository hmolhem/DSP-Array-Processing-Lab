# DSP-Array-Processing-Lab - Handoff Index

## 1. Purpose

This directory preserves the technical continuity of `DSP-Array-Processing-Lab`.

The handoff system records the state, decisions, validation, and next steps associated with major repository changes so that project continuity does not depend on chat history, personal memory, or a single development session.

The handoff system is intended to support:

- long-term repository continuity,
- reproducible engineering development,
- transfer between development sessions or chats,
- recovery of design rationale,
- traceability from pull requests to technical decisions,
- curriculum and engineering-lab tracking,
- clean transition between completed work and the next task.

---

## 2. Handoff Types

The repository uses several handoff types.

### PR Handoff

A PR handoff records the engineering context, decisions, validation, and expected resulting state associated with a pull request.

A PR handoff should normally include:

- PR number and title,
- date,
- source branch,
- base branch,
- relevant commit information and final merge metadata when available,
- purpose,
- files changed,
- technical changes,
- design decisions,
- validation performed,
- known limitations,
- curriculum mapping when applicable,
- resulting repository state,
- recommended next step.

Naming convention:

`PR-NNN_short-description.md`

Example:

`PR-015_repo-text-standards.md`

---

### Lab Start Handoff

A Lab Start Handoff defines the technical starting point for a new Engineering Lab.

It should provide enough context for the lab to be developed in a separate working session or chat without requiring reconstruction of the full repository history.

A Lab Start Handoff should normally include:

- repository state,
- relevant prior labs,
- curriculum mapping,
- engineering objective,
- required theory,
- experiment scope,
- validation requirements,
- expected artifacts,
- Git workflow,
- known constraints,
- first task.

Naming convention:

`EXNN_START_HANDOFF.md`

Example:

`EX02_START_HANDOFF.md`

---

### Project Start Handoff

A Project Start Handoff serves the same role for a larger Flagship Project.

Naming convention:

`PROJECT-NN_START_HANDOFF.md`

Example:

`PROJECT-03_START_HANDOFF.md`

---

## 3. Source-of-Truth Policy

The Git repository is the persistent source of truth for technical project state.

Chat sessions may support planning, reasoning, implementation, debugging, and review, but important engineering decisions should be transferred into repository documentation.

The preferred continuity model is:

Repository State
→ Start / Existing Handoff
→ New Working Session
→ Engineering Work
→ PR Handoff Updated on Feature Branch
→ Pull Request
→ Merge
→ Synchronized Repository State

Important technical decisions should not exist only inside a chat history.

---

## 4. Handoff Lifecycle

For a normal engineering change:

1. Start from synchronized `main`.
2. Create a focused branch.
3. Perform the engineering work.
4. Validate the implementation or documentation.
5. Review the initial Git diff.
6. Commit and push the working branch when appropriate.
7. Open the pull request so the actual PR number and metadata are available.
8. Create or update the PR handoff on the same feature branch before merge.
9. Update this index if a new handoff document was added.
10. Validate the handoff files and review the final Git diff.
11. Commit and push the handoff updates so they become part of the same pull request.
12. Complete final PR review and merge the pull request.
13. Synchronize local `main`.
14. Remove obsolete local and remote branches.

A PR handoff must normally be present in the same pull request before that pull request is merged.

No separate follow-up PR is required merely to record a merge commit, merge timestamp, or other metadata that GitHub already preserves authoritatively.

For major labs or projects, a Start Handoff should be created before implementation begins.

---

## 5. Handoff Quality Standard

A useful handoff must describe more than what files changed.

It should preserve the engineering reasoning needed to continue the work.

A strong handoff should answer:

1. What was the objective?
2. What changed?
3. Why was the change made?
4. What design decisions were made?
5. How was the result validated?
6. What limitations remain?
7. What repository state resulted?
8. What should happen next?

The handoff should be concise enough to review quickly but complete enough to restore technical context.

---

## 6. Relationship to the Master Curriculum

The repository separates:

- Curriculum IDs,
- Engineering Lab IDs,
- Project IDs,
- Pull Request IDs.

These identifiers serve different purposes.

Example:

`DSP-018`

is a curriculum topic.

`Ex01`

is an Engineering Lab.

A single Engineering Lab may cover multiple curriculum topics.

A single Engineering Lab may also require multiple pull requests.

Handoffs should preserve these relationships explicitly when relevant.

---

## 7. Current Handoff Index

| Handoff | Type | Scope | Status |
| --- | --- | --- | --- |
| `PR-013_master-dsp-curriculum.md` | PR Handoff | Master curriculum and Engineering Lab architecture | Active |
| `PR-014_markdown-encoding-math.md` | PR Handoff | Markdown encoding and GitHub math-rendering corrections | Active |
| `PR-015_repo-text-standards.md` | PR Handoff | UTF-8, LF, EditorConfig, and Git attributes standards | Active |
| `PR-016_handoff-system.md` | PR Handoff | Formal handoff documentation system and same-PR continuity lifecycle | Active |
| `EX02_START_HANDOFF.md` | Lab Start Handoff | Ex02 - Window Functions and Spectral Resolution | Ready for use after PR #16 merge |

---

## 8. Historical Backfill

Pull requests prior to PR #13 were completed before the formal handoff system was introduced.

They may be documented later using retrospective handoffs.

The historical backfill should be incremental and should not block current engineering development.

Priority should be given to handoffs that preserve technically important decisions, major portfolio milestones, or architecture changes.

---

## 9. Required Template

New PR handoffs should use:

`docs/handoffs/HANDOFF_TEMPLATE.md`

The template provides a consistent structure while allowing sections to be omitted when they are not relevant.

---

## 10. Current Repository Transition

The handoff system is being introduced after completion of the repository architecture and text-formatting infrastructure.

The immediate transition sequence is:

PR #13
→ Master DSP curriculum and Engineering Lab standard

PR #14
→ Markdown encoding and math-rendering corrections

PR #15
→ Repository text and line-ending standards

PR #16
→ Formal handoff documentation system

Next Engineering Lab
→ Ex02 - Window Functions and Spectral Resolution

---

## 11. Maintenance Rule

Whenever a new handoff document is added:

1. add it under `docs/handoffs/`,
2. add or update its entry in this index,
3. verify internal links and filenames,
4. review Markdown formatting,
5. include the change in the same focused pull request when practical.

This index should remain the primary navigation page for repository handoff documentation.
