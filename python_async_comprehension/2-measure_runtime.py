#!/usr/bin/env python3
""" Measuring time """
from time import perf_counter
from asyncio import gather
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ measures time awaiting async_comprehension """
    start = perf_counter()
    awaitables = [async_comprehension() for _ in range(4)]
    await gather(*awaitables)
    stop = perf_counter()
    return stop - start
