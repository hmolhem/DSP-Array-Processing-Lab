# Exercise 01 Interview Questions: FFT Spectral Leakage

Author: Hossein Molhem
Created: 2026-05-19
Project: DSP-Array-Processing-Lab
Exercise: 01 - FFT Spectral Leakage

## Purpose

This document provides interview-style questions and answers based on Exercise 01: FFT Spectral Leakage.

The goal is to connect the implemented Python exercise to practical DSP interview preparation.

## 1. Fundamental Questions

### Q1. What is the DFT?

The Discrete Fourier Transform, or DFT, converts a finite-length discrete-time signal into a finite set of frequency-domain samples.

For a signal x[n] with N samples, the DFT computes complex coefficients X[k] that represent how much of each discrete frequency bin is present in the signal.

### Q2. What is the FFT?

The Fast Fourier Transform, or FFT, is an efficient algorithm for computing the DFT.

A direct DFT requires approximately N squared operations, while the FFT reduces the computational cost to approximately N log2(N).

### Q3. What does an FFT bin represent?

An FFT bin represents one discrete frequency point in the FFT frequency grid.

For sampling rate fs and N samples, the frequency of bin k is:

f_k = k fs / N

### Q4. What is FFT bin spacing?

FFT bin spacing is the frequency difference between two adjacent FFT bins.

Delta f = fs / N

In Exercise 01, fs = 1000 Hz and N = 256, so Delta f = 3.90625 Hz.

## 2. Coherent and Non-Coherent Sampling

### Q5. What is coherent sampling?

Coherent sampling occurs when the signal frequency aligns exactly with an FFT bin.

In this condition, the sampled time window contains an integer number of signal cycles, and the FFT energy is concentrated near one bin.

### Q6. Why is 125 Hz coherent in Exercise 01?

The FFT bin spacing is 3.90625 Hz.

125.0 / 3.90625 = 32

Since 32 is an integer, 125 Hz lands exactly on FFT bin 32.

### Q7. What is non-coherent sampling?

Non-coherent sampling occurs when the signal frequency does not align exactly with an FFT bin.

The sampled time window does not contain an integer number of signal cycles, so the FFT energy spreads into multiple bins.

### Q8. Why is 123.5 Hz non-coherent in Exercise 01?

The FFT bin spacing is 3.90625 Hz.

123.5 / 3.90625 = 31.616

Since 31.616 is not an integer, 123.5 Hz lies between FFT bins.

## 3. Spectral Leakage

### Q9. What is spectral leakage?

Spectral leakage is the spreading of signal energy across multiple FFT bins when the signal frequency does not align exactly with the FFT frequency grid.

### Q10. Is spectral leakage a coding error?

No. Spectral leakage is not a coding error.

It is a natural consequence of finite-duration signal observation and frequency-grid mismatch.

### Q11. Why does spectral leakage happen?

The FFT assumes that the finite sampled segment repeats periodically.

If the sampled segment does not contain an integer number of cycles, the repeated signal has a discontinuity at the boundary. This artificial discontinuity introduces extra frequency components, causing energy to spread across bins.

### Q12. What is the window interpretation of spectral leakage?

Taking N samples from a signal is equivalent to multiplying the signal by a rectangular window in time.

Multiplication in time corresponds to convolution in frequency.

The spectrum of the rectangular window has sidelobes, and those sidelobes cause leakage into neighboring bins.

## 4. Practical FFT Interpretation

### Q13. Why do we use a single-sided FFT for real signals?

For real-valued time-domain signals, the FFT has conjugate symmetry. The negative-frequency half contains redundant information.

A single-sided FFT keeps only the non-negative frequency components, which is more compact and easier to interpret.

### Q14. What does numpy.fft.rfft do?

numpy.fft.rfft computes the FFT of a real-valued input signal and returns only the non-negative frequency components.

### Q15. What does numpy.fft.rfftfreq do?

numpy.fft.rfftfreq returns the frequency values corresponding to the output bins of numpy.fft.rfft.

### Q16. Why is FFT magnitude divided by N?

