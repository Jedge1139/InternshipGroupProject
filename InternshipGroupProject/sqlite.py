#!/usr/bin/python

import sqlite3


def __init__(self, db):
    self.cur = None

    self.conn = sqlite3.connect(db)
