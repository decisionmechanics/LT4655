import concurrent.futures
import time


def cube(n):
    time.sleep(1)

    return n**3


with concurrent.futures.ThreadPoolExecutor() as executor:
    cubes = executor.map(cube, range(1, 11))

print(list(cubes))
