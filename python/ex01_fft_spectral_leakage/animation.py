"""
Exercise 01 Animation: FFT Spectral Leakage

Author:
    Hossein Molhem

Created:
    2026-05-20

Purpose:
    Generate educational GIF and MP4 animations showing how FFT spectral
    leakage develops as a sinusoidal frequency moves away from an exact FFT bin.

Description:
    The animation sweeps the sinusoidal frequency from the coherent case
    at 125.0 Hz toward the non-coherent case at 123.5 Hz.

    The top panel shows the time-domain sinusoid.
    The bottom panel shows the corresponding single-sided FFT magnitude
    spectrum using a discrete-bin stem-style representation.

    The script saves two outputs:

    - fft_spectral_leakage_animation.gif
    - fft_spectral_leakage_animation.mp4

    The GIF is useful for GitHub documentation and quick previews.
    The MP4 is better suited for LinkedIn and other social-media platforms.

Engineering Notes:
    This script avoids clearing and rebuilding Matplotlib axes inside the
    animation update loop. Static elements such as labels, limits, grids, and
    axis structure are created once. During each frame, only dynamic data are
    updated using set_ydata(), set_segments(), set_offsets(), and set_xdata().

    This design is more efficient and better aligned with future extensions
    such as live DSP visualization, streaming FFT displays, or monitoring
    hardware-generated data.

    The MP4 writer uses imageio-ffmpeg to locate an FFmpeg executable without
    requiring the user to manually add FFmpeg to the system PATH.

    The time-domain panel shows only the first 50 ms for readability.
    The FFT is computed using the full 256-sample record.
"""

from pathlib import Path

import imageio_ffmpeg
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter, FuncAnimation, PillowWriter
from matplotlib.collections import LineCollection

from main import compute_single_sided_fft, generate_sine_wave, magnitude_to_db


mpl.rcParams["animation.ffmpeg_path"] = imageio_ffmpeg.get_ffmpeg_exe()


def compute_frame_data(
    frequency_hz,
    sampling_rate_hz,
    num_samples,
    x_min_hz,
    x_max_hz,
    y_min_db,
):
    """
    Compute the time-domain signal and visible FFT-bin data for one frame.

    Parameters
    ----------
    frequency_hz : float
        Current sinusoidal frequency in hertz.
    sampling_rate_hz : float
        Sampling frequency in hertz.
    num_samples : int
        Number of samples in the finite record.
    x_min_hz : float
        Minimum frequency shown in the FFT panel.
    x_max_hz : float
        Maximum frequency shown in the FFT panel.
    y_min_db : float
        Minimum plotted dB level. Values below this limit are clipped for
        visualization.

    Returns
    -------
    time_vector : numpy.ndarray
        Time vector in seconds.
    signal : numpy.ndarray
        Time-domain sinusoidal signal.
    visible_freqs : numpy.ndarray
        FFT frequency bins inside the plotted frequency range.
    visible_magnitude_db : numpy.ndarray
        Normalized FFT magnitude values in dB for visible bins.
    """
    time_vector, signal = generate_sine_wave(
        frequency_hz,
        sampling_rate_hz,
        num_samples,
    )

    freqs, magnitude = compute_single_sided_fft(
        signal,
        sampling_rate_hz,
    )
    magnitude_db = magnitude_to_db(magnitude)

    frequency_mask = (freqs >= x_min_hz) & (freqs <= x_max_hz)
    visible_freqs = freqs[frequency_mask]
    visible_magnitude_db = magnitude_db[frequency_mask]

    visible_magnitude_db = np.clip(
        visible_magnitude_db,
        y_min_db,
        0.0,
    )

    return time_vector, signal, visible_freqs, visible_magnitude_db


def build_stem_segments(freqs, magnitude_db, baseline_db):
    """
    Build vertical line segments for an efficient stem-style FFT display.

    Parameters
    ----------
    freqs : numpy.ndarray
        Visible FFT frequency bins in hertz.
    magnitude_db : numpy.ndarray
        Normalized FFT magnitude values in dB.
    baseline_db : float
        Lower dB baseline used for the vertical stem segments.

    Returns
    -------
    segments : list[numpy.ndarray]
        List of two-point line segments suitable for LineCollection.
    """
    return [
        np.array(
            [
                [freq, baseline_db],
                [freq, mag_db],
            ]
        )
        for freq, mag_db in zip(freqs, magnitude_db)
    ]


