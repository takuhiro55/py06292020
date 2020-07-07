#!/usr/bin/env python3

import requests

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    ## Create a list to store items with the word "heal"
    healwords = []

    ## Loop though the data I got from API and find a word 'heal' in the items
    for item in items.get("results"):
        if 'heal' in item.get("name"):
            healwords.append(item.get("name"))

    ## List all
    print(f"There are {len(healwords)} words that contain tje word 'heal' in the Pokemon Item API!")
    print(healwords)

main()
