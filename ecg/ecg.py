#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pickle

from datetime import datetime
from pprint import pprint
from collections import namedtuple

import serial
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

import backend


ArduinoConfig = namedtuple("ArduinoConfig", ["int_size", "byte_order"])
config = ArduinoConfig(2, "little")
serial_ports = {
    "bluetooth": ("/dev/tty.HC-05-DevB", 9600),
    "usb": ("/dev/tty.usbmodem14201", 9600),
}


def draw(_, data, subplot, config):
    """ Read data from serial port and redraw graph.
    """
    data.extend(
        [
            int.from_bytes(
                config.port.read(config.int_size),
                byteorder=config.byte_order,
                signed=True,
            )
            for _ in range(config.nsamples)
        ]
    )
    subplot.clear()
    subplot.plot(data[-config.window :])
    pyplot.title("{} sec".format(datetime.now()))


def record_command(args):
    """ Handle record subcommand.
    """
    args.port = serial.Serial(*(serial_ports[args.port]))
    figure = pyplot.figure()
    subplot = figure.add_subplot(1, 1, 1)
    data = [0] * args.window
    ani = animation.FuncAnimation(
        figure, draw, fargs=(data, subplot, args), interval=args.refresh
    )
    pyplot.show()

    if args.save:
        connection = backend.getConnection("ecg.db")
        backend.writeRecord(connection, data)
        connection.close()


def db_command(args):
    """ Handle db subcommands.
    """
    if args.list:
        connection = backend.getConnection(args.db)
        records = backend.listRecords(connection)
        pprint(records)

    elif args.load is not None:
        connection = backend.getConnection(args.db)
        record = backend.getRecordById(connection, args.load)
        pyplot.plot(pickle.loads(record[-1]))
        pyplot.show()

    elif args.init:
        backend.setupNewDatabase(args.db)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--db",
        default="ecg.db",
        help="database filename",
    )
    commands_parsers = parser.add_subparsers()

    # Recording Arguments Parser
    parser_record = commands_parsers.add_parser("record")
    parser_record.set_defaults(func=record_command)
    parser_record.add_argument(
        "--window", type=int, default=1600, help="plot width in samples"
    )
    parser_record.add_argument(
        "--nsamples", type=int, default=80, help="numbder of reads per frame"
    )
    parser_record.add_argument(
        "--refresh", type=int, default=80, help="frame duration in milliseconds"
    )
    parser_record.add_argument(
        "--port",
        choices=["usb", "bluetooth"],
        default="usb",
        help="default serial port",
    )
    parser_record.add_argument(
        "--save",
        action="store_true",
        help="save recording to database on exit"
    )

    # DB Access Arguments Parser
    parser_db = commands_parsers.add_parser("db")
    parser_db.set_defaults(func=db_command)
    parser_db.add_argument(
        "--list",
        action="store_true",
        help="list all records stored in the db"
    )
    parser_db.add_argument(
        "--load",
        type=int,
        help="load ecg data from db"
    )
    parser_db.add_argument(
        "--init",
        action="store_true",
        help="initialize empty db file"
    )

    args = parser.parse_args()
    args.func(args)
