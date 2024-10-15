#!/usr/bin/env python3
"""
0. Async Generator
"""

import asyncio
import random
from typing import Any, AsyncGenerator, List


async def async_generator() -> AsyncGenerator[float, Any]:
    """yields a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == '__main__':
    async def print_yielded_values() -> None:
        result: List[float] = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
