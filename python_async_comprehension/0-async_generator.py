#!/usr/bin/env python3
""" Creating a coroutine """
from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ Yield a random number from 0 to 10 """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
