__author__ = 'bilge'
import numpy as np

# A greedy algorithm for the fractional knapsack problem.
# Note that we sort by v/w without modifying v or w so that we can
# output the indices of the actual items in the knapsack at the end
def KnapsackFrac(v, w, W):
  order = bubblesortByRatio(v, w)            # sort by v/w (see bubblesort below)
  weight = 0.0                               # current weight of the solution
  value = 0.0                                # current value of the solution
  knapsack = []                              # items in the knapsack - a list of (item, faction) pairs
  n = len(v)
  index = 0                                  # order[index] is the index in v and w of the item we're considering
  while (weight < W) and (index < n):
    if weight + w[order[index]] <= W:        # if we can fit the entire order[index]-th item
      knapsack.append((order[index], 1.0))   # add it and update weight and value
      weight = weight + w[order[index]]
      value = value + v[order[index]]
    else:
      fraction = (W - weight) / w[order[index]]  # otherwise, calculate the fraction we can fit
      knapsack.append((order[index], fraction))  # and add this fraction
      weight = W
      value = value + v[order[index]] * fraction
    index = index + 1
  return (knapsack, value)                       # return the items in the knapsack and their value


# sort in descending order by ratio of list1[i] to list2[i]
# but instead of rearranging list1 and list2, keep the order in
# a separate array
def bubblesortByRatio(list1, list2):
  n = len(list1)
  order = range(n)
  for i in range(n - 1, 0, -1):     # i ranges from n-1 down to 1
    for j in range(0, i):           # j ranges from 0 up to i-1
      # if ratio of jth numbers > ratio of (j+1)st numbers then
      if ((1.0 * list1[order[j]]) / list2[order[j]]) < ((1.0 * list1[order[j+1]]) / list2[order[j+1]]):
        temp = order[j]              # exchange "pointers" to these items
        order[j] = order[j+1]
        order[j+1] = temp
  return order

with open("data/ks_19_0") as f:
    n = np.uint32
    k = np.uint32
    n, k = map(np.uint32, f.readline().split(' '))
    i=0
    data = [list(map(np.int_, line.split(" "))) for line in f]