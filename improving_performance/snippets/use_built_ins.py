import time

start_time = time.perf_counter()

total = 0

for i in range(1_000_000):
    total += i

print(f"Took {time.perf_counter() - start_time:.2f} seconds")

print(total)

# Better to...

start_time = time.perf_counter()

total = sum(range(1_000_000))

print(f"Took {time.perf_counter() - start_time:.2f} seconds")

print(total)
