# Day 9. Encoding Error
# https://adventofcode.com/2020/day/9

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(9)
    return [int(x) for x in lines]

    
# Preamble of 25 numbers
# After that each number should be the sum of any two of the 25 immediately previous numbers
# 

def run(nums):
    # First number that does not have this property
    # first 25 numbers store in a set
    preamble_length = 25
    preamble = set(nums[:preamble_length])
    res = []
    
    
    # scan through
    for i in range(preamble_length, len(nums)):
        # check i-th num is a sum of two numbers in preamble
        n = nums[i]
        
        found = False
        for p in preamble:
            if n-p in preamble:
                found = True
                break
        
        if not found: 
            res.append(i)
                
        # remove FIFO
        m = nums[i-25]
        preamble.remove(m)
        preamble.add(n)
    
    return res


def solution1():
    nums = parse_lines()
    res = run(nums)
    return nums[res[0]]
    
    
def solution2():
    N = 69316178
    nums = parse_lines()
    i, j = 0, 0
    S = 0
    
    for j in range(len(nums)):
        S += nums[j]
        
        while S > N and i < j:
            S -= nums[i]
            i += 1
        
        if S == N: break
    
    # List is i-j
    l = nums[i:j+1]
    return min(l) + max(l)
    
            

            
            
        
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())