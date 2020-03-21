import copy


def removeBelowMinimal(distribution, minimalno):
    newdist = {}
    for i in distribution.keys():
        if distribution[i] > minimalno:
            newdist[i] = distribution[i]
    return newdist


def sortdict(distribution):
    newdist = {}
    for i in sorted(distribution.keys()):
        newdist[i] = distribution[i]
    return newdist


def percetageDictCalc(distribution):
    sumdist = 0
    avgdict = {}
    for i in distribution:
        sumdist += distribution[i]
    for i in distribution:
        avgdict[i] = (distribution[i] / sumdist) * 100
    return avgdict


def makearray(distribution):
    keys = []
    values = []
    for key, value in distribution.items():
        keys.append(key)
        values.append(value)

    return (keys, values)


def aligndicts(dist1, dist2):
    newDist1 = copy.deepcopy(dist1)
    newDist2 = copy.deepcopy(dist2)

    for key, value in newDist1.items():
        if key not in newDist2:
            newDist2[key] = 0

    for key, value in newDist2.items():
        if key not in newDist1:
            newDist1[key] = 0

    newDist1 = sortdict(newDist1)
    newDist2 = sortdict(newDist2)
    return (newDist1, newDist2)
