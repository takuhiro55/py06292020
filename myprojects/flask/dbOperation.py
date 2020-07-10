#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:16:57 2020

@author: TSuganuma

This program is experimental.
This program allows you to do database operations with URL. Use sqlite3 and flask.
This program supports the following functionality
- Create a database
- Delete a database
- Create a table
- Insert data into a table
- Updata data in a table
- Delete data in a table


Standard steps to setup a database and a table

1. Create a database 'test' : 'curl http://0.0.0.0:2224/create/db/test'
2. Define a table 'COMPANY' -> register properties of data

    # Example
    # If you would like to form a data with ID, NAME, AGE, ADDRESS, SALARY
    # You need to give commands as below
    # curl http://0.0.0.0:2224/define/test/COMPANY/ID+INT+PRIMARY_KEY+NOT_NULL
    # curl http://0.0.0.0:2224/define/test/COMPANY/NAME+TEXT+NOT_NULL
    # curl http://0.0.0.0:2224/define/test/COMPANY/AGE+TEXT+NOT_NULL
    # curl http://0.0.0.0:2224/define/test/COMPANY/ADDRESS+CHAR(50)
    # curl http://0.0.0.0:2224/define/test/COMPANY/SALARY+REAL

3. Create a table : 'curl http://0.0.0.0:2224/establish/test/COMPANY'
4. Clear a variable used for setting the table : 'curl http://0.0.0.0:2224/define/setting/clear'
5. Insert data : 'curl http://0.0.0.0:2224/insert/test/COMPANY/1+Allen+32+California+2000.00'
-  Display data in the table : 'curl http://0.0.0.0:2224/list/test/COMPANY'
-  Modify data in the table : 'curl http://0.0.0.0:2224/update/test/COMPANY/1/SALARY/30000.0'
    -> Change SALARY of ID = 1 to 30000.0
-  Delete data in the table : 'curl http://0.0.0.0:2224/delete/data/test/COMPANY/2'
    -> Deleting ID = 2
