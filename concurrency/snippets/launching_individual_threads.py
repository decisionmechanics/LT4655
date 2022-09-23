import concurrent.futures
import time


def cube(n):
    time.sleep(1)

    return n**3


with concurrent.futures.ThreadPoolExecutor() as executor:
    wait_for = [executor.submit(cube, i + 1) for i in range(10)]

print([f.result() for f in concurrent.futures.as_completed(wait_for)])
