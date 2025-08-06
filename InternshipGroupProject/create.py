#!/usr/bin/python
import sqlite3


class Tables:
    def __init__(self, db):
        self.cur = None

        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.execute('''CREATE TABLE STUDENT
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            EMAIL          CHAR(30)     NOT NULL,
            PASSWORD       CHAR(12) NOT NULL,
            ADDRESS        CHAR(50),
            PHONE_NUM      INT);''')

        self.conn.execute('''CREATE TABLE INTERNSHIP
            (INTERNSHIP_ID INT PRIMARY KEY     NOT NULL,
            INTERNSHIP_NAME           TEXT    NOT NULL,
            REMOTE        BOOL,
            SALARY         INT,
            START_DATE     DATE,
            END_DATE       DATE
            );''')

        self.conn.execute('''CREATE TABLE COMPANY
        (EMPLOYER_ID INT PRIMARY KEY NOT NULL,
        EMPLOYER_NAME TEXT,
        COMPANY_NAME TEXT,
        INTERNSHIP_ID INT NOT NULL
        
        ''')

        self.conn.execute(''' CREATE TABLE ADMIN
            (ADMIN_ID INT PRIMARY KEY NOT NULL,
            ADMIN_NAME TEXT,
            COMPANY_EXT INT,
            COMPANY_LOCATION CHAR (50));''')

        print("Table created successfully")
        self.conn.commit()
        self.conn.close()
