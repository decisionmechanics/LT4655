import asyncio
import time


async def do_something(n):
    print(f"{n + 1}: Zzz...")
    await asyncio.sleep(1)


async def main():
    start_time = time.perf_counter()

    await asyncio.wait([do_something(i) for i in range(10)])

    duration = time.perf_counter() - start_time

    print(f"Took {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
