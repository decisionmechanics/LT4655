from statistics import mean
import time

numbers = list(range(1_000_000))

start_time = time.perf_counter()

average = mean(numbers)

print(f"Took {time.perf_counter() - start_time:.2f} seconds")

print(average)

# Better to...

start_time = time.perf_counter()

average = sum(numbers) / len(numbers)

print(f"Took {time.perf_counter() - start_time:.2f} seconds")

print(average)
