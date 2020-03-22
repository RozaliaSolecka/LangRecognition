from CreateCompleteDistibution import loadCompleteDistro
from cmpAlgorithms import mycompare1
from createDist import createLangDistribution, appenddist

FILE_TEST_PATH = "testdata\\NewTrainX.txt"
FILE_ANSWER_PATH = "testdata\\NewTrainY.txt"


def runDistroTests():
    dist = loadCompleteDistro()

    sumtests = {}
    sumfails = {}
    ansline = []
    testline = []
    anslineraw = []
    print("Runing tests...")
    counter = 0
    with open(FILE_TEST_PATH, "r", encoding='utf-8') as testf:
        testline = testf.readlines()
    with open(FILE_ANSWER_PATH, "r", encoding='utf-8') as answerf:
        anslineraw = answerf.readlines()

    for x in anslineraw:
        ansline.append(x.rstrip('\n'))

    for x in range(len(ansline)):
        appenddist(sumtests, ansline[x])
        if ansline[x] not in sumfails:
            sumfails[ansline[x]] = 0

        newdistro = createLangDistribution(testline[x])

        # Tutaj wywolujemy nasz algorytm
        result = mycompare1(newdistro, dist)
        if result != ansline[x]:
            appenddist(sumfails, ansline[x])
        counter += 1
        print(f'Tested {counter}/{len(ansline)}')

    print("Printing Stats...")
    for x in sumtests.keys():
        print("Lang: \"{0}\" Failed: {1} Tested: {2} Accuracy: {3:0.3f}%".format(x, sumfails[x], sumtests[x],
                                                                                 ((sumtests[x] - sumfails[x])
                                                                                  /sumtests[x]) * 100))


if __name__ == "__main__":
    runDistroTests()
