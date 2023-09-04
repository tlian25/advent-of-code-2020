# Day 5. Binary Boarding
# https://adventofcode.com/2020/day/5

from util.input_util import read_input_file
from collections import deque

F = 'F'
B = 'B'
R = 'R'
L = 'L'

NR = 128
NC = 8

# Create binary trees
class Node:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.val = None
        self.right = None
        self.left = None
        
def create_tree(lo, hi):
    head = Node(lo, hi)
    q = deque([head])
    while q:
        curr = q.popleft()
        if curr.lo != curr.hi:
            # Create left and right
            m = (curr.lo + curr.hi) // 2
            curr.left = Node(curr.lo, m)
            curr.right = Node(m+1, curr.hi)
            q.append(curr.left)
            q.append(curr.right)
        else:
            # end
            curr.val = curr.lo
        
    return head
            
ROWTREE = create_tree(0, 127)
COLTREE = create_tree(0, 7)

def parse_lines():
    lines = read_input_file(5)
    return lines
    
    
def seatID(line):
    currrow = ROWTREE
    currcol = COLTREE

    for l in line:
        if l == F:
            currrow = currrow.left
        elif l == B:
            currrow = currrow.right
        elif l == L:
            currcol = currcol.left
        elif l == R:
            currcol = currcol.right
        else:
            raise ValueError("Unknown", l)
    
    row = currrow.val
    col = currcol.val
    return row * 8 + col

def solution1():
    
    mxseatid = 0
    for line in parse_lines():
        seatid = seatID(line)
        mxseatid = max(mxseatid, seatid)
    
    return mxseatid
                
    
    
def solution2():
    seatids = []
    for line in parse_lines():
        seatid = seatID(line)
        seatids.append(seatid)
    
    seatids.sort()
    
    for i, n in enumerate(seatids):
        if seatids[i+1] - n == 2:
            return seatids[i+1] - 1
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())