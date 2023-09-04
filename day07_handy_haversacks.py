# Day 7. Handy Haversacks
# https://adventofcode.com/2020/day/7

from util.input_util import read_input_file


class Bag:
    def __init__(self, color):
        self.color = color
        self.holds = {}
    
    def __str__(self):
        return f'Color: {self.color} - Holds: {set(self.holds.keys())}'
    
    def __repr__(self):
        return self.__str__()

graph = {}

def parse_lines():
    # Read twice. Once to create all bags
    lines = read_input_file(7)
    
    for l in lines:
        b, holds = l.split(' contain ')
        b = b.replace(' bags', '')
        graph[b] = Bag(b)

        if 'no' in holds:
            continue

        holds = holds.replace('.', '').split(', ')
        for h in holds:
            
            count = int(h.split()[0])
            color = ' '.join(h.split()[1:3]).replace(' bag', '').replace(' bags', '')
            if color not in graph:
                graph[color] = Bag(color)
            graph[b].holds[color] = (graph[color], count)
            

# Create DAG of bags
def solution1():
    parse_lines()
    
    seen = set(['shiny gold'])
    valid = set(['shiny gold'])
    
    def dfs(color):
        if color in seen:
            return color in valid
        
        seen.add(color)
        if 'shiny gold' in graph[color].holds:
            valid.add(color)
            return True
        
        for h in graph[color].holds:
            if dfs(h):
                valid.add(h)
                valid.add(color)
                return True
            
        return False
                
    for color in graph:
        dfs(color)
    
    return len(valid) - 1 # don't count shiny gold bag itself
        
    
        

    
def solution2():
    parse_lines()
    
    def dfs(color):
        total = 1 # self
        for h in graph[color].holds:
            bag, count = graph[color].holds[h]
            total += count * dfs(bag.color)

        return total 
                
    return dfs('shiny gold') - 1
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())