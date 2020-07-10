#!/usr/bin/env python3

import sqlite3

# Following command will create db if t does not exist
# Otherwise, it will open
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Print out data
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3])

print("Operation done successfully")
conn.close()
