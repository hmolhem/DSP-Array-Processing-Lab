# DSP-Array-Processing-Lab — Engineering Lab Standard

## 1. Purpose

This document defines the engineering standard for technical labs developed in `DSP-Array-Processing-Lab`.

The objective is not to build a collection of disconnected tutorials or code examples. Each lab should demonstrate a traceable engineering process from theory to validated implementation.

The expected engineering flow is:

$$
\text{Problem}
\rightarrow
\text{Theory}
\rightarrow
\text{Mathematical Model}
\rightarrow
\text{Implementation}
\rightarrow
\text{Validation}
\rightarrow
\text{Engineering Interpretation}
$$

For advanced labs:

$$
\text{Failure Analysis}
\rightarrow
\text{Statistical Evaluation}
\rightarrow
\text{Computational Analysis}
\rightarrow
\text{Real-Time / Hardware Considerations}
$$

---

## 2. Core Engineering Questions

A successful lab should answer more than:

> Does the code run?

It should answer:

1. What engineering problem is being studied?
2. What mathematical model describes the problem?
3. What assumptions are required?
4. Why should the method work?
5. How is the algorithm implemented?
6. How is correctness verified?
7. How is performance quantified?
8. Under what conditions does the method fail?
9. What engineering tradeoffs are involved?
10. Where does the method appear in a real signal-processing system?

---

## 3. Standard Lab Structure

A typical lab may use:

```text
python/
└── exXX_topic_name/
    ├── main.py
    ├── experiments.py
    ├── README.md
    ├── notes.md
    ├── figures/
    ├── results/
    └── tests/
```

Not every lab requires every file or directory.

A simple Foundation Lab may contain:

```text
main.py
README.md
notes.md
figures/
```

A more advanced Deep-Dive Lab may additionally contain:

```text
experiments.py
results/
tests/
```

---

## 4. Documentation Policy

### 4.1 Markdown First

Markdown is the canonical technical documentation format for normal repository development.

Detailed theory should normally be stored as:

```text
docs/exXX_topic_theory.md
```

Important interview-preparation material may be stored as:

```text
docs/exXX_topic_interview_questions.md
```

LaTeX and PDF should be reserved primarily for selected Portfolio Milestones, formal technical reports, or publication-quality documents.

The preferred documentation workflow is:

$$
\text{Markdown}
\rightarrow
\text{Technical Maturity}
\rightarrow
\text{LaTeX}
\rightarrow
\text{PDF}
$$

---

## 5. Exercise README Standard

Each exercise-level `README.md` should provide a concise engineering entry point.

Recommended sections:

* Objective
* Problem Statement
* Key Equations
* Experiment Configuration
* How to Run
* Generated Outputs
* Validation
* Main Findings
* Engineering Interpretation
* Limitations
* Connections to Later Topics

The README should be understandable without reading the source code first.

---

## 6. Engineering Notes

The exercise `notes.md` should preserve practical engineering reasoning that may not belong in the formal theory document.

Examples include:

* numerical observations,
* parameter sensitivity,
* debugging lessons,
* unexpected behavior,
* implementation decisions,
* numerical limitations,
* follow-up experiments,
* ideas for improvement.

The purpose is to preserve the engineering thought process, not merely the final result.

---

## 7. Theory Document Standard

A detailed theory document should normally include:

1. Problem Definition
2. Mathematical Background
3. Governing Equations
4. Assumptions
5. Derivation
6. Algorithm
7. Numerical Considerations
8. Validation Strategy
9. Engineering Interpretation
10. Failure Modes
11. Connections to Radar / Array Processing / Embedded DSP
12. References

Equations should be written using LaTeX-compatible Markdown whenever practical.

Example:

$$
\Delta f = \frac{f_s}{N}
$$

where:

* (f_s) is the sampling frequency,
* (N) is the number of samples,
* (\Delta f) is the FFT bin spacing.

For matrix algorithms, dimensions should be stated when useful.

For example:

$$
\mathbf{X}\in\mathbb{C}^{M\times K}
$$

where:

* (M) is the number of sensor channels,
* (K) is the number of snapshots.

---

## 8. Reference Implementation Standard

The default implementation sequence is:

$$
\text{Theory}
\rightarrow
\text{Clear Python Reference}
\rightarrow
\text{Validation}
\rightarrow
\text{Optimization}
$$

The first implementation should prioritize:

* correctness,
* clarity,
* traceability to the mathematics,
* reproducibility.

Premature optimization should be avoided.

Reusable operations should normally be implemented as functions.

