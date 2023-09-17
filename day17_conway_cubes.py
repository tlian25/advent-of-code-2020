# Day 17. Conway Cubes
# https://adventofcode.com/2020/day/17

from util.input_util import read_input_file
from collections import deque

ACTIVE = '#'
INACTIVE = '.'

# 6 cycle bootup
# If cube is active and exactly 2 or 3 nbs also active -> remain active
# If cube is inactive and exactly 3 nbs is active -> active
DIRS3 = []
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        for z in (-1, 0, 1):
            if x == 0 and y == 0 and z == 0:
                continue
            DIRS3.append((x, y, z))
            
            
DIRS4 = []
for w in (-1, 0, 1):
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                if w == 0 and x == 0 and y == 0 and z == 0:
                    continue
                DIRS4.append((w, x, y, z))

def parse_lines():
    lines = read_input_file(17)
    grid = []
    for l in lines:
        grid.append(list(l))
    
    cubes3 = {}
    cubes4 = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            cubes3[(x, y, 0)] = grid[x][y]
            cubes4[(x, y, 0, 0)] = grid[x][y]
    
    return cubes3, cubes4


def run3(cubes):
    newcubes = cubes.copy()
    
    # Expand cube by 1 in all dimensions
    q = set()
    for x, y, z in cubes:
        q.add((x, y, z))
        for dx, dy, dz in DIRS3:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            
            if (nx, ny, nz) not in q:
                q.add((nx, ny, nz))
                
    for x, y, z in q:
        activenbs = 0
        for dx, dy, dz in DIRS3:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            
            if (nx, ny, nz) in cubes and cubes[(nx, ny, nz)] == ACTIVE:
                activenbs += 1
                
        if (x, y, z) in cubes: status = cubes[(x, y, z)]
        else: status = INACTIVE
                
        if status == ACTIVE and 2 <= activenbs <= 3:
            pass # remain active
        elif status == INACTIVE and activenbs == 3:
            newcubes[(x, y, z)] = ACTIVE
        else:
            newcubes[(x, y, z)] = INACTIVE
        
    return newcubes


def run4(cubes):
    newcubes = cubes.copy()
    
    # Expand cube by 1 in all dimensions
    q = set()
    for w, x, y, z in cubes:
        q.add((w, x, y, z))
        for dw, dx, dy, dz in DIRS4:
            nw = w + dw
            nx = x + dx
            ny = y + dy
            nz = z + dz
            
            if (nw, nx, ny, nz) not in q:
                q.add((nw, nx, ny, nz))
                
    for w, x, y, z in q:
        activenbs = 0
        for dw, dx, dy, dz in DIRS4:
            nw = w + dw
            nx = x + dx
            ny = y + dy
            nz = z + dz
            
            if (nw, nx, ny, nz) in cubes and cubes[(nw, nx, ny, nz)] == ACTIVE:
                activenbs += 1
                
        if (w, x, y, z) in cubes: status = cubes[(w, x, y, z)]
        else: status = INACTIVE

        if status == ACTIVE and 2 <= activenbs <= 3:
            pass # remain active
        elif status == INACTIVE and activenbs == 3:
            newcubes[(w, x, y, z)] = ACTIVE
        else:
            newcubes[(w, x, y, z)] = INACTIVE
        
    return newcubes




def solution1():
    cubes, _ = parse_lines()
    for _ in range(6):
        cubes = run3(cubes)
    
    return sum([1 if x == ACTIVE else 0 for x in cubes.values()])
    




def solution2():
    _, cubes = parse_lines()
    for _ in range(6):
        cubes = run4(cubes)
    
    return sum([1 if x == ACTIVE else 0 for x in cubes.values()])
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())