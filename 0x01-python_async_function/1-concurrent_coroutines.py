#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
    The list of the delays are in ascending order without
    because of concurrency."""
    lst = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        res = await task
        lst.append(res)

    return lst


if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
