# Exercise 01 Theory: FFT Spectral Leakage

Author: Hossein Molhem
Created: 2026-05-19
Project: DSP-Array-Processing-Lab
Exercise: 01 - FFT Spectral Leakage

## 1. Purpose

This note explains the theory behind Exercise 01: FFT spectral leakage.

The goal is to understand how the FFT represents a sampled sinusoidal signal, why some frequencies align perfectly with FFT bins, and why other frequencies spread energy across multiple bins.

This concept is fundamental for practical DSP work in spectrum analysis, instrumentation, communications, radar, vibration analysis, and array processing.

## 2. From Continuous-Time Signal to Discrete-Time Samples

A continuous-time sinusoidal signal can be written as:

x(t) = sin(2 pi f0 t)

where:

- f0 is the signal frequency in hertz,
- t is continuous time in seconds.

After sampling at sampling frequency fs, the discrete-time signal becomes:

x[n] = sin(2 pi f0 n / fs)

where:

- n = 0, 1, 2, ..., N - 1,
- fs is the sampling rate in hertz,
- N is the number of samples.

In Exercise 01:

- fs = 1000 Hz
- N = 256

## 3. DFT Definition

The Discrete Fourier Transform, or DFT, converts a finite-length time-domain sequence into a finite set of frequency-domain samples.

For a signal x[n] of length N, the DFT is:

X[k] = sum from n = 0 to N - 1 of x[n] exp(-j 2 pi k n / N)

where:

- X[k] is the complex spectrum at frequency bin k,
- k = 0, 1, 2, ..., N - 1,
- j is the imaginary unit.

Each value X[k] measures how strongly the input signal matches a complex sinusoid at bin k.

## 4. FFT Meaning

The FFT, or Fast Fourier Transform, is an efficient algorithm for computing the DFT.

The DFT equation directly requires approximately N^2 operations.

The FFT reduces the computational cost to approximately N log2(N) operations.

For engineering work, the FFT is the practical tool used to compute the DFT efficiently.

## 5. FFT Frequency Bins

The FFT does not evaluate every possible frequency. It evaluates a discrete frequency grid.

The frequency corresponding to FFT bin k is:

f_k = k fs / N

The spacing between adjacent FFT bins is:

Delta f = fs / N

In Exercise 01:

Delta f = 1000 / 256 = 3.90625 Hz

So the FFT frequency bins are located at:

- 0 Hz
- 3.90625 Hz
- 7.8125 Hz
- 11.71875 Hz
- ...
- 125 Hz
- ...

## 6. Coherent Sampling

Coherent sampling occurs when the signal frequency lands exactly on one FFT bin.

In Exercise 01, the coherent frequency is:

f0 = 125.0 Hz

The bin index is:

k = f0 / Delta f = 125.0 / 3.90625 = 32

Because k is an integer, the sinusoid aligns exactly with FFT bin 32.

This means the sampled signal contains an integer number of cycles inside the observation window.

For the coherent case, the FFT energy is concentrated near one bin.

## 7. Non-Coherent Sampling

Non-coherent sampling occurs when the signal frequency does not land exactly on an FFT bin.

In Exercise 01, the non-coherent frequency is:

f0 = 123.5 Hz

The bin index is:

k = 123.5 / 3.90625 = 31.616

Because k is not an integer, the frequency lies between FFT bins.

The FFT cannot place all signal energy into one bin, so the energy spreads across neighboring bins.

This spreading is called spectral leakage.

## 8. Why Spectral Leakage Occurs

The FFT assumes that the finite signal segment repeats periodically.

If the sampled segment starts and ends smoothly, the periodic repetition is continuous.

If the segment does not contain an integer number of cycles, the repeated signal has a discontinuity at the boundary.

This artificial discontinuity introduces additional frequency components.

As a result, the FFT spectrum spreads energy away from the true signal frequency.

## 9. Window Interpretation

Taking N samples from a signal is equivalent to multiplying the infinite signal by a rectangular time window.

In the frequency domain, multiplication in time becomes convolution in frequency.

Therefore, the true sinusoidal spectrum is convolved with the spectrum of the rectangular window.

The rectangular window has sidelobes, and those sidelobes cause energy to appear in neighboring FFT bins.

This is another way to understand spectral leakage.

## 10. Single-Sided FFT for Real Signals

For real-valued signals, the full FFT has conjugate symmetry.

That means the negative-frequency half of the spectrum contains redundant information.

For this reason, Exercise 01 uses a single-sided FFT with numpy.fft.rfft.

The corresponding frequency bins are computed using numpy.fft.rfftfreq.

This keeps only the non-negative frequency components.

## 11. Magnitude Scaling

The raw FFT output is complex.

The magnitude spectrum is computed as:

magnitude[k] = abs(X[k]) / N

For a single-sided spectrum, the non-DC and non-Nyquist bins are usually doubled to preserve amplitude scaling.

That is why the code applies:

magnitude[1:-1] *= 2

This step makes the single-sided amplitude spectrum easier to interpret.

## 12. Normalized dB Scale

The figure uses a normalized decibel scale.

First, the magnitude spectrum is normalized by its maximum value:

normalized[k] = magnitude[k] / max(magnitude)

Then it is converted to dB:

magnitude_dB[k] = 20 log10(normalized[k])

With this convention:

- the largest spectral peak is near 0 dB,
- smaller components appear as negative dB values,
- leakage sidelobes become visually clear.

## 13. Practical Leakage Measurement

Spectral leakage can be measured in different ways. One useful engineering definition is the ratio of energy outside the main peak region to the total spectral energy.

A simple leakage ratio can be defined as:

total_power = sum over all bins of |X[k]|^2

main_power = sum over selected main-lobe bins of |X[k]|^2

leakage_power = total_power - main_power

leakage_ratio = leakage_power / total_power

leakage_dB = 10 log10(leakage_ratio)

The result depends on how the main-lobe region is defined.

If only the peak bin is counted as the main region, the leakage estimate is stricter.

If the peak bin and nearby bins are counted as the main lobe, the leakage estimate is more tolerant.

## 14. Engineering Interpretation

Spectral leakage is not a coding error. It is a consequence of finite-duration measurement and frequency-grid mismatch.

In practical systems, leakage can affect:

- frequency estimation,
- weak-signal detection,
- harmonic analysis,
- vibration diagnostics,
- radar Doppler processing,
- communication signal analysis,
- beamforming and array-processing pipelines.

Before interpreting FFT peaks, an engineer should check:

- sampling rate,
- number of samples,
- FFT bin spacing,
- signal frequency alignment,
- observation window length,
- whether windowing is needed.

## 15. Connection to Exercise 02

Exercise 01 uses a rectangular observation window implicitly.

Exercise 02 can extend this by applying common windows such as:

- Hann window,
- Hamming window,
- Blackman window.

Windowing reduces sidelobe leakage but usually widens the main lobe.

This creates an important engineering tradeoff between leakage suppression and frequency resolution.

## 16. Summary

The FFT represents a finite signal using discrete frequency bins.

If the signal frequency aligns exactly with an FFT bin, the spectrum is concentrated.

If the signal frequency falls between FFT bins, energy spreads into neighboring bins.

This spreading is spectral leakage.

Understanding spectral leakage is essential before moving to windowing, filtering, spectral estimation, radar processing, and DOA estimation.
