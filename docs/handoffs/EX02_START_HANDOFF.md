# Ex02 Start Handoff — Window Functions and Spectral Resolution

## 1. Handoff Identity

- **Engineering Lab:** `Ex02`
- **Lab Title:** `Window Functions and Spectral Resolution`
- **Repository:** `hmolhem/DSP-Array-Processing-Lab`
- **Primary Curriculum Mapping:** `DSP-019` through `DSP-022`
- **Planned Lab Depth:** `Deep-Dive Engineering Lab`
- **Predecessor Lab:** `Ex01 — FFT Spectral Leakage`
- **Development Status:** `Not yet implemented`
- **Handoff Type:** `Lab Start Handoff`

---

## 2. Purpose of This Handoff

This document defines the technical starting point for Ex02.

It is intended to allow Ex02 to be developed in a separate engineering session or ChatGPT conversation without requiring reconstruction of the full repository history.

The handoff captures:

- repository architecture,
- prior relevant work,
- curriculum mapping,
- engineering objective,
- mathematical scope,
- experiment strategy,
- validation requirements,
- expected artifacts,
- failure cases,
- Git workflow,
- implementation philosophy,
- completion criteria.

The new Ex02 working session should use this document together with:

- `docs/DSP_MASTER_CURRICULUM.md`
- `docs/ENGINEERING_LAB_STANDARD.md`
- `docs/handoffs/HANDOFF_INDEX.md`

as persistent repository references.

---

## 3. Repository Architecture

`DSP-Array-Processing-Lab` follows a three-layer architecture.

### Layer 1 — Knowledge Curriculum

The conceptual DSP learning sequence is defined in:

`docs/DSP_MASTER_CURRICULUM.md`

Curriculum topics are identified using IDs such as:

`DSP-019`

---

### Layer 2 — Engineering Labs

Engineering Labs convert related curriculum concepts into reproducible technical evidence.

Examples:

- `Ex01 — FFT Spectral Leakage`
- `Ex02 — Window Functions and Spectral Resolution`

An Engineering Lab may cover multiple curriculum topics.

---

### Layer 3 — Flagship Projects

Flagship Projects integrate multiple labs and algorithms into larger systems.

Examples include:

- Digital Spectrum Analyzer
- PCA/ICA Multi-Sensor Source Separation
- Beamforming Laboratory
- DOA Estimation Laboratory
- Sparse/MIMO Array Laboratory
- End-to-End Radar DSP Chain

---

## 4. Critical Identifier Rule

Curriculum IDs and Engineering Lab IDs are intentionally different.

Curriculum IDs represent conceptual learning order.

Engineering Lab IDs represent chronological repository implementations.

Therefore:

`Ex01 = DSP-018`

does not imply:

`Ex02 = DSP-019 only`

Ex02 is intentionally expected to span several related curriculum topics.

Do not create one small repository exercise for every individual curriculum ID.

---

## 5. Relevant Repository History

### PR #13 — Master DSP Curriculum and Engineering Lab Standard

PR #13 introduced:

- `docs/DSP_MASTER_CURRICULUM.md`
- `docs/ENGINEERING_LAB_STANDARD.md`
- the three-layer repository architecture,
- formal curriculum numbering,
- lab-depth classifications,
- flagship-project direction.

Detailed handoff:

`docs/handoffs/PR-013_master-dsp-curriculum.md`

---

### PR #14 — Markdown Encoding and Math Rendering Fix

PR #14 corrected:

- UTF-8 mojibake,
- corrupted Unicode characters,
- GitHub display-math formatting,
- Markdown fenced-code-block spacing.

Repository Markdown block mathematics should use:

```text
$$
...
$$
```

rather than:

```text
\[
...
\]
```

Detailed handoff:

`docs/handoffs/PR-014_markdown-encoding-math.md`

---

### PR #15 — Repository Text and Line-Ending Standards

PR #15 introduced:

- `.editorconfig`
- `.gitattributes`

Repository text policy now includes:

