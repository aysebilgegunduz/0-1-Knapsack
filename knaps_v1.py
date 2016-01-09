__author__ = 'bilge'

import numpy as np
import copy
import os
"""
def sort_by_weight(items):
    for i in range(len(items)):
        for j in range (len(items)-1):
            if items[j][1] > items[j+1][1]:
                temp = items[j+1]
                items[j+1] = items[j]
                items[j] = temp
    return items
 """
def sort_by_weight(items):
    items = sorted(items,key=lambda x: x[1],reverse=True)
    return items

def convertInt(myChar, counter):
    tmpList = np.zeros((counter, 2), dtype=np.uint16)
    for i in range(0, counter):
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
    for k in range(0, counter):
        tmpList.append(f.readline().strip().split('\t'))
    return tmpList

def pytKnapsack(n, cap, items):
    i = 0
    bestvalues = np.zeros((len(items)+1, cap+1), dtype=np.long)
    for i, (value, weight) in enumerate(items):
        i += 1
        for capacity in range(cap + 1):
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
#4 400_0
#ks_10000_0
with open("data/ks_19_0") as f:
    n = np.uint32
    k = np.uint32
    n, k = map(np.uint32, f.readline().split(' '))
    unsorted = [list(map(int, line.split())) for line in f]
    items = copy.copy(unsorted)
    items = sort_by_weight(items) #(weights, values)
    #items = concatenate_list(values, weights)
    obj, last_arrays = pytKnapsack(n, k, items)
    result = np.zeros((n), dtype=np.long)
    for i in range(0, len(unsorted)):
        for j in range(0, len(last_arrays)):
            if unsorted[i][0] == last_arrays[j][0] and unsorted[i][1] == last_arrays[j][1]:
                result[i] = 1
    print(obj)
    for i in range(0, len(result)):
        print(result[i], end=" ")