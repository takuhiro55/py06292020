#!/usr/bin/env python3

"""
Author : TSuganuma

This program is for Python Basic lab34 plotting with matplotlib
"""

import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def parse_csv_data():

    summary = []

    #Open csv data
    with open("/home/student/mycode/graphing/2018summary.csv",\
            "r") as downtime:
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (row[0], row[1], row[2], row[3])
            summary.append(rowdat)
    return summary

def main():
    N = 4

    #grab our data
    summary = parse_csv_data()
    localnetMeans = summary[0]
    wanMeans = summary[1]

    # the x locations for the groups
    ind = np.arange(N)
    # the width of the bars : can also be len(x) sequence
    width = 0.35

    # Describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # Stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage(mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # Save the graph
    plt.savefig("/home/student/mycode/graphing/2018summaryv2.png")
    print("Graph created.")

if __name__ == "__main__":
    main()

