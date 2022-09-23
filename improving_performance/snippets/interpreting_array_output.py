import numpy as np


def to_id(i, j, k):
    return (i + 1) * 100 + (j + 1) * 10 + k + 1


a = np.fromfunction(to_id, (2, 3, 4), dtype=np.int64)

print(a)
