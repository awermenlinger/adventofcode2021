import numpy as np
#data = [[[int(y) for y in x.split(',')] for x in line.strip('\n').split(' -> ')] for line in
#        fileinput.input("../../input/day5")]

lines = open('files\day05.txt', 'r').read().rstrip().split('\n')

lines = [line.split(' -> ') for line in lines]
lines = [[l.split(',') for l in line] for line in lines]
clean_lines = []
for line in lines:
    flat_list = [item for sublist in line for item in sublist]
    flat_list = [int(item) for item in flat_list]
    clean_lines.append(flat_list)

a_lines = np.array(clean_lines)
max_x = max((np.max(a_lines[:, 0]), np.max(a_lines[:, 2])))
max_y = max((np.max(a_lines[:, 1]), np.max(a_lines[:, 3])))
zeros = np.zeros((max_y+1,max_x+1))

for line in a_lines:
    if line[0] == line[2]:
        x = line[0]
        y_min = min(line[1], line[3])
        y_max = max(line[1], line[3])
        for y in range(y_min, y_max+1):
            zeros[y][x] += 1
    elif line[1] == line[3]:
        y = line[1]
        x_min = min(line[0], line[2])
        x_max = max(line[0], line[2])
        for x in range(x_min, x_max+1):
            zeros[y][x] += 1

more_then_2 = zeros >= 2
print("Part 1: ", len(zeros[more_then_2]))

zeros = np.zeros((max_y+1,max_x+1))
for line in a_lines:
    if line[0] == line[2]:
        x = line[0]
        y_min = min(line[1], line[3])
        y_max = max(line[1], line[3])
        for y in range(y_min, y_max+1):
            zeros[y][x] += 1
    elif line[1] == line[3]:
        y = line[1]
        x_min = min(line[0], line[2])
        x_max = max(line[0], line[2])
        for x in range(x_min, x_max+1):
            zeros[y][x] += 1
    else: #diagonal
        x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
        
        if x1 < x2: 
            x_step = 1
        else:
            x_step = -1
        
        if y1 < y2:
            y_step = 1
        else:
            y_step = -1
        
        zeros[y1][x1] += 1
        while x1 != x2 and y1 != y2:
            x1 += x_step
            y1 += y_step
            zeros[y1][x1] += 1

more_then_2 = zeros >= 2
print("Part 2: ", len(zeros[more_then_2]))