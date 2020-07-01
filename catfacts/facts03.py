#!/usr/bin/env python3

"""
Author : TSuganuma

This program does somethihg
"""
import random
import requests

def main():
    """Run time code"""
    r = requests.get("https://cat-fact.herokuapp.com/facts")
  
    # convert json data to dictionary
    jsonObj = r.json().get("all")

    # get the size of the data
    size = len(jsonObj)
   
    # get random number
    numChoice = random.choice(range(1, size))
    print("numChoice : "+ str(numChoice))
    print(type(jsonObj))

    # print out the corresponding data
    count = 0;
    for catfact in jsonObj:
        count += 1
        if count == numChoice:
            print(catfact.get("text"))
        
main()
