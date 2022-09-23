import numpy as np

a = np.arange(1, 10).reshape((3, -1))
print(a)

print(a.T)

b = np.arange(1, 4)
print(b)

print(np.matmul(a, b))
