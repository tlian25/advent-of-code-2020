# Day 19. Monster Messages
# https://adventofcode.com/2020/day/19

from util.input_util import read_input_file
from collections import deque

# Build graph of rules
class Node:
    def __init__(self, name:str=""):
        self._n = name
        self._and = None
        self._or = None
        self._eq = None
    
    def __repr__(self):
        return f'[\'{self._n}\'] - EQ: {self._eq}; AND: {self._and}; OR: {self._or}'


def parse_lines():
    lines = read_input_file(19)
    graph = {}
    for i, l in enumerate(lines):
        if l == '': break
        n, rule = l.split(': ')
        node = Node(n)
        if '"' in rule:
            node._eq = set([rule.replace('"', '')])
        elif '|' in rule:
            part1, part2 = rule.split(' | ')
            n1 = Node(n+'a')
            n1._and = part1.split()
            n2 = Node(n+'b')
            n2._and = part2.split()
            node._or = [n+'a', n+'b']
            
            graph[n+'a'] = n1
            graph[n+'b'] = n2
        else:
            node._and = rule.split()
        graph[n] = node
        
    inputs = lines[i+1:]
    return graph, inputs


# "b" -> match single character
#  1 2 -> must match rule 1 then match rule 2

# DFS 
def traverse(n:str, graph:dict):
    node = graph[n]
    if node._eq:
        return node._eq
    
    if node._or:
        s = set()
        for n in node._or:
            for ss in traverse(n, graph):
                s.add(ss)
        
        return s
    
    if node._and:
        p = deque() # list of sets
        for n in node._and:
            p.append(traverse(n, graph))
            
            
        s = p.popleft()
        while p:
            newset = set()
            pp = p.popleft()
            for ss in s:
                for ppp in pp:
                    newset.add(ss+ppp)
            s = newset
                
        return s
            
def solution1():
    graph, inputs = parse_lines()
    
    # Rule 0 - graph traversal
    s = traverse('0', graph)
    
    count = 0
    for ip in inputs:
        if ip in s:
            count += 1
            
    return count
        
    
    
    
def solution2():
    # Replace Rule 8 and 11
    graph, inputs = parse_lines()
    
    # 0: 8 11
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    
    # 0: 8 11
    # 8 -> some number of repeat of 42s
    # 11 -> either 42 + 31 or 42 42 + 31 31
    # Combined - repeat of 42s + repeat of 31s
    
    rule42 = traverse('42', graph)
    rule31 = traverse('31', graph)
    
    lens = set()
    for r in rule42.union(rule31):
        lens.add(len(r))
        
    assert len(lens) == 1, f"Expect only one length. {lens}"
    
    # Both rule 42 and rule 31 are combinations of length 8
    # No intersections
    
    def segmentate(input, L):
        if len(input) % L != 0: return False
        
        totalsegcount = len(input) // L
        # first segment must be in 42
        # Number of 42 segments must be greater than number of 31 segments + 1
        seg42count = 0
        seg31count = 0
        
        i = 0
        while i < len(input):
            seg = input[i:i+L]
            if seg in rule42:
                seg42count += 1
                i += L
            else:
                # Either in rule31 or not at all
                while i < len(input):
                    seg = input[i:i+L]
                    if seg in rule31:
                        seg31count += 1
                        i += L
                    else:
                        return False
                    
        if seg42count < 2: return False
        if seg31count == 0: return False
        if seg31count > seg42count - 1: return False
        if seg42count + seg31count != totalsegcount: return False
        return True
            
    
    count = 0
    L = lens.pop()
    for i in inputs:
        if segmentate(i, L):
            count += 1
            
    return count
        
        

    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())