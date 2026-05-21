# LinkedIn Post Draft: FFT Spectral Leakage

Author: Hossein Molhem
Project: DSP-Array-Processing-Lab
Exercise: 01 - FFT Spectral Leakage
Content Type: LinkedIn post draft
Status: Draft

## Purpose

This document provides a LinkedIn-ready post draft for Exercise 01: FFT Spectral Leakage.

The post is designed to accompany one or more of the following assets:

- LinkedIn carousel storyboard
- zoomed FFT line-marker figure
- FFT stem figure
- FFT spectral leakage animation in GIF and MP4 formats
- GitHub repository link
- future Substack/deep-dive article

## Recommended Media Asset

Primary recommended asset:

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_animation.gif

Alternative static assets:

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_stem.png

Recommended posting strategy:

- Use the MP4 animation for LinkedIn video posting.
- Use the GIF animation for GitHub documentation or quick previews.
- Use the carousel if a more structured educational post is preferred.
- Use the line-marker figure for a simple one-image post.
- Use the stem figure in a follow-up technical comment or second post.

## Main LinkedIn Post

💡 Why does one clean sine wave spread across multiple FFT bins?

If you have ever looked at an FFT spectrum and wondered why a pure tone looks like a wide dome instead of a sharp needle, you are seeing spectral leakage.

In Exercise 01 of my DSP-Array-Processing-Lab repository, I built a Python simulation to demonstrate this effect from both a signal-processing and matrix-based DFT perspective.

The experiment uses:

• Sampling rate: 1000 Hz
• Record length: 256 samples
• FFT bin spacing: 3.90625 Hz

Two cases are compared:

1️⃣ Coherent sampling: 125.0 Hz

The frequency lands exactly on FFT bin 32:

125 / 3.90625 = 32

In the ideal noiseless case, the signal aligns with the FFT frequency grid and its energy is concentrated near one bin.

2️⃣ Non-coherent sampling: 123.5 Hz

The frequency lands between FFT bins:

123.5 / 3.90625 = 31.616

Now the sinusoid is off-grid, so the finite sampled signal projects onto multiple DFT basis vectors.

That spreading of energy is spectral leakage.

To make the concept easier to see, I generated:

✅ a zoomed FFT line-marker figure
✅ a discrete-bin stem plot
✅ GIF and MP4 animations showing the transition from coherent to non-coherent sampling
✅ a LaTeX technical note with matrix-based DFT formulation
✅ interview-style review questions

The key engineering idea:

The FFT does not evaluate every possible frequency.

It evaluates a discrete frequency grid.

When the signal does not align with that grid, leakage appears.

This matters in practical systems such as:

• radar Doppler processing
• weak-target detection
• vibration analysis
• communications spectrum analysis
• beamforming and DOA estimation

A rectangular observation window has a relatively high first sidelobe level of about -13 dB, so leakage from a strong component can mask weaker nearby components.

This is not a coding bug.

It is a finite-window and frequency-grid mismatch effect.

I am building this repository as a practical DSP and array-processing portfolio, gradually connecting:

DSP foundations → spectral estimation → beamforming → DOA estimation → sparse/coarray methods → FPGA/HLS-ready kernels

🔗 GitHub repository link will be in the first comment.

#DigitalSignalProcessing #FFT #SignalProcessing #Python #Radar #MIMO #ArrayProcessing #Engineering #FPGA #GitHub

## First Comment Draft

GitHub repository:

https://github.com/hmolhem/DSP-Array-Processing-Lab

Exercise 01 artifacts include:

- Python implementation
- FFT line-marker figure
- FFT stem figure
- FFT spectral leakage animation in GIF and MP4 formats
- theory notes
- interview questions
- LaTeX technical note and compiled PDF
- LinkedIn carousel storyboard

Exercise path:

FFT spectral leakage → windowing and frequency resolution → filtering → covariance estimation → beamforming → MUSIC DOA estimation → FPGA/HLS mapping

## Short Version

A pure sine wave does not always produce one clean FFT bin.

If the sinusoid frequency aligns with the FFT grid, its energy is concentrated.

If the frequency falls between FFT bins, the finite sampled signal projects onto multiple DFT basis vectors.

That spreading is spectral leakage.

I demonstrated this in Python using:

• coherent sampling at 125.0 Hz
• non-coherent sampling at 123.5 Hz
• fs = 1000 Hz
• N = 256
• Delta f = 3.90625 Hz

I also generated a line-marker plot, stem plot, animation GIF, LaTeX note, and interview questions.

This concept matters in radar, communications, vibration analysis, beamforming, and DOA estimation.

#DigitalSignalProcessing #FFT #Python #Radar #ArrayProcessing

## Technical Angle for Follow-Up Comment

Matrix view:

The DFT can be written as:

$\mathbf{X} = \mathbf{F}_N \mathbf{x}$

The sampled signal vector is projected onto a finite set of orthogonal DFT basis vectors.

If the sinusoid is on-grid, most of the energy appears in one bin.

If the sinusoid is off-grid, the projection is nonzero across multiple DFT basis vectors.

The fractional bin index is:

$k_{\text{frac}} = f_0 / \Delta f$

When $k_{\text{frac}}$ is an integer, the sinusoid aligns with the FFT grid.

When $k_{\text{frac}}$ is non-integer, leakage appears.

That is the matrix interpretation of spectral leakage.

## Suggested Hashtags

#DigitalSignalProcessing
#FFT
#SignalProcessing
#Python
#Radar
#MIMO
#ArrayProcessing
#Beamforming
#DOA
#Engineering
#FPGA
#GitHub

## Publishing Checklist

Before publishing:

- Confirm the GIF renders correctly on LinkedIn.
- If GIF playback is not reliable, use the carousel or static line-marker figure.
- Put the GitHub repository link in the first comment.
- Keep the main post readable on mobile.
- Avoid overclaiming; say sidelobes can mask weaker nearby targets.
- Mention this is Exercise 01 in a broader DSP-to-DOA portfolio.
- Pin or reply with the repository link after posting.
