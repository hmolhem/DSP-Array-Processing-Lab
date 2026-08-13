# PR #13 Handoff — Master DSP Curriculum and Engineering Lab Standard

## 1. PR Identity

- **PR Number:** `#13`
- **PR Title:** `Add master DSP curriculum and engineering lab standard`
- **Status:** `Merged`
- **Date:** `2026-08-12`
- **Repository:** `hmolhem/DSP-Array-Processing-Lab`
- **Source Branch:** `docs/master-dsp-curriculum`
- **Base Branch:** `main`
- **Head Commit:** `aa281de`
- **Merge Commit:** `9d8fb0d`

---

## 2. Purpose

PR #13 established the long-term technical and documentation architecture of `DSP-Array-Processing-Lab`.

Before this PR, the repository already contained a strong first engineering exercise on FFT spectral leakage, but the long-term roadmap was still represented by a relatively short and coarse list of future topics.

The purpose of this PR was to replace that coarse roadmap with a structured engineering framework capable of supporting long-term development from DSP fundamentals through advanced statistical DSP, array processing, DOA estimation, radar processing, and FPGA/HLS-oriented implementation.

The PR intentionally focused on:

- repository architecture,
- curriculum design,
- engineering-lab standards,
- portfolio structure,
- documentation strategy.

No DSP implementation code was changed.

---

## 3. Context Before This PR

Before PR #13:

- `Ex01 — FFT Spectral Leakage` was already complete.
- Ex01 included Python code, theory documentation, interview questions, figures, animation, video, LaTeX, and PDF artifacts.
- The root `README.md` contained an initial roadmap with approximately twelve broad future topics.
- The repository did not yet contain a formal master curriculum.
- There was no written repository-wide Engineering Lab Standard.
- Curriculum concepts and chronological exercise numbering were not formally separated.
- There was no explicit distinction between:
  - conceptual curriculum,
  - engineering labs,
  - integrated flagship projects.

This created a risk that the repository could evolve into either:

- a collection of disconnected tutorials, or
- a large number of very small exercises without a coherent engineering architecture.

---

## 4. Files Changed

### Added

- `docs/DSP_MASTER_CURRICULUM.md`
  - Defines the complete DSP learning and engineering progression.
  - Organizes the curriculum into fifteen technical modules.
  - Defines curriculum topics from `DSP-001` through `DSP-142`.
  - Establishes integrated flagship-project directions.

- `docs/ENGINEERING_LAB_STANDARD.md`
  - Defines the engineering quality standard for future labs.
  - Establishes expectations for theory, implementation, validation, quantitative evaluation, failure analysis, reproducibility, computational analysis, testing, and hardware awareness.

### Modified

- `README.md`
  - Replaced the coarse initial roadmap with the new repository architecture.
  - Added links to the Master Curriculum and Engineering Lab Standard.
  - Added the three-layer portfolio model.
  - Added flagship-project direction.
  - Mapped Ex01 to the formal curriculum.

---

## 5. Technical Changes

### 5.1 Three-Layer Repository Architecture

The repository was formally organized into three layers:

1. **Knowledge Curriculum**
2. **Engineering Labs**
3. **Flagship Projects**

The purpose of this architecture is to prevent curriculum concepts, implementation chronology, and integrated engineering projects from being conflated.

---

### 5.2 Master Curriculum

The curriculum was expanded into fifteen modules:

1. Signal Foundations
2. Systems, Sampling, and Convolution
3. Fourier Analysis, DFT, and FFT
4. Z-Transform and Digital Filters
5. Random Signals and Statistical DSP
6. Matrix DSP, EVD, SVD, PCA, and ICA
7. Spectral and Time-Frequency Estimation
8. Detection and Estimation
9. Adaptive, Multirate, and Complex-Baseband DSP
10. Array Processing Fundamentals
11. DOA and Subspace Processing
12. Sparse Arrays, Coarrays, and MIMO
13. Radar Signal Processing
14. Tracking and Sensor Estimation
15. Real-Time, Numerical, and FPGA/HLS DSP

The curriculum currently extends from:

`DSP-001`

through:

`DSP-142`

---

### 5.3 Curriculum ID vs Exercise ID

A critical architecture decision was made:

**Curriculum topic IDs and repository exercise IDs are intentionally different.**

Curriculum IDs describe the conceptual knowledge sequence.

Exercise IDs describe chronological engineering implementations.

Therefore:

`Repository Ex01 = Curriculum DSP-018`

