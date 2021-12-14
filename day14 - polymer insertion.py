import numpy as np
from collections import defaultdict

def load_inputs(path): 
    poly_dict = defaultdict(int)
    with open(path) as f:
        inputs = f.read()
        polymer, instructions = inputs.split("\n\n")
    last = polymer[-1]
    for i in range(len(polymer)):
        if polymer[i] != polymer[-1]:
            poly_dict[polymer[i]+polymer[i+1]] += 1
    inst_dict = defaultdict(str)
    for inst in instructions.split("\n"):
        key, value = inst.split(" -> ")
        inst_dict[key] = value
    return poly_dict, inst_dict, last

def solve(file, iter):
    poly, inst, last = load_inputs(file)

    for i in range (iter):
        new_poly = defaultdict(int)
        for k, v in poly.items():
            if k in inst:
                new_poly[k[0]+inst[k]]+=v
                new_poly[inst[k]+k[1]]+=v
            else:
                new_poly[k]+=v
        poly = new_poly

    results = defaultdict(int)
    for k, v in poly.items():
        results[k[0]]+=v    
    results[last]+=1

    return (max(results.values())-min(results.values()))

print("Part 1: ", solve("files\day14.txt", 10))
print("Part 2: ", solve("files\day14.txt", 40))