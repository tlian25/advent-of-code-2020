# Day 6. Custom Customs 
# https://adventofcode.com/2020/day/6

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(6)
    return lines

# 26 y/n questions marked a-z
# anyone is gorup answers yes


def solution1():
    total_counts = 0
    curr = set()
    for l in parse_lines():
        if l == '':
            total_counts += len(curr)
            curr = set()
        else:
            for ans in l:
                curr.add(ans)
                
    return total_counts
    
    
def solution2():
    total_counts = 0
    curr = None
    for l in parse_lines():
        if l == '':
            total_counts += len(curr)
            curr = None
        elif curr is None:
            curr = set(l)
        else:
            curr = curr.intersection(set(l))
                
    return total_counts
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())