import numpy as np

a = np.arange(1, 25).reshape((2, 3, -1))
print(a)

b = np.arange(1, 13).reshape((3, -1))
print(b)

print(a * b)
