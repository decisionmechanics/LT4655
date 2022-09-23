import functools
import time
from nth_prime import main as find_nth_prime


@functools.lru_cache(maxsize=16)
def find_cached_nth_prime(n):
    return find_nth_prime(n)


start_time = time.perf_counter()
find_cached_nth_prime(1_000)
print(f"Took {time.perf_counter() - start_time:.4f} seconds")

start_time = time.perf_counter()
find_cached_nth_prime(1_000)
print(f"Took {time.perf_counter() - start_time:.4f} seconds")
