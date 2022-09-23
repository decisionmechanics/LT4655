import time

start_time = time.perf_counter()

odd_cubes = []
for n in range(1_000_000):
    if n % 2 == 1:
        odd_cubes.append(n**3)

print(f"Took {time.perf_counter() - start_time:.4f} seconds")

print(odd_cubes[:10])

# Better to...

start_time = time.perf_counter()

odd_cubes = [n**3 for n in range(1_000_000) if n % 2 == 1]

print(f"Took {time.perf_counter() - start_time:.4f} seconds")

print(odd_cubes[:10])
