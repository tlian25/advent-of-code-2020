# Day 4. Passport Processing
# https://adventofcode.com/2020/day/4

from util.input_util import read_input_file

BYR = 'byr'
IYR = 'iyr'
EYR = 'eyr'
HGT = 'hgt'
HCL = 'hcl'
ECL = 'ecl'
PID = 'pid'
CID = 'cid'

def parse_lines():
    passports = []
    lines = read_input_file(4)
    curr = {}
    for l in lines:
        if l == '':
            passports.append(curr)
            curr = {}
        else:
            for field in l.split():
                k, v = field.split(':')
                curr[k] = v
    
    if curr:
        passports.append(curr)
    
    return passports
            
        
def validate_passport(p):
    if {BYR, IYR, EYR, HGT, HCL, ECL, PID}.difference(set(p.keys())): return False

    if len(p[BYR]) != 4 or int(p[BYR]) < 1920 or int(p[BYR]) > 2002: return False
    if len(p[IYR]) != 4 or int(p[IYR]) < 2010 or int(p[IYR]) > 2020: return False
    if len(p[EYR]) != 4 or int(p[EYR]) < 2020 or int(p[EYR]) > 2030: return False
    
    if p[HGT][-2:] not in {'cm', 'in'}: return False
    if p[HGT][-2:] == 'cm':
        if int(p[HGT][:-2]) < 150 or int(p[HGT][:-2]) > 193: return False
    elif p[HGT][-2:] == 'in':
        if int(p[HGT][:-2]) < 59 or int(p[HGT][:-2]) > 76: return False
    
    if p[HCL][0] != '#' or len(p[HCL]) != 7: return False
    
    if p[ECL] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}: return False

    if len(p[PID]) != 9: return False

    try:
        int(p[HCL][1:], 16)
        int(p[PID])
    except Exception as e:
        return False
    
    return True
    


def solution1():
    passports = parse_lines()
    invalid_count = 0
    for p in passports:
        if {BYR, IYR, EYR, HGT, HCL, ECL, PID}.difference(set(p.keys())):
            invalid_count += 1
        
    return len(passports) - invalid_count
                

    
    
    
    
    
def solution2():
    passports = parse_lines()
    invalid_count = 0
    for p in passports:
        if not validate_passport(p):
            invalid_count += 1
    
    return len(passports) - invalid_count
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())