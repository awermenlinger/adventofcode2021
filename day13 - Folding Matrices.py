import numpy as np
def load_inputs(path): 
    with open(path) as f:
        inputs = f.read()
        coords, instructions = inputs.split("\n\n")
    
    t_paper = [[int(i) for i in i.strip().split(",") if i != ""] for i in coords.split("\n")]
    t_paper = set([tuple(l) for l in t_paper])
    instructions = instructions.split("\n")
    cleaned_instructions = []
    for inst in instructions:
        left, right = inst.split("=")
        cleaned_instructions.append([left[-1], int(right)])
    return t_paper, cleaned_instructions

def fold_along_x(t_paper, x):
    temp_coords = t_paper.copy()
    for coord in t_paper:
        if coord[0] > x:
            temp_coords.remove(coord)
            new_x = x - (coord[0]-x)
            if new_x >=0: 
                y = coord[1]
                temp_coords.add((new_x,y))
    return temp_coords

def fold_along_y(t_paper, y):
    temp_coords = t_paper.copy()
    for coord in t_paper:
        if coord[1] > y:
            temp_coords.remove(coord)
            new_y = y - (coord[1]-y)
            if new_y >=0: 
                x = coord[0]
                temp_coords.add((x,new_y))
    return temp_coords

t_paper, instructions = load_inputs("files\day13.txt")

if instructions[0][0] == "x":
    t_paper = fold_along_x(t_paper, instructions[0][1])
else:
    t_paper = fold_along_y(t_paper, instructions[0][1])
print("Part 1: ", len(t_paper))

t_paper, instructions = load_inputs("files\day13.txt")

for inst in instructions:
    if inst[0] == "x":
        t_paper = fold_along_x(t_paper, inst[1])
    else:
        t_paper = fold_along_y(t_paper, inst[1])

x_max = max([coord[0] for coord in t_paper])
y_max = max([coord[1] for coord in t_paper])
matrix = np.zeros((y_max+1,x_max+1))
for coord in t_paper:
    x, y = coord[0], coord[1]
    matrix[y][x] = 1

print("Part 2: ")
for row in range(matrix.shape[0]):
    lst_str = [str(item) for item in list(matrix[row])]
    lst_str = [item.replace("1.0", "#") for item in lst_str]
    lst_str = [item.replace("0.0", " ") for item in lst_str]
    print ("".join(lst_str))