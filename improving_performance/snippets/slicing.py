import numpy as np

a = np.arange(1, 25).reshape((2, 3, -1))
b = a[1:2, 1:2, 1:2]

print(b)
