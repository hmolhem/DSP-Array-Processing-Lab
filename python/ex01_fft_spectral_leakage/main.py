"""
Exercise 01: FFT Spectral Leakage

Author:
    Hossein Molhem

Created:
    2026-05-19

Purpose:
    Demonstrate FFT spectral leakage by comparing a coherent sinusoid
    with a non-coherent sinusoid.

Description:
    This script generates two discrete-time sinusoidal signals, computes
    their single-sided FFT magnitude spectra, converts the spectra to a
    normalized decibel scale, and saves a comparison figure.

    The coherent sinusoid is aligned with an FFT frequency bin, so its
    spectral energy is concentrated near one bin. The non-coherent sinusoid
    is not aligned with an FFT bin, so its energy spreads across neighboring
    bins. This spreading is called spectral leakage.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def generate_sine_wave(frequency_hz, sampling_rate_hz, num_samples):
    """
    Generate a real-valued discrete-time sinusoidal signal.

    Parameters
    ----------
    frequency_hz : float
        Sinusoidal signal frequency in hertz.
    sampling_rate_hz : float
        Sampling frequency in hertz.
    num_samples : int
        Number of discrete-time samples.

    Returns
    -------
    t : numpy.ndarray
        Time vector in seconds.
    x : numpy.ndarray
        Sinusoidal signal samples.
    """
    n = np.arange(num_samples)
    t = n / sampling_rate_hz
    x = np.sin(2.0 * np.pi * frequency_hz * t)
    return t, x


def compute_single_sided_fft(x, sampling_rate_hz):
    """
    Compute the single-sided FFT magnitude spectrum of a real signal.

    Parameters
    ----------
    x : numpy.ndarray
        Real-valued input signal.
    sampling_rate_hz : float
        Sampling frequency in hertz.

    Returns
    -------
    freqs : numpy.ndarray
        Non-negative FFT frequency bins in hertz.
    magnitude : numpy.ndarray
        Single-sided FFT magnitude spectrum.
    """
    num_samples = len(x)

    # For real-valued signals, rfft keeps only the non-negative frequencies.
    freqs = np.fft.rfftfreq(num_samples, d=1.0 / sampling_rate_hz)

    # Normalize FFT magnitude by the number of samples.
    spectrum = np.fft.rfft(x)
    magnitude = np.abs(spectrum) / num_samples

    # Convert two-sided amplitude scaling to single-sided amplitude scaling.
    # DC and Nyquist bins are not doubled.
    if num_samples > 1:
        magnitude[1:-1] *= 2.0

    return freqs, magnitude


def magnitude_to_db(magnitude):
    """
    Convert a magnitude spectrum to a normalized decibel scale.

    Parameters
    ----------
    magnitude : numpy.ndarray
        Linear FFT magnitude spectrum.

    Returns
    -------
    magnitude_db : numpy.ndarray
        Normalized magnitude spectrum in dB, where the largest component is
        approximately 0 dB.
    """
    eps = 1e-12
    normalized = magnitude / (np.max(magnitude) + eps)
    magnitude_db = 20.0 * np.log10(normalized + eps)
    return magnitude_db


def plot_fft_comparison(freqs, coherent_mag, noncoherent_mag, output_path):
    """
    Plot coherent and non-coherent FFT spectra on the same axes.

    Parameters
    ----------
    freqs : numpy.ndarray
        Frequency bins in hertz.
    coherent_mag : numpy.ndarray
        FFT magnitude spectrum for the coherent sinusoid.
    noncoherent_mag : numpy.ndarray
        FFT magnitude spectrum for the non-coherent sinusoid.
    output_path : pathlib.Path
        Path where the output figure will be saved.

    Returns
    -------
    None
        The function saves a PNG figure to output_path.
    """
    coherent_db = magnitude_to_db(coherent_mag)
    noncoherent_db = magnitude_to_db(noncoherent_mag)

    plt.figure(figsize=(10, 5))
    plt.plot(freqs, coherent_db, label="Coherent sampling: 125.0 Hz")
    plt.plot(freqs, noncoherent_db, label="Non-coherent sampling: 123.5 Hz")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalized magnitude (dB)")
    plt.title("FFT Spectral Leakage: Coherent vs Non-Coherent Sampling")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def main():
    """
    Run the FFT spectral leakage experiment.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The function prints experiment parameters and saves a figure.

    Notes
    -----
    The FFT bin spacing is:

        Delta f = fs / N

    For this exercise:

        fs = 1000 Hz
        N = 256
        Delta f = 3.90625 Hz

    The coherent frequency is 125.0 Hz, which equals 32 FFT bins.
    The non-coherent frequency is 123.5 Hz, which does not align exactly
    with an FFT bin.
    """
    sampling_rate_hz = 1000.0
    num_samples = 256

    coherent_frequency_hz = 125.0
    noncoherent_frequency_hz = 123.5

    _, coherent_signal = generate_sine_wave(
        coherent_frequency_hz,
        sampling_rate_hz,
        num_samples,
    )
    _, noncoherent_signal = generate_sine_wave(
        noncoherent_frequency_hz,
        sampling_rate_hz,
        num_samples,
    )

    freqs, coherent_mag = compute_single_sided_fft(
        coherent_signal,
        sampling_rate_hz,
    )
    _, noncoherent_mag = compute_single_sided_fft(
        noncoherent_signal,
        sampling_rate_hz,
    )

    output_dir = Path(__file__).resolve().parent / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    figure_path = output_dir / "fft_spectral_leakage.png"
    plot_fft_comparison(freqs, coherent_mag, noncoherent_mag, figure_path)

    print("Exercise 01: FFT spectral leakage")
    print(f"Sampling rate: {sampling_rate_hz} Hz")
    print(f"Number of samples: {num_samples}")
    print(f"FFT bin spacing: {sampling_rate_hz / num_samples:.6f} Hz")
    print(f"Coherent frequency: {coherent_frequency_hz} Hz")
    print(f"Non-coherent frequency: {noncoherent_frequency_hz} Hz")
    print(f"Saved figure: {figure_path}")


if __name__ == "__main__":
    main()
