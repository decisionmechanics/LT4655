import numpy as np

print(np.random.uniform(low=0, high=100, size=2))
print(np.random.normal(loc=100, scale=16, size=2))
print(np.random.triangular(left=2, mode=5, right=10, size=2))
print(np.random.binomial(n=10, p=0.5, size=5))
print(np.random.poisson(lam=2.5, size=2))
print(np.random.beta(a=2, b=5, size=2))
