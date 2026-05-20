# LinkedIn Carousel Draft: FFT Spectral Leakage

Author: Hossein Molhem
Project: DSP-Array-Processing-Lab
Exercise: 01 - FFT Spectral Leakage
Content Type: LinkedIn educational carousel
Status: Draft storyboard

## Purpose

This document provides a slide-by-slide LinkedIn carousel draft for Exercise 01: FFT Spectral Leakage.

The goal is to convert the GitHub implementation, theory notes, interview questions, and LaTeX technical note into a professional LinkedIn educational post.

This carousel is intended for an audience interested in:

- Digital Signal Processing
- FFT and spectrum analysis
- Engineering simulation
- Radar and communications signal processing
- Array processing and DOA estimation
- Technical interview preparation

## Recommended Carousel Format

Recommended design target:

- Format: portrait carousel
- Aspect ratio: 4:5
- Working canvas: 1080 x 1350 px
- Slides: 10
- Style: clean engineering layout
- Visual language: dark text on light background, clear equations, minimal clutter

Design notes:

- Use one key idea per slide.
- Keep equations large and readable.
- Use the generated FFT figure from the repository on the result slide.
- Use consistent slide numbering.
- Keep technical claims conservative and precise.
- End with a GitHub call-to-action.

Source figure:

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png

Related technical note:

papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.pdf

## Carousel Title

FFT Spectral Leakage: Why One Sine Wave Becomes Many FFT Bins

## Slide 1: Hook

Title:

Why does one sine wave spread across many FFT bins?

Body:

A pure sinusoid should look like one clean frequency.

But in the FFT, it often spreads energy into nearby bins.

That effect is called spectral leakage.

Footer:

DSP-Array-Processing-Lab | Exercise 01

Visual Direction:

Use a simple split visual:

- left: clean sine wave
- right: FFT spectrum with spread energy

Keep this slide minimal and attention-grabbing.

## Slide 2: The Setup

Title:

The experiment

Body:

I compared two sinusoidal signals:

- Coherent sinusoid: 125.0 Hz
- Non-coherent sinusoid: 123.5 Hz
- Sampling rate: 1000 Hz
- Number of samples: 256
- FFT bin spacing: 3.90625 Hz

Footer:

Same sampling rate. Same record length. Different FFT behavior.

Visual Direction:

Use a small parameter table.

Highlight 125.0 Hz and 123.5 Hz in separate rows.

## Slide 3: FFT Bin Spacing

Title:

The FFT sees a frequency grid

Body:

The FFT does not evaluate every possible frequency.

It evaluates a discrete frequency grid.

Formula:

$$\Delta f = \frac{f_s}{N} = \frac{1000}{256} = 3.90625 \text{ Hz}$$

$$f_k = k \cdot \Delta f$$

Interpretation:

- $\Delta f$ is the FFT bin spacing.
- $f_k$ is the physical frequency of bin $k$.
- A sinusoid is coherent only when its frequency lands exactly on this grid.

Footer:

Frequency resolution depends on sampling rate and record length.

Visual Direction:

Show a horizontal frequency axis with equally spaced bins.

Label a few bins:

0 Hz, 3.90625 Hz, 7.8125 Hz, ..., 125 Hz

Keep the equations large and readable.

## Slide 4: Coherent Sampling

Title:

Case 1: coherent sampling

Body:

The 125.0 Hz sinusoid lands exactly on an FFT bin.

Calculation:

125.0 / 3.90625 = 32

So the signal aligns with bin 32.

Result:

Energy is concentrated near one FFT bin.

Footer:

Coherent sampling means the signal fits the FFT grid.

Visual Direction:

Show one strong peak at bin 32.

Use a clean vertical arrow at 125 Hz.

## Slide 5: Non-Coherent Sampling

Title:

Case 2: non-coherent sampling

Body:

The 123.5 Hz sinusoid does not land exactly on an FFT bin.

Calculation:

123.5 / 3.90625 = 31.616

This frequency lies between bins.

Result:

Energy spreads across neighboring bins.

Footer:

Off-grid frequency creates spectral leakage.

Visual Direction:

Show the frequency located between bin 31 and bin 32.

Use a spread spectrum illustration.

## Slide 6: What Is Spectral Leakage?

Title:

Spectral leakage

Body:

Spectral leakage occurs when a finite sampled signal does not align with the FFT frequency grid.

Instead of one compact peak, energy appears in multiple neighboring bins.

This is not a coding error.

It is a finite-window and frequency-grid mismatch effect.

Footer:

Leakage is a measurement and representation issue.

Visual Direction:

Use a simple before/after:

- ideal: one peak
- practical FFT: main lobe plus sidelobes

## Slide 7: Matrix View

Title:

Matrix interpretation

Body:

The DFT can be written in vector-matrix form:

$$\mathbf{X} = \mathbf{F}_N \mathbf{x}$$

Expanded form for the slide:

$$
\begin{bmatrix} X[0] \\ X[1] \\ \vdots \\ X[N-1] \end{bmatrix}
=
\begin{bmatrix}
1 & 1 & \dots & 1 \\
1 & W_N^1 & \dots & W_N^{N-1} \\
\vdots & \vdots & \ddots & \vdots \\
1 & W_N^{N-1} & \dots & W_N^{(N-1)(N-1)}
\end{bmatrix}
\begin{bmatrix} x[0] \\ x[1] \\ \vdots \\ x[N-1] \end{bmatrix}
$$

Where:

