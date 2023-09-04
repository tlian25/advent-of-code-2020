# Day 1. Report Repair
# https://adventofcode.com/2020/day/1

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(1)
    return [int(l) for l in lines]



def solution1():
    lines = parse_lines()
    seen = set()
    for n in lines:
        if 2020 - n in seen:
            # found
            return n * (2020 - n)
        else:
            seen.add(n)

        
    
def solution2():
    lines = parse_lines()
    nums = set(lines)
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            n1 = lines[i]
            n2 = lines[j]
            n3 = 2020 - n1 - n2
            if n3 in nums:
                return n1 * n2 * n3
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())