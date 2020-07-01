#!/usr/bin/env python3

"""
Author : TSuganuma

This program does somethihg
"""

import requests

def main():
    """Run time code"""
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    print(r.json())
   # print(r.json().get("all"))
   # print("\n\n\n")
    for catfact in r.json()["all"]:
        print(catfact.get("text"))
main()
