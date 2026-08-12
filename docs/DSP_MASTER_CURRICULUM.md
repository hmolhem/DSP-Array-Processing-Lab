# DSP-Array-Processing-Lab — Master Curriculum

## 1. Purpose

`DSP-Array-Processing-Lab` is a structured engineering laboratory for developing signal-processing knowledge from first principles through advanced statistical signal processing, array processing, radar DSP, and implementation-oriented FPGA/HLS concepts.

The repository is intended to serve simultaneously as:

- a long-term DSP knowledge base,
- a reproducible engineering laboratory,
- a professional technical portfolio,
- an interview-preparation resource,
- a bridge from mathematical theory to numerical implementation,
- a bridge from Python reference models to real-time and hardware-oriented implementations.

The long-term technical direction is:

$$
\text{Signal Foundations}
\rightarrow
\text{DSP}
\rightarrow
\text{Statistical DSP}
\rightarrow
\text{Array Processing}
\rightarrow
\text{DOA}
\rightarrow
\text{MIMO / Sparse Arrays}
\rightarrow
\text{Radar DSP}
\rightarrow
\text{Real-Time / FPGA / HLS}
$$

---

## 2. Portfolio Architecture

The repository follows a three-layer architecture.

### Layer 1 — Knowledge Curriculum

A structured curriculum covering the complete theoretical path from basic signals to advanced radar and array-processing methods.

### Layer 2 — Engineering Labs

Focused numerical experiments that convert theory into reproducible engineering evidence.

A lab should answer:

1. What problem is being solved?
2. What is the mathematical model?
3. Why does the method work?
4. How is it implemented?
5. How is correctness validated?
6. Under what conditions does it fail?
7. What are the engineering tradeoffs?
8. Where does the concept appear in radar, array processing, communications, sensing, or embedded DSP?

### Layer 3 — Flagship Projects

Integrated projects combining multiple topics into end-to-end engineering systems.

---

## 3. Documentation Policy

### Markdown First

Markdown is the canonical technical documentation format for normal repository development.

Typical artifacts include:

- `README.md`
- `notes.md`
- `docs/*_theory.md`
- `docs/*_interview_questions.md`

LaTeX and PDF are reserved primarily for selected portfolio milestones, formal technical reports, or publication-quality documents.

The preferred workflow is:

$$
\text{Markdown}
\rightarrow
\text{Technical Maturity}
\rightarrow
\text{LaTeX}
\rightarrow
\text{PDF}
$$

This minimizes duplicated documentation and keeps technical material easy to review through Git and GitHub.

---

## 4. Curriculum IDs vs Repository Exercise IDs

Curriculum IDs describe the conceptual learning sequence.

Repository exercise IDs describe the chronological order in which engineering labs are implemented.

These are intentionally separate.

Example:

| Repository Exercise | Curriculum Topic | Topic |
|---|---|---|
| Ex01 | DSP-018 | FFT Spectral Leakage |

Therefore, the existing Exercise 01 remains unchanged.

Future mappings will be recorded as labs are implemented.

---

# 5. Master Knowledge Curriculum

## Module 1 — Signal Foundations

### DSP-001 — Continuous-Time and Discrete-Time Signals

- continuous vs discrete signals
- deterministic vs random signals
- periodic vs aperiodic signals
- real vs complex signals
- sample index and sampling interval

### DSP-002 — Sinusoids and Complex Exponentials

- amplitude
- phase
- frequency
- angular frequency
- Euler identity
- phasor representation
- negative frequencies

### DSP-003 — Discrete-Time Frequency

- normalized frequency
- radians/sample
- frequency periodicity
- discrete-time sinusoidal equivalence

### DSP-004 — Signal Energy, Power, RMS, and Decibels

- energy signals
- power signals
- RMS
- amplitude ratios
- power ratios
- dB and dBm

### DSP-005 — Basic Signal Operations

- delay
- advance
- reversal
- scaling
- addition
- multiplication
- modulation
- conjugation

### DSP-006 — Elementary DSP Signals

- impulse
- step
- ramp
- exponential
- sinusoid
- rectangular pulse
- sinc

---

