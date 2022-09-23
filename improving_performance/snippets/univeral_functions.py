import numpy as np
import timeit


def to_fahrenheit(deg_c):
    return deg_c * 9.0 / 5.0 + 32


temperatures = np.array([0, 50, 100])

times = timeit.repeat(
    stmt=lambda: to_fahrenheit(temperatures), number=100_000, repeat=7
)
print(np.mean(times))

np_to_fahrenheit = np.frompyfunc(to_fahrenheit, 1, 1)

times = timeit.repeat(
    stmt=lambda: np_to_fahrenheit(temperatures), number=100_000, repeat=7
)
print(np.mean(times))
