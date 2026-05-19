# DSP-Array-Processing-Lab

A practical DSP and array-processing portfolio lab focused on signal-processing fundamentals, array-processing algorithms, reproducible Python/C++ experiments, and FPGA/HLS-ready implementation concepts.

## Purpose

This repository is being developed as a multi-purpose engineering portfolio:

- practice and reinforce core digital signal processing concepts,
- build small, reproducible DSP and array-processing projects,
- connect theory to implementation, visualization, and validation,
- create GitHub-ready technical artifacts for resume development,
- generate professional technical content for LinkedIn posts.

Long-term direction:

DSP foundations -> array processing -> DOA estimation -> sparse/coarray methods -> FPGA/HLS-ready kernels

## Repository Strategy

Each exercise or project should be small, focused, and reviewable. The goal is not only to write code, but also to document the engineering reasoning behind each result.

A typical project may include:

- a short problem statement,
- clean Python or C++ implementation,
- figures or numerical results,
- validation notes,
- reproducibility instructions,
- engineering interpretation,
- optional LinkedIn post draft.

## Initial Roadmap

Planned project sequence:

1. FFT spectral leakage
2. Windowing and frequency resolution
3. FIR and IIR filtering basics
4. Sampling, aliasing, and reconstruction
5. Noise modeling and SNR analysis
6. Sample covariance matrix estimation
7. Beamforming fundamentals
8. MUSIC DOA estimation
9. Sparse-array and coarray processing
10. Mutual-coupling effects in array processing
11. Lag-domain regularization concepts
12. FPGA/HLS mapping of selected DSP kernels

## Completed Exercises

### Exercise 01: FFT Spectral Leakage

Exercise 01 demonstrates FFT spectral leakage using coherent and non-coherent sinusoidal sampling.

It compares:

- a coherent sinusoid at 125.0 Hz,
- a non-coherent sinusoid at 123.5 Hz,
- a sampling rate of 1000 Hz,
- a record length of 256 samples,
- an FFT bin spacing of 3.90625 Hz.

Artifacts:

- Python implementation: [python/ex01_fft_spectral_leakage/main.py](python/ex01_fft_spectral_leakage/main.py)
- Exercise README: [python/ex01_fft_spectral_leakage/README.md](python/ex01_fft_spectral_leakage/README.md)
- Exercise notes: [python/ex01_fft_spectral_leakage/notes.md](python/ex01_fft_spectral_leakage/notes.md)
- Generated figure: [python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png](python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png)
- Theory notes: [docs/ex01_fft_spectral_leakage_theory.md](docs/ex01_fft_spectral_leakage_theory.md)
- Interview questions: [docs/ex01_fft_spectral_leakage_interview_questions.md](docs/ex01_fft_spectral_leakage_interview_questions.md)
- LaTeX technical note: [papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.tex](papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.tex)
- Compiled PDF note: [papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.pdf](papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.pdf)

Key engineering idea:

Spectral leakage occurs when a finite sampled signal does not align with the FFT frequency grid, causing its energy to spread across neighboring frequency bins.

## Technical Focus Areas

This lab is intended to gradually connect the following areas:

- Digital Signal Processing
- Python-based numerical experimentation
- C++ implementation readiness
- Array signal processing
- Beamforming and DOA estimation
- MUSIC and covariance-based methods
- Sparse arrays and coarray concepts
- FPGA/HLS-oriented algorithm decomposition
- Reproducible engineering workflows

## Current Status

Exercise 01 is complete and includes implementation, generated figure, theory notes, interview questions, and a LaTeX technical note with a compiled PDF.

The next planned technical exercise is Exercise 02: Windowing and Frequency Resolution.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.
