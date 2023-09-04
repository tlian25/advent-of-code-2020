# Day 3. Toboggan Trajectory
# https://adventofcode.com/2020/day/3

from util.input_util import read_input_file

TREE = '#'
OPEN = '.'

def parse_lines():
    grid = []
    lines = read_input_file(3)
    for l in lines:
        grid.append(list(l))
    return grid

# Wrap around grid

def count_trees_on_slope(grid, right, down):
    NR = len(grid)
    NC = len(grid[0])
    r = 0
    c = 0
    trees = 0
    while r < NR:
        if grid[r][c] == TREE:
            trees += 1
        c = (c + right) % NC # wrap around
        r += down
    
    return trees
        
        
        
def solution1():
    grid = parse_lines()
    return count_trees_on_slope(grid, 3, 1) 

    
    
    
def solution2():
    grid = parse_lines()
    product = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees = count_trees_on_slope(grid, right, down)
        product *= trees
    
    return product
        
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())