This avoids renumbering existing repository history and allows one Engineering Lab to cover multiple curriculum topics.

---

### 5.4 Engineering Lab Standard

A formal engineering flow was established:

Problem
→ Theory
→ Mathematical Model
→ Implementation
→ Validation
→ Engineering Interpretation

For advanced labs, the flow extends to:

Failure Analysis
→ Statistical Evaluation
→ Computational Analysis
→ Real-Time / Hardware Considerations

Important labs are expected to include, when relevant:

- explicit assumptions,
- mathematical models,
- quantitative metrics,
- parameter sweeps,
- Monte Carlo evaluation,
- failure modes,
- numerical considerations,
- computational complexity,
- reproducibility,
- testing,
- hardware-awareness analysis.

A successful plot alone is not considered sufficient validation.

---

### 5.5 Lab Depth Classification

Three lab-depth classes were established.

#### Foundation Lab

Typical expectations:

- mathematical explanation,
- Python implementation,
- explicit validation,
- figures,
- README,
- notes.

#### Deep-Dive Lab

May additionally include:

- detailed theory,
- parameter sweeps,
- quantitative metrics,
- failure analysis,
- computational considerations,
- Monte Carlo evaluation,
- interview preparation.

#### Portfolio Milestone

May additionally include:

- LaTeX report,
- compiled PDF,
- animation or video,
- C++ implementation,
- fixed-point analysis,
- HLS/FPGA implementation,
- benchmark results,
- professional technical communication.

Ex01 was classified as the initial Portfolio Milestone.

---

### 5.6 Markdown-First Documentation Strategy

Markdown was selected as the canonical development format for technical documentation.

The intended progression is:

Markdown
→ Technical Maturity
→ LaTeX
→ PDF

LaTeX/PDF should be used selectively for formal reports or Portfolio Milestones rather than for every exercise.

---

### 5.7 Integrated Project Roadmap

Eight initial flagship-project directions were defined:

- `PROJECT-01 — Digital Spectrum Analyzer`
- `PROJECT-02 — Weak Signal Next to a Strong Interferer`
- `PROJECT-03 — PCA/ICA Multi-Sensor Source Separation`
- `PROJECT-04 — Adaptive Interference Canceller`
- `PROJECT-05 — Beamforming Laboratory`
- `PROJECT-06 — DOA Estimation Laboratory`
- `PROJECT-07 — Sparse and MIMO Array Laboratory`
- `PROJECT-08 — End-to-End Radar DSP Chain`

The end-to-end radar direction is intended to connect:

Waveform
→ Target / Channel Model
→ ADC
→ Range
→ Doppler
→ Detection
→ Array / DOA
→ Target Estimates
→ Tracking

---

## 6. Design Decisions

### Decision 1 — Do Not Create One Exercise per Curriculum Topic

#### Rationale

The curriculum contains more than one hundred concepts.

Creating one repository folder for every concept would produce a tutorial-style repository with excessive fragmentation.

#### Consequence

A single Engineering Lab may cover several curriculum IDs.

---

### Decision 2 — Preserve Historical Exercise Numbering

#### Rationale

Ex01 already existed with significant repository history and multiple prior PRs.

Renumbering it to match the curriculum would damage traceability and unnecessarily rewrite established history.

#### Consequence

Exercise IDs remain chronological and independent of curriculum IDs.

---

### Decision 3 — Engineering Evidence Over Tutorial Volume

#### Rationale

The repository is intended to demonstrate engineering capability, not merely topic exposure.

#### Consequence

Important labs should emphasize:

- validation,
- metrics,
- tradeoffs,
- failure conditions,
- reproducibility,
- computational implications.

---

### Decision 4 — Python as Initial Golden Reference

#### Rationale

Python provides rapid numerical implementation and clear correspondence with mathematical models.

#### Consequence

Selected algorithms may later follow:

Mathematics
→ Python Reference
→ Validated Experiment
→ Optimized Implementation
→ C++
→ Fixed Point
→ HLS / FPGA

---

### Decision 5 — Hardware Awareness Begins Before Hardware Implementation

#### Rationale

Not every algorithm should immediately be implemented on FPGA.

However, computational and architecture implications should be considered early.

#### Consequence

Advanced labs should progressively discuss:

- streaming,
- frame buffering,
- memory,
- throughput,
- latency,
- parallelism,
- fixed-point feasibility,
- matrix inversion,
- EVD/SVD cost,
- CPU vs FPGA partitioning.

---

## 7. Validation Performed

