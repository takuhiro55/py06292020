import sqlite3

# Open the database
conn = sqlite3.connect('issdata.db')
print("Opened database successfully")

# Print out the database info
cursor = conn.execute("SELECT id, longitude, latitude, timestamp from ISS2")
for row in cursor:
    print("ID = ", row[0])
    print("LONGITUDE = ", row[1])
    print("LATITUDE = ", row[2])
    print("TIMESTMP = ", row[3], "\n")

print("Operation done successfully")

# Close the database
conn.close()
