#!/usr/bin/env python3
""" First asynchronous coroutine """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Random wait time to test async """
    wait_time = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
