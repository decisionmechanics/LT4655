import numpy as np

a = np.arange(1, 10, dtype=np.float64).reshape((3, -1))

i = (a >= 2.5) & (a <= 6.5)
print(i)

a[i] = np.nan
print(a)
