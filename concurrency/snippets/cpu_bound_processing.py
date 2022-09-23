import time
from nth_prime import is_prime


def find_primes(min, max):
    return [i for i in range(min, max) if is_prime(i)]


def main():
    start_time = time.perf_counter()
    total = sum(find_primes(2, 2_000_000))
    duration = time.perf_counter() - start_time
    print(total)
    print(f"Calculation took {duration:.2f} seconds")


if __name__ == "__main__":
    main()
