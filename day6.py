import numpy as np

fishes = open('files\day6.txt', 'r').read().rstrip().split(',')

fishes = [int(fish) for fish in fishes]
fishes = np.array(fishes)

for day in range(80):
    fishes -= 1
    at_zero = fishes == -1
    new_fishes = len(fishes[at_zero])*[8]
    fishes[fishes == -1] = 6
    fishes = np.append(fishes, new_fishes)

print("Part 1: ", len(fishes))

# Part 2, https://github.com/mebeim/aoc/blob/master/2021/README.md
# Was getting stuck with the too large number in memory, searched and found the above solution
# Learned the wonders of defaultdict, but solution below is not mine.
from collections import defaultdict

data = open('files\day6.txt', 'r').read().rstrip().split(',')
data = [int(fish) for fish in data]

fishes_dict = defaultdict(int)
for fish in data:
    fishes_dict[fish] += 1
print(fishes_dict)

for day in range(256):
    fishes_dict_update = defaultdict(int)
    for key, value in fishes_dict.items():
        key -= 1
        if key == -1:
            fishes_dict_update[6] += value
            fishes_dict_update[8] += value
        else:
            fishes_dict_update[key] += value
    fishes_dict = fishes_dict_update

print("Part 1: ", sum(fishes_dict.values()))

