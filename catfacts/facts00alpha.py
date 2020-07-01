#!/usr/bin/env python3

"""
Author : TSuganuma

This program does CAT
"""

import requests

def main():
    """Run time code"""
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    # print(dir(r))
    print(r.json())
main()
