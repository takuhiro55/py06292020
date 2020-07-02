#!/

"""

"""

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 4
    localnetMeans = (20, 35, 30, 35)
    wanMeans = (25, 32, 34, 20)
    ind = np.arange(N)
    width = 0.35

    # Describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)

    # Stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # Display the graph 
    # -> Since tmux does not work, I will save it and take it to gitHub
    # plt.show()
    plt.savefig("/home/student/mycode/graphing/2018summary.pdf")

if __name__ == "__main__":
    main()
