#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time: float = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time: float = time.perf_counter()
    return end_time - start_time


if __name__ == '__main__':
    async def main() -> float:
        return await (measure_runtime())

    print(asyncio.run(main()))
