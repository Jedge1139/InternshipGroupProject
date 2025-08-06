#!/usr/bin/python

import sqlite3


class Update:
    def __init__(self, db):
        self.cur = None

        self.conn = sqlite3.connect(db)

        print("Opened database successfully")

    def update(self, internship_id, internship_name, company, salary):
        self.cur.execute("UPDATE INTERNSHIP SET internship name = ?, company = ?, salary = ? WHERE ID = ?",
                         (internship_id, internship_name, company, salary))
        self.conn.commit()
        print("Total number of rows updated :", self.conn.total_changes)

        cursor = self.conn.execute("SELECT id, internship_name, company, salary from INTERNSHIP")
        for row in cursor:
            print("INTERNSHIP_ID = ", row[0])
            print("INTERNSHIP_NAME = ", row[1])
            print("COMPANY = ", row[2])
            print("SALARY = ", row[3], "\n")

        print("Operation done successfully")
        self.conn.close()


def db():
    return None