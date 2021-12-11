import numpy as np
import functools
import operator

lines = open('files\day11.txt', 'r').read().rstrip().split('\n')
octopi = np.array([[int(i) for i in line] for line in lines])

def generate_neighbors(coords, octo):
    neighbors = []
    for i in range(coords[0]-1, coords[0]+2):
        for j in range(coords[1]-1, coords[1]+2):
            if i == coords[0] and j == coords[1]:
                continue
            if i < 0 or j < 0:
                continue
            if i >= len(octo) or j >= len(octo[0]):
                continue
            neighbors.append((i, j))
    return neighbors

explosions_total = 0
for i in range(100):
    octopi += 1
    has_exploded = np.zeros(octopi.shape, dtype=bool)
    while True:
        exploding = [coords for coords in np.ndindex(octopi.shape) if octopi[coords] >= 10 and not has_exploded[coords]]
        neighbors_boom = [generate_neighbors(coords,octopi) for coords in np.ndindex(octopi.shape) if octopi[coords] >= 10 and not has_exploded[coords]]
        neighbors_boom = functools.reduce(operator.iconcat, neighbors_boom, [])
        for b in neighbors_boom: octopi[b] += 1
        for e in exploding: has_exploded[e] = True
        if neighbors_boom == []:
            break
    explosions_total += len(octopi[octopi >= 10])
    octopi[octopi >= 10] = 0

print("Part 1: ", explosions_total)

octopi = np.array([[int(i) for i in line] for line in lines])
step = 1
while True:
    octopi += 1
    has_exploded = np.zeros(octopi.shape, dtype=bool)
    while True:
        exploding = [coords for coords in np.ndindex(octopi.shape) if octopi[coords] >= 10 and not has_exploded[coords]]
        neighbors_boom = [generate_neighbors(coords,octopi) for coords in np.ndindex(octopi.shape) if octopi[coords] >= 10 and not has_exploded[coords]]
        neighbors_boom = functools.reduce(operator.iconcat, neighbors_boom, [])
        for b in neighbors_boom: octopi[b] += 1
        for e in exploding: has_exploded[e] = True
        if neighbors_boom == []:
            break
    octopi[octopi >= 10] = 0
    if octopi.nonzero()[0].size == 0:
        print("Part 2: ", step)
        break
    step += 1