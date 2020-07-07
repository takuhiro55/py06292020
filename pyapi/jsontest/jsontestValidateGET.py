#!/usr/bin/env python3

"""
Author : TSuganuma

API Lab15 - Use GET to validate JSON
"""

import requests
import json

# define the URL we want to use
GETURL = "http://validate.jsontest.com/"

def main():

    mydata = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]}

    # Use json library to convert to legal json, then strip out whitespace
    jsonToValidate = f"json={ json.dumps(mydata).replace(' ','')}"
    
    # Use requests library to send an HTTP GET
    # insert '?' between {GETURL} and {jsonToValidate}
    resp = requests.get(f"{GETURL}?{jsonToValidate}")

    # Strip off JSON response
    # and convert to PYTHONIC LIST/DICT
    respjson = resp.json()

    # Display our PYTHONIC data (LIST/DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
