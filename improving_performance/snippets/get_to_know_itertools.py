import itertools
import time

numbers = list(range(100))

start_time = time.perf_counter()

cum_sum = []
running_total = 0

for n in numbers:
    cum_sum.append(running_total + n)
    running_total += n

print(f"Took {time.perf_counter() - start_time:.8f} seconds")

print(cum_sum[:10])

# Better to...

start_time = time.perf_counter()

cum_sum = list(itertools.accumulate(numbers))

print(f"Took {time.perf_counter() - start_time:.8f} seconds")

print(cum_sum[:10])
