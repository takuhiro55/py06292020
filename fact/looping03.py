#!/usr/bin/env python3

"""
UUID :  universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems
"""

import uuid

def main():
    howmany = int(input("How many UUIDs should be generated?"))
    print("Generating UUIDs...")

    for rando in range(howmany):
        print(uuid.uuid4())

if __name__ == "__main__":
    main()
