#!/usr/bin/env python3

"""
Author : TSuganuma

This is a program for API Lab 11
"""

#import pprint
import requests

AOIF = "https://www.anapioficeandfire.com/api"
AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"
AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters"

def main():
    # gotrep = requests.get(AOIF_BOOKS)
    got_charToLookup = input("What is the name of the character we should lookup?")
    gotrep = requests.get(AOIF_CHAR + "?name"+ got_charToLookup)

    # Dictionary
    got_dj = gotrep.json()
    
    print(got_dj)
    print(f"The character {got_charToLookup} has the URL:{got_dj[0]['url']}")
    
if __name__ == "__main__":
    main()
