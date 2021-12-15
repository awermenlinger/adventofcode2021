import numpy as np

def load_input(file):
    risk_level = open(file, 'r').read().rstrip().split('\n')
    risk_level = [[int(i) for i in line] for line in risk_level]
    risk_level = np.array(risk_level)
    return risk_level

def findMinCost_table(cost):
    M, N = len(cost), len(cost[0])
    T = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            if j == 0 and i == 0:
                continue
            T[i][j] = cost[i][j]
            if i == 0 and j > 0:
                T[0][j] += T[0][j - 1]
            elif j == 0 and i > 0:
                T[i][0] += T[i - 1][0]
            elif i > 0 and j > 0:
                T[i][j] += min(T[i - 1][j], T[i][j - 1])
    return T[M - 1][N - 1]-T[0][0]

def replicate_grid(grid):
    grid += 1
    grid[grid>9] -= 9
    return grid

def create_part2(grid):
    grids = []
    # create top row
    for i in range(5):
        if i == 0 :
            grids.append(grid.copy())
        else:
            grids.append(replicate_grid(grids[i-1].copy()))
            grid = np.hstack((grid, grids[i]))
    #replicate rows down
    grids = []
    for j in range(5):
        if j == 0 :
            grids.append(grid.copy())
        else:
            grids.append(replicate_grid(grids[j-1].copy()))
            grid = np.vstack((grid, grids[j]))

    return grid
        

print("Part 1: ", findMinCost_table(load_input("files\day15.txt")))
print("Part 2: ", findMinCost_table(create_part2(load_input("files\day15.txt"))))

#2874 too high
#Answer 2: 2868 is target