#!/usr/bin/env python3
"""
0. The basics of async
"""

import asyncio
import random


async def wait_random(wait_random: int = 10) -> float:
    """Takes in an integer argument (max_delay, with a default value of 10)
    and waits for a random delay between 0 and max_delay seconds"""
    delay = random.uniform(0, wait_random)
    await asyncio.sleep(delay)
    return delay


if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
