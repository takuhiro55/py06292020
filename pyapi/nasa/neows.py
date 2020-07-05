#!/usr/bin/env python3

import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    with open("/home/student/nasa/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()

    #remove any newline characters from the api
    nasacreds = "api_key=" + nasacreds.strip("\n")

    #update the date below
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    enddate = "end_date=2019-12-11"

    #  make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" +nasacreds)

    # Strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOS data
    print(neodata)

if __name__ == "__main__":
    main()
