#!/usr/bin/python3


#import urllib.request
import requests
import json

SPACEXURI= "http://api.spacexdata.com/v3/cores"

def main():
    
    #Get data from URL
    coreData = requests.get(SPACEXURL)
   #coreData = urllib.request.urlopen(SPACEXURI)
    xString = coreData.read().decode()
    print(type(xString))

    #Convert
    listOfCores = json.loads(xString)
    print(type(listOfCores))

    #Looping through the data and extract data I need
    for core in listOfCores:

        #Temporary store data
        coreSerial =  core.get("core_serial")
        originalLaunch = core.get("original_launch")
        missions = core.get("missions")
        
        #Print out data
        print(coreSerial, end = " : ")
        print(originalLaunch)
    
        for mis in missions:
            print("[", end="")
            print("Mission name # " + mis.get("name"), end=' : ')
            print("Flight # "+ str(mis.get("flight")), end='')
            print("]")
         
        print("\n")

if __name__ == "__main__":
    main()
