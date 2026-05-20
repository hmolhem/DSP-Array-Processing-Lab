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
    normalized decibel scale, and saves comparison figures.

    The coherent sinusoid is aligned with an FFT frequency bin, so its
    spectral energy is concentrated near one bin. The non-coherent sinusoid
    is not aligned with an FFT bin, so its energy spreads across neighboring
    bins. This spreading is called spectral leakage.

    This exercise uses an implicit rectangular observation window because
    the finite record is analyzed directly without applying an explicit
    tapering window. This prepares the transition to Exercise 02, where
    window functions such as Hann, Hamming, and Blackman can be compared.
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

    freqs = np.fft.rfftfreq(num_samples, d=1.0 / sampling_rate_hz)

    spectrum = np.fft.rfft(x)
    magnitude = np.abs(spectrum) / num_samples

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
        exactly 0 dB unless the input magnitude is numerically zero.
    """
    eps = 1e-12
    peak = np.max(magnitude)

    if peak <= eps:
        return np.full_like(magnitude, 20.0 * np.log10(eps))

    normalized = magnitude / peak
    magnitude_db = 20.0 * np.log10(np.clip(normalized, eps, 1.0))
    return magnitude_db


def plot_fft_comparison(freqs, coherent_mag, noncoherent_mag, output_path):
    """
    Plot coherent and non-coherent FFT spectra on the same axes using
    line plots with markers.

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

    Notes
    -----
    The x-axis is intentionally zoomed around the target frequencies so the
    leakage pattern is easier to see in reports, slides, and LinkedIn posts.
    Markers are included to emphasize that the FFT samples a discrete set of
    frequency bins.
    """
    coherent_db = magnitude_to_db(coherent_mag)
    noncoherent_db = magnitude_to_db(noncoherent_mag)

    plt.figure(figsize=(10, 5))
    plt.plot(
        freqs,
        coherent_db,
        marker="o",
        markersize=4,
        linewidth=1.6,
        label="Coherent sampling: 125.0 Hz",
    )
    plt.plot(
        freqs,
        noncoherent_db,
        marker="s",
        markersize=4,
        linewidth=1.6,
        label="Non-coherent sampling: 123.5 Hz",
    )
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalized magnitude (dB)")
    plt.title("FFT Spectral Leakage: Coherent vs Non-Coherent Sampling")
    plt.xlim(100.0, 150.0)
    plt.ylim(-80.0, 5.0)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def plot_fft_stem_comparison(freqs, coherent_mag, noncoherent_mag, output_path):
    """
    Plot coherent and non-coherent FFT spectra using stem plots to emphasize
    the discrete-bin nature of the FFT.

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

    Notes
    -----
    Two stacked subplots are used to avoid visual clutter. This figure is
    intended mainly for educational documentation and technical explanation.
    """
    coherent_db = magnitude_to_db(coherent_mag)
    noncoherent_db = magnitude_to_db(noncoherent_mag)

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    markerline, stemlines, baseline = axes[0].stem(
        freqs,
        coherent_db,
        linefmt="C0-",
        markerfmt="C0o",
        basefmt=" ",
    )
    plt.setp(markerline, markersize=4)
    plt.setp(stemlines, linewidth=1.2)
    axes[0].set_title("Coherent sampling: 125.0 Hz")
    axes[0].set_ylabel("Normalized magnitude (dB)")
    axes[0].set_xlim(100.0, 150.0)
    axes[0].set_ylim(-80.0, 5.0)
    axes[0].grid(True, alpha=0.3)

    markerline, stemlines, baseline = axes[1].stem(
        freqs,
        noncoherent_db,
        linefmt="C1-",
        markerfmt="C1s",
        basefmt=" ",
    )
    plt.setp(markerline, markersize=4)
    plt.setp(stemlines, linewidth=1.2)
    axes[1].set_title("Non-coherent sampling: 123.5 Hz")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Normalized magnitude (dB)")
    axes[1].set_xlim(100.0, 150.0)
    axes[1].set_ylim(-80.0, 5.0)
    axes[1].grid(True, alpha=0.3)

    fig.suptitle("FFT Spectral Leakage: Discrete-Bin Stem View")
    fig.tight_layout(rect=[0.0, 0.0, 1.0, 0.97])
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def main():
    """
    Run the FFT spectral leakage experiment.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The function prints experiment parameters and saves figures.

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

    No explicit tapering window is applied, so the analysis corresponds to
    an implicit rectangular observation window.
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
    stem_figure_path = output_dir / "fft_spectral_leakage_stem.png"

    plot_fft_comparison(freqs, coherent_mag, noncoherent_mag, figure_path)
    plot_fft_stem_comparison(
        freqs,
        coherent_mag,
        noncoherent_mag,
        stem_figure_path,
    )

    print("Exercise 01: FFT spectral leakage")
    print(f"Sampling rate: {sampling_rate_hz} Hz")
    print(f"Number of samples: {num_samples}")
    print(f"FFT bin spacing: {sampling_rate_hz / num_samples:.6f} Hz")
    print(f"Coherent frequency: {coherent_frequency_hz} Hz")
    print(f"Non-coherent frequency: {noncoherent_frequency_hz} Hz")
    print("Window: implicit rectangular observation window")
    print("Plot range: 100 Hz to 150 Hz")
    print(f"Saved figure: {figure_path}")
    print(f"Saved stem figure: {stem_figure_path}")


if __name__ == "__main__":
    main()
