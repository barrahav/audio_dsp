import numpy as np
import matplotlib.pyplot as plt


def generate_test_signal(fs=44100, duration=1.0):
    """
    Generate a 440 Hz sine wave that increases amplitude halfway.
    """
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    signal = np.sin(2 * np.pi * 440 * t)

    # Increase amplitude halfway through
    halfway_index = int(0.5 * fs)
    signal[halfway_index:] *= 2

    return signal, fs


def envelope_moving_average(signal, window_size=500):
    """
    Simple envelope detector:
    1. Full-wave rectification
    2. Moving average low-pass filter
    """
    rectified = np.abs(signal)

    window = np.ones(window_size) / window_size
    envelope = np.convolve(rectified, window, mode='same')

    return envelope


def main():
    signal, fs = generate_test_signal()

    envelope = envelope_moving_average(signal)

    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(signal, alpha=0.4, label="Signal")
    plt.plot(envelope, label="Envelope", linewidth=2)
    plt.title("Envelope Detection (Moving Average)")
    plt.legend()
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.show()


if __name__ == "__main__":
    main()