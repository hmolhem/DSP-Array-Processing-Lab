# DSP-Array-Processing-Lab

A structured engineering laboratory for developing digital signal processing from first principles through statistical signal processing, array processing, DOA estimation, radar DSP, and implementation-oriented FPGA/HLS concepts.

The goal of this repository is not simply to collect code examples. It is designed to demonstrate a complete engineering progression:

**Theory → Mathematical Modeling → Numerical Implementation → Validation → Engineering Interpretation → System Integration**

---

## Purpose

`DSP-Array-Processing-Lab` is being developed as a long-term technical knowledge base and engineering portfolio.

The repository is intended to:

* build a rigorous foundation in digital signal processing,
* connect mathematical theory to reproducible numerical experiments,
* develop engineering judgment through quantitative validation,
* study algorithm limitations and failure modes,
* progress from single-channel DSP to multi-sensor and array processing,
* connect DSP fundamentals to radar and sensing applications,
* develop selected algorithms toward C++, fixed-point, and FPGA/HLS implementations,
* create technically defensible portfolio artifacts for engineering interviews and professional work.

The long-term technical direction is:

**Signal Foundations → DSP → Statistical DSP → PCA / ICA → Detection & Estimation → Array Processing → DOA → Sparse / MIMO Arrays → Radar DSP → Real-Time / FPGA / HLS**

---

## Repository Architecture

The repository follows a three-layer development model.

### 1. Knowledge Curriculum

A structured technical curriculum defines the complete learning path from elementary signals to advanced radar and array-processing methods.

The detailed curriculum is maintained in:

[docs/DSP_MASTER_CURRICULUM.md](docs/DSP_MASTER_CURRICULUM.md)

### 2. Engineering Labs

Focused experiments convert individual concepts into reproducible engineering evidence.

A significant lab should address questions such as:

* What problem is being solved?
* What mathematical model describes it?
* What assumptions are required?
* How is the method implemented?
* How is correctness validated?
* What metrics quantify performance?
* Under what conditions does the method fail?
* What are the computational and implementation tradeoffs?

The engineering standard for repository labs is defined in:

[docs/ENGINEERING_LAB_STANDARD.md](docs/ENGINEERING_LAB_STANDARD.md)

### 3. Flagship Projects

Integrated projects will combine multiple DSP topics into larger engineering systems such as:

* digital spectrum analysis,
* weak-signal detection,
* PCA/ICA multi-sensor source separation,
* adaptive interference cancellation,
* beamforming,
* DOA estimation,
* sparse and MIMO array processing,
* end-to-end radar signal processing.

---

## Technical Curriculum

The master curriculum is organized into the following technical modules:

1. **Signal Foundations**
2. **Systems, Sampling, and Convolution**
3. **Fourier Analysis, DFT, and FFT**
4. **Z-Transform and Digital Filters**
5. **Random Signals and Statistical DSP**
6. **Matrix DSP, EVD, SVD, PCA, and ICA**
7. **Spectral and Time-Frequency Estimation**
8. **Detection and Estimation**
9. **Adaptive, Multirate, and Complex-Baseband DSP**
10. **Array Processing Fundamentals**
11. **DOA and Subspace Processing**
12. **Sparse Arrays, Coarrays, and MIMO**
13. **Radar Signal Processing**
14. **Tracking and Sensor Estimation**
15. **Real-Time, Numerical, and FPGA/HLS DSP**

The curriculum currently defines topics from `DSP-001` through `DSP-142`.

Curriculum IDs describe the conceptual learning sequence. Repository exercise numbers describe the chronological order in which engineering labs are implemented.

These identifiers are intentionally separate so that the existing repository history remains unchanged.

---

## Documentation Strategy

This repository follows a **Markdown-first** documentation workflow.

Markdown is the canonical format for normal technical development because it is:

* lightweight,
* easy to review with Git,
* directly readable on GitHub,
* suitable for equations, figures, tables, and code,
* easy to migrate later into formal LaTeX documents.

Typical technical artifacts include:

```text
README.md
notes.md
docs/*_theory.md
docs/*_interview_questions.md
```

Selected portfolio milestones may additionally include:

```text
LaTeX technical report
compiled PDF
animation or video
C++ implementation
fixed-point analysis
FPGA/HLS implementation
benchmark results
professional technical content
```

Not every exercise needs to become a full portfolio milestone.

---

## Engineering Philosophy

A plot or a successful script is not considered sufficient evidence that a lab is complete.

Important labs should progressively include:

