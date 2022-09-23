import time
from nth_prime import is_prime

NUMBER = 997

start_time = time.time()
print(is_prime(NUMBER))
duration = time.time() - start_time
print(f"time recorded {duration} second(s)")

start_time = time.perf_counter()
print(is_prime(NUMBER))
duration = time.perf_counter() - start_time
print(f"perf_counter recorded {duration} second(s)")
