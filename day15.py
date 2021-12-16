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


##Djikstra's algorithm

from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

adjacancy = load_input("files\day_small.txt")
G = Graph()
for i in range(len(adjacancy)):
    for j in range(len(adjacancy[i])):        
        for neighbor in [(1,0),(-1,0),(0,1),(0,-1)]:
        n_i = i + neighbor[0]
        n_j = j + neighbor[1]
        if n_i < 0 or n_i >= len(adjacancy) or n_j < 0 or n_j >= len(adjacancy[0]):
            continue
        else:
            G.add_edge(i, j, adjacancy[i][j])
            G.add_edge(j, i, adjacancy[i][j])

D = dijkstra(G, 0)

print(D)





""" from queue import PriorityQueue
with open('input15', 'r') as f:
    matrix = [list(map(int, line)) for line in f.read().splitlines()]

# solved using priority queue
def solve_dis(m):
    h, w = len(m), len(m[0])
    pq = PriorityQueue()
    # Add starting position in priority queue
    pq.put((0, (0, 0)))
    visited = {(0, 0), }
    while pq:
        curr_risk, (i, j) = pq.get()
        # Once we reach the end of the matrix, we can stop and return the risk
        if i == h - 1 and j == w - 1:
            return curr_risk
        #Check the neighbors 
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < h and 0 <= y < w and (x, y) not in visited:
                weight = m[x][y]
                pq.put((curr_risk + weight, (x, y)))
                visited.add((x, y))

print(f'Part 1 : {solve_dis(matrix)}')
print(f'Part 2 : {solve_dis(make_big_matrix())}') """