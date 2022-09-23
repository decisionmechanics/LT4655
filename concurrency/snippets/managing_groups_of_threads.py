import concurrent.futures
import time


def do_something(n):
    print(f"{n + 1}: Zzz...")
    time.sleep(1)


start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(do_something, range(10))

duration = time.perf_counter() - start_time

print(f"Took {duration:.2f} seconds")
