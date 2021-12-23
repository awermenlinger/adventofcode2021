import numpy as np

def get_algo_val(coords, matrix):
    neighbors = []
    for i in range(coords[0]-1, coords[0]+2):
        for j in range(coords[1]-1, coords[1]+2):
            if i < 0 or j < 0:
                continue
            if i >= len(matrix) or j >= len(matrix[0]):
                continue
            neighbors.append((i, j))
    neighbors = int("".join([str(image[x]) for x in neighbors]), 2)
    return neighbors

file = "files\day_small.txt"
with open(file) as f:
    enhance_algo, image = f.read().strip().split('\n\n')

enhance_algo = [0 if x == "." else 1 for x in enhance_algo]
image = image.split('\n')
image = np.array([[0 if x == "." else 1 for x in line] for line in image])

coords = [2,2]
binary = get_algo_val(coords, image)
output_pixel = enhance_algo[binary]
print(output_pixel)


#def pad_matrix(light):