- UTF-8,
- LF for normal repository text,
- final newline,
- trailing-whitespace control,
- explicit binary-file declarations,
- CRLF exceptions for Windows-oriented scripts.

Detailed handoff:

`docs/handoffs/PR-015_repo-text-standards.md`

---

### PR #16 — Handoff Documentation System

PR #16 introduces the persistent handoff architecture.

Its purpose is to prevent project continuity from depending only on chat history or personal memory.

Ex02 should begin only after PR #16 is merged, local `main` is synchronized, and the PR #16 feature branch is cleaned up.

The new Ex02 development branch should be created from synchronized `main`.

---

## 6. Relevant Completed Lab

### Ex01 — FFT Spectral Leakage

Ex01 is the predecessor to Ex02 and serves as the first Portfolio Milestone.

Ex01 established the physical and numerical meaning of spectral leakage.

Important experiment parameters included:

- sampling frequency: `1000 Hz`,
- number of samples: `256`,
- FFT bin spacing: approximately `3.90625 Hz`,
- coherent sinusoid: `125.0 Hz`,
- non-coherent sinusoid: `123.5 Hz`.

The experiment demonstrated that a finite-duration sinusoid whose frequency does not align with the DFT frequency grid spreads spectral energy across neighboring FFT bins.

Ex01 includes:

- Python reference implementation,
- engineering README,
- engineering notes,
- detailed theory document,
- interview questions,
- line-marker spectrum,
- stem spectrum,
- GIF animation,
- MP4 animation,
- LaTeX technical note,
- compiled PDF.

Ex01 should be treated as the technical starting point for Ex02 rather than duplicated.

---

## 7. Ex02 Curriculum Mapping

Ex02 should primarily cover:

### DSP-019 — Window Functions

Study common analysis windows and their effect on finite-record spectral estimation.

### DSP-020 — Frequency Resolution

Distinguish FFT bin spacing, observation duration, main-lobe width, and practical ability to distinguish nearby spectral components.

### DSP-021 — Zero Padding

Demonstrate the distinction between:

- denser FFT sampling,
- interpolated spectral appearance,
- true resolving capability.

### DSP-022 — Two-Tone Spectral Resolution

Study the ability to distinguish two nearby tones, especially when one tone is substantially weaker than the other.

---

## 8. Lab Classification

Ex02 should be developed as a:

### Deep-Dive Engineering Lab

It should not be implemented as a simple window-function tutorial.

A completed Ex02 should contain:

- mathematical explanation,
- Python reference implementation,
- explicit validation,
- quantitative metrics,
- parameter sweeps,
- failure analysis,
- engineering interpretation,
- reusable figures,
- engineering README,
- engineering notes,
- detailed theory documentation,
- tests where meaningful.

A LaTeX/PDF report is not automatically required.

Promotion to Portfolio Milestone should be decided only after technical maturity is reached.

---

## 9. Central Engineering Problem

The central engineering question is:

> How does window selection affect spectral leakage, frequency discrimination, amplitude accuracy, and the ability to detect a weak spectral component located near a stronger spectral component?

The lab should make clear that window selection is an engineering tradeoff.

No single window should be presented as universally superior.

The relevant trade space includes:

- main-lobe width,
- sidelobe level,
- leakage suppression,
- equivalent noise bandwidth,
- coherent gain,
- scalloping loss,
- amplitude correction,
- close-tone discrimination,
- weak-tone visibility.

---

## 10. Core Research Questions

Ex02 should answer at least the following questions.

### Q1 — Why do windows exist?

What mathematical operation is performed when a finite observation interval is applied to a theoretically infinite signal?

How does multiplication in the time domain affect the frequency domain?

---

### Q2 — What does the rectangular window actually mean?

Ex01 implicitly used a rectangular observation window.

Ex02 should make this assumption explicit.

The rectangular window should be treated as a real window with specific spectral characteristics, not as the absence of windowing.

---

### Q3 — What is gained by reducing sidelobes?

How does sidelobe suppression improve visibility of weak signals near stronger spectral components?

---

### Q4 — What is sacrificed when sidelobes are reduced?

How does widening of the main lobe affect frequency discrimination?

