#!/usr/bin/env python3

def main():
    # with statement, file close automatically after finish process
    with  open("dnsservers.txt", "r") as dnsfile:
         #dnslist = dnsfile.readlines()
         for svr in dnsfile:
             print(svr, end="")
   # dnsfile.close()

if __name__ == "__main__":
    main()
