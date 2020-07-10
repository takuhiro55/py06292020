import sqlite3

conn = sqlite3.connect('issdata.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE ISS2
(ID INT PRIMARY KEY NOT NULL,
LONGITUDE REAL,
LATITUDE REAL,
TIMESTAMP INT);''')

print("Table created successfully")
conn.close()
