import time

start_time = time.perf_counter()
time.sleep(1)
duration = time.perf_counter() - start_time
print(f"Slept for {duration} second(s)")
