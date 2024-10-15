#!/usr/bin/env python3
"""
1. Async Comprehensions
"""

import asyncio
from typing import Any, AsyncGenerator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[AsyncGenerator[float, Any]]:
    return [i async for i in async_generator()]


if __name__ == '__main__':
    async def main() -> None:
        print(await async_comprehension())

    asyncio.run(main())
