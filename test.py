# [[1,2],3] becomes a list of either brackets or numbers, excluding comas:
# [ [ 1 2 ] 3 ]
def parse(line):
    import re
    return re.findall(r"\d+|[\[\]]", line)
lines = [parse(l.rstrip()) for l in open("files\day18.txt").readlines()]

def int_to_pair(num):
    import math
    return [str(math.floor(num / 2)), str(math.ceil(num / 2))]

def add(a, b): return ['['] + a + b + [']']

def explode(sfnum, pos):
    def seek_digit(sfnum, pos, direction):
        while 0 < pos < len(sfnum)-1:
            pos += direction
            if sfnum[pos].isdigit(): return pos
        return None
    a,b = int(sfnum[pos]), int(sfnum[pos+1])
    l_pos = seek_digit(sfnum, pos, -1)
    r_pos = seek_digit(sfnum, pos+1, +1)
    if l_pos: sfnum[l_pos] = str(a + int(sfnum[l_pos]))
    if r_pos: sfnum[r_pos] = str(b + int(sfnum[r_pos]))
    return sfnum[0:pos-1] + ['0'] + sfnum[pos+3:]

def split(sfnum, pos):
    return sfnum[0:pos] + ['['] + int_to_pair(int(sfnum[pos])) + [']'] + sfnum[pos+1:]

def reduce_step(sfnum):
    depth = 0
    for pos in range(len(sfnum)):
        if sfnum[pos] == "[": depth += 1
        elif sfnum[pos] == "]": depth -= 1
        elif depth == 5: return explode(sfnum, pos)

    for pos in range(len(sfnum)):
        if sfnum[pos].isdigit() and int(sfnum[pos]) >= 10: return split(sfnum, pos)
    raise EOFError

def reduce_fully(sfnum):
    while True:
        try: sfnum = reduce_step(sfnum)
        except EOFError: break
    return sfnum

def add_list(numbers):
    result = numbers.pop(0)
    for i in numbers:
        result = reduce_fully(add(result, i))
    return(result)

def magnitude(sfnum):
    def p(sfnum):
        for i in range(len(sfnum)-1):
            if sfnum[i].isdigit() and sfnum[i+1].isdigit():
                sfnum = sfnum[0:i-1] + [str(int(sfnum[i]) * 3 + int(sfnum[i+1]) * 2)] + sfnum[i+3:]
                return sfnum
        raise EOFError
    while True:
        try: sfnum = p(sfnum)
        except EOFError: break
    return int(sfnum[0])

p1 = magnitude(add_list(lines))
print(f"Part 1: {p1}")

## Part 2 #############################################################

from itertools import permutations

p2 = 0
for a, b in permutations(lines, 2):
    val = magnitude(add_list([a, b]))
    if val > p2: p2 = val

print(f"Part 2: {p2}")
