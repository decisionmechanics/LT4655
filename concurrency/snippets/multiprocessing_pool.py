import multiprocessing
import time
from nth_prime import is_prime


def find_primes(min, max):
    return [i for i in range(min, max) if is_prime(i)]


def sum_primes(x):
    return sum(find_primes(x[0], x[1]))


def main():
    start_time = time.perf_counter()

    with multiprocessing.Pool() as pool:
        values = [
            (2, 500_000),
            (500_000, 1_000_000),
            (1_000_000, 1_500_000),
            (1_500_000, 2_000_000),
        ]

        primes = pool.map(sum_primes, values)

    total = sum(primes)

    duration = time.perf_counter() - start_time

    print(total)
    print(f"Calculation took {duration:.2f} seconds")


if __name__ == "__main__":
    main()
