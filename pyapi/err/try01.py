#!/usr/bin/env python3

# Start with an infinite loop
while True:
    try:
        print("Enter a file name:")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems witht that file name.")
        break
    except:
        print("Error with that file name! Try again...")

