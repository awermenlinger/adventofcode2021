import numpy as np
from itertools import permutations
from collections import Counter
from tqdm import tqdm

def parse_input(path): # from https://github.com/davearussell/advent2021/blob/master/day19/solve.py
    scanners = []
    for line in open(path):
        if '---' in line:
            assert int(line.split()[2]) == len(scanners)
            scanners.append([])
        elif line.strip():
            scanners[-1].append(tuple(map(int, line.split(','))))
    return scanners

# define rotation matrixes
def establish_rotations(): # from: https://github.com/xdavidliu/advent-code-2021/blob/main/day19.py
    rotations = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                for q in permutations([[x,0,0], [0,y,0], [0,0,z]]):
                    m = np.array(q)
                    if np.linalg.det(m) == 1:
                        rotations.append(m)
    return rotations

def get_rotations(scanner):
    rots = []
    rotations = establish_rotations()
    for r in rotations:
        rot = []
        for s in scanner:
            rot.append(tuple(np.dot(s, r)))
        rots.append(rot)
    return rots

def parse_beacons(file):
    good_beacons = set()
    scanners = parse_input(file)
    #translation_vectors_good_scanners = [[0,0,0]]
    #establish the first scanner has the base 0,0,0 scanner
    for j in scanners[0]: good_beacons.add(tuple(j))
    good_scanners = [tuple((0,0,0))]
    other_scanners = scanners[1:]
    #main solving loop
    while len(other_scanners) != 0:
        for scanner in tqdm(other_scanners):
            scanner_rotations = get_rotations(scanner)
            for sc_rot in scanner_rotations:
                #calculate the distance vectors between all the combinations of elements
                #count them with the counter to find if a rotation has 12 matching points --> same distance vectors
                count_vecs = Counter()
                for x in sc_rot:
                    for y in good_beacons:
                        count_vecs[tuple(np.array(x)-np.array(y))] += 1
                most_common_vec = count_vecs.most_common()[0]
                if most_common_vec[1] >= 12: #we found the rotation
                    temp_scanner = [tuple(np.array(x) - most_common_vec[0]) for x in sc_rot] #transform the current scanner with the vector
                    for i in temp_scanner: good_beacons.add(i) # add the beacons to the beacon set (duplicates don't get added)
                    good_scanners.append(most_common_vec[0]) # add the properly rotated and basised scanner to the list of good scanners
                    index = other_scanners.index(scanner)
                    other_scanners.pop(index) #remove from the list of other scanners
                    break

    return good_scanners, good_beacons


def manhattan_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])

def parse_scanners(scanners):
    options = permutations(scanners,2)
    distances = [manhattan_distance(x[0],x[1]) for x in options]
    return distances
scanners_vectors, beacons = parse_beacons("files\day19.txt")

print ("Part 1: ", len(beacons))
print ("Part 2: ", max(parse_scanners(scanners_vectors)))