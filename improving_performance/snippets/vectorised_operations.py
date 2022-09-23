import numpy as np

temperatures = np.array([[0.0, 50.0, 100.0], [-10.0, -50.0, -100.0]])

print(temperatures * 9.0 / 5.0 + 32.0)

radii = np.array([1, 3, 10.0])
print(np.pi * radii**2)

revenue = np.array([1_000_000, 1_100_000, 1_200_000])
costs = np.array([800_000, 850_000, 900_000])
print(revenue - costs)
