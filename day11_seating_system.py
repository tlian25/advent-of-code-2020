# Day 11. Seating System
# https://adventofcode.com/2020/day/11

from util.input_util import read_input_file
from collections import defaultdict


OCC = "#"
EMPTY = "L"
FLOOR = "."

def parse_lines():
    lines = read_input_file(11)
    grid = []
    for l in lines:
        grid.append(list(l))
    return grid

grid = parse_lines()
NR = len(grid)
NC = len(grid[0])


def print_grid():
    for row in grid:
        print(''.join(row))

# If seat is empty and no occupied seats adjacent, seat becomes occ
# If seat is occ, and four or more seats adjacent, the seat becomes empty
# Otherwise seat's state does not change
# Floor never changes
# 8 directions around seat


DIRS = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

def adjacent(r, c):
    adjcount = 0
    for dr, dc in DIRS:
        nr = r+dr
        nc = c+dc
        if 0 <= nr < NR and 0 <= nc < NC and grid[nr][nc] == OCC:
            adjcount += 1
    
    return adjcount



def create_adjacentdircache():
    cache = defaultdict(list)

    for r in range(NR):
        for c in range(NC):
            # Get all adjacents in each direction
            if grid[r][c] == FLOOR:
                continue
            
            for dr, dc in DIRS:
                nr = r+dr
                nc = c+dc
                while 0 <= nr < NR and 0 <= nc < NC:
                    if grid[nr][nc] in (OCC, EMPTY):
                        cache[(r,c)].append((nr, nc))
                        break
                    else:
                        nr += dr
                        nc += dc
    return cache


cache = create_adjacentdircache()

def adjacentdir(r, c):
    adjcount = 0
    for nr, nc in cache[(r,c)]:
        if grid[nr][nc] == OCC:
            adjcount += 1
    
    return adjcount


def run(adjfunc, count):
    # First mark everything then change all at once
    toChange = []
    for r in range(NR):
        for c in range(NC):
            s = grid[r][c]
            if s == FLOOR:
                continue
            
            adjcount = adjfunc(r, c)
            if s == EMPTY and adjcount == 0:
                toChange.append((r,c))
            elif s == OCC and adjcount >= count:
                toChange.append((r,c))
                
    for r, c in toChange:
        grid[r][c] = OCC if grid[r][c] == EMPTY else EMPTY 

    return len(toChange)


def count_occuppied():
    count = 0
    for r in range(NR):
        for c in range(NC):
            if grid[r][c] == OCC:
                count += 1
    return count
    

def solution1():
    changed = run(adjacent, 4)

    while changed > 0 :
        changed = run(adjacent, 4)
    
    return count_occuppied()
    

def solution2():
    changed = run(adjacentdir, 5)

    while changed:
        changed = run(adjacentdir, 5)
    
    return count_occuppied()
    
    
    
if __name__ == '__main__':
    # Since we mutate grid, only run one solution at a time or will clash
    # print(solution1())
    
    print('--------------')
    
    print(solution2())