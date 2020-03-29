#
# Tu beda nasze algorytmy porownojace rozklady
#

# nasza funkcja 1
import sys

from globalVariables import EPSILON
import math


def mycompare1(unnowndist, distcore):
    return 'pol'


def KullbackLeibner(unnowndist, distcore):
    min_value = 1e10
    corect_lang = ""

    for langname in distcore.keys():
        complete_known_dist = MinMaxNormalise(distcore[langname].alain(unnowndist))
        completen_unnown_dist = MinMaxNormalise(unnowndist.alain(distcore[langname]))
        value = CalculateKullbackLeibner(complete_known_dist, completen_unnown_dist)
        if value < min_value:
            min_value = value
            corect_lang = langname

    return corect_lang


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
