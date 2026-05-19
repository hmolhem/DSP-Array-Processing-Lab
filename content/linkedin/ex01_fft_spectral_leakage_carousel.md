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

It evaluates a discrete grid.

Formula:

Delta f = fs / N

For this experiment:

Delta f = 1000 / 256 = 3.90625 Hz

Footer:

Frequency resolution depends on sampling rate and record length.

Visual Direction:

Show a horizontal frequency axis with equally spaced bins.

Label a few bins:

0 Hz, 3.90625 Hz, 7.8125 Hz, ..., 125 Hz

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

The DFT can be written as:

X = F_N x

Where:

- x is the sampled signal vector
- F_N is the DFT matrix
- X is the frequency-domain coefficient vector

Interpretation:

The DFT projects the signal onto a finite set of frequency-basis vectors.

Footer:

Leakage is off-grid basis mismatch.

Visual Direction:

Use a block diagram:

sampled vector x -> DFT matrix F_N -> spectrum X

Keep the equation large and clean.

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

Footer:

FFT interpretation is not just math. It is an engineering decision.

Visual Direction:

Use icons or small labels for radar, communications, vibration, and arrays.

Avoid clutter.

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

FFT Spectral Leakage: Why One Sine Wave Becomes Many FFT Bins

In Exercise 01 of my DSP-Array-Processing-Lab repository, I implemented a Python simulation to demonstrate FFT spectral leakage.

The experiment compares two sinusoidal signals:

- 125.0 Hz: coherent with the FFT grid
- 123.5 Hz: non-coherent with the FFT grid

Both use the same sampling rate and record length:

- fs = 1000 Hz
- N = 256
- Delta f = 3.90625 Hz

The key result:

The 125.0 Hz sinusoid aligns exactly with FFT bin 32, so its energy is concentrated.

The 123.5 Hz sinusoid falls between FFT bins, so its energy spreads across neighboring bins.

That spreading is spectral leakage.

I also documented the topic from multiple angles:

- Python implementation
- Generated FFT figure
- Theory notes
- Interview questions
- LaTeX technical note with matrix-based DFT formulation

The main lesson is simple but important:

FFT interpretation depends on sampling rate, record length, bin spacing, and signal alignment with the frequency grid.

This concept is foundational for windowing, spectral estimation, radar Doppler processing, communications, beamforming, and array-processing workflows.

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
