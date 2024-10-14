#!/usr/bin/env python3
"""
4. Tasks
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
    The list of the delays are in ascending order without
    because of concurrency."""
    lst = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        res = await task
        lst.append(res)

    return lst


if __name__ == '__main__':
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
