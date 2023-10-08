# Day 21. Allergen Assessment
# https://adventofcode.com/2020/day/21

import re
from collections import defaultdict
from heapq import heappop, heappush

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(21)
    foods = []
    for l in lines:
        idx = l.index('(')
        allergens = l[idx+1:-1].replace('contains ', '').split(', ')
        ingreds = l[:idx-1].split()
        foods.append((set(ingreds), set(allergens)))
        
    return foods
        


# Each allergen is found in exactly one ingredient
# Each ingredient contians zero or one allergen


def build_sets(foods) -> (set, dict):
    # For each allergen, list possible ingredients containing it
    possible = {}
    all_ings = set()
    for ing, algs in foods:
        all_ings = all_ings.union(ing)
        for a in algs:
            if a in possible:
                possible[a] = possible[a].intersection(ing)
            else:
                possible[a] = ing

    return all_ings, possible
    
            
def allergen_free_ings(all_ings, possible) -> set:
    for a, ings in possible.items():
        all_ings -= ings
        
    return all_ings


def count_appearances(foods):
    counts = defaultdict(int)
    for ings, _ in foods:
        for i in ings:
            counts[i] += 1
            
    return counts


def solution1():
    foods = parse_lines()
    all_ings, possible = build_sets(foods)
    free_ings = allergen_free_ings(all_ings, possible)
    counts = count_appearances(foods)

    res = 0
    for i in free_ings:
        res += counts[i]
        
    return res
    
    
    
def solution2():
    foods = parse_lines()
    all_ings, possible = build_sets(foods)
    free_ings = allergen_free_ings(all_ings, possible)
    
    h = [] # heap
    for algs, ings in possible.items():
        ings = ings - free_ings
        heappush(h, (len(ings), algs, ings))
        
    res = [] # results (alg, ing) to allow sorting alphabetically by allergen
    tmp = [] # store temp results to add back to heap
    seen = set()
    while h:
        _, alg, ings = heappop(h)
        ings = ings - seen
        count = len(ings)

        if count == 1: #found a match
            i = ings.pop()
            seen.add(i)
            res.append((alg, i))
            
            # Add any tmp back to heap
            while tmp:
                heappush(h, tmp.pop())
        
        else: # keep popping stuff off heap
            tmp.append((count, alg, ings))
    
    res.sort()
    return ','.join([r[1] for r in res])

            
        
        
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())