#!/usr/bin/python

import sqlite3


class Delete:
    def __init__(self, db):
        self.cur = None
        self.conn = sqlite3.connect(db)

    def remove(self, internship_id):
        self.conn.execute("DELETE from COMPANY where ID = ?;", (internship_id,))
        self.conn.commit()
        print("Total number of rows deleted :", self.conn.total_changes)

        print("Operation done successfully")
        self.conn.close()


def db():
   return None