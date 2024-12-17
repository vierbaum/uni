import numpy as np

a = np.array([
    [0, 1, 3, 0],
    [8, 5, 0, 6],
    [0, 0, -1, -2]
])
b = np.array([
    [0, 1],
    [0, 0],
    [3, 3],
    [9, 5]
])
c = np.array([
    [-1, 1, -3,],
    [8, 5, -4],
    [0, 0, 6]
])
d = np.array([
    [1, -3,],
    [5, 0],
])
e = np.array([
    [1],
    [5],
    [3]
])
f = np.array([
    [2,3,0]
])

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a @ b)
