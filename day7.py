import numpy as np
h_positions = np.array([int(i) for i in open('files\day7.txt').readlines()[0].split(',')])
distances = [np.abs(h_pos - np.median(h_positions)) for h_pos in h_positions]
distances = sum(distances)
print ("Part 1: ", distances)

for x in range(min(h_positions), max(h_positions)+1):
    delta = np.abs(h_positions - x)
    if x == min(h_positions):
        min_fuel_cost = np.sum([sum(range(1, d+1)) for d in delta])
    else:
        fuel_cost = np.sum([sum(range(1, d+1)) for d in delta])
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost

print("Part 2: ", min_fuel_cost)