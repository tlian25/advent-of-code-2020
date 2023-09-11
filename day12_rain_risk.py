# Day 12. Rain Risk
# https://adventofcode.com/2020/day/12

from util.input_util import read_input_file

N, S, E, W = 'N', 'S', 'E', 'W'
F, B, L, R = 'F', 'B', 'L', 'R'
DIRS = [N, E, S, W]

def parse_lines():
    lines = read_input_file(12)
    inst = []
    for l in lines:
        d = l[0]
        c = int(l[1:])
        inst.append((d, c))
    return inst



def turn(face, dir, amount):
    n = amount // 90
    idx = DIRS.index(face)
    if dir == L:
        idx = (idx - n) % 4
    else:
        idx = (idx + n) % 4
    return DIRS[idx]



def move_front_back(x, y, face, dir, amount):
    if (face == N and dir == F) or (face == S and dir == B):
        y += amount
    elif (face == N and dir == B) or (face == S and dir == F):
        y -= amount
    elif (face == E and dir == F) or (face == W and dir == B):
        x += amount
    elif (face == E and dir == B) or (face == W and dir == F):
        x -= amount
        
    return x, y
        

def move_dir(x, y, dir, amount):
    if dir == N:
        y += amount
    elif dir == S:
        y -= amount
    elif dir == E:
        x += amount
    elif dir == W:
        x -= amount
    return x, y


    
def rotate_waypoint(wx, wy, dir, amount):
    n = amount // 90
    while n > 0:
        wx, wy = wy, wx
        if dir == R:
            wy *= -1
        elif dir == L:
            wx *= -1 

        n -= 1
    return wx, wy
            
            
    
    
     

def move_to_waypoint(x, y, wx, wy, dir, amount):
    for _ in range(amount):
        if dir == F:
            x += wx
            y += wy
        else:
            x -= wx
            y -= wy
            
    return x, y
    
    

# ship starts by facing each
# L and R change the direction the ship is facing

def solution1():
    instructions = parse_lines()
    x, y = 0, 0
    face = E
    
    for d, n in instructions:
        if d in (L, R):
            face = turn(face, d, n)
        elif d in (F, B):
            x, y = move_front_back(x, y, face, d, n)
        else:
            x, y = move_dir(x, y, d, n)
            
    return abs(x) + abs(y)
            
    
def solution2():
    instructions = parse_lines()
    x, y = 0, 0
    wx, wy = 10, 1
    
    for d, n in instructions:
        if d in (F, B):
            x, y = move_to_waypoint(x, y, wx, wy, d, n)
        elif d in (L, R):
            wx, wy = rotate_waypoint(wx, wy, d, n)
        else:
            # Move waypoint in direction
            wx, wy = move_dir(wx, wy, d, n)
            
    return abs(x) + abs(y)
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())