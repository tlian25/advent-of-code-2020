# Day 14. Docking Data
# https://adventofcode.com/2020/day/14

from util.input_util import read_input_file


def parse_lines():
    lines = read_input_file(14)
    instructions = []
    for l in lines:
        l = l.split()
        if l[0] == 'mask':
            instructions.append((l[0], l[2]))
        else:
            key = l[0].replace('mem[','').replace(']','')
            instructions.append(('mem', int(key), int(l[2])))
    
    return instructions


def apply_mask(val, mask):
    s = list(format(val, 'b').zfill(36))
    for i, v in enumerate(mask):
        if v != 'X':
            s[i] = v

    return int(''.join(s), 2)


def apply_mask2(key, val, mask, mem):
    s = list(format(key, 'b').zfill(36))
    wildcards = []
    for i, v in enumerate(mask):
        if v == '1':
            s[i] = '1'
        elif v == 'X':
            s[i] = '0'
            wildcards.append(i)
    
    
    base = int(''.join(s), 2)
    keys = set([base])
    for i in wildcards:
        newkeys = keys.copy()
        for k in keys:
            n = 2 ** (35-i)
            newkeys.add(k+n)
        keys = newkeys
    for k in keys:
        mem[k] = val
        
    
def solution1():
    instructions = parse_lines()
    mem = {}
    mask = None
    for inst in instructions:
        if inst[0] == 'mask':
            # transform to a dict of instructions
            mask = inst[1]
        else:
            mem[inst[1]] = apply_mask(inst[2], mask)
    
    return sum(mem.values())


def solution2():
    instructions = parse_lines()
    mem = {}
    mask = None
    for inst in instructions:
        if inst[0] == 'mask':
            mask = inst[1]
        else:
            key, val = inst[1], inst[2]
            apply_mask2(key, val, mask, mem)
            
    return sum(mem.values())
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())