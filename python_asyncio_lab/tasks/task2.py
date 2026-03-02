import asyncio


async def licznik(n):
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(1)


asyncio.run(licznik(5))
