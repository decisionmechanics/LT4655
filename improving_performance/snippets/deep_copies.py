import numpy as np

a = np.arange(1, 25, dtype=np.float64).reshape((2, 3, -1))

c = a[0:2, 0:2, 0:2].copy()
c[:] = np.nan

print(a)
