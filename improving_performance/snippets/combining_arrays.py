import numpy as np

a = np.arange(1, 5).reshape((2, 2))
b = np.arange(5, 9).reshape((2, 2))

print(np.hstack((a, b)))
print(np.vstack((a, b)))
print(np.concatenate((a, b), axis=1))
