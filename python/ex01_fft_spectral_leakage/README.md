# Exercise 01: FFT Spectral Leakage

## Purpose

This exercise demonstrates FFT spectral leakage using two sinusoidal signals:

- a coherent sinusoid whose frequency falls exactly on an FFT bin,
- a non-coherent sinusoid whose frequency does not fall exactly on an FFT bin.

The goal is to show why frequency-bin alignment matters in practical DSP analysis.

## Concept

For an FFT with sampling rate fs and N samples, the frequency-bin spacing is:

Delta f = fs / N

In this example:

- fs = 1000 Hz
- N = 256
- Delta f = 3.90625 Hz

The coherent sinusoid is placed at 125.0 Hz, which aligns with FFT bin 32.

The non-coherent sinusoid is placed at 123.5 Hz, which does not align exactly with an FFT bin.

The non-coherent case spreads energy into neighboring bins, producing spectral leakage.

This exercise uses an implicit rectangular observation window because no explicit tapering window is applied before the FFT.

## Run

From the repository root:

python python/ex01_fft_spectral_leakage/main.py

## Output

The main script prints the experiment parameters and saves two FFT comparison figures:

- python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png
- python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_stem.png

## Figures

The line-marker figure is zoomed to 100-150 Hz so the leakage pattern around the target frequencies is easier to see. This figure is optimized for reports, presentations, and LinkedIn carousel content.

The stem figure uses two stacked panels to emphasize the discrete-bin nature of the FFT:

- top panel: coherent sampling at 125.0 Hz,
- bottom panel: non-coherent sampling at 123.5 Hz.


## Animation

This exercise also includes an educational animation script:

python/ex01_fft_spectral_leakage/animation.py

Run it from the repository root with:

python python/ex01_fft_spectral_leakage/animation.py

The animation output is saved to:

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage_animation.gif

The animation sweeps the sinusoidal frequency from 125.0 Hz to 123.5 Hz and shows how the FFT spectrum changes as the signal moves away from an exact FFT bin.

The animation displays:

- the time-domain sinusoid,
- the FFT stem spectrum,
- the fractional bin index k_frac,
- the nearest FFT bin,
- the bin offset from the nearest integer bin.

The animation code avoids clearing and rebuilding the Matplotlib axes inside the update loop. Static plot elements are created once, while dynamic objects are updated using set_ydata(), set_segments(), set_offsets(), and set_xdata().

## Expected Observation

- coherent sampling produces a concentrated spectral peak,
- non-coherent sampling spreads energy across multiple FFT bins,
- the stem view makes the discrete FFT bins more explicit.

## Engineering Relevance

Spectral leakage affects practical frequency analysis in instrumentation, communications, radar, vibration analysis, and array-processing systems.

Understanding leakage is important before applying windowing, filtering, covariance estimation, beamforming, or DOA algorithms.

The implicit rectangular-window case in this exercise prepares the transition to Exercise 02, where explicit window functions can be compared.

## Files

- main.py: Python implementation and static figure generation.
- animation.py: GIF animation showing the dynamic development of spectral leakage.
- figures/fft_spectral_leakage.png: Zoomed line-marker FFT comparison figure.
- figures/fft_spectral_leakage_stem.png: Stem-plot figure showing the discrete-bin FFT view.
- figures/fft_spectral_leakage_animation.gif: Animation showing frequency movement from coherent to non-coherent sampling.
