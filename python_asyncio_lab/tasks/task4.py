import asyncio
import time


async def zadanie1():
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")


async def zadanie2():
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone")


async def main():
    start = time.time()

    await asyncio.gather(
        zadanie1(),
        zadanie2()
    )

    end = time.time()
    print(f"Czas wykonania: {end - start:.2f} sekundy")


asyncio.run(main())
