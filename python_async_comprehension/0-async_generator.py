#!/usr/bin/env python3
""" Creating a coroutine """
import asyncio
import random


async def async_generator():
    """ Yield a random number from 0 to 10 """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