-  Display the setting of a table : curl http://0.0.0.0:2224/list/setting/test/COMPANY
-  Delete a database : curl http://0.0.0.0:2224/delete/db/test
"""

#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
import requests
import sqlite3
import os
import json

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

#mainTableSetting = {'ID': ['INT', 'PRIMARY KEY', 'NOT NULL'], 'NAME': ['TEXT', 'NOT NULL'], 'AGE': ['TEXT', 'NOT NULL'], 'ADDRESS': ['CHAR(50)'], 'SALARY': ['REAL']}
mainTableSetting = {}

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/iss")
def hello_iss():
    ### This is a test of Flask : Nothing to do with sqlite3 ###
    
    # Get ISS data and return the data of longitude and latitude
    JSON_WEB_LINK = 'http://api.open-notify.org/iss-now.json'
    
    response = requests.get(JSON_WEB_LINK)
    responseData = response.json()
    datalist = '[longitude:'+ str(responseData['iss_position']['longitude'])
    datalist += ', latitude:'+ str(responseData['iss_position']['latitude'] +"]")
   
    return str(datalist)

@app.route("/")
def availableFunc():
    
    ### This function is to show the available functionality of sqlite ###
    
    dictFunct = {}
    dictFunct["Create DB"] = '/create/db/<dbname>'
    dictFunct["Delete DB"] = '/delete/db/<dbname>'
    dictFunct["Define table"] = '/define/<dbname>/<tablename>/<tablesetting>'
    dictFunct["Display setting 'define table'"] = "/define/setting/display"
    dictFunct["Clear setting 'define table'"] = "/define/setting/clear"
    dictFunct["Create table"] = '/establish/<dbname>/<tablename>'
    dictFunct["Delete data"] = "/delete/data/<dbname>/<tablename>/<primaryKeyValue>"
    dictFunct["Insert data"] = "/insert/<dbname>/<tablename>/<dataInsert>" 
    dictFunct["Update data"] = "/update/<dbname>/<tablename>/<primaryKeyValue>/<dataName>/<value>"
    dictFunct["Display data in table"] = " /list/<dbname>/<tablename>"
    dictFunct["Display table setting"] = " /list/setting/<dbname>/<tablename>"
    
    return json.dumps(dictFunct, indent = 4)

@app.route("/create/db/<dbname>")
def create_db(dbname):

    #### This function is to create a DB ####
    
    # To access this functionality,
    # -> e.g. 'curl http://0.0.0.0:2224/create/db/test'
    
    conn = sqlite3.connect(dbname + '.db')
    conn.close()
    return dbname + '.db was created successfully'

@app.route("/delete/db/<dbname>")
def delete_db(dbname):
    
    #### This function is to delete a DB ####
   
    # To access this functionality,
    # -> e.g. curl http://0.0.0.0:2224/delete/db/test
    
    os.remove(dbname + ".db")
    return dbname + '.db was deleted successfully'

  

@app.route("/define/<dbname>/<tablename>/<tablesetting>")
def defineTable(dbname, tablename, tablesetting):
    
    #### This function is to define the setting of table ####
    
    # The setting is stored as a JSON file
    # To access to this functionarity,
    # -> e.g. curl http://0.0.0.0:2224/define/test/COMPANY/NAME+TEXT+NOT_NULL
    
    # Example
    # If you would like to form a data with ID, NAME, AGE, ADDRESS, SALARY
    # You need to give commands as below
    # curl http://0.0.0.0:2224/define/test/COMPANY/ID+INT+PRIMARY_KEY+NOT_NULL
    # curl http://0.0.0.0:2224/define/test/COMPANY/NAME+TEXT+NOT_NULL
    # curl http://0.0.0.0:2224/define/test/COMPANY/AGE+TEXT+NOT_NULL
    # curl http://0.0.0.0:2224/define/test/COMPANY/ADDRESS+CHAR(50)
    # curl http://0.0.0.0:2224/define/test/COMPANY/SALARY+REAL
    
    
    # More details about 'tablesetting'
    # Input table setting with + and _ e.g.NAME+TEXT+NOT_NULL
    # -> Order has to be in the following way:
    # 1. Data name (e.g. NAME)
    # 2. Data type (e.g. TEXT, CHAR(50), REAL, INT)
    # 3. (Optional) if null is allowed (e.g. NOT_NULL)
    #First data info you are typing in has to be PRIMARY KEY data info 
    
    
    #### Create a dictionary for 1 data ####
    tablesettingParts = tablesetting.split('+')
    
    entrysettingItem = [] # Initialize a list 
    getFirstItem = False # This flag is used to get a first item in the <tablesettingParts> -> This is going to be a key
    
    # Create a list -> register it in dictionary
    for item in tablesettingParts:
        item = item.replace("_", " ")
        if getFirstItem == False:
            getFirstItem = True
            dataEntryName = item
        else:
            entrysettingItem.append(item)
    
    # Register the list just created to the main dictionary
    # mainTableSetting is a global dictionary variable
    mainTableSetting[dataEntryName] = entrysettingItem
    
    #### The setting is written to a JSON file ####
    
    # create a file name
    fileName = dbname + "_" + tablename
    
    # Writing a JSON file
    jsonObj = json.dumps(mainTableSetting, indent = 4)
    with open(fileName + ".json", "w") as file:
        file.write(jsonObj)
    
    return "success"

@app.route('/define/setting/display')
def define_setting__display():
    
    #### This function is to display 'mainTableSetting' ####
    # -> 'mainTableSetting' is a setting file created by defineTable() and use it in establish_table()
    
    return str(mainTableSetting)

@app.route('/define/setting/clear')
def define_setting__clear():
    
    #### This function is to empty 'mainTableSetting' ####
    # -> 'mainTableSetting' is a setting file created by defineTable() and use it in establish_table()
    
    mainTableSetting.clear()
    return "'mainTableSetting' is empty" 

@app.route("/establish/<dbname>/<tablename>")
def establish_table(dbname, tablename):
    
    #### This function is to establish the table ####
    
    # Setting of the table is taken from a json file created by defineTable()
    # To access to this functionality,
    # -> e.g. curl http://0.0.0.0:2224/establish/test/COMPANY
    
    tableName = tablename
    dbName = dbname + ".db"
    
    #### Create a string command ####
    # e.g. CREATE TABLE cars(ID INT PRIMARY KEY NOT NULL,BRAND TEXT NOT NULL,MODEL TEXT NOT NULL,PLACE TEXT NOT NULL,PRICE REAL)
    countKeys = 0 # initialize a variable
    totalKeys = len(mainTableSetting) # get the total number of keys
    settingString = "CREATE TABLE "+tableName+"(" # initialize a String variable
    
    # Read table setting from a dictionary "mainTableSetting"
    # Create a string command
    for item in mainTableSetting:
        key = item
        settingString += key
        settingString += " "
        
        countValues = 0 
        totalValues = len(mainTableSetting[key])
        
        for value in mainTableSetting[key]:

            settingString += value
            if countValues < totalValues - 1:
                settingString += " "
            countValues += 1
        countKeys += 1
        
        if countKeys < totalKeys:
            settingString += ","
    settingString += ")"
    print(settingString)
    
    #### Open the database ####
    conn = sqlite3.connect(dbName)
    conn.execute(settingString)
    
    #### Close the database ####
    conn.close()
    
    return f"Table '{tableName}' was created successfully"


@app.route("/delete/data/<dbname>/<tablename>/<primaryKeyValue>")
def deleteData(dbname, tablename, primaryKeyValue):
    
    #### This function is to delete an entry ####
    
    # To access to this function
    # -> e.g. curl http://0.0.0.0:2224/delete/data/test/COMPANY/2
    
    #### Open the file and convert JSON to dict ####
    # Generate file name from dbname and tablename
    filename = dbname + "_" + tablename
    
    # Open the table setting file stored in the directory
    with open(filename + ".json", "r") as jsonFileData:
        tableSetting = json.load(jsonFileData)
    
    #### Get the primary key ####
    # Assumption : Primary key is the first key in tableSetting
    for key in tableSetting:
        primaryKey = key
        primaryKeyDataType = tableSetting[key][0] # first value of the key is datatype
        if primaryKeyDataType == 'TEXT' or primaryKeyDataType.startswith('CHAR'):
           primaryKeyValue = f"\'{primaryKeyValue}\'" 
        break;
    
    #### Create a string command ####
    stringCommand = "DELETE from " + tablename + " where "
    stringCommand += primaryKey +" = "+ primaryKeyValue
    #print(stringCommand)
    
    #### Open the database ####
    conn = sqlite3.connect(dbname + ".db")
    conn.execute(stringCommand)
    
    #### Commit the change to the database ####
    conn.commit()
    
    #### Close the database ####
    conn.close()
    
    return "success"

@app.route("/insert/<dbname>/<tablename>/<dataInsert>")
def insertData(dbname, tablename, dataInsert):
    
    #### This function is to insert data ####
    
    # To access to this function
    # -> e.g. curl http://0.0.0.0:2224/insert/test/COMPANY/1+Allen+32+California+2000.00
    
    # <dataInsert> : Order is how you define a table
    # e.g. table COMPANY is defined as ID,NAME,AGE,ADDRESS,SALARY -> 1+Allen+32+California+2000.00 
    
    
    #### Open the file and convert JSON to dict ####
    # Generate file name from dbname and tablename
    filename = dbname + "_" + tablename
    
    # Open the file and convert JSON to dict
    with open(filename + ".json", "r") as jsonFileData:
        tableSetting = json.load(jsonFileData)
    
    
    #### Create a string command ####
    #Analyze dataInsert e.g. 1+Allen+32+California+2000.00
    datalist= []
    datalist = dataInsert.split("+")
    
    # Generate string from keys
    numKeys = len(tableSetting)
    keyCount = 0
    keyDataTypeList = []
    keysString = "INSERT INTO " + tablename + " ("
    for key in tableSetting:
        keyDataTypeList.append(tableSetting[key][0])
        keysString += key
        if keyCount < numKeys - 1:
            keysString += ", "
        keyCount += 1
    keysString += ") VALUES"
    
    # Generate a string command from <dataInsert>
    keyCount = 0
    dataString = "("
    while keyCount < numKeys:
        if keyDataTypeList[keyCount] == 'TEXT' or keyDataTypeList[keyCount].startswith('CHAR'):
            dataString += f"\'{datalist[keyCount]}\'"
        else:
            dataString += datalist[keyCount]
        if keyCount < numKeys - 1:
            dataString += ","
        keyCount += 1
    dataString += ")"
    
    # Combine string commands
    keysString += dataString
    print(keysString)
    
    #### Open the database ####
    conn = sqlite3.connect(dbname + ".db")
    conn.execute(keysString)
    
    #### Commit the change to the database ####
    conn.commit()
    
    #### Close the database ####
    conn.close()
    
    return "successful"

@app.route("/update/<dbname>/<tablename>/<primaryKeyValue>/<dataName>/<value>")
def updateData(dbname, tablename, primaryKeyValue, dataName, value):
    
    #### This function is to update data ####
    
    # Access to this functionarity by 
    # -> e.g. curl http://0.0.0.0:2224/update/test/COMPANY/1/SALARY/30000.0
    
    #### Open the file and convert JSON to dict ####
    # Generate file name from dbname and tablename
    filename = dbname + "_" + tablename
    
    # Open the table setting file stored in the directory
    with open(filename + ".json", "r") as jsonFileData:
        tableSetting = json.load(jsonFileData)
    
    #### Get the primary key ####
    # Assumption : Primary key is the first key in tableSetting
    for key in tableSetting:
        primaryKey = key
        primaryKeyDataType = tableSetting[key][0] # first value of the key is datatype
        if primaryKeyDataType == 'TEXT' or primaryKeyDataType.startswith('CHAR'):
           primaryKeyValue = f"\'{primaryKeyValue}\'" 
        break;
    
    #### Get the datatype of dataName specified ####
    for key in tableSetting:
        if dataName == key:
            dataNameDataType = tableSetting[key][0] # first value of the key is datatype
            if dataNameDataType == 'TEXT' or dataNameDataType.startswith('CHAR'):
                value = f"\'{value}\'"
            break
        
    #### Create a command string ####
    # e.g. UPDATE COMPANY set SALARY = 30000.0 where ID = 1
    stringCommand = "UPDATE "+ tablename +" set "+ dataName + " = " + value 
    stringCommand += " where " + primaryKey + " = " + primaryKeyValue
    
    
    #### Open the database ####
    conn = sqlite3.connect(dbname + ".db")
    conn.execute(stringCommand)
    
    #### Commit the change to the database ####
    conn.commit()
    
    #### Close the database ####
    conn.close()
    
    return "success"


@app.route("/list/<dbname>/<tablename>")
def listData(dbname, tablename):
    
    #### This function is to listup data ####
    # It will return JSON file
    
    # Accessing this functionarity by
    # e.g. curl http://0.0.0.0:2224/list/test/COMPANY
    
    #### Open the file and convert JSON to dict ####
    # Generate file name from dbname and tablename
    filename = dbname + "_" + tablename
    
    # Open the table setting file stored in the directory
    with open(filename + ".json", "r") as jsonFileData:
        tableSetting = json.load(jsonFileData)
    
    
    #### Generate a command string for getting data from the table specified ###
    # The command example : SELECT ID, NAME, AGE, ADDRESS, SALARY from COMPANY
    numKeys = len(tableSetting) # get the number of keys
    keyCount = 0 # initialize counter for keys
    keylist = [] # initialize a list for storing keys
    keysString = "SELECT " # initialize base string variable
    
    # Create a command string
    for key in tableSetting:
        keylist.append(key) # create a list for keys for later
        keysString += key
        if keyCount < numKeys - 1:
            keysString += ", "
        keyCount += 1
    keysString += " from " + tablename
    
    
    #### Open the database ####
    conn = sqlite3.connect(dbname + ".db")
    cursor = conn.execute(keysString)
    
    #### Get actual data from a table in the database ####
    # *** Assumption : first data of every dataset is primary ***
    # table data will be returned with JSON format -> Create a dictionary first
    dataDict = {} # initialize main dictionary for storing data read from the table
    for row in cursor:
        keyCount = 0 # initialize the counter
        dataDictElem = {} # initialize a dictionary for storing one set of data
        for dataName in keylist: # keylist is generated when a command was generated
            dataDictElem[dataName] = row[keyCount] # store data as key-value pair
            keyCount += 1
        dataDict[row[0]] = dataDictElem # primary key for every dataset is used as key for the dataset 
    
    #### Close the database ####
    conn.close()
    
    #### Return data with JSON format ####    
    return json.dumps(dataDict, indent = 4)


@app.route("/list/setting/<dbname>/<tablename>")
def listSetting(dbname, tablename):
    
    #### This function is to return the setting of a table as JSON ####
    # To access this functionarity,
    # -> e.g. curl http://0.0.0.0:2224/list/setting/test/COMPANY
    
    #### Open the file and convert JSON to dict ####
    # Generate file name from dbname and tablename
    filename = dbname + "_" + tablename
    
    # Open the file and convert JSON to dict
    with open(filename + ".json", "r") as jsonFileData:
        tableSetting = json.load(jsonFileData)
    
    #### return JSON data ####
    return json.dumps(tableSetting, indent = 4)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
    # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

