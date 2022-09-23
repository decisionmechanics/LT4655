import asyncio


async def cube(n):
    await asyncio.sleep(1)

    return n**3


async def main():
    cubes = await asyncio.gather(*(cube(i + 1) for i in range(10)))

    print(cubes)


if __name__ == "__main__":
    asyncio.run(main())
