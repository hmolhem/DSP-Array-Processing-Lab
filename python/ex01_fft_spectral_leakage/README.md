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

The coherent sinusoid is placed at 125.0 Hz, which aligns with an FFT bin.

The non-coherent sinusoid is placed at 123.5 Hz, which does not align with an FFT bin.

The non-coherent case spreads energy into neighboring bins, producing spectral leakage.

## Run

From the repository root:

python python/ex01_fft_spectral_leakage/main.py

## Output

The script prints the experiment parameters and saves the FFT comparison figure to:

python/ex01_fft_spectral_leakage/figures/fft_spectral_leakage.png

## Result

The generated figure compares the normalized FFT magnitude spectra for coherent and non-coherent sampling.

Expected observation:

- coherent sampling produces a concentrated spectral peak,
- non-coherent sampling spreads energy across multiple FFT bins.

## Engineering Relevance

Spectral leakage affects practical frequency analysis in instrumentation, communications, radar, vibration analysis, and array-processing systems.

Understanding leakage is important before applying windowing, filtering, covariance estimation, or DOA algorithms.

## Files

- main.py: Python implementation and figure generation.
- figures/fft_spectral_leakage.png: Generated FFT comparison figure.
