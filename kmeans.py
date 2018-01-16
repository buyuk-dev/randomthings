import math
import random
from matplotlib import pyplot
from pprint import pprint


def getInitialMeans(k, dims=2):
    return [
        tuple(random.random() for dim in range(dims))
        for mean in range(0, k)        
    ]


def euclidDist(pointA, pointB):
    return math.sqrt(sum(((x-y)**2 for x,y in zip(pointA, pointB))))


def pointToPointDist(pointA, pointB):
    return euclidDist(pointA, pointB)


def findBestMatch(point, means):
    dists = [pointToPointDist(point, mean) for mean in means]
    return dists.index(max(dists))


def mapDataToMeans(data, means):
    mapping = [[] for mean in means]
    for point in data:
        bestMeanIndex = findBestMatch(point, means)
        mapping[bestMeanIndex].append(point)
    return mapping


def calculateMean(points):
    return [sum(x) / len(points) for x in zip(*points)]


def calculateUpdatedMeans(mapping):
    return [
        calculateMean(points)
        for points in mapping
    ]


def areMeansTheSame(meansA, meansB):
    for x, y in zip(meansA, meansB):
        if pointToPointDist(x, y) > 0.01:
            return False
    return True


def plotStep(means, mapping):
    for points in mapping:
        pyplot.plot(list(zip(*points))[0], list(zip(*points))[1], "o")

    pyplot.plot(list(zip(*means))[0], list(zip(*means))[1], "or")
    pyplot.xlim((0.0, 1.0))
    pyplot.ylim((0.0, 1.0))
    pyplot.show()


def kMeans(data, k):
    means = getInitialMeans(k, len(data[0]))
    pprint(means)
    mapping = mapDataToMeans(data, means)
    newMeans = calculateUpdatedMeans(mapping)
    while not areMeansTheSame(means, newMeans):
        plotStep(means, mapping)
        means = newMeans
        mapping = mapDataToMeans(data, means)
        newMeans = calculateUpdatedMeans(mapping)

    return mapping


if __name__ == '__main__':
    data = [(random.random(), random.random()) for i in range(1000)]
    out = kMeans(data, 2)
