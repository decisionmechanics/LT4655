import time


def do_something(n):
    print(f"{n + 1}: Zzz...")
    time.sleep(1)


start_time = time.perf_counter()

for i in range(10):
    do_something(i)

duration = time.perf_counter() - start_time

print(f"Took {duration:.2f} seconds")
