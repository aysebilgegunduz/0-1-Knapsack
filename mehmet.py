__author__ = 'bilge'
import sys
def convert(items, reconstruction):
    j=0
    result = [0] * len(items)
    for i in range(0,len(items)):
        for j in range(0,len(reconstruction)):
            if items[i] == reconstruction[j]:
                result[i] = 1
    return result
def knapsack(items, maxweight):
    bestvalues = [[0] * (maxweight + 1)
                  for i in xrange(len(items) + 1)]
    for i, (value, weight) in enumerate(items):

        i += 1
        for capacity in xrange(maxweight + 1):
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

"""
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: knapsack.py [file]')
        sys.exit(1)
"""
#with open('data/ks_4_0') as f:
with open(sys.argv[1]) as f:
    maxweight = int(f.readline().split()[1])
    items = [map(int, line.split()) for line in f]
    bestvalue, reconstruction = knapsack(items, maxweight)
    result=convert(items,reconstruction)
    print(bestvalue)
    myresult=''
    for i in result:
        myresult= myresult + str(i) + ' '
    print(myresult)
    #print('Items:')
    #for value, weight in reconstruction:
       # print('V: {0}, W: {1}'.format(value, weight))
