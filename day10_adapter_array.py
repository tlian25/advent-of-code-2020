# Day 10. Adapter Array
# https://adventofcode.com/2020/day/10

from util.input_util import read_input_file
from collections import deque

def parse_lines():
    lines = read_input_file(10)
    adapters = [int(x) for x in lines]
    adapters.sort()
    adapters += [adapters[-1]+3]
    return adapters


# Can take an input 1,2,3 jolts lower than rating
# Built-int adapter for 3 jolts higher than highest


def solution1():
    adapters = parse_lines()
    count1 = 0
    count3 = 0
    curr = 0
    for i, a in enumerate(adapters):
        diff = a - curr

        if diff == 1:
            count1 += 1
        elif diff == 3:
            count3 += 1
        
        curr = a
    
    return count1 * count3
            
    
def solution2():
    adapters = parse_lines()

    q = deque()
    for i, a in enumerate(adapters):
        if a <= 3:
            q.append(i)

    cache = [0 for _ in range(max(adapters)+1)]
    cache[0] = 1

    for i, a in enumerate(adapters):
        for offset in (1,2,3):
            if a - offset >= 0:
                cache[a] += cache[a-offset]
        
    return cache[-1]

    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())