- $\mathbf{x}$ is the sampled signal vector.
- $\mathbf{F}_N$ is the DFT matrix.
- $\mathbf{X}$ is the frequency-domain coefficient vector.
- $W_N = e^{-j2\pi/N}$.

Interpretation:

The DFT projects the sampled signal vector onto a finite set of orthogonal frequency-basis vectors.

If the input sinusoid is exactly on-grid, most of the energy appears in one DFT bin.

If the sinusoid is off-grid, its projection is nonzero across multiple DFT basis vectors. This is spectral leakage.

Footer:

Leakage is off-grid DFT-basis mismatch.

Visual Direction:

Use a clean block diagram:

sampled vector x -> DFT matrix F_N -> spectrum X

If the full matrix is too dense for one slide, use the compact equation on the slide and place the expanded matrix as a secondary visual element.

## Slide 8: Python Result

Title:

Simulation result

Body:

The Python simulation confirms the theory.

Observation:

- 125.0 Hz produces a concentrated FFT peak
- 123.5 Hz spreads energy across nearby bins

This is the visual signature of spectral leakage.

Footer:

Code + figure available in the GitHub repository.

Visual Direction:

Use the generated figure:

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png

Crop or place the figure so labels remain readable.

## Slide 9: Why Engineers Should Care

Title:

Why this matters

Body:

Spectral leakage affects real engineering systems:

- frequency estimation
- weak-signal detection
- vibration analysis
- communications spectrum analysis
- radar Doppler processing
- beamforming and array-processing pipelines

Radar and array-processing example:

A rectangular window has a relatively high first sidelobe level of about -13 dB.

In radar, Doppler processing, and DOA estimation pipelines, sidelobes from a strong target can mask weaker nearby targets, especially when the weaker target has lower radar cross section or lies close in frequency, range, Doppler, or angle.

Footer:

FFT interpretation is not just math. It is an engineering decision.

Visual Direction:

Use a simple strong-target / weak-target illustration.

Show a large main target with sidelobes and a smaller nearby target partially hidden by those sidelobes.

Avoid overstating the result: say "can mask" rather than "always masks."

## Slide 10: Takeaway and GitHub CTA

Title:

Key takeaway

Body:

FFT results depend on:

- sampling rate
- number of samples
- bin spacing
- observation window
- signal alignment with the FFT grid

If the signal is off-grid, spectral leakage appears.

Call to Action:

I documented the implementation, theory notes, interview questions, and LaTeX technical note in my GitHub repository.

Footer:

DSP-Array-Processing-Lab | Exercise 01

Visual Direction:

Use a clean closing slide with:

- repository name
- short takeaway
- GitHub call-to-action

## LinkedIn Post Caption

💡 Why does a single, pure sine wave spread across multiple FFT bins?

If you have ever looked at an FFT spectrum and wondered why a clean frequency looks like a wide dome instead of a sharp needle, you are seeing spectral leakage.

In Exercise 01 of my DSP-Array-Processing-Lab repository, I built a Python simulation to break down the mathematics behind this phenomenon.

The experiment:

• Sampling rate fs: 1000 Hz
• Record length N: 256 samples
• FFT bin spacing Delta f: 3.90625 Hz

We compare two cases:

1️⃣ Coherent sampling: 125.0 Hz

The frequency lands exactly on FFT bin 32:

125 / 3.90625 = 32

In the ideal noiseless case, the signal aligns with the DFT grid and its energy is concentrated in the corresponding FFT bin.

2️⃣ Non-coherent sampling: 123.5 Hz

The frequency lands between FFT bins:

123.5 / 3.90625 = 31.616

The periodic extension of the finite record is no longer smooth at the boundary, so the FFT represents the signal using multiple DFT basis vectors.

That spreading of energy is spectral leakage.

🔴 Why radar and antenna-array engineers should care:

A rectangular window has a relatively high first sidelobe level of about -13 dB.

In radar, Doppler processing, and DOA estimation pipelines, sidelobes from a strong target can mask weaker nearby targets, especially when the weaker target has lower radar cross section or lies close in frequency, range, Doppler, or angle.

This is not a coding bug.

It is a fundamental finite-window and measurement-grid effect.

I documented this exercise in my repository, including:

✅ Python implementation
✅ Generated FFT figure
✅ Theory notes
✅ Matrix-based DFT technical note
✅ Interview preparation questions

🔗 Deep-dive article and repository link will be shared in the first comment.

#DigitalSignalProcessing #FFT #SignalProcessing #Python #Engineering #Radar #MIMO #ArrayProcessing #GitHub

## Suggested Hashtags

#DigitalSignalProcessing
#FFT
#SignalProcessing
#Python
#Engineering
#Radar
#Communications
#ArrayProcessing
#STEM
#GitHub

## Design Checklist

Before publishing the carousel:

- Verify slide text is readable on mobile.
- Use one main idea per slide.
- Use the generated FFT figure on Slide 8.
- Keep equations large and uncluttered.
- Add consistent slide numbers.
- Use a professional technical color palette.
- Include the GitHub repository name on the final slide.
- Avoid unsupported performance claims.
- Keep the post educational and engineering-focused.

## Source Artifacts

Implementation:

python/ex01_fft_spectral_leakage/main.py

Generated figure:

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png

Theory note:

docs/ex01_fft_spectral_leakage_theory.md

Interview questions:

docs/ex01_fft_spectral_leakage_interview_questions.md

LaTeX technical note:

papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.tex

Compiled PDF:

papers/ex01_fft_spectral_leakage_note/ex01_fft_spectral_leakage_note.pdf
