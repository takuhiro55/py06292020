#!/usr/bin/env python3

def main():
    # with statement, file close automatically after finish process
    with  open("dnsservers.txt", "r") as dnsfile:
         #dnslist = dnsfile.readlines()
        for svr in dnsfile:
            svr = svr.rstrip('\n') #remove newline 

            if svr.endswith('org'):
                with open("org-domain.txt", "a") as srvfile:
                    srvfile.write(svr + "\n")
            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as srvfile:
                    srvfile.write(svr + "\n")

            # pirint(svr, end="")
   # dnsfile.close()

if __name__ == "__main__":
    main()
