import time

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

start_time = time.perf_counter()

in_both = []

for p in primes:
    for f in fibonacci:
        if p == f:
            in_both.append(p)

print(f"Took {time.perf_counter() - start_time:.8f} seconds")

print(in_both)

# Better to...

start_time = time.perf_counter()

in_both = set(primes) & set(fibonacci)

print(f"Took {time.perf_counter() - start_time:.8f} seconds")

print(in_both)
