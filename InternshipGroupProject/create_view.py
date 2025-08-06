#!/usr/bin/python
import sqlite3


class Views:

    def __init__(self, db ):
        self.cur = None

        self.conn = sqlite3.connect(db)
        self.conn = sqlite3.connect('internship.db')

        self.conn.execute('''
        CREATE VIEW student_view as 
        SELECT * FROM INTERNSHIP ''')

        print(self.conn.execute("SELECT * FROM student_view").fetchall())
        self.conn.close()
