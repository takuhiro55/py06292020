#!/usr/bin/env python3

import requests

## Define NEOW URL
#NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"
MARS = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000"

def main():
    with open("/home/student/nasa/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()

    #remove any newline characters from the api
    nasacreds = "api_key=" + nasacreds.strip("\n")

    #update the date below
    #startdate = "start_date=2019-11-11"

    solParam = "none"
    cameraParam = "all"
    pageParam ="1"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=2019-12-11"

    #  make a request with the request library
    marsrequest = requests.get(MARS +"&page="+pageParam+"&"+nasacreds)

    # Strip off json attachment from our response
    neodata = marsrequest.json()

    data = neodata["photos"]
    for element in data:
        print(element["id"], end=":")
        print(element["sol"], end=":")
        print(element["earth_date"], end=":")
        print(element["rover"]["name"])

    ## display NASAs NEOS data
    #print(data)

if __name__ == "__main__":
    main()
