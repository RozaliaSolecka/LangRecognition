from dictfunctions import LangDistro
from globalVariables import FILE_TEST_PATH, FILE_ANSWER_PATH
from DistributionCoreHandler import loadCompleteDistro
from cmpAlgorithms import mycompare1
from generateDistribution import createLangDistribution

#
# Glowny plik testujacy nasze algorytmy
#


def runDistroTests():
    #ladujemy nasz korpus
    dist = loadCompleteDistro()

    sumtests = LangDistro() #ile testow z danego jezyka bylo
    sumfails = LangDistro() #ile testow nasz algorytm zawalil
    ansline = []
    print("Runing tests...")
    counter = 0
    #laduemy linijki testow
    with open(FILE_TEST_PATH, "r", encoding='utf-8') as testf:
        testline = testf.readlines()
    #i jezykow w ktorych zostaly napisane - nasze poprawne odpowiedzi
    with open(FILE_ANSWER_PATH, "r", encoding='utf-8') as answerf:
        anslineraw = answerf.readlines()

    #obcinamy zbedny znak konca lini
    for x in anslineraw:
        ansline.append(x.rstrip('\n'))

    #Testujemy!
    for x in range(len(ansline)):

        #Zwiekszamy ilosc testow o 1
        sumtests.appenddist(ansline[x])
        #Przygotowywujemy licznik do testow oblanych z akrutalnego jezyka
        if ansline[x] not in sumfails:
            sumfails[ansline[x]] = 0

        #analizujemy teskst
        newdistro = createLangDistribution(testline[x])

        # Tutaj wywolujemy nasz algorytm porowujacy rozklad tesktu w nieznanym jezyku z naszymi zapisanymi jezykaim
        # Porownojemy je i zwracamy najbardziej nazwe najbardziej podobnego jezyka
        result = mycompare1(newdistro, dist)

        #Jezeli zly jezyk zwiekszamy liczne porazek
        if result != ansline[x]:
            sumfails.appenddist(ansline[x])
        counter += 1

        print(f'Tested {counter}/{len(ansline)}')

    #Wypisujemy statysyki
    print("Printing Stats...")
    for x in sumtests.keys():
        print("Lang: \"{0}\" Failed: {1} Tested: {2} Accuracy: {3:0.3f}%".format(x, sumfails[x], sumtests[x],
                                                                                 ((sumtests[x] - sumfails[x])
                                                                                  / sumtests[x]) * 100))


if __name__ == "__main__":
    runDistroTests()
