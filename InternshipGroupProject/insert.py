#!/usr/bin/python

import sqlite3


class Insert:

    def __init__(self, db):
        self.cur = None

        self.conn = sqlite3.connect(db)
        print("Opened database successfully")

    def insert(self, internship_name, company, salary, internship_id):
        self.cur.execute("INSERT INTO INTERNSHIP (INTERNSHIP_ID,INTERNSHIP_NAME,COMPANY,ADDRESS, "
                         "PHONE_NUM, START_DATE, END_DATE) \
      VALUES (?, ?, ?, NULL)", (internship_name, company, salary, internship_id))

        self.conn.commit()

        print("Records created successfully")
        self.conn.close()
