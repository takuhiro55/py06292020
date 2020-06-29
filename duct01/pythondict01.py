#!/usr/bin/env python3

'''
This is lab11 dictionary
'''

#create a dictionary
switch = {"hostname":"sw1", "ip":"10.0.1.1", "version":"1.2", "vendor":"cisco"}

#display parts of the dictionary
print(switch["hostname"])
print(switch['ip'])

#request a 'fake' key -> This will blow up the program
#print(switch["lynx"])
print("First test - .get()")
print(switch.get("lynx"))

print("Second test - .get()")
print(switch.get("lynx", "The Key is in Another Castle"))

print("Third test - .get()")
print(switch.get("version"))

print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.values())

print("Sixth test - .pop()")
switch.pop("version") #remove "version"
print(switch.keys())
print(switch.values())

print("Seventh test - ADD a new value")
switch["adminlogin"]= "karl08"
print(switch.keys())
print(switch.values())

print("Eighth test - ADD a new value")
switch["password"]= "qwerty"
print(switch.keys())
print(switch.values())
