import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from CreateCompleteDistibution import loadCompleteDistro
from dictfunctions import makearray, aligndicts


def printDistribution(langname, distcore, distcore2=None, langname2=None):
    # repair dada

    if distcore2 is not None:
        tmptuple = aligndicts(distcore, distcore2)
        distcore = tmptuple[0]
        distcore2 = tmptuple[1]

        tmptuple = makearray(distcore)
        keys = tmptuple[0]
        values = tmptuple[1]

        tmptuple = makearray(distcore2)
        keys2 = tmptuple[0]
        values2 = tmptuple[1]

    else:
        # data to plot
        tmptuple = makearray(distcore)
        keys = tmptuple[0]
        values = tmptuple[1]

    for i in range(len(keys)):
        keys[i] = " " + keys[i] + " "

    matplotlib.rc('font', family='Arial')
    if distcore2 is not None:
        ind = np.arange(len(keys))
        width = 0.35

        rects1 = plt.bar(ind, values, width,
                         color='g',
                         label=langname)

        rects2 = plt.bar(ind + width, values2, width,
                         color='r',
                         label=langname2)

        plt.xticks(ind + width / 2, keys)
    else:
        rects1 = plt.bar(keys, values,
                         color='g',
                         label=langname)

    plt.xlabel('Leters')
    plt.ylabel('Percentage [%]')
    plt.title('Letters Distribution')
    plt.legend()

    plt.show()


if __name__ == "__main__":
    dist = loadCompleteDistro()
    parser = argparse.ArgumentParser()
    parser.add_argument("lname", help="lang name",
                        type=str)
    parser.add_argument("-lname2", help="lang2 name",
                        type=str, default=None)

    args = parser.parse_args()
    if args.lname2 is not None:
        dist2 = dist[args.lname2]
    else:
        dist2 = None
    printDistribution(args.lname, dist[args.lname], dist2, args.lname2)