## Module 2 — Systems, Sampling, and Convolution

### DSP-007 — LTI Systems

- linearity
- time invariance
- causality
- stability
- memory
- impulse response

### DSP-008 — Convolution

- convolution sum
- graphical interpretation
- numerical implementation
- filtering interpretation

### DSP-009 — Correlation

- autocorrelation
- cross-correlation
- lag
- similarity
- time-delay estimation

### DSP-010 — Sampling Theorem

- Nyquist rate
- Nyquist frequency
- band-limited signals
- reconstruction

### DSP-011 — Aliasing

- frequency folding
- undersampling
- alias-equivalent frequencies
- visualization

### DSP-012 — Quantization and ADC Fundamentals

- bit depth
- quantization step
- quantization noise
- ADC dynamic range
- quantization SNR

---

## Module 3 — Fourier Analysis, DFT, and FFT

### DSP-013 — Fourier Series Intuition

- harmonic decomposition
- amplitude spectrum
- phase spectrum

### DSP-014 — Discrete-Time Fourier Transform

- DTFT definition
- frequency-domain representation
- periodicity in frequency

### DSP-015 — DFT from First Principles

- DFT equation
- DFT basis
- matrix representation
- orthogonality

### DSP-016 — FFT Algorithms and Complexity

- DFT complexity
- FFT complexity
- radix-2 concepts
- butterfly structure

### DSP-017 — FFT Bins and Bin Spacing

- frequency grid
- bin index
- bin spacing
- record duration

### DSP-018 — FFT Spectral Leakage

- coherent sampling
- non-coherent sampling
- implicit rectangular window
- leakage
- off-grid DFT basis mismatch
- Dirichlet-kernel interpretation

**Repository mapping:** `Ex01 — FFT Spectral Leakage`

### DSP-019 — Window Functions

- rectangular
- Hann
- Hamming
- Blackman
- Kaiser
- main-lobe width
- sidelobe level
- coherent gain
- ENBW
- scalloping loss

### DSP-020 — Frequency Resolution

- FFT bin spacing
- observation time
- physical resolution
- window-dependent resolution

### DSP-021 — Zero Padding

- FFT interpolation
- spectral visualization
- distinction between interpolation and physical resolution

### DSP-022 — Two-Tone Spectral Resolution

- closely spaced tones
- strong and weak signals
- leakage masking
- window tradeoffs

### DSP-023 — FFT Scaling, Parseval, and Spectral Power

- FFT normalization
- single-sided spectra
- power spectra
- Parseval relation

---

## Module 4 — Z-Transform and Digital Filters

### DSP-024 — Difference Equations

### DSP-025 — Z-Transform

### DSP-026 — Transfer Functions and Frequency Response

### DSP-027 — FIR Filters

### DSP-028 — FIR Filter Design

### DSP-029 — IIR Filters

### DSP-030 — Butterworth, Chebyshev, and Elliptic Filters

### DSP-031 — FIR vs IIR Engineering Tradeoffs

### DSP-032 — Fast Convolution

- overlap-add
- overlap-save
- FFT convolution

---

## Module 5 — Random Signals and Statistical DSP

### DSP-033 — Probability Foundations for DSP

### DSP-034 — Random Variables and Noise Distributions

- Gaussian
- uniform
- Rayleigh
- exponential
- complex Gaussian

### DSP-035 — Random Processes

- ensemble
- realization
- stationarity
- WSS
- ergodicity

### DSP-036 — Mean, Variance, and Autocorrelation

### DSP-037 — Cross-Correlation and Cross-Covariance

### DSP-038 — White and Colored Noise

### DSP-039 — Signal-to-Noise Ratio

### DSP-040 — Monte Carlo Methods

- repeated trials
- random seeds
- empirical distributions
- confidence intervals
- reproducibility

---

## Module 6 — Matrix DSP, EVD, SVD, PCA, and ICA

### DSP-041 — Vector and Matrix Representation of Signals

- inner products
- norms
- orthogonality
- projections

### DSP-042 — Covariance Matrix

- population covariance
- sample covariance
- complex covariance
- snapshot matrices

### DSP-043 — Eigenvalues and Eigenvectors

