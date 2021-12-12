from collections import defaultdict
from os import truncate
# inspired by https://github.com/jdgunter/aoc2021/blob/master/12/12.py while searching for DFS implementation
data = [l.strip().split('-') for l in open('files\day12.txt')]
G = defaultdict(list)


def is_small_cave(node):
    return str.islower(node)

for edge in data:
    a, b = edge[0], edge[1]

    if b != 'start':
        G[a].append(b)
    if a != 'start':
        G[b].append(a)


def dfs(graph, path, visited_small, double_visit):
    path_count = 0
    if path[-1] == 'end':
        return 1
    
    for to_explore in G[path[-1]]:
        next_double_visit = double_visit
        if to_explore in visited_small:
            if not double_visit:
                continue
            elif to_explore == "start":
                continue
            else:
                next_double_visit = False

        next_visited_small = visited_small | {to_explore} if is_small_cave(to_explore) else visited_small
        path.append(to_explore)
        path_count += dfs(graph, path, next_visited_small, next_double_visit)
        path.pop()
    
    return path_count

print("Part 1: ", dfs(G, ["start"], {"start"}, double_visit=False))
print("Part 2: ", dfs(G,['start'], {'start'}, double_visit=True))