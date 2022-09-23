import time

numbers = list(range(1_000_000))

start_time = time.perf_counter()

contains = numbers.index(500_000) != 0

print(f"Took {time.perf_counter() - start_time:.4f} seconds")

print(contains)

# Better to...

start_time = time.perf_counter()

contains = 500_000 in numbers

print(f"Took {time.perf_counter() - start_time:.4f} seconds")

print(contains)
