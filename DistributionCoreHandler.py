import pickle

import generateDistribution as ld
from globalVariables import LANGS, CORE_DISTRO_FILEPATH

#
#W tym skrypcie tworzymy oraz ladujemy cala nasza baze rozkladow wszystkich jezykow
#
#

def loadCompleteDistro():
    with open(CORE_DISTRO_FILEPATH, 'rb') as file:
        DistroCore = pickle.load(file)
    print("Loaded CoreDistro!")
    return DistroCore


def saveCompleteDistro():
    print("Starting loading lang distribution...")
    DistroCore = {}
    i = 0
    for x in LANGS:
        DistroCore[x] = ld.createDistroFormFile("traindata\\" + x + ".txt")
        i += 1
        print("\"" + x + "\" lang (" + str(i) + "/" + str(len(LANGS)) + ") Loaded!")
    print("Complete!")

    with open(CORE_DISTRO_FILEPATH, 'wb') as file:
        pickle.dump(DistroCore, file)
    print("Saved CoreDistro!")


if __name__ == "__main__":
    saveCompleteDistro()
