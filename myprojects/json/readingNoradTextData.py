#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 08:39:25 2020

@author: TSuganuma

Create a dictionary/JSON from reading a data of txt with spaces stored in the web
"""

import urllib.request
import json

FILE_NAME = 'norad' # file name you want to have for saving this JSON data
NUM_SATELLITES = 20; # How many satellite data you want to extract


####### FIXED DATA #######
DATA_NUM_EACH_SATELLITE = 2; # How many lines of data each satellite has
ADDRESS = "http://www.celestrak.com/NORAD/elements/active.txt"
##########################

def main():
    
    # Initilize the variables
    count = 0
    numSatellite = 0;
    dataMain = {}
    
    # Get data from address
    file = urllib.request.urlopen(ADDRESS)
    
    # Extracting data
    for line in file:
        decoded_line = line.decode("utf-8")
        
        # Reset list
        satelliteNameParts = []
        
        # Get satellite name
        if count == 0:
            decoded_line = decoded_line.split(' ')
            countData = 0
            for data in decoded_line:
                if data != '':
                    satelliteNameParts.append(data)
                satelliteName = "".join(satelliteNameParts)
            
            
            #Reset dictionary
            dataDicElem = {}
        
        # Get satellite data
        if count != 0:
            dataset = []
            decoded_line = decoded_line.replace("\r\n", "")
            listData = decoded_line.split(' ')
            countData = 0 # this is used for eliminating data you want to store as value
            for data in listData:
                if countData == 0:
                    name = data # 'sub title' of the Satellite data
                    #print(name)
                else:
                    if (data != ''):
                        dataset.append(data)
                countData += 1
                
            #Register to sub dictionary
            dataDicElem[name] = dataset
        
            #Register to main dictionary
            dataMain[satelliteName.replace("\r\n", "")] = dataDicElem
        
        # Keep track of a number of data for each satellite
        count += 1
        
        # Counting a number of datapoint and satellite
        if count == DATA_NUM_EACH_SATELLITE + 1:
            if numSatellite >= NUM_SATELLITES - 1:
                break
            numSatellite += 1
            count = 0
        
    
    #print(dataMain)
    jsonObj = json.dumps(dataMain, indent = 4)
    print(jsonObj)
    
    # Write to a file
    with open(FILE_NAME + ".json", "w") as file:
        file.write(jsonObj)
    print("JSON obj was written to a file");
    

main()
