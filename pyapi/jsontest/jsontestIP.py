#!/usr/bin/env python3

"""
Author : TSuganuma

API LAB 15 - Displaying my IP address

"""

import requests

IPURL= "http://ip.jsontest.com/"

def main():
    #use requests library to send an HTTP GET
    resp = requests.get(IPURL)

    # Strip off JSON response
    # and convert to Pythonic List/Dict
    respjson = resp.json()

    # Display our pythonic data(List/Dict)
    print(respjson)

    #Just Display the value of "ip"
    print(f"The current WAN IP is --> {respjson['ip']}")

if __name__ == "__main__":
    main()
