#!/usr/bin/env python3

"""
Authoer : TSuganuma

API Lab16 - ETCD and RESTful API
"""

import requests
import pprint

def main():

    ## ----- PUT1 -----
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans'})
    print("r # " + str(r))
    print(f"Status Code - {r.status_code}")
    pprint.pprint(r.json())

    ## ----- PUT2 -----
    print('******')
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans, version 2'})
    print("r # "+ str(r))
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    print('******')

    ## ----- GET ------
    # issue an HTTP GET to our keys/requests
    r = requests.get("http://127.0.0.1:2379/v2/keys/requests")
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    pprint.pprint(r.json())

main()
