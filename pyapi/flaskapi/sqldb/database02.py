#!/usr/bin/env python3

import sqlite3

# Following command will create db if t does not exist
# Otherwise, it will open
conn = sqlite3.connect('test.db')
print("Opened database successfully")


# Create a table
conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE TEXT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')

print("Table created successfully")
conn.close()