### DSP-044 — Eigendecomposition

### DSP-045 — Singular Value Decomposition

### DSP-046 — PCA from First Principles

- centering
- covariance
- eigendecomposition
- principal directions
- explained variance

### DSP-047 — PCA via SVD

- covariance EVD vs direct SVD
- numerical considerations

### DSP-048 — PCA Denoising and Dimensionality Reduction

- component selection
- reconstruction
- reconstruction error
- low-rank approximation

### DSP-049 — Whitening

- covariance normalization
- PCA whitening
- preprocessing for ICA

### DSP-050 — ICA and Blind Source Separation

- linear mixing model
- statistical independence
- non-Gaussianity
- unmixing

### DSP-051 — PCA vs ICA

- decorrelation vs independence
- second-order vs higher-order statistical structure

### DSP-052 — Multi-Sensor Source Separation

- source generation
- mixing
- noise
- PCA
- whitening
- ICA
- source recovery metrics

---

## Module 7 — Spectral and Time-Frequency Estimation

### DSP-053 — Periodogram

### DSP-054 — Bartlett Spectral Estimation

### DSP-055 — Welch PSD

### DSP-056 — PSD Bias-Variance Tradeoff

### DSP-057 — Autoregressive Spectral Estimation

### DSP-058 — Short-Time Fourier Transform

### DSP-059 — Spectrogram

### DSP-060 — Wavelet Introduction

---

## Module 8 — Detection and Estimation

### DSP-061 — Matched Filtering

### DSP-062 — Detection in Noise

### DSP-063 — Detection Thresholds, Probability of Detection, and False Alarm

### DSP-064 — ROC Curves

### DSP-065 — Parameter Estimation Basics

- amplitude
- frequency
- phase
- delay

### DSP-066 — Maximum Likelihood Estimation

### DSP-067 — MAP and MMSE Estimation

### DSP-068 — Cramér-Rao Lower Bound

---

## Module 9 — Adaptive, Multirate, and Complex-Baseband DSP

### DSP-069 — LMS Adaptive Filtering

### DSP-070 — NLMS

### DSP-071 — RLS

### DSP-072 — Adaptive Noise and Interference Cancellation

### DSP-073 — Decimation and Interpolation

### DSP-074 — Polyphase Filtering

### DSP-075 — Hilbert Transform and Analytic Signals

### DSP-076 — I/Q Signals and Complex Baseband

### DSP-077 — Digital Mixing, DDC, and DUC

---

## Module 10 — Array Processing Fundamentals

### DSP-078 — Sensor Array Signal Model

### DSP-079 — Uniform Linear Array Geometry

### DSP-080 — Steering Vectors

### DSP-081 — Array Factor

### DSP-082 — Spatial Sampling and Grating Lobes

### DSP-083 — Aperture, Beamwidth, and Angular Resolution

### DSP-084 — Conventional / Bartlett Beamforming

### DSP-085 — Delay-and-Sum Beamforming

### DSP-086 — Null Steering

### DSP-087 — MVDR / Capon Beamforming

---

## Module 11 — DOA and Subspace Processing

### DSP-088 — Signal and Noise Subspaces

### DSP-089 — MUSIC DOA

### DSP-090 — MUSIC Resolution vs SNR and Snapshots

### DSP-091 — Number-of-Sources Estimation

- eigenvalue gap
- AIC
- MDL

### DSP-092 — Coherent Sources

### DSP-093 — Spatial Smoothing

### DSP-094 — Root-MUSIC

### DSP-095 — ESPRIT

### DSP-096 — DOA Cramér-Rao Bounds

### DSP-097 — Array Calibration Errors

### DSP-098 — Mutual Coupling Effects

---

## Module 12 — Sparse Arrays, Coarrays, and MIMO

### DSP-099 — Nonuniform Arrays

### DSP-100 — Sparse Array Fundamentals

### DSP-101 — Minimum Redundancy Arrays

### DSP-102 — Nested Arrays

### DSP-103 — Coprime Arrays

### DSP-104 — Difference Coarrays

### DSP-105 — Virtual ULAs

### DSP-106 — Covariance Vectorization and Kronecker Structure

