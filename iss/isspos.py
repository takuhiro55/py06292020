#!/usr/bin/env python3
'''
'''

import requests
import threading

def main():
   
    #i = 0
    #while i<1000:
    #    i = i + 1
    for x in range(10):
        print(x)
        webData = requests.get('http://api.open-notify.org/iss-now.json')
        issdata = webData.json()
        longitude =float(issdata["iss_position"]["longitude"])
        latitude = float(issdata["iss_position"]["latitude"])
        
        print("[longitude:"+str(longitude) + ", latitude:"+str(latitude)+"]");
       # print(type(longitude)) 
        

        if x > 0:
            deltaLong = longitude - oldLongitude
            deltaLati = latitude - oldLatitude
            if deltaLong > 0.0 or deltaLati > 0.0:
                 print("delta=["+ str(deltaLong) + "," + str(deltaLati) + "]")


        oldLongitude = longitude
        oldLatitude = latitude

        i = 0
        while i<30000:
            i = i + 0.5


#    webData = requests.get('http://api.open-notify.org/iss-now.json')
#    for data in webData.json():
#        print(data) # this will display the KEYS in the data
        # print(webData.json()[data]) # this will display the VALUES in the data

    # it might be easier to manually pick out the data, rather than use a for loop
    # example...
#    issdata = webData.json()

#    print(issdata["iss_position"]) # from our dictionary, we want the value associated with the KEY iss_position
#    print(issdata["iss_position"]["latitude"])
#    longitude = issdata["iss_position"]["longitude"]
#    latitude = issdata["iss_position"]["latitude"]
#    print("[longitude:"+longitude + ", latitude:"+latitude+"]");

if __name__ == '__main__':
    main()