---

### Q5 — What does frequency resolution actually mean?

The lab must distinguish:

- FFT bin spacing,
- spectral sampling density,
- observation duration,
- window main-lobe width,
- practical two-tone resolution.

These concepts should not be treated as synonyms.

---

### Q6 — Does zero padding improve frequency resolution?

Ex02 must demonstrate numerically that zero padding:

- produces a denser sampling of the underlying DFT/DTFT structure,
- may improve visual peak localization,
- may support interpolation,

but:

- does not create new measured information,
- does not fundamentally improve resolving power between two unresolved tones.

---

### Q7 — Can a weak tone be hidden by a strong tone?

The lab should demonstrate conditions under which a weak nearby signal becomes buried under the sidelobe structure of a stronger component.

---

### Q8 — Can windowing reduce amplitude accuracy?

The effect of coherent gain must be studied.

Windowed amplitude estimates should not be interpreted without considering window-dependent amplitude correction.

---

## 11. Minimum Window Set

At minimum, compare:

- Rectangular
- Hann
- Hamming
- Blackman

Additional windows should be introduced only if they answer a specific engineering question.

Possible later additions include:

- Blackman-Harris
- Kaiser
- Flat Top

Do not add windows merely to produce more plots.

---

## 12. Mathematical Model

A sampled sinusoid may be represented as:

$$
x[n]
=
A\cos
\left(
2\pi \frac{f_0}{f_s}n + \phi
\right)
$$

for:

$$
n = 0,1,\ldots,N-1
$$

Windowing produces:

$$
x_w[n] = x[n]w[n]
$$

where:

- $x[n]$ is the sampled signal,
- $w[n]$ is the selected window,
- $x_w[n]$ is the windowed finite record.

The DFT is:

$$
X[k]
=
\sum_{n=0}^{N-1}
x_w[n]
e^{-j2\pi kn/N}
$$

The relationship between time-domain multiplication and frequency-domain convolution should be explained conceptually and mathematically.

---

## 13. FFT Bin Spacing

The FFT bin spacing is:

$$
\Delta f
=
\frac{f_s}{N}
$$

The observation duration is:

$$
T_{\mathrm{obs}}
=
\frac{N}{f_s}
$$

Therefore:

$$
\Delta f
=
\frac{1}{T_{\mathrm{obs}}}
$$

This relationship is fundamental but must not be misinterpreted as a complete definition of two-tone resolving capability.

---

## 14. Window Metrics

Ex02 should define and evaluate meaningful quantitative window metrics.

### 14.1 Coherent Gain

A useful normalized definition is:

$$
CG
=
\frac{1}{N}
\sum_{n=0}^{N-1} w[n]
$$

This metric is important for amplitude correction.

---

### 14.2 Equivalent Noise Bandwidth

A normalized ENBW in FFT-bin units may be written as:

$$
\mathrm{ENBW}_{\mathrm{bins}}
=
N
\frac{
\sum_{n=0}^{N-1} w^2[n]
}{
\left(
\sum_{n=0}^{N-1} w[n]
\right)^2
}
$$

Its interpretation and units must be clearly documented.

If ENBW is reported in hertz:

$$
\mathrm{ENBW}_{\mathrm{Hz}}
=
\mathrm{ENBW}_{\mathrm{bins}}
\Delta f
$$

---

### 14.3 Peak Sidelobe Level

Peak sidelobe level should be measured relative to the main-lobe peak.

The exact measurement procedure must be documented so that the result is reproducible.

---

### 14.4 Main-Lobe Width

Main-lobe width must be defined before measurement.

Possible definitions include:

- null-to-null width,
- 3 dB width.

Do not mix different definitions in the same comparison.

---

### 14.5 Scalloping Loss

Scalloping loss should quantify the amplitude loss associated with a sinusoid located between FFT-bin centers.

The exact frequency offset used for the measurement must be documented.

---

## 15. Required Experiment Families

Ex02 should contain several coherent experiment families rather than one oversized script.

### Experiment A — Window Frequency Responses

Compare the spectral responses of the selected windows.

