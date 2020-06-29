#!/usr/bin/env python3

import functools
import operator

'''
This is the lab 10 'Slicing complex lists' for the first week.
'''
# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

#display list
print(list1)

#display list1[1] which should only display arista_eos
print(list1[1])

#create a new list containing a single item
list2 = ["juniper"]

#combining list1 and list2
list1.extend(list2)

#display list1, which now contains list2
print(list1)

#create list3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

# Append list3 to list1
list1.append(list3)

# print list
print(list1)

# display the list of IP address only
print(list1[4][0])
# display the specific number of the IP address
print(list1[4][0][0])
print(list1[4][0][1])
print(list1[4][0][2])
print(list1[4][0][3])

# Try to flatten the list
#list_flat = functools.reduce(operator.iconcat, list1, []);
#print(list_flat)

# Optional Challenge
list_animal = ["Fox", "Fly", "Ant", "Bee", "Cat"]
print(list_animal)


