__author__ = 'bilge'
import sys
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def find_best_estimate(items_sorted, capacity, selections):
    value = 0
    weight = 0
    for itm in range(len(items_sorted)):
        if itm < len(selections) and selections[itm] == 0: continue
        i = items_sorted[itm]
        if weight + i.weight > capacity:
            value += i.value * (((capacity - weight) * 1.0) / i.weight) 
            break
        value += i.value
        weight += i.weight

    return value

class Node():
    best_value = 0
    best_selections = []
    capacity = 0
    items_sorted = []
    
    def __init__(self, value, room, selections, previous_estimate):
        self.value = value
        self.room = room
        self.estimate = previous_estimate if previous_estimate != -1 else find_best_estimate(Node.items_sorted, Node.capacity, selections)
        self.selections = selections
        self.index = len(self.selections)
        
    def left_child(self):
        item = Node.items_sorted[self.index]
        return Node(self.value + item.value, self.room - item.weight, self.selections + [1], self.estimate)
    
    def right_child(self):
        item = Node.items_sorted[self.index]
        return Node(self.value, self.room, self.selections + [0], -1)
    
    def is_leaf(self):
        return self.index == len(Node.items_sorted)
    
def bab_knapsack(capacity, items):
    Node.capacity = capacity
    Node.items_sorted = sorted(items, key = lambda i: i.density, reverse = True)
    Node.best_value = 0
    Node.best_selections = []
    
    root = Node(0, capacity, [], -1)
    stack = [root.right_child(), root.left_child()]
    while stack:
        node = max(stack, key = lambda i: i.value)
        stack.remove(node)
        
        if node.room < 0 or node.estimate < Node.best_value: continue
        
        if node.is_leaf() and node.value > Node.best_value:
            Node.best_value = node.value
            Node.best_selections = node.selections
            continue
        
        if not node.is_leaf():
            stack.append(node.left_child())
            stack.append(node.right_child())
    
    selections = [0] * len(items)
    for idx in range(len(Node.best_selections)):
        if Node.best_selections[idx] == 1: selections[Node.items_sorted[idx].index] = 1
    
    output_data = str(Node.best_value) + '\n'
    output_data += ' '.join(map(str, selections))
    return output_data


def solve(input_data):
    # parse the input
    lines = input_data.split('\n')

    item_count, capacity = map(int, lines[0].split())

    items = []
    for i in range(1, item_count+1):
        v, w = map(int, lines[i].split())
        items.append(Item(i-1, v, w, (v * 1.0) / w))


    return bab_knapsack(capacity, items)


if __name__ == '__main__':
    file_location = sys.argv[1]
    input_data_file = open(file_location, 'r')
    input_data = ''.join(input_data_file.readlines())
    output = solve(input_data)
    print(output)
