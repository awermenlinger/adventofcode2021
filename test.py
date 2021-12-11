import numpy as np

test = np.zeros((3, 3))
print(test)
test[(0, 1), (1, 1)] = 1
print(test)
test[(0, 0)] = 5

test[test == 5] = 11
print(test)