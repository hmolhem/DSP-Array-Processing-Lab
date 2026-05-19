# Notes: FFT Spectral Leakage

## Key Idea

Spectral leakage occurs when the analyzed signal does not contain an integer number of cycles inside the sampled time window.

In that case, the FFT assumes a periodic extension of a signal segment whose endpoints do not match smoothly. This discontinuity spreads spectral energy into neighboring frequency bins.

## Coherent Sampling

Coherent sampling occurs when the signal frequency aligns exactly with an FFT bin.

For this exercise:

- sampling rate: 1000 Hz
- samples: 256
- bin spacing: 3.90625 Hz
- coherent frequency: 125.0 Hz

Since 125.0 Hz is exactly 32 times the bin spacing, the FFT energy is concentrated at one bin.

## Non-Coherent Sampling

The non-coherent frequency is 123.5 Hz.

This frequency does not align exactly with an FFT bin, so the FFT energy spreads across multiple bins.

## Practical Lesson

Before interpreting FFT peaks, always consider:

- sampling rate,
- number of samples,
- FFT bin spacing,
- signal-window alignment,
- whether windowing is needed.

This concept is foundational for later DSP topics such as window design, filtering, spectral estimation, radar processing, and array-processing algorithms.
