#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

WINDOW = 3000
NSAMPLES = 100
REFRESH = 100


#PORT = ("/dev/tty.HC-05-DevB", 9600)
PORT = ("/dev/tty.usbmodem14201", 9600)
port = serial.Serial(*PORT)


figure = plt.figure()
subplot = figure.add_subplot(1, 1, 1)
data = [0] * WINDOW


def draw(i, data):
    data.extend([
        int.from_bytes(port.read(2), byteorder="little", signed=True)
        for i in range(NSAMPLES)
    ])
    subplot.clear()
    subplot.plot(data[-WINDOW:])


if __name__ == "__main__":
    ani = animation.FuncAnimation(figure, draw, fargs=(data,), interval=REFRESH)
    plt.show()
