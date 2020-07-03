#!/usr/bin/env python3

"""
Author: TSuganuma

This is basic Lab36 'Python and Excel'
"""

import pyexcel

def get_ip_data():
    input_foodName = input("\nWhat is the name of food?")
    input_quantity = input("What is the quantity?")
    input_price = input("What is the price?")
    d = {"Food":input_foodName, "Quantity":input_quantity, "Price":input_price}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")

def main():

    mylistdict = []
    print("Hello! This program will make you a *.xls file")

    while(True):
        mylistdict.append(get_ip_data())
        keep_going= input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit:")
        if (keep_going.lower() == 'q'):
            break
    filename = input("\nWhat is the name of the *.xls file? ")
    pyexcel.save_as(records = mylistdict, dest_file_name = f'{filename}.xls')
    print("The file " + filename + ".xls should be in your local directory")

if __name__ == "__main__":
    main()
