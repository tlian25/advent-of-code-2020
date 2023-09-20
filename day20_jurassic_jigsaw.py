# Day 20. Jurassic Jigsaw
# https://adventofcode.com/2020/day/20

from util.input_util import read_input_file
from collections import defaultdict

class Tile:
    def __init__(self, n, grid):
        self._n = n
        self._grid = grid
    
    # Rotate 90 degrees counterclockwise
    def rotate90left(self):
        # flip x and y
        # then reverse order rows
        for x in range(10):
            for y in range(x):
                self._grid[x][y], self._grid[y][x] = self._grid[y][x], self._grid[x][y]
        self._grid.reverse()
        
    def rotate90right(self):
        self.rotate90left()
        self.rotate90left()
        self.rotate90left()
        
    
    def fliphorizontal(self):
        for row in self._grid:
            row.reverse()
            
    def flipvertical(self):
        self._grid.reverse()
            
        

    def __repr__(self):
        s = f'Tile: {self._n}:\n'
        for row in self._grid:
            s += ''.join(row) + '\n'
        return s


def parse_lines():
    lines = read_input_file(20)
    n = None
    grid = []
    tiles = []
    for l in lines:
        if 'Tile' in l:
            n = l.split()[1][:-1]
        elif l == '':
            t = Tile(n, grid)
            tiles.append(t)
            grid = []
        else:
            grid.append(list(l))
    
    return tiles
    
        
            
            
        

def solution1():
    tiles = parse_lines()
    
    # Four corner tiles
    sides = defaultdict(list)
    for t in tiles:
        n = t._n
        top = ''.join(t._grid[0])
        bot = ''.join(t._grid[-1])
        if top in sides:
            sides[top].append(n)
        elif top[::-1] in sides:
            sides[top[::-1]].append(n)
        else:
            sides[top].append(n)
            
        if bot in sides:
            sides[bot].append(n)
        elif bot[::-1] in sides:
            sides[bot[::-1]].append(n)
        else:
            sides[bot].append(n)
            
        t.rotate90right()
        top = ''.join(t._grid[0])
        bot = ''.join(t._grid[-1])
        if top in sides:
            sides[top].append(n)
        elif top[::-1] in sides:
            sides[top[::-1]].append(n)
        else:
            sides[top].append(n)
            
        if bot in sides:
            sides[bot].append(n)
        elif bot[::-1] in sides:
            sides[bot[::-1]].append(n)
        else:
            sides[bot].append(n)

    
    outsidetiles = defaultdict(int)
    for s, ts in sides.items():
        if len(ts) == 1:
            outsidetiles[ts[0]] += 1
    
    res = 1
    for t, count in outsidetiles.items():
        if count == 2:
            print(t)
            res *= int(t)
            
    return res
    
    
    
    
    
    
    
def solution2():
    pass
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())