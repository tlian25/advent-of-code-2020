# Day 25. Combo Breaker
# https://adventofcode.com/2020/day/25

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(25)
    return int(lines[0]), int(lines[1])

# Transforms a subject number
# Start with 1, then a number of times called the loop size
# Set value to itself multiplied by subject number
# Set value to remainder after dividing value by 20201227

# Card always uses specific secret loop size
# Door always uses a different, secret loop size

# Card transform -> card public key
# Door transform -> door public key

# Have both pks but neither loop size
# Card transforms door's pk -> encryption key
# Door transforms card's pk -> encryption key
# Encryption key should match

def transform(subject, loopsize):
    n = 1
    MOD = 20201227
    for _ in range(loopsize):
        n = (n * subject) % MOD
    
    return n


def solution1():
    cpk, dpk = parse_lines()
    
    # Find card loop
    cls, dls = None, None
    n = 1
    MOD = 20201227
    SUBJECT = 7

    for loopsize in range(1_000_000_000):
        n = (n * SUBJECT) % MOD
        if loopsize % 1_000_000 == 0:
            print(loopsize, '\r', end='')

        if n == cpk:
            print("Card loop size:", loopsize)
            cls = loopsize + 1
        if n == dpk: 
            print("Door loop size:", loopsize)
            dls = loopsize + 1

        if cls and dls:
            break
    
    # Transform either cpk with dls or dpk with cls -> same encryption key
    ek1 = transform(cpk, dls)
    ek2 = transform(dpk, cls)
    assert ek1 == ek2, f'{ek1} - {ek2}'
    return ek1


    
    
def solution2():
    pass
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())