Purpose:

- visualize main-lobe width,
- visualize sidelobe structure,
- quantify window metrics.

---

### Experiment B — Single-Tone Leakage

Extend the Ex01 leakage experiment using multiple windows.

Compare:

- coherent tone,
- non-coherent tone,
- window choice,
- amplitude correction.

Purpose:

demonstrate what each window changes relative to Ex01.

---

### Experiment C — Frequency-Resolution Study

Investigate nearby equal-amplitude tones.

Sweep tone separation.

Purpose:

identify the relationship between:

- record length,
- window main-lobe width,
- practical two-tone discrimination.

---

### Experiment D — Weak Tone Near Strong Tone

Use:

- one strong sinusoid,
- one weaker nearby sinusoid.

Sweep:

- frequency separation,
- weak-to-strong amplitude ratio,
- window type.

Purpose:

determine when sidelobe suppression becomes more important than narrow main-lobe width.

This should become one of the central engineering demonstrations of Ex02.

---

### Experiment E — Zero-Padding Study

For the same fixed observation record, compare several FFT lengths.

Example concept:

```text
N samples
→ N-point FFT
→ 4N-point FFT
→ 8N-point FFT
```

The underlying measured data must remain unchanged.

Purpose:

demonstrate that denser FFT sampling does not create new resolving information.

---

### Experiment F — Observation-Length Study

Change the actual number of measured samples.

Purpose:

contrast true increase in observation duration with zero padding.

This provides the critical comparison:

```text
More measured samples
vs
More zero-padded FFT samples
```

---

## 16. Parameter Sweeps

Candidate sweep parameters include:

- window type,
- number of measured samples $N$,
- FFT length,
- tone separation,
- strong-tone frequency,
- weak-tone frequency,
- weak-to-strong amplitude ratio,
- coherent vs non-coherent frequency placement.

Possible amplitude-ratio cases may include:

- `0 dB`
- `-20 dB`
- `-40 dB`
- `-60 dB`

These values are not frozen.

The experiment design should determine which cases provide meaningful engineering evidence.

Avoid exhaustive sweeps without a clear question.

---

## 17. Required Quantitative Outputs

At minimum, Ex02 should consider a table containing window metrics such as:

| Window | Coherent Gain | ENBW | Main-Lobe Width | Peak Sidelobe Level | Scalloping Loss |
| --- | ---: | ---: | ---: | ---: | ---: |
| Rectangular | TBD | TBD | TBD | TBD | TBD |
| Hann | TBD | TBD | TBD | TBD | TBD |
| Hamming | TBD | TBD | TBD | TBD | TBD |
| Blackman | TBD | TBD | TBD | TBD | TBD |

Values must come from validated implementation or clearly identified analytical references.

Do not insert remembered constants without validation.

---

## 18. Possible Two-Tone Performance Metrics

Potential two-tone metrics include:

- resolved / unresolved classification,
- detected weak-tone peak,
- peak-location error,
- weak-tone amplitude error,
- minimum resolvable separation,
- minimum detectable weak-to-strong ratio,
- spectral-valley depth.

The exact resolution criterion must be defined before automated evaluation.

Do not use a subjective visual judgment as the only criterion.

---

## 19. Validation Strategy

Ex02 must include explicit validation.

Possible validation sources include:

### Analytical Checks

- coherent gain formulas,
- FFT bin spacing,
- observation duration,
- known window characteristics.

### Library Comparison

Compare generated windows against trusted NumPy or SciPy implementations when appropriate.

### Special Cases

Examples:

- rectangular window should reproduce Ex01 behavior,
- a coherent tone should concentrate energy according to the expected window response,
- zero padding should not alter the original time-domain observation.

### Numerical Consistency

Check:

- dimensions,
- normalization,
- amplitude correction,
- reproducibility,
- expected spectral symmetry where applicable.

### Reference Values

Published or library-documented window characteristics may be used for cross-checking.

Reference values must be cited or identified in the theory document.

---

## 20. Failure and Limitation Analysis

Ex02 must include:

### When Does It Fail?

