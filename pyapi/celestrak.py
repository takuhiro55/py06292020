#!user/bin/nv python3

"""


"""

import pandas as pd

ADDRESS = "http://www.celestrak.com/NORAD/elements/active.txt"

def main():

    dataset = pd.read_csv(ADDRESS, sep = '\s+')
    dataCal = dataset['CALSPHERE']

main()
