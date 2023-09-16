# Day 16. Ticket Translation
# https://adventofcode.com/2020/day/16

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(16)
    
    # Fields
    fields = {}
    for i, l in enumerate(lines):
        if l == '': break
        f = l.split(':')[0]
        r1, r2 = l.split(': ')[1].split(' or ')
        r1 = tuple(int(x) for x in r1.split('-'))
        r2 = tuple(int(x) for x in r2.split('-'))
        fields[f] = [r1, r2]
        
    # My Ticket
    ticket = [int(x) for x in lines[i+2].split(',')]
    
    othertickets = []
    for l in lines[i+5:]:
        othertickets.append([int(x) for x in l.split(',')])
    
    return fields, ticket, othertickets


def binary_search(x, ranges):
    i, j = 0, len(ranges)
    while i < j:
        m = (i+j) // 2
        r = ranges[m]
        if r[0] <= x <= r[1]: return True
        
        elif x < r[0]:
            j = m
        else:
            i = m+1
    return False


def solution1():
    fields, ticket, otickets = parse_lines()
    allranges = []
    for _, rng in fields.items():
        allranges += rng
        
    allranges.sort()
    invalid = []
    for t in otickets:
        for n in t:
            if not binary_search(n, allranges):
                invalid.append(n)
                
    return sum(invalid)



def solution2():
    fields, ticket, otickets = parse_lines()
    allranges = []
    for _, rng in fields.items():
        allranges += rng
        
    allranges.sort()
    validtickets = []
    for t in otickets:
        valid = True
        for n in t:
            if not binary_search(n, allranges):
                valid = False
                break
        
        if valid:
            validtickets.append(t)

    fieldcols = {f:set(range(len(ticket))) for f in fields}
    
    for t in validtickets:
        for i, n in enumerate(t):
            for f in fieldcols:
                valid = True
                if i in fieldcols[f]:
                    valid = binary_search(n, fields[f])
            
                if not valid:
                    fieldcols[f].remove(i)
    
    # Sort all fields by number of possibilities in ascending order    
    fieldcounts = [(len(x), k, x) for k, x in fieldcols.items()]
    fieldcounts.sort()
    
    # Starting from least possibilities, narrow down possible index for each field
    # i.e. first field has 1 possibility 
    # second field has 2 possibilities, but only 1 left after first field is assigned
    fieldidx = {}
    seen = set()
    for _, f, possible in fieldcounts:
        fieldidx[f] = possible.difference(seen).pop()
        seen = seen.union(possible)
    
    # Product of departure fields
    s = 1
    for f in fieldidx:
        if 'departure' in f:
            s *= ticket[fieldidx[f]]
            
    return s
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())