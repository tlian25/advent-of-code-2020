# Day 8. Handheld Halting
# https://adventofcode.com/2020/day/8

from util.input_util import read_input_file

acc = 'acc' # accumulator
jmp = 'jmp' # jump
nop = 'nop' # no operation

def parse_lines():
    lines = read_input_file(8)
    instructions = []
    for l in lines:
        cmd, n = l.split()
        instructions.append([cmd, int(n)])
    return instructions


def run(instructions):
    count = 0
    idx = 0
    seen = set()
    while idx not in seen and idx < len(instructions):
        seen.add(idx)
        cmd, n = instructions[idx]

        if cmd == acc:
            count += n
            idx += 1
        elif cmd == jmp:
            idx += n
        else: # nop
            idx += 1
    
    # Return accumulator count and boolean if we hit a loop
    return count, idx in seen


def solution1():
    instructions = parse_lines()
    count, _ = run(instructions)
    return count
    
    
def solution2():
    instructions = parse_lines()
    
    for i in range(len(instructions)):
        if instructions[i][0] in (jmp, nop):
            # swap instructions and run
            old = instructions[i][0]
            new = jmp if old == nop else nop
            instructions[i][0] = new
            count, loop = run(instructions)
            if loop == False: return count

            # else revert
            instructions[i][0] = old
        
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())