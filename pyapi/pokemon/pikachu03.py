#!/usr/bin/env python3

"""
Author : TSUganuma

API Lab16 - works with padas data framework
"""

import argparse
import requests
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    ## get "item" from web
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    ## create a variable for list to store matched words
    matchedwords = []

    ## looping through the data from web and store them in the list
    for item in items.get("results"):
        if args.searchword in item.get("name"):
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()

    ## map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["matched"] = finishedlist

    ## list all words containing matched word
    print(f"There are {len(matchedwords)} words that contain the word '{args.searchword}' in the Pokemon Item API")
    print(f"List of Pokemon items containing '{args.searchword}'")
    print(matchedwords)

    ## make a dataframe of pandas
    itemsdf = pandas.DataFrame(matchedwords)
    itemsdf.to_excel("pokemonitems.xlsx", index = False)
    print("Excel file was created")
    
    itemsdf.to_csv("pokemonitems.csv", index=False)
    print("CSV file was created")

    itemsdf.to_json("pokemonitems.json")
    print("JSON file was created")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()

