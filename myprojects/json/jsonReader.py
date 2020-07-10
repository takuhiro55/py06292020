#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:39:10 2020

@author: TSuganuma

This is experimental
This program displays the flatterned JSON data
Motivation : I would like to extract JSON data without writing a program
"""

import json
import requests

## Operation choices
# 0: display 'Flatterned' local JSON data -> Store a file name with .json in FILE_NAME
# 1: display 'Flatterned' online JSON data -> Store a weblink (String) in 'JSON_WEB_LINK'
# 2: Paste Raw JSON data
OPERATION_CHOICE = 1 



## Examples of JSON_WEB_LINK
#https://cat-fact.herokuapp.com/facts
#https://api.spacexdata.com/v3/cores
#http://api.open-notify.org/iss-now.json
#https://www.anapioficeandfire.com/api
#https://www.anapioficeandfire.com/api/books
#https://www.anapioficeandfire.com/api/characters
#https://www.anapioficeandfire.com/api/houses

JSON_WEB_LINK = 'http://api.open-notify.org/iss-now.json'
#FILE_NAME = 'TestJsonImport.json'
FILE_NAME = 'WalmartSample.json'

class AnalyzingData:
    
    def __init__(self, data):
        
        # Check the data type         
        if type(data) == dict:
            self.processDict(data)
        elif type(data) == list:
            self.processList(data)
        
    
    # This is for processing dictionary data
    def processDict(self, dictItems):    
        
        # Separate keys and values
        keys = []
        values = []
        for item in dictItems:
            keys.append(item)
            values.append(dictItems[item])
        
        # Display keys
        print(keys)
        
        
        # Analyze the values
        for item in values:
            
            if type(item) == list:
                print(">> "+keys.pop(0), end= " -> ")
                self.processList(item)
                print()
            elif type(item) == dict:
                print(">> "+keys.pop(0), end= " -> ")
                self.processDict(item)
                print()
            elif type(item) == str or type(item) == int or type(item) == float or type(item) == bool or type(item) == type(None):
                print(">> "+keys.pop(0), end= " -> ")
                print(item)
                 #print()
            else:
                print(item)
            
    # This is for processing list data
    def processList(self, listItems):
        for item in listItems:
            if type(item) == dict:
                self.processDict(item)
                print()
            elif type(item) == str or type(item) == int or type(item) == float or type(item) == bool or type(item) == type(None):
                print(item)
                #print()
            else:
                print(item)
                


def main():
    
    if OPERATION_CHOICE == 0:
        with open(FILE_NAME, "r") as jsonFileData:
            data = json.load(jsonFileData)
        AnalyzingData(data)
    elif OPERATION_CHOICE == 1:
        response = requests.get(JSON_WEB_LINK)
        responseData = response.json()
        AnalyzingData(responseData)
    elif OPERATION_CHOICE ==2:
        data = input("Paste your JSON data : \n")
        data = json.loads(data)
        AnalyzingData(data)
    
main()
