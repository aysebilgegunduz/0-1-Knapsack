__author__ = 'bilge'

import numpy as np
import ast
def total_value(items, max_weight):
    return  sum([x[2] for x in items]) if sum([x[1] for x in items]) < max_weight else 0

cache = []
include = []
include.append([])
def solve(items, max_weight):
    i=0
    if not items:
        return []
    if (items,max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include[i].append(head)
        include[i].append(solve(tail, max_weight - head[1]))
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items,max_weight)] = answer
    return cache[(items,max_weight)]
"""
def sort_by_weight(items):
    sorted_x = sorted(items.items(), key=operator.itemgetter(0),reverse=True)
    return sorted_x
"""
#os.chdir("data/ks_10000_0")
#4 400_0
#ks_10000_0
with open("data/ks_19_0") as f:
    n = np.uint32
    k = np.uint32
    n, k = map(np.uint32, f.readline().split(' '))
    tmp_items = ()
    i=0
    #list alıp tuple yap dedi biraz daha arastir
    for line in f:
        value,weight = (map(int, line.split(' ')))
        tmp_items[i] = (value,weight)
    unsorted = tmp_items
    #tmp_items = sort_by_weight(tmp_items)
    """
    solve(tmp_items,k)
    result = np.zeros((n), dtype=np.long)
    for i in range(0, len(unsorted)):
        for j in range(0, len(last_arrays)):
            if unsorted[i][0] == last_arrays[j][0] and unsorted[i][1] == last_arrays[j][1]:
                result[i] = 1
    print(obj)
    for i in range(0, len(result)):
        print(result[i], end=' ')
            """