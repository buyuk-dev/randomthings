#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Audio sinusoidal waves generator.
    ---------------------------------
    Can be used to generate waves of the particular frequency,
    or sum of all frequencies for frequency response measurements. 
"""

import argparse
import numpy
import sounddevice


SAMPLING = 44100  # Hz


def generate_signal(frequency, cycles):
    """ Generates samples of the sine wave at specified frequency
        over the length of given number of cycles. Amplitude is 
        scaled down to avoid getting over the <-1; 1> range.
    """
    T = 1 / frequency
    X = numpy.linspace(0, T, T * SAMPLING)
    Y = 0.9 * numpy.sin(2 * numpy.pi * frequency * X)
    return numpy.tile(Y, cycles)


def generate_spectral_signal(frequencies, cycles):
    """ Generate normalized sum of all given frequencies.
    """
    F = [generate_signal(f, cycles) for f in frequencies]
    L = [len(f) for f in F]
    minLen = min(L)
    X = sum(f[:minLen] for f in F)
    return X / numpy.max(X)


def compute_spectrum(X, cutoff=numpy.inf):
    """ Compute normalized frequency spectrum.
    """
    fft = numpy.abs(numpy.fft.fft(X)) / len(X)
    fft = fft[range(int(len(X) / 2))]

    freq = numpy.fft.fftfreq(len(X), 1.0 / SAMPLING)
    freq = freq[range(int(len(X) / 2))]

    index = numpy.where(freq < cutoff)[0][-1]
    freq = freq[:index]
    fft = fft[:index]

    return freq[1:], fft[1:]


def configure():
    """ Configure sounddevice to use default audio
        output device at the given sampling rate.
    """
    sounddevice.default.samplerate = SAMPLING
    sounddevice.default.device = sounddevice.query_devices()[1]["name"]


def play(frequency, length):
    """ Generate signal and play it. This function
        blocks until the entire signal is played.
        Can be stopped by <Ctrl + C> signal.
    """
    signal = generate_signal(frequency, length)
    sounddevice.play(signal)
    sounddevice.wait()


def play_frequency_spectrum(low, high, cycles):
    """ Play signal composed of all frequencies in range <low; high).
    """
    signal = generate_spectral_signal(range(low, high), cycles)
    print("playing signal...")
    sounddevice.play(signal)
    sounddevice.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frequency", type=int, help="Wave frequency")
    parser.add_argument(
        "--cycles",
        type=int,
        default=1,
        help="Length of the signal in multiples of the wave period.",
    )
    args = parser.parse_args()

    configure()
    play(args.frequency, args.cycles)