Important cases include:

### Short Observation Interval

Insufficient observation duration limits discrimination regardless of FFT visualization quality.

### Two Tones Too Close

Two spectral components may remain unresolved because their window-shaped main lobes overlap.

### Weak Tone Hidden by Sidelobes

A weak component may be buried under the leakage structure of a strong component.

### Inappropriate Window Choice

A low-sidelobe window may sacrifice too much close-tone discrimination.

A narrow-main-lobe window may expose excessive sidelobe leakage.

### Misleading Zero Padding

A smooth zero-padded spectrum may visually suggest improved resolution even when the measured record contains no additional resolving information.

### Missing Coherent-Gain Correction

Windowed spectral amplitude may be systematically biased if amplitude correction is ignored.

### Incorrect Normalization

Comparisons between windows may become meaningless if FFT scaling and window normalization are inconsistent.

---

## 21. Engineering Interpretation Standard

Avoid statements such as:

> Hann is better than rectangular.

Prefer engineering conclusions such as:

> The Hann window suppresses sidelobe leakage relative to the rectangular window, which can improve detection of a weak tone near a strong component. The cost is a wider main lobe, which can reduce discrimination between closely spaced spectral components.

Every important result should explain:

- what improved,
- what degraded,
- why,
- under what operating condition the tradeoff matters.

---

## 22. Expected Figures

Candidate figures include:

### Figure 1 — Window Shapes

Time-domain window functions.

### Figure 2 — Window Frequency Responses

Normalized frequency response on a dB scale.

### Figure 3 — Single-Tone Leakage Comparison

Same non-coherent sinusoid under multiple windows.

### Figure 4 — Two Equal Nearby Tones

Resolution comparison across windows.

### Figure 5 — Weak Tone Near Strong Tone

Demonstrate sidelobe masking.

### Figure 6 — Zero Padding

Same observation with multiple FFT lengths.

### Figure 7 — Observation Length

Compare actual increased record duration against zero padding.

### Figure 8 — Resolution Sweep

Quantitative minimum-separation behavior.

The final figure set should be selected based on engineering value rather than quantity.

---

## 23. Expected Numerical Tables

Potential tables include:

### Table A — Window Metrics

- coherent gain,
- ENBW,
- main-lobe width,
- peak sidelobe level,
- scalloping loss.

### Table B — Two-Tone Resolution

Possible columns:

- window,
- $N$,
- tone separation,
- relative amplitude,
- resolved/unresolved result,
- measured error.

### Table C — Zero Padding vs Observation Length

Demonstrate the distinction between:

- denser FFT sampling,
- additional measured information.

---

## 24. Proposed Repository Structure

The initial expected structure is:

```text
python/
└── ex02_windowing_spectral_resolution/
    ├── main.py
    ├── experiments.py
    ├── README.md
    ├── notes.md
    ├── figures/
    ├── results/
    └── tests/
```

Detailed theory:

```text
docs/ex02_windowing_spectral_resolution_theory.md
```

Interview-preparation material may later be added as:

```text
docs/ex02_windowing_spectral_resolution_interview_questions.md
```

The exact implementation structure should be frozen before coding.

Do not create unnecessary files merely because the Engineering Lab Standard allows them.

---

## 25. Implementation Philosophy

Use the progression:

```text
Engineering Question
→ Mathematical Definition
→ Python Reference Implementation
→ Validation
→ Controlled Experiments
→ Quantitative Metrics
→ Failure Analysis
→ Engineering Interpretation
```

Do not optimize prematurely.

Python should act as the numerical golden reference.

Reusable functionality should be modular.

Possible functions include:

```text
generate_tone(...)
generate_two_tone_signal(...)
get_window(...)
compute_spectrum(...)
compute_window_metrics(...)
apply_coherent_gain_correction(...)
measure_main_lobe_width(...)
measure_peak_sidelobe_level(...)
estimate_scalloping_loss(...)
evaluate_two_tone_resolution(...)
```

These names are conceptual only.

The new Ex02 session should design the API before implementation.

---

## 26. Testing Expectations

