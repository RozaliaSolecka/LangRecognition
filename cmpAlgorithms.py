
#
# Tu beda nasze algorytmy porownojace rozklady
#

#nasza funkcja 1
import math


def mycompare1(unnowndist, distcore):

    max_probability = 1e6
    language = ""
    for lang in distcore.keys():   # tablica ze wszytskimi skrótami języków, i - język
        distcore2 = distcore[lang].alain(unnowndist)
        unnowndist2 = unnowndist.alain(distcore[lang])
        probability = 0

        for key in distcore2.keys():
            probability += math.pow((math.sqrt(distcore2[key]) - math.sqrt(unnowndist2[key])), 2) # ~ileś set

        probability = math.sqrt(probability)
        probability = probability / math.sqrt(2)

        if probability < max_probability:  #im bliżej zera tym lepiej
            max_probability = probability
            language = lang

    return language
