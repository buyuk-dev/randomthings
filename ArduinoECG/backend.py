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
import sqlite3
import pickle
from datetime import datetime


def getConnection(filename):
    """ Return sqlite db connection object.
    """
    if not os.path.isfile(filename):
        raise Exception(f"Database {filename} not found")
    return sqlite3.connect(filename)


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
    record = (datetime.now().isoformat(timespec="seconds"), pickle.dumps(data))
    connection.cursor().execute(
        "insert into ecg values (?, ?)", record
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


def getRecordByTimestamp(connection, timestamp):
    cursor = connection.cursor()
    cursor.execute(
        "select * from ecg where time like ?%",
        (timestamp.isoformat(timespec="seconds"),)
    )
    return cursor.fetchone()