The raw FFT magnitude scales with the number of samples. Dividing by N normalizes the amplitude and makes the spectrum easier to interpret.

### Q17. Why are non-DC and non-Nyquist bins doubled in a single-sided FFT?

A single-sided FFT removes the negative-frequency half of the spectrum.

For real signals, the positive- and negative-frequency components share energy. Doubling the non-DC and non-Nyquist bins preserves the amplitude scale in the single-sided spectrum.

### Q18. Why convert FFT magnitude to dB?

The dB scale makes it easier to visualize large dynamic ranges.

Small sidelobes and leakage components are easier to see in dB than in linear magnitude.

## 5. Engineering and Interview Discussion

### Q19. How can spectral leakage affect engineering systems?

Spectral leakage can affect:

- frequency estimation,
- weak-signal detection,
- harmonic analysis,
- vibration diagnostics,
- radar Doppler processing,
- communications spectrum analysis,
- beamforming and array-processing pipelines.

### Q20. How can spectral leakage be reduced?

Spectral leakage can be reduced by applying a window function such as:

- Hann window,
- Hamming window,
- Blackman window.

Windowing reduces sidelobe leakage but usually widens the main lobe.

### Q21. What is the tradeoff when using window functions?

Windowing reduces sidelobe leakage, but it also widens the main lobe.

This means there is a tradeoff between leakage suppression and frequency resolution.

### Q22. What should an engineer check before interpreting FFT peaks?

An engineer should check:

- sampling rate,
- number of samples,
- FFT bin spacing,
- signal frequency alignment,
- observation duration,
- windowing choice,
- noise level,
- whether the signal is stationary during the observation window.

### Q23. How would you explain spectral leakage in one sentence?

Spectral leakage occurs when a finite sampled signal does not align with the FFT frequency grid, causing its energy to spread into neighboring frequency bins.

### Q24. What is the main lesson from Exercise 01?

The main lesson is that FFT interpretation depends strongly on sampling rate, sample count, bin spacing, and signal alignment with the FFT frequency grid.

## 6. Short Interview Answers

### Q25. What is Delta f?

Delta f is the FFT frequency resolution or bin spacing.

Delta f = fs / N

### Q26. What happens when a sinusoid falls exactly on an FFT bin?

Its energy is concentrated near that bin.

### Q27. What happens when a sinusoid falls between FFT bins?

Its energy spreads across neighboring bins, causing spectral leakage.

### Q28. Is increasing N useful?

Yes. Increasing N reduces bin spacing and improves frequency-grid resolution, but it also requires a longer observation window or more samples.

### Q29. Does zero-padding remove leakage?

No. Zero-padding interpolates the spectrum and makes plots smoother, but it does not remove leakage caused by the original finite-time window.

### Q30. What is the connection between leakage and windowing?

Leakage is strongly affected by the time-domain window. Window functions reshape the leakage pattern by reducing sidelobes at the cost of wider main lobes.

## 7. Resume-Oriented Explanation

A strong resume or interview explanation could be:

In Exercise 01, I implemented a Python-based FFT spectral leakage demonstration. I generated coherent and non-coherent sinusoidal signals, computed their single-sided FFT spectra, normalized the magnitudes, converted them to dB, and generated a comparison figure. The exercise demonstrates how FFT bin alignment affects spectral energy concentration and why non-coherent sampling produces leakage across neighboring bins.

## 8. Possible Follow-Up Interview Questions

An interviewer may ask:

- How would the result change if the number of samples increased?
- How would a Hann window change the leakage pattern?
- What is the difference between spectral leakage and noise?
- How does leakage affect weak target detection in radar?
- How does FFT bin spacing relate to observation time?
- Why does zero-padding not truly improve frequency resolution?
- How would you estimate the true frequency of a non-bin-centered sinusoid?
- How does leakage influence DOA or beamforming pipelines?

## 9. Summary

FFT spectral leakage is a fundamental DSP concept.

It occurs when a finite observation window does not contain an integer number of cycles of the signal.

Understanding leakage is essential before moving to windowing, filtering, spectral estimation, radar processing, and array-processing applications.
