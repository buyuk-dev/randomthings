#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import backend


ARDUINO_INT_BYTES = 2
ARDUINO_BYTE_ORDER = "little"


def draw(_, data, subplot, config):
    """ Read data from serial port and redraw graph.
    """
    data.extend(
        [
            int.from_bytes(
                config.port.read(ARDUINO_INT_BYTES),
                byteorder=ARDUINO_BYTE_ORDER,
                signed=True,
            )
            for _ in range(config.nsamples)
        ]
    )
    subplot.clear()
    subplot.plot(data[-config.window :])
    plt.title("{} sec".format(datetime.now()))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--window", type=int, default=1600, help="plot width in samples"
    )
    parser.add_argument(
        "--nsamples", type=int, default=80, help="numbder of reads per frame"
    )
    parser.add_argument(
        "--refresh", type=int, default=80, help="frame duration in milliseconds"
    )
    parser.add_argument(
        "--port",
        choices=["usb", "bluetooth"],
        default="usb",
        help="default serial port",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="save recording to database on exit"
    )
    args = parser.parse_args()

    args.port = serial.Serial(
        *(
            {
                "bluetooth": ("/dev/tty.HC-05-DevB", 9600),
                "usb": ("/dev/tty.usbmodem14201", 9600),
            }[args.port]
        )
    )

    figure = plt.figure()
    subplot = figure.add_subplot(1, 1, 1)
    data = [0] * args.window
    ani = animation.FuncAnimation(
        figure, draw, fargs=(data, subplot, args), interval=args.refresh
    )
    plt.show()

    if args.save:
        connection = sqlite3.connect("ecg.db")
        backend.writeRecord(connection, data)
        connection.close()
