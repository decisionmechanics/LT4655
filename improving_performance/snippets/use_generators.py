import itertools
import time

start_time = time.perf_counter()

numbers = [n**3 for n in range(1_000_000) if n % 2 == 1]
total = sum(numbers[:10])

print(f"Took {time.perf_counter() - start_time:.4f} seconds")

print(total)

# Better to...

start_time = time.perf_counter()

numbers = (n**3 for n in range(1_000_000) if n % 2 == 1)
total = sum(itertools.islice(numbers, 10))

print(f"Took {time.perf_counter() - start_time:.4f} seconds")

print(total)
