import math
import re

def parse(line):
    return re.findall(r"\d+|[\[\]]", line)
lists = [parse(l.rstrip()) for l in open("files\day18.txt").readlines()]
lists = [[int(ele) if ele.isnumeric() else ele for ele in list] for list in lists]

def add_fish(a, b):
    a = a.copy()
    b = b.copy()
    a = ["["] + a
    b.append("]")
    a.extend(b)
    return a

def explode(fish, pos):
   #find if there are five "[ in a row with a stack
   #take the fifth and the next 3 items
    #delete leftmost bracket
    fish = fish.copy()
    left, right = fish[:pos], fish[pos+3:]
    l_v, r_v = fish[pos+1], fish[pos+2]
    loop = True
    i = len(left)-1
    while loop:
        if i == 0: loop = False
        if type(left[i]) == int:
            loop = False
            fish[i] += l_v
        i -= 1

    loop = True
    i = 0
    while loop:
        if i == len(right)-1: loop = False
        if type(right[i]) == int:
            loop = False
            fish[pos+3+i] += r_v
        i += 1
    
    fish[pos] = 0
    del fish[pos+1:pos+4]
    return fish

def split(fish, pos):
    fish = fish.copy()
    left, right = fish[:pos], fish[pos+1:]
    l_v, r_v = math.floor(fish[pos]/2), math.ceil(fish[pos]/2)
    new_pair = ["[", l_v, r_v, "]"]
    new_fish = left + new_pair + right
    return new_fish

def reduce(fish):
    fish = fish.copy()
    no_more_moves = False
    while not no_more_moves:
        no_more_explodes = False
        while not no_more_explodes:
            stack = []
            for i in range(len(fish)):
                ch = fish[i]
                if ch == "[":
                    stack.append(ch)
                elif ch == "]":
                    stack.pop()
                
                if stack.count("[") == 5:
                    fish = explode(fish, i)
                    break
                
            if len(stack) == 0:
                no_more_explodes = True

        no_more_splits = False
        while not no_more_splits and no_more_explodes:
            for i in range(len(fish)):
                if type(fish[i]) == int:
                    if fish[i] >= 10:
                        fish = split(fish, i)
                        no_more_explodes = False
                        break
            if i == len(fish)-1:
                no_more_splits = True

        if no_more_explodes and no_more_splits:
            no_more_moves = True
    return fish

def magnitude(fish):
    fish = fish.copy()
    mag_finished = False
    while mag_finished == False:
        #print(fish)
        for i in range(len(fish)):
            if type(fish[i]) == int and type(fish[i+1]) == int:
                #print(fish[i], fish[i+1])
                #print( 3 * fish[i], 2 * fish[i+1])
                mag_add = 3 * fish[i] + 2 * fish[i+1]
                del fish[i-1:i+3]
                fish.insert(i-1, mag_add)
                #print(fish)
                break
        if len(fish)==1:
            mag_finished = True
      
    return fish[0]

main = lists[0]
for i in range(1, len(lists)):
    main = reduce(add_fish(main.copy(), lists[i])).copy()
    
    
print("Part 1: ", magnitude(main))
 
#Part 2: Find max between x+y or y+x for all pairs of fishes
from itertools import permutations

max_mag = 0

for a, b in permutations(lists, 2):
    mag_res = magnitude(reduce(add_fish(a, b)))
    if mag_res > max_mag:
        max_mag = mag_res
print("Part 2: ", max_mag)