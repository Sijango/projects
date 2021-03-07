import asyncio
import time

from multithreading.decorators import measure_time, async_measure_time


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tack')


async def main():
    # await asyncio.gather(tick(), tick(), tick())
    awaitable_obj = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitable_obj

if __name__ == '__main__':
    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print('coroutines have finished')
    finally:
        loop.close()
        print('loop is closed')