* explicit mathematical assumptions,
* reproducible experiment parameters,
* analytical or numerical validation,
* quantitative performance metrics,
* parameter sweeps,
* failure-case analysis,
* Monte Carlo evaluation when randomness matters,
* computational complexity,
* numerical considerations,
* real-time and hardware-awareness discussions.

The repository should demonstrate not only that an algorithm works, but also **why it works, when it fails, and what engineering tradeoffs it introduces**.

---

## Implementation Strategy

Python is used as the initial numerical reference environment.

Selected algorithms may later follow the implementation path:

**Mathematical Model → Python Reference → Validated Experiment → Optimized Implementation → C++ → Fixed Point → FPGA/HLS**

Potential hardware-oriented kernels include:

* FIR filtering,
* FFT,
* correlation,
* matched filtering,
* beamforming,
* covariance accumulation,
* selected radar preprocessing kernels.

Python implementations will act as numerical golden references for later implementations.

---

## Completed Engineering Lab

### Exercise 01 — FFT Spectral Leakage

**Curriculum mapping:** `Ex01 → DSP-018`

Exercise 01 demonstrates spectral leakage by comparing coherent and non-coherent sinusoidal sampling.

Experiment configuration:

* sampling rate: 1000 Hz,
* number of samples: 256,
* FFT bin spacing: 3.90625 Hz,
* coherent sinusoid: 125.0 Hz,
* non-coherent sinusoid: 123.5 Hz.

The exercise demonstrates that a finite-duration sinusoid that does not align with the DFT frequency grid spreads energy across neighboring FFT bins.

### Exercise 01 Artifacts

* Python implementation: [python/ex01_fft_spectral_leakage/main.py](python/ex01_fft_spectral_leakage/main.py)
* Animation implementation: [python/ex01_fft_spectral_leakage/animation.py](python/ex01_fft_spectral_leakage/animation.py)
* Exercise README: [python/ex01_fft_spectral_leakage/README.md](python/ex01_fft_spectral_leakage/README.md)
* Engineering notes: [python/ex01_fft_spectral_leakage/notes.md](python/ex01_fft_spectral_leakage/notes.md)
* Line-marker spectrum: [python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png](python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png)
* Stem spectrum: [python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_stem.png](python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_stem.png)
* GIF animation: [python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_animation.gif](python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_animation.gif)
* MP4 animation: [python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_animation.mp4](python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_animation.mp4)
* Theory document: [docs/ex01_fft_spectral_leakage_theory.md](docs/ex01_fft_spectral_leakage_theory.md)
* Interview questions: [docs/ex01_fft_spectral_leakage_interview_questions.md](docs/ex01_fft_spectral_leakage_interview_questions.md)
* LaTeX technical note: [papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.tex](papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.tex)
* Compiled technical note: [papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.pdf](papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.pdf)

Exercise 01 serves as the initial **Portfolio Milestone** and establishes the quality standard for future deep-dive labs.

---

## Planned Integrated Projects

The long-term portfolio will progressively include:

### PROJECT-01 — Digital Spectrum Analyzer

Sampling, FFT, windowing, spectral scaling, and PSD.

### PROJECT-02 — Weak Signal Next to a Strong Interferer

Spectral leakage, dynamic range, window selection, SNR, and frequency resolution.

### PROJECT-03 — PCA/ICA Multi-Sensor Source Separation

Covariance estimation, PCA, whitening, ICA, and quantitative source-recovery evaluation.

### PROJECT-04 — Adaptive Interference Canceller

LMS, NLMS, and RLS comparison.

### PROJECT-05 — Beamforming Laboratory

Bartlett, delay-and-sum, null steering, and MVDR.

### PROJECT-06 — DOA Estimation Laboratory

Conventional beam scan, MUSIC, Root-MUSIC, and ESPRIT with statistical performance evaluation.

### PROJECT-07 — Sparse and MIMO Array Laboratory

Sparse geometry, coarrays, virtual arrays, covariance processing, MUSIC, and robustness analysis.

### PROJECT-08 — End-to-End Radar DSP Chain

Waveform and target modeling through range, Doppler, detection, DOA, and target estimation.

---

## Reproducibility and Software Quality

As the repository grows, development will progressively include:

* controlled random seeds,
* automated numerical checks,
* reusable tests,
* numerical tolerances,
* dependency management,
* focused Git branches,
* reviewable pull requests,
* continuous integration.

The objective is to maintain the repository as engineering software rather than a collection of isolated notebooks.

---

## Current Status

* Repository architecture defined.
* Master DSP curriculum established.
* Engineering Lab Standard established.
* Exercise 01 complete as the initial Portfolio Milestone.
* Future development will proceed from foundational DSP concepts toward integrated radar and array-processing systems.

---

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.
