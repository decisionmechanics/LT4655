import asyncio
import math


async def sqrt(n):
    await asyncio.sleep(1)

    return math.sqrt(n)


async def main():
    try:
        sqrts = await asyncio.gather(
            *(sqrt(i + 1) for i in range(5, -6, -1)), return_exceptions=False
        )

        print(sqrts)
    except ValueError as exc_info:
        print("Exception:", exc_info)


if __name__ == "__main__":
    asyncio.run(main())
