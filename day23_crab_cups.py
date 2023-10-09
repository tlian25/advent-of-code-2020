# Day 23. Crab Cups
# https://adventofcode.com/2020/day/23

from collections import deque
from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(23)
    return deque([int(x) for x in lines[0]])


# Cups clockwise
# each move
# - current cup
# - picks up 3 next cups after current cup
# - selects a destination cup -> label equal to current cups's label minus one
# - keep subtracting one until finds a cup that wasn't picked up
# - wraps around to highest value cup instead
# - places pikced up cups immediately counter clockwise of destination cup

def find_next(curr, c1, c2, c3, mx):
    next = curr-1
    next = next if next else mx
    while next in {c1, c2, c3}:
        next = next-1
        next = next if next else mx
    return next


def round(cups):
    curr = cups.popleft()
    c1 = cups.popleft()
    c2 = cups.popleft()
    c3 = cups.popleft()
    
    # find next cup
    next = find_next(curr, c1, c2, c3, 9)
    idx = cups.index(next)
    cups = list(cups)
    cups = deque(cups[:idx+1] + [c1, c2, c3] + cups[idx+1:] + [curr])
    return cups


def solution1():
    cups = parse_lines()
    for _ in range(100):
        cups = round(cups)

    idx = cups.index(1)
    cups = list(cups)
    cups = cups[idx+1:] + cups[:idx]
    return ''.join([str(x) for x in cups])


def find_next_node(curr, c1, c2, c3, mx):
    next = curr.val-1
    next = next if next else mx
    while next in {c1.val, c2.val, c3.val}:
        next = next-1
        next = next if next else mx
    return next


## Use a linked list
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
    def __repr__(self):
        return f'{self.val}'

    
def solution2():
    # TLE
    cups = parse_lines()
    m = {}
    head = Node()
    m['head'] = head
    prev = head
    for i in range(10, 1_000_001):
        cups.append(i)

    for c in cups:
        m[c] = Node(c)
        prev.next = m[c]
        prev = m[c]

    # Connect circle
    prev.next = head.next

    curr = head.next
    for i in range(10_000_000):
        # pick up next 3
        c1 = curr.next
        c2 = c1.next
        c3 = c2.next
        nxt = c3.next

        curr.next = nxt # connect curr with next

        # Find place to put the 3 we picked up
        nextidx = find_next_node(curr, c1, c2, c3, 1_000_000)
        
        # insert picked up nodes
        tmp = m[nextidx].next
        m[nextidx].next = c1
        c3.next = tmp
        
        # Set new curr
        curr = nxt
        
    n1 = m[1].next.val
    n2 = m[1].next.next.val
    return n1 * n2

    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())