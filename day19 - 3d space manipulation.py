import numpy as np
from itertools import permutations
from collections import defaultdict, Counter
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
def establish_ROTATIONS(): # from: https://github.com/xdavidliu/advent-code-2021/blob/main/day19.py
    ROTATIONS = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                for q in permutations([[x,0,0], [0,y,0], [0,0,z]]):
                    m = np.array(q)
                    if np.linalg.det(m) == 1:
                        ROTATIONS.append(m)
    return ROTATIONS

def get_rotations(scanner):
    rots = []
    for r in ROTATIONS:
        rot = []
        for s in scanner:
            rot.append(tuple(np.dot(s, r)))
        rots.append(rot)
    return rots

def check_12_points(org, scan):
    s_org = set(tuple(map(tuple, org)))
    s_scan = set(tuple(map(tuple, scan)))
    valid = len(s_org.intersection(s_scan))
    return valid >= 12

def get_dist_adj(vec, scan):
    new_scan = [vec-s for s in scan]


def parse_scanners(file):
    good_beacons = set()
    scanners = parse_input(file)
    translation_vectors_good_scanners = [[0,0,0]]
    #establish the first scanner has the base 0,0,0 scanner
    for x in scanners[0]: good_beacons.add(tuple(x))
    good_scanners = scanners[0]
    other_scanners = scanners[1:]
    #main solving loop
    while len(other_scanners) != 0:
        for scanner in tqdm(other_scanners):
            scanner_rotations = get_rotations(scanner)
            for sc_rot in scanner_rotations:
                #calculate the distance vectors between all the combinations of elements
                #count them with the counter to find if a rotation has 12 matching points --> same distance vectors
                for good_scan in good_scanners:
                    count_vecs = Counter()
                    for x in sc_rot:
                        for y in good_scan:
                            count_vecs[tuple(np.array(x)-np.array(y))] += 1
                    most_common_vec = count_vecs.most_common()[0]
                    if most_common_vec[1] >= 12: #we found the rotation
                        #temp_scanner = [tuple(np.array(x) + most_common_vec[0]) for x in sc_rot] #transfor the current scanner with the vector
                        #for x in temp_scanner: good_beacons.add(x) # add the beacons to the beacon set (duplicates don't get added)
                        #good_scanners.append(temp_scanner) # add the properly rotated and basised scanner to the list of good scanners
                        #find the tr_vec for the current scanner
                        
                        #translation_vectors_good_scanners.append(most_common_vec[0])
                        index = other_scanners.index(scanner)
                        other_scanners.pop(index) #remove from the list of other scanners
                        break

    #MISSING: Once matching need to align beacons to 0,0,0
    #so if scan 1 matches scan 4
    # v_scan0_vscan1 (ie v_scan1) + vscan1_scan4 = vscan0_4

    return good_beacons

ROTATIONS = establish_ROTATIONS()
print(len(parse_scanners("files\day19.txt")))

#959 is too high

"""
while other_set is not empty:
  for each scanner in other_set:
    get beacon_locations from the good_scanners set
    for each dir in the 48 directions:
       get the loc of the beacons in scanner from the other_set for this dir
       for each beacon in the scanner's range:
          for each beacon in the good_scanners set:
             calculate dx, dy, dz between the beacon in the good_scanners_set and the beacons in the scanner
             if dx, dy, dz is same for 12:
                 then we have found dx, dy, dz for the scanner
                 remove scanner from other_set
                 add scanner to good_scanners set
                 adjust the position of the scanner's beacons by dx, dy, dz
part1: find the number of beacons found in each of the good scanner
"""

#answers should be 419 and 13210