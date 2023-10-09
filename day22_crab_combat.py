# Day 22. Crab Combat
# https://adventofcode.com/2020/day/22

from collections import deque

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(22)
    d1, d2 = deque(), deque()
    curr = d1
    for l in lines:
        if l == '':
            curr = d2
            
        elif 'Player' not in l:
            curr.append(int(l))

    return d1, d2

# split the cards so each player has their own deck
# Rounds - both players draw top card
# player with higher-valued card wins the round
# winner keeps both cards, place on bottom on deck so winner's card is above other
# game ends when one player has all the cards

# Score = card * position in deck

        

P1 = "player1"
P2 = "player2"


def serialize(d1, d2):
    return '-'.join([str(x) for x in d1]) + '::' + \
            '-'.join([str(x) for x in d2])


def round(d1, d2):
    p1 = d1.popleft()
    p2 = d2.popleft()
    
    if p1 > p2:
        d1.append(p1)
        d1.append(p2)
    else:
        d2.append(p2)
        d2.append(p1)



def game(d1, d2) -> str:
    while d1 and d2:
        round(d1, d2)
        
    # return winner
    if d1: return P1
    return P2




def rec_round(d1, d2, i):
    p1 = d1.popleft()
    l1 = len(d1)
    p2 = d2.popleft()
    l2 = len(d2)

    # If enough cards left, then play subgame
    # Copy next number of cards
    if l1 >= p1 and l2 >= p2:
        d1copy = deque() 
        for i, n in enumerate(d1):
            if i == p1:
                break
            d1copy.append(n)

        d2copy = deque() 
        for i, n in enumerate(d2):
            if i == p2:
                break
            d2copy.append(n)

        winner = rec_game(d1copy, d2copy, i+1)
    elif p1 > p2:
        winner = P1
    else:
        winner = P2 
        
    if winner == P1:
        d1.append(p1)
        d1.append(p2)
    else:
        d2.append(p2)
        d2.append(p1)



def rec_game(d1, d2, i) -> str:
    SEEN = set()
    while d1 and d2:
        s = serialize(d1, d2)
        if s in SEEN: 
            return P1
        SEEN.add(s)
        rec_round(d1, d2, i)
    
    if d1: return P1
    return P2


def score(d):
    s = 0
    L = len(d)
    for i, n in enumerate(d):
        s += (L-i) * n
    return s



def solution1():
    d1, d2 = parse_lines()
    winner = game(d1, d2)

    if winner == P1:
        return score(d1)
    else:
        return score(d2)


# Recursive
# Before round, if there was a previous round in this game with same cards -> game ends
# If both players have at least as many cards remaining in their deck as the value of the card draw
# Continue playing recursively

def solution2():
    d1, d2 = parse_lines()
    winner = rec_game(d1, d2, 1)

    if winner == P1:
        return score(d1)
    else:
        return score(d2) 

    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())