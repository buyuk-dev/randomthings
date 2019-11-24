#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DB structure:
-------------

1. ECG DATA TABLE:

   ROWID  |  TIME       |  DATA
   ----------------------------
   INT    |  DATETIME   |  BLOB (pickle)

"""

import os
import argparse
import sqlite3
import pickle
from datetime import datetime


def setupNewDatabase(filename):
    """ Create database file and setup table.
    """
    connection = sqlite3.connect(filename)
    connection.cursor().execute(
        """
        create table ecg
        (
            time TEXT,
            data BLOB
        )
    """
    )
    connection.commit()


def writeRecord(connection, data):
    """ Insert data record with timestamp to ecg table.
    """
    connection.cursor().execute(
        "insert into ecg values (?, ?)", (str(datetime.now()), pickle.dumps(data))
    )
    connection.commit()


def listRecords(connection):
    """ Return timestamps of all records
    """
    cursor = connection.cursor()
    cursor.execute("select time from ecg")
    return cursor.fetchall()


def getRecordById(connection, rowid):
    """ Return n-th record from the ecg table.
    """
    cursor = connection.cursor()
    cursor.execute("select time, data from ecg where rowid=?", (rowid,))
    return cursor.fetchone()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="ecg.db", help="sqlite database file")
    parser.add_argument("--list", action="store_true", help="list db entries")
    parser.add_argument("--add", action="store_true", help="insert random record")
    parser.add_argument("--select", type=int, help="print data for id")
    args = parser.parse_args()
    if not os.path.isfile(args.db):
        setupNewDatabase(args.db)
