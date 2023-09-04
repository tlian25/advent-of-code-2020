# Day 2. Password Philosophy
# https://adventofcode.com/2020/day/2

from util.input_util import read_input_file
from collections import Counter

def parse_lines():
    policy = []
    lines = read_input_file(2)
    for l in lines:
        counts, letter, pwd = l.split()
        low, high = counts.split('-')
        letter = letter.replace(':', '')
        policy.append((int(low), int(high), letter, pwd))
    
    return policy


# Each line gives the password policy and then the password
# Policy indicates the lowest and highest number of times a given letter must appear
# For the password to be valid.


def solution1():
    policy = parse_lines()
    valid_count = 0
    for low, high, letter, pwd in policy:
        counts = Counter(pwd)
        if letter in counts and low <= counts[letter] <= high:
            valid_count += 1
            
    return valid_count
        
    
    
def solution2():
    policy = parse_lines()
    valid_count = 0
    for idx1, idx2, letter, pwd in policy:
        if pwd[idx1-1] == letter and pwd[idx2-1] == letter:
            pass
        elif pwd[idx1-1] == letter or pwd[idx2-1] == letter:
            valid_count += 1
    
    return valid_count



    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())