Examples:

```python
generate_signal(...)
compute_fft(...)
estimate_covariance(...)
compute_steering_vector(...)
music_spectrum(...)
```

Important experiment parameters should remain visible and documented.

Examples include:

* sampling rate,
* number of samples,
* SNR,
* number of snapshots,
* number of sensors,
* sensor spacing,
* source angles,
* window type,
* filter order,
* Monte Carlo trial count.

---

## 9. Validation Standard

Every significant lab must contain at least one explicit validation mechanism.

Possible validation methods include:

* analytical reference values,
* known special cases,
* NumPy or SciPy reference comparison,
* dimensional checks,
* conservation relationships,
* Parseval verification,
* reconstruction error,
* numerical tolerances,
* Monte Carlo statistics,
* comparison with theoretical bounds.

A visually convincing plot alone is not sufficient validation.

---

## 10. Quantitative Metrics

Whenever practical, conclusions should be supported by numerical metrics.

### Spectral Analysis

Possible metrics:

* main-lobe width,
* peak sidelobe level,
* ENBW,
* scalloping loss,
* frequency-estimation error.

### Filtering

Possible metrics:

* passband ripple,
* stopband attenuation,
* transition width,
* group delay.

### PCA / ICA

Possible metrics:

* explained variance,
* reconstruction error,
* source correlation,
* separation quality.

### Beamforming / DOA

Possible metrics:

* angular bias,
* angular RMSE,
* resolution probability,
* peak-location error,
* probability of successful source separation.

### Radar

Possible metrics:

* range error,
* Doppler error,
* detection probability,
* false-alarm probability,
* CFAR performance.

---

## 11. Failure-Case Standard

Important Deep-Dive Labs should contain a section such as:

```text
Failure Modes
```

or:

```text
When Does It Fail?
```

A strong engineering portfolio must demonstrate understanding of algorithm limitations.

Examples follow.

### FFT / Spectral Analysis

* insufficient observation time,
* spectral leakage,
* close-tone masking,
* inappropriate window selection.

### PCA

* inappropriate feature scaling,
* outlier sensitivity,
* variance not representing useful information,
* nonlinear structure.

### ICA

* Gaussian source distributions,
* insufficient source independence,
* permutation ambiguity,
* scaling ambiguity.

### MUSIC

* low SNR,
* insufficient snapshots,
* coherent sources,
* incorrect source-count assumption,
* calibration errors,
* mutual coupling,
* steering-vector mismatch.

---

## 12. Parameter Sweeps

Important algorithms should not be evaluated at only one operating point.

Useful sweep parameters include:

* SNR,
* number of samples,
* record duration,
* number of snapshots,
* signal frequency,
* source separation,
* number of array elements,
* window parameters,
* filter order,
* model mismatch.

Parameter sweeps should expose engineering behavior rather than simply create additional figures.

---

## 13. Monte Carlo Validation

When randomness affects algorithm performance, Monte Carlo evaluation should be considered.

For an estimated parameter:

$$
\hat{\theta}_1,
\hat{\theta}_2,
\ldots,
\hat{\theta}_L
$$

over (L) trials, useful metrics include:

* mean error,
* bias,
* variance,
* RMSE,
* percentiles,
* confidence intervals,
* probability of successful estimation.

Random seeds should be controlled when reproducibility is required.

---

## 14. Visualization Standard

Figures should communicate engineering information rather than serve as decoration.

A technical figure should normally contain:

* axis labels,
* physical units,
* meaningful title,
* legend when appropriate,
* readable scales,
* adequate resolution.

Useful visualization types include:

* time-domain waveform,
* stem spectrum,
* magnitude spectrum,
* PSD,
* histogram,
* CDF,
* parameter-sweep curve,
* heatmap,
* beam pattern,
* MUSIC pseudospectrum,
* range-Doppler map.

---

## 15. Engineering Interpretation

Every significant experiment should explain what the numerical result means.

Avoid conclusions such as:

> The algorithm worked.

Prefer conclusions such as:

> The Hann window reduces sidelobe leakage relative to the rectangular window, improving weak-tone visibility near a strong spectral component at the cost of a wider main lobe and reduced frequency discrimination.

The purpose is to develop engineering judgment rather than merely generate numerical output.

---

## 16. Computational Considerations

Advanced labs should progressively analyze:

* algorithmic complexity,
* memory requirements,
* latency,
* throughput,
* vectorization,
* parallelism,
* numerical conditioning.

Examples include comparing:

$$
O(N^2)
$$

with:

