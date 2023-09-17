# Day 18. Operation Order
# https://adventofcode.com/2020/day/18

from util.input_util import read_input_file
from collections import deque

def parse_lines():
    lines = read_input_file(18)
    eqs = []
    for l in lines:
        eqs.append(deque(l.replace(' ', '')))
    return eqs

    
# Operators have same precedence left to right
# DFS with parenthesis
ADD = '+'
MULT = '*'


def operate(oper, a, b):
    if oper == ADD: return int(a) + int(b)
    elif oper == MULT: return int(a) * int(b)
    else: raise ValueError("Unknown operator", oper)
    

# Use stack to recursively evaluate parenthesis first
# Simplify expression with parenthesis to one without
# Order from left to right
def eval(expr:deque):
    stack = deque()
    while expr:
        x = expr.popleft()
        if x == ')':
            # pop off stack until we have an expression without parenthesis
            innerexpr = deque()
            while stack[-1] != '(':
                innerexpr.appendleft(stack.pop())
            stack.pop() # pop (
            
            val = eval(innerexpr)
            stack.append(val)
        else:
            stack.append(x)
    
    # evaluate expression without parens from left to right
    while len(stack) > 1:
        a = stack.popleft()
        oper = stack.popleft()
        b = stack.popleft()
        res = operate(oper, a, b)
        stack.appendleft(res)
        
    return stack[0]
        


# Addition before mult
def eval2(expr:deque):
    stack = deque()
    while expr:
        x = expr.popleft()
        if x == ')':
            # pop off stack until we have an expression without parenthesis
            innerexpr = deque()
            while stack[-1] != '(':
                innerexpr.appendleft(stack.pop())
            stack.pop() # pop (
            val = eval2(innerexpr)
            stack.append(val)
        else:
            stack.append(x)
    
    # evaluate expression without parens for addition first
    for i, x in enumerate(stack):
        if x == ADD:
            # sum left and right chars
            # replace value in right
            # replace other values with None
            a = stack[i-1]
            b = stack[i+1]
            res = operate(ADD, a, b)
            stack[i-1] = None
            stack[i] = None
            stack[i+1] = res
            
    # evaluate multiplies
    prod = 1
    for i, x in enumerate(stack):
        if x is not None and x != MULT:
            prod *= int(x)
        
    return prod


def solution1():
    eqs = parse_lines()
    
    sum = 0
    for expr in eqs:
        res = eval(expr)
        sum += res
        
    return sum

    
    
def solution2():
    eqs = parse_lines()
    
    sum = 0
    for expr in eqs:
        res = eval2(expr)
        sum += res
        
    return sum
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())