### DSP-107 — Coarray MUSIC

### DSP-108 — Lag-Domain Weighting and Regularization

### DSP-109 — MIMO Radar Virtual Arrays

---

## Module 13 — Radar Signal Processing

### DSP-110 — Radar Signal Models

### DSP-111 — Pulsed Radar and Range

### DSP-112 — LFM / Chirp Signals

### DSP-113 — Pulse Compression

### DSP-114 — FMCW Radar Fundamentals

### DSP-115 — Range FFT

### DSP-116 — Doppler Processing

### DSP-117 — Range-Doppler Maps

### DSP-118 — Windowing in Radar Processing

### DSP-119 — CFAR Detection

### DSP-120 — Angle FFT and Beamforming

### DSP-121 — Range-Angle Processing

### DSP-122 — Range-Doppler-Angle Processing

### DSP-123 — Radar with MUSIC DOA

### DSP-124 — MIMO Radar Processing Chain

---

## Module 14 — Tracking and Sensor Estimation

### DSP-125 — State-Space Models

### DSP-126 — Kalman Filtering

### DSP-127 — Alpha-Beta Tracking

### DSP-128 — Multi-Target Tracking Concepts

- gating
- data association
- track initiation
- track termination

---

## Module 15 — Real-Time, Numerical, and FPGA/HLS DSP

### DSP-129 — Algorithmic Complexity

- operation counts
- memory
- latency
- scalability

### DSP-130 — Numerical Precision and Conditioning

### DSP-131 — Fixed-Point Arithmetic

### DSP-132 — Fixed-Point FIR

### DSP-133 — Fixed-Point FFT

### DSP-134 — Streaming DSP Architectures

### DSP-135 — Python-to-C++ DSP Kernels

### DSP-136 — SIMD and Vectorized DSP

### DSP-137 — FPGA/HLS FIR

### DSP-138 — FPGA/HLS FFT

### DSP-139 — FPGA/HLS Beamforming

### DSP-140 — FPGA/HLS Covariance Kernels

### DSP-141 — Hardware/Software Partitioning

### DSP-142 — Cross-Implementation Verification

- Python reference
- C++ implementation
- HLS implementation
- numerical tolerances
- golden-reference validation

---

# 6. Integrated Engineering Projects

## PROJECT-01 — Digital Spectrum Analyzer

Integrates:

- sampling
- FFT
- windowing
- dB scaling
- PSD

## PROJECT-02 — Weak Signal Next to a Strong Interferer

Studies:

- spectral leakage
- dynamic range
- windowing
- SNR
- frequency resolution

## PROJECT-03 — PCA/ICA Multi-Sensor Source Separation

Pipeline:

$$
\text{Sources}
\rightarrow
\text{Mixing}
\rightarrow
\text{Noise}
\rightarrow
\text{Covariance}
\rightarrow
\text{PCA}
\rightarrow
\text{Whitening}
\rightarrow
\text{ICA}
\rightarrow
\text{Recovered Sources}
$$

## PROJECT-04 — Adaptive Interference Canceller

Compares:

- LMS
- NLMS
- RLS

## PROJECT-05 — Beamforming Laboratory

Compares:

- Bartlett
- delay-and-sum
- null steering
- MVDR

## PROJECT-06 — DOA Estimation Laboratory

Compares:

- conventional beam scan
- MUSIC
- Root-MUSIC
- ESPRIT

Performance dimensions:

- SNR
- snapshots
- source separation
- number of elements
- calibration errors

## PROJECT-07 — Sparse and MIMO Array Laboratory

Integrates:

- sparse geometry
- coarrays
- virtual arrays
- covariance processing
- MUSIC
- robustness analysis

## PROJECT-08 — End-to-End Radar DSP Chain

Target architecture:

$$
\text{Waveform}
\rightarrow
\text{Target / Channel Model}
\rightarrow
\text{ADC Samples}
\rightarrow
\text{Range Processing}
\rightarrow
\text{Doppler Processing}
\rightarrow
\text{Detection}
\rightarrow
\text{Array Processing / DOA}
\rightarrow
\text{Target Estimates}
\rightarrow
\text{Tracking}
$$