$$
O(N\log N).
$$

For matrix algorithms, complexity should be related to relevant dimensions.

For example, covariance estimation:

$$
\hat{\mathbf R}
=

\frac{1}{K}
\mathbf X\mathbf X^H
$$

should be interpreted in terms of:

* (M): number of sensors,
* (K): number of snapshots.

---

## 17. Real-Time and FPGA/HLS Considerations

For selected algorithms, include a hardware-awareness section.

Useful questions include:

* Can the algorithm operate on streaming samples?
* Does it require frame buffering?
* Which operations can be parallelized?
* Does the method require matrix inversion?
* Does it require eigendecomposition or SVD?
* What numerical precision is necessary?
* Is fixed-point implementation practical?
* What throughput is required?
* What latency is acceptable?
* Which stages naturally map to FPGA?
* Which stages are better suited to CPU or software?

---

## 18. Implementation Progression

Selected algorithms may follow the progression:

$$
\text{Python}
\rightarrow
\text{Optimized Python}
\rightarrow
\text{C++}
\rightarrow
\text{Fixed Point}
\rightarrow
\text{HLS / FPGA}
$$

The Python implementation acts as the numerical reference or golden model.

Priority hardware-oriented kernels may include:

* FIR filtering,
* FFT,
* correlation,
* matched filtering,
* beamforming,
* covariance accumulation,
* selected radar preprocessing kernels.

Not every algorithm needs to traverse the complete implementation chain.

---

## 19. Testing Standard

As the repository grows, reusable numerical functions should progressively receive automated tests.

Useful tests include:

* deterministic reference cases,
* shape and dimension checks,
* numerical tolerance tests,
* expected symmetry,
* energy conservation,
* reconstruction accuracy,
* known-frequency recovery,
* known-angle DOA recovery.

Testing should focus on meaningful algorithmic behavior rather than superficial code coverage.

---

## 20. Reproducibility Standard

A reproducible experiment should document:

* dependencies,
* execution command,
* important parameters,
* random seeds when applicable,
* generated artifacts,
* validation criteria,
* expected outputs.

Generated results should be reproducible from repository code whenever practical.

---

## 21. Git Workflow Standard

Engineering changes should normally be developed through focused branches and pull requests.

Preferred workflow:

```text
main
  ↓
focused feature branch
  ↓
implementation
  ↓
validation
  ↓
documentation
  ↓
staged review
  ↓
pull request
  ↓
mergee
```

Before commit:

```powershell
git status
git diff
git diff --check
```

After staging:

```powershell
git diff --cached --stat
git diff --cached --check
git diff --cached --name-status
```

Pull requests should remain focused on coherent technical changes.

---

## 22. Lab Depth Classification

### Foundation Lab

Expected artifacts:

* mathematical explanation,
* Python implementation,
* explicit validation,
* figures,
* README,
* notes.

### Deep-Dive Lab

Adds as appropriate:

* detailed theory document,
* parameter sweeps,
* quantitative metrics,
* failure analysis,
* computational considerations,
* Monte Carlo evaluation,
* interview questions.

### Portfolio Milestone

May additionally include:

* formal LaTeX report,
* compiled PDF,
* animation or video,
* C++ implementation,
* fixed-point analysis,
* HLS implementation,
* performance benchmarks,
* professional technical communication.

Not every exercise should become a Portfolio Milestone.

---

## 23. Portfolio Quality Gate

Before a Deep-Dive Lab is considered complete, evaluate:

* Is the problem clearly defined?
* Is the mathematics correct?
* Are assumptions documented?
* Is the implementation reproducible?
* Is there explicit validation?
* Are conclusions quantitative where possible?
* Are important failure modes discussed?
* Are engineering tradeoffs identified?
* Are the figures technically useful?
* Is the code understandable?
* Is the connection to real systems explained?
* Are computational implications discussed when relevant?

If several of these questions cannot be answered, the lab should not yet be considered complete.

---

## 24. Long-Term Objective

The repository should demonstrate progression from mathematical signal-processing fundamentals to integrated sensing systems.

The intended evidence chain is:

$$
\text{Mathematical Understanding}
\rightarrow
\text{Numerical Implementation}
\rightarrow
\text{Validation}
\rightarrow
\text{Engineering Judgment}
\rightarrow
\text{System Integration}
\rightarrow
\text{Real-Time Implementation Awareness}
$$

The quality of `DSP-Array-Processing-Lab` should be measured by technical depth, reproducibility, quantitative validation, and engineering reasoning rather than by the number of exercises.
