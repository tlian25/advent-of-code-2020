# Day 24. Lobby Layout
# https://adventofcode.com/2020/day/24

from collections import deque
from util.input_util import read_input_file

E = 'e'
SE = 'se'
SW = 'sw'
W = 'w'
NW = 'nw'
NE = 'ne'

DIRS = {E: (1,0), SE: (0.5, -0.5), NE: (0.5, 0.5),
       W: (-1,0), SW: (-0.5, -0.5), NW: (-0.5, 0.5)}

'''
    NE  NW
E           W
    SE  SW
'''

WHITE = 'white'
BLACK = 'black'

class Tile:
    def __init__(self, color=WHITE):
        self.color = color
    
    def flip(self):
        self.color = BLACK if self.color == WHITE else WHITE

    def isBlack(self):
        return self.color == BLACK


def parse_lines():
    lines = read_input_file(24)
    instructions = []
    for l in lines:
        l = deque(l)
        ins = []
        while l:
            a = l.popleft()
            if a not in {E, W}:
                a += l.popleft()
            
            assert a in {E, SE, SW, W, NW, NE}, a
            ins.append(a)

        instructions.append(ins)
    return instructions
    
# Hexagonal - white/black
# list of tiles that need to be flipped over
# reference tile in the middle of the room

def traverse(curr, ins, GRID):
    for d in ins:
        x, y = curr
        dx, dy = DIRS[d]
        nxt = (x + dx, y + dy)        
        curr = nxt
    
    if nxt in GRID:
        GRID[curr].flip()
    else:
        GRID[curr] = Tile(BLACK)
        
        
def count_black(GRID):
    # Count number of black tiles
    count = 0
    for _, t in GRID.items():
        if t.isBlack():
            count += 1
    
    return count
    


def solution1():
    instructions = parse_lines()
    GRID = {(0,0): Tile(WHITE)}

    for ins in instructions:
        ref = (0, 0)
        traverse(ref, ins, GRID)
    
    # Count number of black tiles
    return count_black(GRID)
    
# Any BLACK tile with zero or >2 BLACK nbs -> WHITE
# Any WHITE tile with exactly 2 BLACK nbs -> BLACK


def day(GRID):
    # Mark GRID by 1 around the perimeter
    toBeAdded = []
    for xy, t in GRID.items():
        for dx, dy in DIRS.values():
            nb = xy[0]+dx, xy[1]+dy
            if nb not in GRID:
                toBeAdded.append(nb)
    
    # Expand GRID
    for xy in toBeAdded:
        GRID[xy] = Tile(WHITE)
    
    # Mark to be flipped
    toBeFlipped = []
    for xy, t in GRID.items():
        blackNbs = 0
        for dx, dy in DIRS.values():
            nb = xy[0]+dx, xy[1]+dy
            if nb in GRID and GRID[nb].isBlack():
                blackNbs += 1
        
        if t.isBlack():
            if blackNbs == 0 or blackNbs > 2:
                toBeFlipped.append(xy)
        else:
            if blackNbs == 2:
                toBeFlipped.append(xy)
        
    # Flip all at once
    for xy in toBeFlipped:
        GRID[xy].flip()


def solution2():
    instructions = parse_lines()
    GRID = {(0,0): Tile(WHITE)}

    for ins in instructions:
        ref = (0, 0)
        traverse(ref, ins, GRID)
    
    #
    for d in range(100):
        day(GRID)
    
    # Count number of black tiles
    return count_black(GRID)
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())