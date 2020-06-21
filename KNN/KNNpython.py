import math
import csv


class distClass:
    vec = []
    dist = -1  # distance of current point from test point
    tag = '-'  # tag of current point


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += pow(num1 - num2, 2)
    return math.sqrt(distance)


def ManhattanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += abs(float(instance1[x]) - float(instance2[x]))
    return distance


def HammingDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        if float(instance1[x]) != float(instance2[x]):
            distance += 1
    return distance


def distanceFromTestPoint(testPoint, points, disAlgo):
    eucDistances = []  # list of distances, will hold objects of type distClass

    # Find the distance if all the vectors from the first one
    for i in range(1, len(points)):
        point = points[i]
        label = point[-1]
        if disAlgo == "e":
            d = euclideanDistance(testPoint, point, len(point) - 1)
        elif disAlgo == "m":
            d = ManhattanDistance(testPoint, point, len(point) - 1)
        else:
            d = HammingDistance(testPoint, point, len(point) - 1)
        obj = distClass()  # one record's distance and tag
        obj.vec = point[:-1]
        obj.dist = d
        obj.tag = label
        eucDistances.append(obj)

    # Sort the list according to the distance
    eucDistances.sort(key=lambda x: x.dist)
    return eucDistances


def predictTag(k, tags, eucDistances):
    if k % 2 == 0:
        return
    # counting the most common sign
    counter = [0] * len(tags)
    for i in range(1, k + 1):
        for j in range(len(tags)):
            if tags[j] == eucDistances[i].tag:
                counter[j] += 1

    maxTag = max(counter)
    indx = counter.index(maxTag)
    return tags[indx]


def readFile(filename):
    with open(filename, 'r') as myCsvfile:
        lines = csv.reader(myCsvfile)
        return list(lines)


def writeFile(filename, checkPoints):
    with open(filename, 'w', newline='') as myCSVtest:
        writer = csv.writer(myCSVtest)
        writer.writerows(checkPoints)


def knnAlgo(testFile, trainFile, tags, k, disAlgo):
    # The main KNN function.
    # Read from the train and test files, finds the tag of each point in the test file and Write it to new file

    points = readFile(trainFile + ".csv")[1:]
    checkPoints = readFile(testFile + ".csv")

    hit = 1
    for point in checkPoints[1:]:
        listDistances = distanceFromTestPoint(point, points, disAlgo)
        tag = predictTag(k, tags, listDistances)
        if point[-1] == tag:
            hit += 1
        point[-1] = tag

    writeFile(testFile + str(k) + disAlgo + ".csv", checkPoints)
    return hit / len(checkPoints)


def printAccuracy(k, disAlgo, accuracy):
    print("KNN with k=", k, "and", disAlgo, ", the accuracy is:", accuracy)


# Tar 4 part 2

euclideanDis = "e"
manhattanDis = "m"
hammingDis = "h"

accuracy = knnAlgo('myFile_test', 'myFile', ['F', 'M'], 3, euclideanDis)

# working with mytest and mytrain files
accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 1, euclideanDis)
printAccuracy(1, "euclidean distance", accuracy)
accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 7, euclideanDis)
printAccuracy(7, "euclidean distance", accuracy)
accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 19, euclideanDis)
printAccuracy(19, "euclidean distance", accuracy)

accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 1, manhattanDis)
printAccuracy(1, "manhattan distance", accuracy)
accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 7, manhattanDis)
printAccuracy(7, "manhattan distance", accuracy)
accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 19, manhattanDis)
printAccuracy(19, "manhattan distance", accuracy)

accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 1, hammingDis)
printAccuracy(1, "hamming distance", accuracy)
accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 7, hammingDis)
printAccuracy(7, "hamming distance", accuracy)
accuracy = knnAlgo('mytest', 'mytrain', ['F', 'M'], 19, hammingDis)
printAccuracy(19, "hamming distance", accuracy)
