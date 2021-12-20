import numpy as np
from itertools import permutations

def parse_input(path): # from https://github.com/davearussell/advent2021/blob/master/day19/solve.py
    scanners = []
    for line in open(path):
        if '---' in line:
            assert int(line.split()[2]) == len(scanners)
            scanners.append([])
        elif line.strip():
            scanners[-1].append(tuple(map(int, line.split(','))))
    return scanners


# from: https://github.com/xdavidliu/advent-code-2021/blob/main/day19.py
# define rotation matrixes
rotations = []
for x in [-1, 1]:
    for y in [-1, 1]:
        for z in [-1, 1]:
            for q in permutations([[x,0,0], [0,y,0], [0,0,z]]):
                m = np.array(q)
                if np.linalg.det(m) == 1:
                    rotations.append(m)

def get_rotations(scanner):
    rots = []
    for r in rotations:
        rot = []
        for s in scanner:
            rot.append(np.dot(s, r))
        rots.append(rot)
    return rots

def check_12_points(org, scan):
    s_org = set(tuple(map(tuple, org)))
    s_scan = set(tuple(map(tuple, scan)))
    valid = len(s_org.intersection(s_scan))
    return valid >= 12

def get_dist_adj(vec, scan):
    new_scan = [vec-s for s in scan]


test = np.array([[1,2,3], [4,5,6], [7,8,9]])
test_rot1 = np.array([[3,2,3], [4,5,6], [2,8,9]])
check = check_12_points(test, test_rot1)
print(check)
#scanners = parse_input('files\day_small.txt')

#print(scanners[0])

def transform_scanner(scanner):

    return scanners