This project is intended to become a flagship repository demonstration.

---

# 7. Engineering Lab Depth Levels

## Foundation Lab

Expected artifacts:

- mathematical explanation
- Python implementation
- one or more validation checks
- figures
- README
- engineering notes

## Deep-Dive Lab

Adds:

- detailed theory document
- parameter sweeps
- quantitative metrics
- failure-case studies
- Monte Carlo analysis when appropriate
- interview questions
- computational considerations

## Portfolio Milestone

Adds selected professional artifacts:

- formal technical report
- LaTeX/PDF
- animation or video where technically useful
- C++ or HLS implementation where appropriate
- benchmark results
- professional technical communication material

Not every lab should become a Portfolio Milestone.

---

# 8. Required Engineering Questions

Each significant lab should address the following questions when applicable:

1. What is the physical or mathematical problem?
2. What assumptions are being made?
3. What are the governing equations?
4. What is the reference implementation?
5. What constitutes correct behavior?
6. What metrics quantify performance?
7. What are the failure modes?
8. How sensitive is the method to noise or model mismatch?
9. What is the computational complexity?
10. What are the memory and latency considerations?
11. Can the algorithm be parallelized?
12. Is the algorithm suitable for real-time implementation?
13. Which parts map naturally to FPGA/HLS?
14. Where does the method appear in radar, sensing, communications, or array processing?

---

# 9. Reproducibility Standard

Engineering results should progressively include:

- controlled random seeds,
- documented parameters,
- automated numerical checks,
- unit tests where useful,
- reproducible figures,
- numerical tolerances,
- clean dependency management,
- Git-based change history,
- focused pull requests.

As the repository matures, CI should be introduced to automate basic validation.

---

# 10. Implementation Strategy

The default implementation path is:

$$
\text{Mathematical Model}
\rightarrow
\text{Python Reference}
\rightarrow
\text{Validated Experiment}
\rightarrow
\text{Optimized Numerical Implementation}
\rightarrow
\text{C++ Kernel}
\rightarrow
\text{Fixed Point}
\rightarrow
\text{FPGA/HLS}
$$

Not every algorithm will traverse the entire chain.

Priority hardware-oriented kernels include:

- FIR filtering
- FFT
- correlation
- matched filtering
- beamforming
- covariance accumulation
- selected radar preprocessing kernels

---

# 11. Chat Naming Convention

A dedicated discussion should be created for major curriculum topics.

Recommended format:

`DSP-XXX | Topic Name`

Examples:

- `DSP-001 | Continuous-Time and Discrete-Time Signals`
- `DSP-019 | Window Functions`
- `DSP-042 | Covariance Matrix`
- `DSP-046 | PCA from First Principles`
- `DSP-050 | ICA and Blind Source Separation`
- `DSP-089 | MUSIC DOA`
- `DSP-119 | CFAR Detection`

Integrated projects use:

`PROJECT-XX | Project Name`

This master curriculum remains the reference for curriculum structure and sequencing.

---

# 12. Current Repository Status

Completed:

### Repository Ex01 — FFT Spectral Leakage

Curriculum mapping:

`Ex01 -> DSP-018`

Current artifacts include:

- Python reference implementation
- line-marker FFT figure
- stem FFT figure
- GIF animation
- MP4 animation
- exercise README
- engineering notes
- detailed Markdown theory document
- interview questions
- LaTeX technical note
- compiled PDF
- LinkedIn carousel storyboard
- LinkedIn post draft

Exercise 01 serves as the initial portfolio-quality reference implementation.

---

# 13. Immediate Development Plan

The next repository actions are:

1. Establish this Master Curriculum.
2. Establish the Engineering Lab Standard.
3. Update the root README to reference these architecture documents.
4. Begin foundational curriculum work without modifying the historical Ex01 numbering.
5. Gradually build Engineering Labs and Flagship Projects.
6. Introduce automated testing and CI as the code base grows.
7. Introduce C++ and FPGA/HLS selectively for computationally important DSP kernels.

The repository should grow in depth, validation quality, and system-level integration rather than simply accumulating disconnected examples.
