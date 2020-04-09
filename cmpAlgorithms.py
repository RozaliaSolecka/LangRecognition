#
# Tu beda nasze algorytmy porownojace rozklady
#


# nasza funkcja 1
import sys
from globalVariables import EPSILON
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


def KullbackLeibner(unnowndist, distcore):
    min_value = 1e10
    corect_lang = ""

    for langname in distcore.keys():
        value=KullbackLeibnerIteration(distcore[langname].alain(unnowndist),unnowndist.alain(distcore[langname]))
        if value < min_value:
            min_value = value
            corect_lang = langname
    return corect_lang

def KullbackLeibnerIteration(one,two):
    complete_known_dist = MinMaxNormalise(one)
    completen_unnown_dist = MinMaxNormalise(two)
    value = CalculateKullbackLeibner(complete_known_dist, completen_unnown_dist)
    return value

def MinMaxNormalise(distribution):
    for x in distribution.keys():
        distribution[x] = distribution[x] + EPSILON
        distribution[x] = distribution[x] / (100 + EPSILON)
    return distribution


def CalculateKullbackLeibner(unnowndist, knowndist):
    finalsum = 0
    for letter in knowndist.keys():
        finalsum += knowndist[letter] * math.log(knowndist[letter] / unnowndist[letter], 2)
    return finalsum