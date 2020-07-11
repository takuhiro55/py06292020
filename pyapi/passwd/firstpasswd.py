#!/usr/bin/env python3

import getpass

def main():

    # Input password
    p= getpass.getpass()

    # Show what password I input
    print("Password entered:", p)

if __name__ == "__main__":
    main()
