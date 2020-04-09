import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from DistributionCoreHandler import loadCompleteDistro
from dictfunctions import LangDistro


#
# Bywa tak ze chcemy zobaczyc jak wyglaja rozklady dwoch roznych jezykow bo cos sie nam nie zgadza
# Ten skrypt to nam pokaze
#

def printDistribution(langname, distcore, distcore2=None, langname2=None):
    # repair dada

    if distcore2 is not None:
        # Wyrownujemy nasze rozklady aby mialy ten sam sklad liter
        newdistro1 = distcore.alain(distcore2)
        newdistro2 = distcore2.alain(distcore)

        tmptuple = newdistro1.retArrays()
        keys = tmptuple[0]
        values = tmptuple[1]

        tmptuple = newdistro2.retArrays()
        keys2 = tmptuple[0]
        values2 = tmptuple[1]

    else:
        tmptuple = distcore.retArrays()
        keys = tmptuple[0]
        values = tmptuple[1]

    # Magiczny myk bo inaczej zle to wyglada na wykresach
    for i in range(len(keys)):
        keys[i] = " " + keys[i] + " "

    matplotlib.rc('font', family='Arial')
    # Wyswietlamy!
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


# Wstawiamy w postaci argumentow jakie jezyki chemy wyswietlic 1 wymagany 2 opcjonalny np. pol -lname2 eng
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