Before commit and merge:

- `git status` was reviewed.
- The two new documentation files were inspected.
- Markdown math delimiters were checked.
- `git diff --check` passed.
- The three intended files were staged explicitly.
- `git diff --cached --stat` was reviewed.
- `git diff --cached --check` passed.
- `git diff --cached --name-status` confirmed the intended scope.

Staged scope was:

- modified `README.md`,
- added `docs/DSP_MASTER_CURRICULUM.md`,
- added `docs/ENGINEERING_LAB_STANDARD.md`.

The commit contained:

- 3 changed files,
- 1860 insertions,
- 70 deletions.

No implementation code was modified.

---

## 8. Issues Encountered

### Issue 1 — PowerShell Here-String Handling

#### Symptom

While creating long Markdown content through PowerShell, malformed here-string handling caused PowerShell to remain in continuation mode.

#### Cause

Large Markdown blocks contained code fences and syntax that made the shell-based editing workflow error-prone.

#### Resolution

Long technical Markdown files were subsequently edited directly in VS Code rather than injected through complex PowerShell here-strings.

---

### Issue 2 — Initial Math-Delimiter Verification

#### Symptom

One documentation file temporarily contained standalone:

`[`

and:

`]`

instead of proper display-math delimiters.

#### Resolution

A targeted sanity check counted standalone brackets and corrected the delimiters before the PR was committed.

---

## 9. Known Limitations

At the time PR #13 was merged:

- the formal handoff documentation system did not yet exist,
- repository-wide UTF-8 and line-ending standards had not yet been added,
- some GitHub Markdown rendering and encoding issues were discovered after merge,
- historical PRs had not been documented through formal handoffs.

The Markdown encoding and rendering issues were subsequently addressed by PR #14.

Repository text-formatting standards were subsequently addressed by PR #15.

---

## 10. Curriculum and Lab Mapping

This PR establishes the complete mapping framework.

Relevant explicit mapping:

- **Engineering Lab:** `Ex01`
- **Curriculum Topic:** `DSP-018 — FFT Spectral Leakage`

The repository architecture allows later labs to span multiple curriculum topics.

---

## 11. Repository State After Merge

Immediately after PR #13 merged:

- `main` advanced to merge commit `9d8fb0d`.
- `docs/DSP_MASTER_CURRICULUM.md` existed on `main`.
- `docs/ENGINEERING_LAB_STANDARD.md` existed on `main`.
- the root `README.md` reflected the new repository architecture.
- the old coarse roadmap had been replaced by a structured long-term curriculum.
- Ex01 was formally mapped to `DSP-018`.
- future labs could now be classified as Foundation, Deep-Dive, or Portfolio Milestone work.
- future flagship projects had formal repository-level direction.

After merge:

- remote branch `docs/master-dsp-curriculum` was deleted,
- local `main` was synchronized,
- the local feature branch was deleted.

---

## 12. Follow-Up Work

### Required Follow-Up

PR #13 exposed documentation-rendering and encoding problems that required correction.

These were handled in:

`PR #14 — Fix Markdown encoding and math rendering`

### Optional Follow-Up

- historical curriculum cross-linking,
- automated documentation linting,
- formal handoff documentation,
- future CI checks.

---

## 13. Recommended Next Step

The immediate next step after PR #13 was:

**repair Markdown encoding and GitHub math rendering before beginning additional Engineering Labs.**

This became PR #14.

---

## 14. Continuity Notes

The most important architectural rules introduced by this PR are:

1. Do not equate curriculum IDs with exercise IDs.
2. Do not create one tiny repository exercise for every DSP concept.
3. Use coherent Engineering Labs to cover related curriculum topics.
4. Require quantitative validation where practical.
5. Include failure cases and engineering interpretation.
6. Treat Python as the reference implementation environment.
7. Reserve formal LaTeX/PDF artifacts for selected milestones.
8. Preserve the three-layer structure:
   - Knowledge Curriculum,
   - Engineering Labs,
   - Flagship Projects.

These rules should remain stable unless a future architecture PR explicitly revises them.

---

## 15. Historical Accuracy

This handoff was created retrospectively during PR #16.

PR identity, branch names, commit information, changed-file counts, and merge state were reconstructed from verified Git/GitHub history.

Engineering rationale and workflow details were reconstructed from the development session associated with PR #13.

---

## 16. Completion Status

PR #13 is complete and merged.

Its architecture remains active and serves as the foundation for all subsequent DSP-Array-Processing-Lab development.
