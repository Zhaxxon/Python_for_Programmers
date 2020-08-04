# Python 3.4 coroutine example
import asyncio

@asyncio.coroutine
def my_coro():
    yield from func()

# Python 3.5
import asyncio

async def my_coro():
    await func()