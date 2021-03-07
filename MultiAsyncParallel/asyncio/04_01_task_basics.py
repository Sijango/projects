import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tack')
    return 'Tick-Tack'


async def main():
    t1 = asyncio.create_task(tick())
    t2 = asyncio.ensure_future(tick())

    results = await asyncio.gather(t1, t2)

    for x in results:
        print(x)
    
    # await t1
    # await t2

    print(f'Task t1. Done = {t1.done()}')
    print(f'Task t2. Done = {t2.done()}')


if __name__ == '__main__':
    asyncio.run(main())
