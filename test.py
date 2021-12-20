import numpy as np

s = np.array([1,2,3])
rot = np.array([[ 0, -1,  0],
       [-1,  0,  0],
       [ 0,  0, -1]])

test = np.dot(s, rot)

a = np.array([1,2,3])
b = np.array([5,8,9])
print (a-b)