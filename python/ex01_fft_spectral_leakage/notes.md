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

## Implicit Rectangular Window

This exercise does not apply an explicit tapering window before the FFT.

Therefore, the finite record is analyzed with an implicit rectangular observation window.

The rectangular-window case is important because it produces a clear leakage pattern and prepares the transition to Exercise 02, where Hann, Hamming, and Blackman windows can be compared.

## Visualization Notes

The script generates two complementary figures:

- `fft_spectral_leakage.png`
- `fft_spectral_leakage_stem.png`

The line-marker figure is zoomed to 100-150 Hz to make the leakage pattern around the target frequencies easier to see.

This figure is useful for:

- reports,
- presentations,
- LinkedIn carousel content,
- quick visual comparison of coherent and non-coherent sampling.

The stem figure emphasizes that the FFT evaluates discrete frequency bins rather than a continuous frequency axis.

This figure is useful for:

- explaining the finite-bin nature of the FFT,
- showing that the coherent case concentrates energy near one bin,
- showing that the non-coherent case spreads energy across multiple bins,
- connecting the visual result to the DFT matrix interpretation.

The two figures should be interpreted together:

- the line-marker figure gives a presentation-friendly comparison,
- the stem figure gives a more discrete, bin-centered engineering view.

## Matrix Interpretation

The DFT can be written in vector-matrix form:

$$\mathbf{X} = \mathbf{F}_N \mathbf{x}$$

Expanded form:

$$
\begin{bmatrix}
X[0] \\
X[1] \\
\vdots \\
X[N-1]
\end{bmatrix}
=
\begin{bmatrix}
1 & 1 & \dots & 1 \\
1 & W_N^1 & \dots & W_N^{N-1} \\
\vdots & \vdots & \ddots & \vdots \\
1 & W_N^{N-1} & \dots & W_N^{(N-1)(N-1)}
\end{bmatrix}
\begin{bmatrix}
x[0] \\
x[1] \\
\vdots \\
x[N-1]
\end{bmatrix}
$$

where:

- $\mathbf{x}$ is the sampled signal vector,
- $\mathbf{F}_N$ is the DFT matrix,
- $\mathbf{X}$ is the frequency-domain coefficient vector,
- $W_N = e^{-j2\pi/N}$.

The DFT projects the sampled signal vector onto a finite set of orthogonal frequency-basis vectors.

If the input sinusoid is exactly on-grid, most of the energy appears in one DFT bin.

If the sinusoid is off-grid, its projection is nonzero across multiple DFT basis vectors. This is the matrix-view interpretation of spectral leakage.

## Practical Lesson

Before interpreting FFT peaks, always consider:

- sampling rate,
- number of samples,
- FFT bin spacing,
- signal-window alignment,
- implicit or explicit window choice,
- whether additional windowing is needed.

This concept is foundational for later DSP topics such as window design, filtering, spectral estimation, radar processing, and array-processing algorithms.