def create_spectral_leakage_animation(
    sampling_rate_hz,
    num_samples,
    start_frequency_hz,
    end_frequency_hz,
    num_frames,
    gif_output_path,
    mp4_output_path,
    x_min_hz=100.0,
    x_max_hz=150.0,
    y_min_db=-80.0,
    y_max_db=5.0,
    fps=15,
    time_display_window_s=0.05,
):
    """
    Create and save the FFT spectral leakage animation as GIF and MP4.

    Parameters
    ----------
    sampling_rate_hz : float
        Sampling frequency in hertz.
    num_samples : int
        Number of samples in the finite record.
    start_frequency_hz : float
        Starting sinusoidal frequency in hertz.
    end_frequency_hz : float
        Ending sinusoidal frequency in hertz.
    num_frames : int
        Number of animation frames.
    gif_output_path : pathlib.Path
        Output path for the generated GIF animation.
    mp4_output_path : pathlib.Path
        Output path for the generated MP4 animation.
    x_min_hz : float, optional
        Minimum frequency shown in the FFT panel.
    x_max_hz : float, optional
        Maximum frequency shown in the FFT panel.
    y_min_db : float, optional
        Minimum dB value shown in the FFT panel. This parameter controls the
        displayed dynamic range and can be adjusted for future windowing
        experiments.
    y_max_db : float, optional
        Maximum dB value shown in the FFT panel.
    fps : int, optional
        Frames per second used when saving the animations.
    time_display_window_s : float, optional
        Time span shown in the time-domain panel. This affects only the
        display window, not the FFT analysis record.

    Returns
    -------
    output_paths : tuple[pathlib.Path, pathlib.Path]
        Paths to the saved GIF and MP4 animation files.

    Notes
    -----
    The fractional bin index is defined as:

        k_frac = f0 / Delta f

    where Delta f = fs / N.

    When k_frac is an integer, the sinusoid is aligned with the FFT grid.
    When k_frac is non-integer, the sinusoid is off-grid and has nonzero
    projections onto multiple DFT basis vectors. This is the matrix-view
    interpretation of spectral leakage.
    """
    bin_spacing_hz = sampling_rate_hz / num_samples
    frequency_steps_hz = np.linspace(
        start_frequency_hz,
        end_frequency_hz,
        num_frames,
    )

    initial_frequency_hz = frequency_steps_hz[0]

    (
        time_vector,
        signal,
        visible_freqs,
        visible_magnitude_db,
    ) = compute_frame_data(
        frequency_hz=initial_frequency_hz,
        sampling_rate_hz=sampling_rate_hz,
        num_samples=num_samples,
        x_min_hz=x_min_hz,
        x_max_hz=x_max_hz,
        y_min_db=y_min_db,
    )

    fig, (time_ax, fft_ax) = plt.subplots(
        2,
        1,
        figsize=(9, 7),
        constrained_layout=True,
    )

    fig.suptitle(
        "Dynamics of FFT Spectral Leakage",
        fontsize=14,
        fontweight="bold",
    )

    # Static time-domain panel.
    time_line, = time_ax.plot(
        time_vector,
        signal,
        linewidth=1.8,
    )

    time_title = time_ax.set_title(
        f"Time-domain sinusoid | f0 = {initial_frequency_hz:.2f} Hz"
    )

    time_ax.set_xlim(0.0, time_display_window_s)
    time_ax.set_ylim(-1.2, 1.2)
    time_ax.set_xlabel("Time (s)")
    time_ax.set_ylabel("Amplitude")
    time_ax.grid(True, alpha=0.3)

    # Static FFT-domain panel.
    stem_segments = build_stem_segments(
        visible_freqs,
        visible_magnitude_db,
        baseline_db=y_min_db,
    )

    stem_collection = LineCollection(
        stem_segments,
        linewidths=1.2,
    )
    fft_ax.add_collection(stem_collection)

    marker_points = fft_ax.scatter(
        visible_freqs,
        visible_magnitude_db,
        s=18,
    )

    frequency_line = fft_ax.axvline(
        initial_frequency_hz,
        linestyle="--",
        linewidth=1.4,
    )

    fft_title = fft_ax.set_title("FFT stem spectrum")
    fractional_bin_text = fft_ax.text(
        0.02,
        0.92,
        "",
        transform=fft_ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox={
            "boxstyle": "round",
            "facecolor": "white",
            "alpha": 0.85,
        },
    )

    fft_ax.set_xlim(x_min_hz, x_max_hz)
    fft_ax.set_ylim(y_min_db, y_max_db)
    fft_ax.set_xlabel("Frequency (Hz)")
    fft_ax.set_ylabel("Normalized magnitude (dB)")
    fft_ax.grid(True, alpha=0.3)

    def update(frame_index):
        """
        Update only dynamic artists for one animation frame.

        Parameters
        ----------
        frame_index : int
            Index of the current animation frame.

        Returns
        -------
        artists : tuple
            Updated Matplotlib artists.
        """
        frequency_hz = frequency_steps_hz[frame_index]
        fractional_bin = frequency_hz / bin_spacing_hz
        nearest_bin = int(np.round(fractional_bin))
        bin_offset = fractional_bin - nearest_bin

        (
            _,
            signal,
            visible_freqs_frame,
            visible_magnitude_db_frame,
        ) = compute_frame_data(
            frequency_hz=frequency_hz,
            sampling_rate_hz=sampling_rate_hz,
            num_samples=num_samples,
            x_min_hz=x_min_hz,
            x_max_hz=x_max_hz,
            y_min_db=y_min_db,
        )

        time_line.set_ydata(signal)
        time_title.set_text(
            f"Time-domain sinusoid | f0 = {frequency_hz:.2f} Hz"
        )

        updated_segments = build_stem_segments(
            visible_freqs_frame,
            visible_magnitude_db_frame,
            baseline_db=y_min_db,
        )
        stem_collection.set_segments(updated_segments)

        marker_offsets = np.column_stack(
            [
                visible_freqs_frame,
                visible_magnitude_db_frame,
            ]
        )
        marker_points.set_offsets(marker_offsets)

        frequency_line.set_xdata([frequency_hz, frequency_hz])

        fft_title.set_text("FFT stem spectrum")
        fractional_bin_text.set_text(
            "f0 = "
            f"{frequency_hz:.2f} Hz\n"
            "k_frac = "
            f"{fractional_bin:.3f}\n"
            "nearest bin = "
            f"{nearest_bin}\n"
            "bin offset = "
            f"{bin_offset:+.3f}"
        )

        return (
            time_line,
            stem_collection,
            marker_points,
            frequency_line,
            time_title,
            fft_title,
            fractional_bin_text,
        )

    animation = FuncAnimation(
        fig,
        update,
        frames=num_frames,
        interval=1000 / fps,
        blit=False,
    )

    gif_output_path.parent.mkdir(parents=True, exist_ok=True)
    mp4_output_path.parent.mkdir(parents=True, exist_ok=True)

    gif_writer = PillowWriter(fps=fps)
    animation.save(gif_output_path, writer=gif_writer)

    mp4_writer = FFMpegWriter(
        fps=fps,
        codec="libx264",
        bitrate=1800,
        extra_args=[
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
        ],
    )
    animation.save(mp4_output_path, writer=mp4_writer)

    plt.close(fig)

    return gif_output_path, mp4_output_path


