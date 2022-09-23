import numpy as np

a = np.arange(1, 25, dtype=np.float64).reshape((2, 3, -1))
b = a.view()

print(b is a)
print(b.base is a.base)

c = a[0:2, 0:2, 0:2]
c[:] = np.nan
print(a)
