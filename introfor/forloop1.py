#!/usr/bin/env python3

'''
Lab22 Looping with for
'''

#create the list called vendors
def main():

    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
    vendors_approved = ["cisco", "juniper", "big_ip"]

    print("\n-----------------------")
    for x in vendors:
       # print("The vendor is:" + x)
        if x not in vendors_approved:
            print("Vendor:" + x +  " - NOT APPROVED!")
        else:
            print("Vendor:" + x + " - APPROVED")
        
    print("\nOur loop has ended")

if __name__ == "__main__":
    main()