Potential automated tests include:

- known FFT-bin spacing,
- window-array length,
- coherent-gain calculation,
- zero-padding invariance of measured time-domain data,
- comparison against trusted window implementations,
- deterministic coherent-tone amplitude recovery,
- known special cases for the rectangular window.

Tests should validate meaningful numerical behavior rather than superficial code coverage.

---

## 27. Reproducibility Requirements

Important experiment parameters should be explicit.

Examples:

- $f_s$,
- $N$,
- FFT length,
- window type,
- tone frequencies,
- amplitudes,
- phase,
- zero-padding factor.

If random noise is introduced later:

- use controlled random seeds,
- document SNR definition,
- define Monte Carlo trial count.

The initial Ex02 design does not require noise unless it adds clear engineering value.

---

## 28. Computational Considerations

Ex02 should begin introducing implementation awareness.

Possible topics include:

- cost of window multiplication,
- FFT complexity,
- memory impact of large zero-padded FFTs,
- distinction between increased FFT size and increased acquisition duration,
- suitability of windows for real-time streaming/frame-based DSP,
- precomputation of deterministic window coefficients.

Hardware implementation is not required for Ex02.

However, the theory document may briefly explain that deterministic window coefficients are well suited to precomputation and fixed-coefficient multiplication in real-time systems.

---

## 29. Relationship to Flagship Projects

Ex02 provides foundational knowledge for several later integrated projects.

### PROJECT-01 — Digital Spectrum Analyzer

Direct relevance:

- window selection,
- FFT scaling,
- spectral display,
- frequency resolution.

### PROJECT-02 — Weak Signal Next to a Strong Interferer

Ex02 provides much of the spectral theory required for this flagship project.

### Radar DSP

Windowing later becomes important in:

- range FFT,
- Doppler FFT,
- range-Doppler processing,
- sidelobe control,
- target masking,
- dynamic-range management.

### Array Processing

The same engineering tradeoff between main-lobe width and sidelobe suppression has conceptual parallels in spatial beamforming and array weighting.

These connections should be noted but should not expand Ex02 beyond its spectral-analysis scope.

---

## 30. Git Workflow

Use the established repository workflow.

Start only after PR #16 is merged and `main` is synchronized.

Then:

```text
main
  ↓
focused Ex02 branch
  ↓
design
  ↓
implementation
  ↓
validation
  ↓
documentation
  ↓
diff review
  ↓
staged audit
  ↓
commit
  ↓
push
  ↓
pull request
  ↓
merge
  ↓
prune
  ↓
synchronize main
  ↓
delete local feature branch
```

Do not mix unrelated repository infrastructure changes into Ex02 branches.

---

## 31. PR Strategy for Ex02

Ex02 does not have to be completed in one very large pull request.

Prefer coherent incremental PRs if the work becomes substantial.

A possible sequence is:

### Ex02 PR A — Core Window Analysis

- reference implementation,
- window metrics,
- single-tone comparison,
- validation.

### Ex02 PR B — Two-Tone Resolution

- equal-tone and weak-tone experiments,
- parameter sweeps,
- metrics,
- failure cases.

### Ex02 PR C — Documentation / Deep-Dive Completion

- final theory,
- engineering interpretation,
- tests,
- figures,
- README refinement.

This sequence is not frozen.

The Ex02 working session should determine the cleanest PR decomposition after the experiment architecture is designed.

---

## 32. Handoff Policy During Ex02

Every merged Ex02 PR should receive a PR handoff.

Use:

`docs/handoffs/HANDOFF_TEMPLATE.md`

The central index must also be updated:

`docs/handoffs/HANDOFF_INDEX.md`

When Ex02 reaches completion, create a final continuation record that captures:

- curriculum topics completed,
- final experiment set,
- quantitative findings,
- validation status,
- limitations,
- artifacts,
- next recommended lab.

This ensures the Master Reference workflow remains independent of chat history.

---

## 33. Working-Session Policy

The dedicated Ex02 session should focus only on Ex02.

Repository-wide architecture decisions should remain aligned with the Master Reference documentation.

