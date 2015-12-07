__author__ = 'bilge'

import numpy as np
import os

def convertInt(myChar, counter):
    tmpList = np.zeros((counter, 2), dtype=np.uint16)
    for i in xrange(0, counter):
        tmpstr = myChar[i][0]
        tmpstr = tmpstr.strip().split(' ')
        if(len(tmpstr) == 2):
            tmpList[i][0] = long(tmpstr[0])
            tmpList[i][1] = long(tmpstr[1])
        elif(len(tmpstr) == 3):
            tmpList[i][0] = long(tmpstr[0])
            tmpList[i][1] = long(tmpstr[2])
    return tmpList

def giveAsMatrix(f, counter):
    tmpList = []
    f.seek(0)
    for k in xrange(0, counter):
        tmpList.append(f.readline().strip().split('\t'))
    return tmpList

def pytKnapsack(n, cap, items):
    i = 0
    bestvalues = np.zeros((len(items)+1, cap+1), dtype=np.long)
    for i, (value, weight) in enumerate(items):
        i += 1
        for capacity in xrange(cap + 1):
            if weight > capacity:
                bestvalues[i][capacity] = bestvalues[i - 1][capacity]
            else:
                candidate1 = bestvalues[i - 1][capacity]
                candidate2 = bestvalues[i - 1][capacity - weight] + value
                bestvalues[i][capacity] = max(candidate1, candidate2)
    reconstruction = []
    i = n
    j = cap
    while i >= 0:
        if bestvalues[i][j] != bestvalues[i - 1][j]:
            reconstruction.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1
    reconstruction.reverse()
    return bestvalues[len(items)][cap], reconstruction

#os.chdir("data/ks_10000_0")
with open("data/ks_4_0") as f:
    counter = len(f.readlines())
    myChar = giveAsMatrix(f, counter)
    myChar = convertInt(myChar, counter)
    #according to my data set for the first row,
    #first values is my number of value and second value is my capacity
    n = int(myChar[0][0])
    k = myChar[0][1]
    values = np.zeros((n))
    weights = np.zeros((n))
    for i in xrange(1, counter):
        values[i-1] = myChar[i][0]
        weights[i-1] = myChar[i][1]
    unsorted = concatenate_list(values, weights)
    weights, values = sortbyWeight(weights, values)
    items = concatenate_list(values, weights)
    obj, last_arrays = pytKnapsack(counter-1, k, items)
    result = np.zeros((n), dtype=np.long)
    for i in xrange(0, len(unsorted)):
        for j in xrange(0, len(last_arrays)):
            if unsorted[i][0] == last_arrays[j][0] and unsorted[i][1] == last_arrays[j][1]:
                result[i] = 1
    print obj
    for i in xrange(0, len(result)):
        print(result[i])