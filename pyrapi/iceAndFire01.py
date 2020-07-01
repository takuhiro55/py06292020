#!/usr/bin/env python3

"""
Author : TSuganuma

This is a program for API Lab 11
"""

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    gotrep = requests.get(AOIF)
   
    # Dictionary
    got_dj = gotrep.json()
    
    print(got_dj)
    
if __name__ == "__main__":
    main()
