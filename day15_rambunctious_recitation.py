# Day 15. Rambunctious Recitation
# https://adventofcode.com/2020/day/15

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(15)
    return [int(x) for x in lines[0].split(',')]


# List of starting numbers
# consider most recently spoken number
# If first time -> current player plays 0
# otherwise -> current player announces how many turns apart the number is when it was spoken
# After staring numbers -> each turn either 0 or age


def solution1():
    start = parse_lines()
    print(start)
    last = {}
    
    prev = None
    for i, n in enumerate(start[:-1]):
        last[n] = i
    
    prev = start[-1]
    for i in range(i+2, 2020):
        # print('turn', i+1, 'prev', prev)
        if prev not in last:
            newprev = 0
        else:
            newprev = i - last[prev] - 1
        
        last[prev] = i-1
        prev = newprev
        # print(i+1, prev)
    return prev
            
        
        
    
    
    
def solution2():
    start = parse_lines()
    print(start)
    last = {}
    
    prev = None
    for i, n in enumerate(start[:-1]):
        last[n] = i
    
    prev = start[-1]
    for i in range(i+2, 30000000):
        # print('turn', i+1, 'prev', prev)
        if prev not in last:
            newprev = 0
        else:
            newprev = i - last[prev] - 1
        
        last[prev] = i-1
        prev = newprev
        # print(i+1, prev)
    return prev
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())