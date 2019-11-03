#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Audio sinusoidal waves generator.
    ---------------------------------
    Can be used to generate waves of the particular frequency,
    or sum of all frequencies for frequency response measurements. 

    Required sounddevice package can be installed using pip:
    
        pip install sounddevice
 
"""

import argparse
import math

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


def play(frequency, length):
    """ Generate signal and play it. This function
        blocks until the entire signal is played.
        Can be stopped by <Ctrl + C> signal.
    """
    signal = generate_signal(frequency, length)
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
