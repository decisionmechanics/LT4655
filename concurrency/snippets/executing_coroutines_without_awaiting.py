import asyncio


async def do_something(n):
    print(f"{n + 1}: Zzz...")
    await asyncio.sleep(1)
    print(f"{n + 1}: Sleeping Beauty never awoke")


async def main():
    # Fire and forget
    for i in range(10):
        asyncio.ensure_future(do_something(i))


if __name__ == "__main__":
    asyncio.run(main())
