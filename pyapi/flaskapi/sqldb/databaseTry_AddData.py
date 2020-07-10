import requests
import sqlite3

# Get JSON data
JSON_WEB_LINK = 'http://api.open-notify.org/iss-now.json'
response = requests.get(JSON_WEB_LINK)
responseData = response.json()

# Get ID number for database
idNum = input("Type in ID number : ")

# Print out data - for checking purpose
print(responseData['iss_position']['longitude'])
print(responseData['iss_position']['latitude'])
print(responseData['timestamp'])

# Store data into variables
longitude = responseData['iss_position']['longitude']
latitude = responseData['iss_position']['latitude']
timestamp = responseData['timestamp']

# Open the database
conn = sqlite3.connect('issdata.db')
print('Opened database successfully')

# Store the value of variables
conn.execute("INSERT INTO ISS2 (ID,LONGITUDE,LATITUDE,TIMESTAMP)VALUES (?,?,?,?)", (idNum, longitude, latitude, timestamp))

conn.commit()
print("Records created successfully")

# Close the database
conn.close()
