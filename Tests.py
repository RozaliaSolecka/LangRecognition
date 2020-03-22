from CreateCompleteDistibution import loadCompleteDistro
from cmpAlgorithms import mycompare1
from createDist import createLangDistribution, appenddist

LANGS = ["bul", "ces", "dan", "deu", "ell", "eng", "est", "fin", "fra", "gle", "hrv", "hun",
         "ita", "lav", "lit", "mlt", "nld", "pol", "por", "ron", "slk", "slv", "spa", "swe"]

FILE_TEST_PATH = ""
FILE_ANSWER_PATH = ""


def runDistroTests():
    dist = loadCompleteDistro()

    sumtests={}
    sumfails={}
    with open(FILE_TEST_PATH, "r") as testf:
        with open(FILE_ANSWER_PATH, "r") as answerf:
            testline = testf.readline()
            ansline = answerf.readline().rstrip('\n')
            sumtests=appenddist(sumtests,ansline)

            newdistro = createLangDistribution(testline)
            result = mycompare1(newdistro, dist)
            if result!=ansline:
                sumfails=appenddist(sumfails,ansline)


if __name__ == "__main__":
    runDistroTests()