The session should work step-by-step.

Do not jump directly into code.

Before implementation, freeze:

1. engineering questions,
2. mathematical definitions,
3. experiment matrix,
4. quantitative metrics,
5. validation strategy,
6. file architecture,
7. expected figures,
8. expected tables,
9. completion criteria.

Only then begin implementation.

---

## 34. Minimum Completion Criteria

Ex02 should not be considered complete unless it demonstrates all of the following.

### Theory

- windowing explained mathematically,
- frequency resolution defined carefully,
- zero-padding interpretation explained,
- two-tone resolution discussed.

### Implementation

- reproducible Python implementation,
- modular signal generation,
- multiple windows,
- spectrum computation,
- quantitative window metrics.

### Validation

- at least one analytical or trusted-reference validation for major metrics,
- consistent FFT normalization,
- coherent-gain treatment,
- zero-padding interpretation verified numerically.

### Experiments

- single-tone leakage comparison,
- window-response comparison,
- two-tone resolution experiment,
- weak-tone-near-strong-tone experiment,
- zero-padding experiment,
- observation-length comparison.

### Quantitative Analysis

- window metric table,
- at least one resolution-related quantitative metric,
- documented operating parameters.

### Failure Analysis

- unresolved close tones,
- weak-tone masking,
- inappropriate window tradeoff,
- zero-padding misconception,
- amplitude-bias case.

### Documentation

- exercise README,
- engineering notes,
- detailed theory document,
- reproducible run instructions,
- clear generated artifacts.

### Engineering Interpretation

The lab must answer:

> Which window should be used under which spectral-analysis condition, and what is the engineering cost of that choice?

---

## 35. Scope Boundaries

Ex02 should not expand unnecessarily into:

- full PSD estimation,
- Welch method,
- adaptive spectral estimation,
- CFAR,
- radar range-Doppler processing,
- beamforming,
- FPGA implementation,
- advanced frequency estimators.

These topics belong to later curriculum modules or projects.

Ex02 should build the spectral-windowing foundation required by those later topics.

---

## 36. First Task for the Ex02 Working Session

Do not start coding immediately.

The first task is:

### Design and freeze the complete Ex02 engineering experiment

The dedicated Ex02 session should first produce a design containing:

1. precise engineering questions,
2. mathematical definitions of all window metrics,
3. baseline signal parameters,
4. selected windows,
5. experiment families,
6. parameter-sweep ranges,
7. two-tone resolution criterion,
8. validation references,
9. expected figures,
10. expected numerical tables,
11. failure cases,
12. proposed file architecture,
13. proposed PR decomposition,
14. minimum completion criteria.

Only after this design is reviewed and accepted should implementation begin.

---

## 37. Continuity Instruction for a New Chat

When this handoff is supplied to a new ChatGPT conversation, that conversation should treat:

- this handoff,
- `DSP_MASTER_CURRICULUM.md`,
- `ENGINEERING_LAB_STANDARD.md`,
- the current repository state,

as the governing context for Ex02.

The new conversation should not redesign the overall repository architecture unless a genuine conflict is discovered.

Its immediate responsibility is:

**design, implement, validate, document, and complete Ex02 — Window Functions and Spectral Resolution according to the established Engineering Lab Standard.**

---

## 38. Start Condition

Ex02 implementation may begin when:

- PR #16 has been merged,
- the PR #16 remote branch has been deleted,
- local `main` has been synchronized with `origin/main`,
- the PR #16 local branch has been deleted,
- `git status -sb` shows a clean synchronized `main`,
- a dedicated Ex02 working session or chat has been created.

At that point, create the focused Ex02 development branch from `main`.

---

## 39. Current Status

At creation of this handoff:

- Ex01 is complete.
- Master Curriculum is active.
- Engineering Lab Standard is active.
- Markdown rendering fixes are active.
- repository UTF-8/LF standards are active.
- the formal handoff system is being established through PR #16.
- Ex02 has not yet begun implementation.

The next major technical activity after completion of PR #16 is:

### Ex02 — Window Functions and Spectral Resolution
