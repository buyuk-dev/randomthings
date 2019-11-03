#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Audio sinusoidal waves generator.
    ---------------------------------
    Can be used to generate waves of the particular frequency,
    or sum of all frequencies for frequency response measurements. 
"""

import argparse
import math

import numpy.fft
import matplotlib.pyplot as pyplot

import sounddevice


class Config:
    """ Common parameters which should be user-agnostic.
    """
    samplingFrequency = 44100  # Hz


def drange(a, b, step):
    """ Decimal range generator. It uses multiplication to avoid
        cumulative error due to floating-point arithmetic.
    """
    dt = (b - a) / step
    for i in range(0, int(dt)):
        yield i * step


def generate_signal(frequency, cycles):
    """ Generates samples of the sine wave at specified frequency
        over the length of given number of cycles. Amplitude is 
        scaled down to avoid getting over the <-1; 1> range.
    """
    step = 1.0 / Config.samplingFrequency
    scale = 0.9
    print(f"generating signal at {frequency} Hz")
    return [
        scale * math.sin(2 * math.pi * frequency * x)
        for x in drange(0, 2 * math.pi * cycles, step)
    ]


def configure():
    """ Configure sounddevice to use default audio
        output device at the given sampling rate.
    """
    sounddevice.default.samplerate = Config.samplingFrequency
    sounddevice.default.device = sounddevice.query_devices()[1]["name"]


def normalize(signal):
    """ Normalize signal to the <-1; 1> range.
    """
    total = max(signal)
    return [
        2 * x / total - 1
        for x in signal
    ]


def generate_spectral_signal(frequencies, cycles):
    """ Generate normalized sum of all given frequencies.
    """
    X = [
        generate_signal(freq, cycles)
        for freq in frequencies
    ]
    return normalize([sum(s) for s in zip(*X)])


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


def compute_spectrum(X):
    """ Compute normalized frequency spectrum.
    """
    FFT = numpy.abs(numpy.fft.fft(X)) / len(X)
    FFT = FFT[range(int(len(X) / 2))]

    freq = numpy.fft.fftfreq(len(X), 1.0/Config.samplingFrequency)
    freq = freq[range(int(len(X) / 2))]

    return freq, FFT



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

