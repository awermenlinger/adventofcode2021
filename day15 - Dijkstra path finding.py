import numpy as np
from queue import PriorityQueue
import networkx as nx

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
#print("Part 2: ", findMinCost_table(create_part2(load_input("files\day15.txt"))))
#Dynamic programming failed for part 2

##Djikstra's algorithm to the rescue!
def dijkstra(graph, start_vertex, end_vertex):
    D = dict()
    visited = set()

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        if current_vertex == end_vertex:
            return dist

        for neighbor in graph.neighbors(current_vertex):
            if neighbor in visited:
                continue    
            old_cost = D.get(neighbor)
            distance = graph.edges[current_vertex, neighbor]["weight"]
            new_cost = dist + distance

            if old_cost and new_cost >= old_cost:
                continue

            D[neighbor] = new_cost
            pq.put((new_cost, neighbor))
        visited.add(current_vertex)
    print(D)

def graph_from_adj(adjacancy):
    G = nx.DiGraph()
    for i in range(len(adjacancy)):
        for j in range(len(adjacancy[i])):        
            for neighbor in [(1,0),(-1,0),(0,1),(0,-1)]:
                n_i = i + neighbor[0]
                n_j = j + neighbor[1]
                if n_i < 0 or n_i >= len(adjacancy) or n_j < 0 or n_j >= len(adjacancy[0]):
                    continue
                else:
                    G.add_edge((n_i, n_j), (i,j), weight=adjacancy[i][j])
    return G

adjacancy = create_part2(load_input("files\day15.txt"))
start = (0,0)
end = (len(adjacancy)-1, len(adjacancy[0])-1)
G = graph_from_adj(adjacancy)
print("Part 2: ", dijkstra(G, start, end))