def main():
    """
    Run the FFT spectral leakage animation generator.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The function saves GIF and MP4 animations and prints their paths.
    """
    sampling_rate_hz = 1000.0
    num_samples = 256

    start_frequency_hz = 125.0
    end_frequency_hz = 123.5
    num_frames = 80

    x_min_hz = 100.0
    x_max_hz = 150.0
    y_min_db = -80.0
    y_max_db = 5.0
    fps = 15
    time_display_window_s = 0.05

    output_dir = Path(__file__).resolve().parent / "figures"
    gif_output_path = output_dir / "fft_spectral_leakage_animation.gif"
    mp4_output_path = output_dir / "fft_spectral_leakage_animation.mp4"

    saved_gif_path, saved_mp4_path = create_spectral_leakage_animation(
        sampling_rate_hz=sampling_rate_hz,
        num_samples=num_samples,
        start_frequency_hz=start_frequency_hz,
        end_frequency_hz=end_frequency_hz,
        num_frames=num_frames,
        gif_output_path=gif_output_path,
        mp4_output_path=mp4_output_path,
        x_min_hz=x_min_hz,
        x_max_hz=x_max_hz,
        y_min_db=y_min_db,
        y_max_db=y_max_db,
        fps=fps,
        time_display_window_s=time_display_window_s,
    )

    print("Exercise 01: FFT spectral leakage animation")
    print(f"Sampling rate: {sampling_rate_hz} Hz")
    print(f"Number of samples: {num_samples}")
    print(f"FFT bin spacing: {sampling_rate_hz / num_samples:.6f} Hz")
    print(f"Frequency sweep: {start_frequency_hz} Hz to {end_frequency_hz} Hz")
    print(f"Number of frames: {num_frames}")
    print(f"FFT plot range: {x_min_hz} Hz to {x_max_hz} Hz")
    print(f"Displayed dynamic range: {y_min_db} dB to {y_max_db} dB")
    print(f"Animation FPS: {fps}")
    print(f"Time display window: 0.0 s to {time_display_window_s} s")
    print(f"FFT analysis record length: {num_samples / sampling_rate_hz:.3f} s")
    print(f"Saved GIF animation: {saved_gif_path}")
    print(f"Saved MP4 animation: {saved_mp4_path}")


if __name__ == "__main__":
    main()
