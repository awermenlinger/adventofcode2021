import numpy as np
lines = open('files\day9.txt', 'r').read().rstrip().split('\n')
smoke_basin = np.array([[int(i) for i in line] for line in lines])

def get_window_max(coords, arr):
    local_min = False
    if coords[0] == 0:
        top = arr[coords[0]][coords[1]]
    else:
        top = arr[coords[0]-1][coords[1]]
    if coords[0] == arr.shape[0]-1:
        bot = arr[coords[0]][coords[1]]
    else:
        bot = arr[coords[0]+1][coords[1]]
    if coords[1] == 0:
        left = arr[coords[0]][coords[1]]
    else:
        left = arr[coords[0]][coords[1]-1]
    if coords[1] == arr.shape[1]-1:
        right = arr[coords[0]][coords[1]]
    else:
        right = arr[coords[0]][coords[1]+1]
    tgt = arr[coords[0]][coords[1]]
    if tgt == top == bot == left == right:
        pass
    elif min(tgt, top, bot, left, right) == tgt:
        local_min = True
    
    return local_min

loc_minima = []
loc_minima_loc = []
for i in range(smoke_basin.shape[0]):
    for j in range(smoke_basin.shape[1]):
        if get_window_max([i, j], smoke_basin):
            loc_minima.append(smoke_basin[i][j]+1)
            loc_minima_loc.append([i,j])
print("Part1: ", sum(loc_minima))

basins = []
for loc_min in loc_minima_loc:
    #create a copy of smoke_basin and transform everything that is not 9
    data = smoke_basin.copy()

    row_max, col_max = data.shape
    import time
    def flood_fill(row, col):
        if row < 0 or col < 0 or row >= row_max or col >= col_max:
            return
        if data[row][col] == 9 or data[row][col] == 10:
            return
        data[row][col] = 10
        flood_fill(row, col+1)
        flood_fill(row, col-1)
        flood_fill(row+1, col)
        flood_fill(row-1, col)

    #flood_fill(loc_min[0], loc_min[1])
    flood_fill(loc_min[0], loc_min[1])

    basin = data == 10
    basin_size = len(data[basin])
    basins.append(basin_size)
    top_3_basins = sorted(basins)[-3:]

print("part 2: ", top_3_basins[0] * top_3_basins[1] * top_3_basins[2])