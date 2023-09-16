# Day 13. SHuttle Search
# https://adventofcode.com/2020/day/13

import math
from util.input_util import read_input_file

X = 'x'

def parse_lines():
    lines = read_input_file(13)
    mins = int(lines[0])
    busses = []
    for i, x in enumerate(lines[1].split(',')):
        if x != X:
            busses.append((int(x), i))
    return mins, busses



def solution1():
    mins, busses = parse_lines()

    earliest_bus = None 
    earliest_time = float('inf')
    for b, _ in busses:
        n = math.ceil(mins / b)
        t = n * b
        if t < earliest_time:
            earliest_time = t
            earliest_bus = b

    wait_time = earliest_time - mins
    return wait_time * earliest_bus
    

def test_t(t, busses):
    for b, i in busses:
        if (t+i) % b != 0: return False
            
    return True



def solution2():
    _, busses = parse_lines()
    # First bus ID departs at time t
    # Each subsequent listed bus ID departs at that subsequent minute

    delta = 1
    i = 0
    
    # Using Chinese remainder theorem. We add to the delta each time.
    for bus, offset in busses:
        while True:
            # Search until we find next number that satisfies offset
            i += delta
            if (i + offset) % bus == 0:
                # Update delta
                delta *= bus
                break

    return i
    

    
    
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())