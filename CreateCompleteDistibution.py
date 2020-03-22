import pickle

import createDist as ld

LANGS = ["bul", "ces", "dan", "deu", "ell", "eng", "est", "fin", "fra", "gle", "hrv", "hun",
         "ita", "lav", "lit", "mlt", "nld", "pol", "por", "ron", "slk", "slv", "spa", "swe"]


def loadCompleteDistro():
    filename = 'CoreDistro'

    with open(filename, 'rb') as file:
        DistroCore = pickle.load(file)
    print("Loaded CoreDistro!")
    return DistroCore


def saveCompleteDistro():
    filename = 'CoreDistro'
    print("Starting loading lang distribution...")
    DistroCore = {}
    i = 0
    for x in LANGS:
        DistroCore[x] = ld.createDistroFormFile("traindata\\" + x + ".txt")
        i += 1
        print("\"" + x + "\" lang (" + str(i) + "/" + str(len(LANGS)) + ") Loaded!")
    print("Complete!")

    with open(filename, 'wb') as file:
        pickle.dump(DistroCore, file)
    print("Saved CoreDistro!")


if __name__ == "__main__":
    saveCompleteDistro()
