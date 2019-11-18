#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


WINDOW = 3000
NSAMPLES = 200
REFRESH = 100


port = serial.Serial("/dev/tty.usbmodem14201", 9600)
figure = plt.figure()
subplot = figure.add_subplot(1, 1, 1)
data = [0] * WINDOW


def draw(i, data):
    data.extend([
        int.from_bytes(port.read(), byteorder='big')
        for i in range(NSAMPLES)
    ])
    subplot.clear()
    subplot.plot(data[-WINDOW:])


if __name__ == '__main__':
    ani = animation.FuncAnimation(figure, draw, fargs=(data,), interval=REFRESH)
    plt.show()
