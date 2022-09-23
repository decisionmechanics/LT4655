import asyncio
import pytest


async def cube(n):
    await asyncio.sleep(1)

    return n**3


@pytest.mark.asyncio
async def test_some_asyncio_code():
    three_cubed = await cube(3)
    assert three_cubed == 27
