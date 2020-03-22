from CreateCompleteDistibution import loadCompleteDistro
from cmpAlgorithms import mycompare1
from createDist import createLangDistribution

LANGS = ["bul", "ces", "dan", "deu", "ell", "eng", "est", "fin", "fra", "gle", "hrv", "hun",
         "ita", "lav", "lit", "mlt", "nld", "pol", "por", "ron", "slk", "slv", "spa", "swe"]

FILE_TEST_PATH = ""
FILE_ANSWER_PATH = ""


def runDistroTests():
    dist = loadCompleteDistro()

    with open(FILE_TEST_PATH, "r") as testf:
        with open(FILE_ANSWER_PATH, "r") as answerf:
            line = testf.readline()
            newdistro = createLangDistribution(line)
            result = mycompare1(newdistro, dist)


if __name__ == "__main__":
    runDistroTests()
