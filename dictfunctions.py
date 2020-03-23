import copy

#
# A to je nasza klasa od trzymania w niej rozkladu
# W zasadzie jest to pythonowy Dictionary z kilkoma dodatkowymi funkcjami
#

class LangDistro(dict):
    def removeBelowMinimal(distribution, minimalno):
        dis=copy.deepcopy(distribution)
        for i in dis.keys():
            if dis[i] < minimalno:
                distribution.pop(i)

    def sort(distribution):
        newdist = {}
        for i in sorted(distribution.keys()):
            newdist[i] = distribution[i]

        distribution.clear()

        for i in newdist.keys():
            distribution[i]=newdist[i]

    def makePercentage(distribution):
        sumdist = 0
        avgdict = {}
        for i in distribution:
            sumdist += distribution[i]
        for i in distribution:
            avgdict[i] = (distribution[i] / sumdist) * 100


        distribution.clear()

        for i in avgdict.keys():
            distribution[i] = avgdict[i]

    def retArrays(distribution):
        keys = []
        values = []
        for key, value in distribution.items():
            keys.append(key)
            values.append(value)

        return (keys, values)

    def alain(dist1, dist2):
        dist = copy.deepcopy(dist1)
        for key, value in dist2.items():
            if key not in dist:
                dist[key] = 0

        dist.sort()
        return dist

    def appenddist(self, c):
        if c in self:
            self[c] += 1
        else:
            self[c] = 1
