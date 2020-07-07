#!/usr/bin/env python3

"""
PART A Pull timestamp of now (format is up to you)
PART B Pull the IP address of your current system
PART C Read in a list of servers from a file called, myservers.txt (you'll need to make this)
PART D format the data in the following manner: {"json": "time: <<PART A>>, ip: <<PARTB>>, mysvrs: [ <<PARTC>> ]"}
PART E Validate your JSON with a POST
"""

import requests

TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com/"

def main():
    
    ## PART A
    print("\nPART A")
    resp = requests.get(TIMEURL)
    mytime = resp.json()
    print("Raw data # " + str(mytime))
    mytime = mytime["time"].replace(" ","").replace(":", "-")
    print("Get time from the raw data and replace(' ','').replace(':', '-') # " + mytime)

    ## PART B
    print("\nPART B")
    resp = requests.get(IPURL)
    myip = resp.json()
    print("myip # "+ str(myip))
    myip = myip["ip"]
    print("myip['ip'] # " + str(myip))

    ## PART C
    print("\nPART C")
    with open("myservers.txt") as myfile:
        mysvrs = myfile.readlines()
    print(mysvrs)

    ## PART D
    print("\nPART D")
    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs
    print("jsonToTest # "+ str(jsonToTest))

    mydata = {}
    mydata["json"] = str(jsonToTest)
    print("mydata # " + str(mydata))


    # PART E
    print("\nPART E")
    # -> POST
    resp = requests.post(VALIDURL, data=mydata)
    respjson = resp.json()
    print(respjson)
    print(f"Is your JSON valid? {respjson['validate']}")

main()
