#!/usr/bin/python

import sqlite3
from sqlite3 import Connection


class Select:
    def __init__(self, db):

        self.cur = None

        self.conn = sqlite3.connect(db)
        print("Opened database successfully")

    def fetch(self, internship_name=''):
        self.cur.execute(
            "SELECT * FROM INTERNSHIP WHERE INTERNSHIP_NAME LIKE ?", ('%' + internship_name + '%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

        print("Operation done successfully")
        self.conn.close()
