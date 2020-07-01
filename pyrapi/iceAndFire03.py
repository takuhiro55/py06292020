#!/usr/bin/env python3

"""
Author : TSuganuma

This is a program for API Lab 11
"""

#import pprint
import requests

AOIF = "https://www.anapioficeandfire.com/api"
AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    gotrep = requests.get(AOIF_BOOKS)
   
    # Dictionary
    got_dj = gotrep.json()
    
    for singlebook in got_dj:
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}")
        print(f"\tISBN -> {singlebook['isbn']}")
        print(f"\tPUBLISHER -> {singlebook['publisher']}")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")
    
if __name__ == "__main__":
    main()
