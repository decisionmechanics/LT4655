import statistics
import timeit
from nth_prime import main

N = 100_000
t = timeit.repeat(stmt=lambda: main(N), repeat=3, number=1)
print(t)
print(f"Mean execution time is {statistics.mean(t):.2f}")
