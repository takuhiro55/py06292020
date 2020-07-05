#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:31:44 2020

@author: TSuganuma


Purpose of this program is to create a JSON file by typing keys and values
Program flow:
        1. Type in a list of keys
        2. Type in values for each key
            you have 2 options
                - Option1 : single value
                - Option2 : a list of values
        3. System will ask you if you want to type another set of values with the same keys
            Answer "y" for yes and "n" for no
                -> "y" : repeat the process 2 and 3
        4. System will ask you name the data set
        5. System will ask you if you want to create another data set
            Answer "y" for yes and "n" for no
                -> "y" : repeat the process from 1 to 5
        6. System will ask you if you want to display the json
            Answer "y" : displaying the JSON
            Answer "n" : not displaying
        7. System will ask you if you want to write the json to a file
            Answer "y" : write the JSON to a file
                -> Type in a file name (.json will be added automatically)

"""

import json
NUM_INDENT_JSON = 4 # How many indents you want to have for formatting JSON 

# Class for pairing keys and values
# Set a list of keys in constructor and pair them up with a list of values by calling "assignValue(values)"
# Return value for "assignValue()" is dictionary
class PairingKeyValue:
    
    def __init__(self, keyList):
        self.keyList = keyList
        
    def printKeyList(self):
        for key in self.keyList:
            print(key)
            
    def assignValue(self, value):
        thisdict = {}
        count = 0;
        for key in self.keyList:
            thisdict[key] = value[count]
            count += 1
        return thisdict

# Class for converting a list to a dictionary
# Set a list in the constructor and set the name for the list
# To get the dictionary, execute "getDictionary()"
class ConvertingtListToDict:
                
    def __init__(self, listElem, listName):
        dictionary = {}
        dictionary[listName]= listElem;
        self.listElem = listElem
        self.dictionary = dictionary

    def getDictionary(self):
        return self.dictionary
    
    def getList(self):
        return self.listElem
        

# Class for joining dictionaries
# Appending dictionary by calling appendDict(dictAppend)
class JoinDictionary:
    
    def __init__(self):
        dictionary = {}
        self.dictionary = dictionary
    
    def appendDict(self, dictAppend):
        
        # Separate key and value
        for item in dictAppend:
            key = item;
            value = dictAppend.get(key)
            self.dictionary[key] = value
    
    #Write a function to create a deeper than single layer
    
    def getDictionary(self):
        return self.dictionary

# Class for converting dictionary to JSON
class ConvertingDictJson:
    
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.jsonObj = json.dumps(dictionary, indent = NUM_INDENT_JSON)
        
    def getJsonObj(self):
        return self.jsonObj
    
    def writeJsonObj(self, fileName):
        if type(fileName) == str and len(fileName) > 0:
            with open(fileName + ".json", "w") as file:
                file.write(self.jsonObj)
                print("JSON obj was written to a file");


def askToTypeinKeys():
    keys = input(">> Please type in keys, put \" \" between keys : ")
    keyList = keys.split(" ")
    return keyList;


# Function for getting values and pairing them up with keys, then convert it to dictionary and append
def createDictionarySet(keyList, dictionarySet):
    
    dictList = []
    while True:
        dictList = askValuesAndPairUpWithKeys(keyList, dictList) 
        print(dictList)
        choice = input(">> Would you like to input another set of values with the same keys? (y/n) : ")
        if choice == "n":
            break;
    nameDict = input(">> Please name the data set : ")
    dictElem = ConvertingtListToDict(dictList, nameDict) # Creating dictionary by pairing the name and a list
    dictionarySet.appendDict(dictElem.getDictionary())  # Append the dictionary
    return dictionarySet


# Sub-function of createDictionarySet()
# Ask a user to type in values
# For future development, adding one more option for specifying saved dictionary and use this as a value
def askValuesAndPairUpWithKeys(keyList, dictList):
    valueList = []
    for item in keyList:
        
        while True:
            valueType = input(f">> Is the value of key \"{item}\", single or a list? [0: single, 1: list] : ")
            if not(valueType == "0" or valueType == "1"):
                print(f"Choice {valueType} is invalid.")
            else:
                break;
        
        if valueType == "0":
            value = input(">>>> Type the value : ")
            valueList.append(value)
        else:
            valueListElem = []
            count = 0
            print("Type the values. To finish typing, enter \"#x\"")
            while True:
                count += 1
                value = input(f">>>> ValueList - value{count} : ")
                if value != "#x":
                    valueListElem.append(value)
                else:
                    break
            valueList.append(valueListElem)
        print(valueList)
        
    # Pairing a list of keys and a list of values
    keyValuePairList = PairingKeyValue(keyList) # instantiate by setting a list of keys
    dictList.append(keyValuePairList.assignValue(valueList)) # create a dictionary by pairing keys and values
    return dictList


    
def main():
    
    
    # Instantiate class for joining dictionary together
    dictionarySet = JoinDictionary()
    
    
    # Getting keylist and values and pair them up
    while True:
        
        #ask user type in keys
        keyList = askToTypeinKeys()
        print(keyList)
        
        #Create a dictionary by inputting values for keys
        dictionarySet = createDictionarySet(keyList, dictionarySet)
        choice = input(">> Would you like to create another data set? (y/n) : ")
        if choice == "n": 
            break;
    
    # Creating JSON
    jsonData = ConvertingDictJson(dictionarySet.getDictionary()); # Instantiate by setting dictionary appended
    print("Congraturation! You just created a json.")
    choice = input(">> Would you like to see the json? (y/n) : ")
    if choice == "y":
        print(jsonData.getJsonObj())
        
    choice = input(">> Would you like to save this json to a file? (y/n) : ")
    if choice == "y":
        nameFile = input(">> Type in the file name (\".json\" is added automatically) : ")
        jsonData.writeJsonObj(nameFile) # Writing JSON to a file
    

main()
