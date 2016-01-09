__author__ = 'bilge'
"""
I used for instance 3
"""
import sys

def convert(items, reconstruction):
    j=0
    result = [0] * len(items)
    for i in range(0,len(items)):
        for j in range(0,len(reconstruction)):
            if items[i] == reconstruction[j]:
                result[i] = 1
    return result

def dyn_knapsack(items, maxweight):
    bestvalues = [[0] * (maxweight + 1)
                  for i in range(len(items) + 1)]
    for i, (value, weight) in enumerate(items):
        i += 1
        for capacity in range(maxweight + 1):
            if weight > capacity:
                bestvalues[i][capacity] = bestvalues[i - 1][capacity]
            else:
                candidate1 = bestvalues[i - 1][capacity]
                candidate2 = bestvalues[i - 1][capacity - weight] + value
                bestvalues[i][capacity] = max(candidate1, candidate2)

    reconstruction = []
    i = len(items)
    j = maxweight
    while i > 0:
        if bestvalues[i][j] != bestvalues[i - 1][j]:
            reconstruction.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1

    reconstruction.reverse()

    return bestvalues[len(items)][maxweight], reconstruction

with open(sys.argv[1]) as f:
    maxweight = int(f.readline().split()[1])
    items = [list(map(int, line.split())) for line in f]
    bestvalue, reconstruction = dyn_knapsack(items, maxweight)
    result=convert(items,reconstruction)
    print(bestvalue)
    myresult=''
    for i in result:
        myresult= myresult + str(i) + ' '
    print(myresult)
