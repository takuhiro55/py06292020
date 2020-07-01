#!/usr/bin/env python3
'''
'''

import json
import requests

# Setting for what data display [0: not display, 1: display]
# Please see the DATA_TITLE below for which is correspond to what
DATA_DISPLAY = [1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
#---------------------------------------------------------

DATA_TITLE = ["Country", "countryCode","region","regionName","city", "latitude", "longitude", "isp", "org", "as"]

ADR_BASE = 'http://ip-api.com/json/'

def main():
    
    # Create IP address
    address = input("Type IP address you want to look up: ")
    address = ADR_BASE + address

    response = requests.get(address)
    responseData = response.json()
   # print(responseData)
    status = responseData["status"]
    if status == "success":
        print("Success")
        dataProcess(responseData)
    else:
        print("Fail")

def dataProcess(responseData):

    country = responseData["country"]
    countryCode = responseData["countryCode"]
    region = responseData["region"]
    regionName = responseData["regionName"]
    city = responseData["city"]
    latitude = responseData["lat"]
    longitude = responseData['lon']
    isp = responseData["isp"]
    org = responseData["org"]
    aS = responseData["as"]

    dataArray = [country, countryCode, region, regionName, city, latitude, longitude, isp, org, aS]

    count = 0
    for displayChoice in DATA_DISPLAY: 
        if displayChoice == 1:
           # if count == 0:
           #     print("IP address: " + address)
            print("["+DATA_TITLE[count], end=":")
            print(str(dataArray[count])+"]")
        count += 1


if __name__ == "__main__":
    main()
