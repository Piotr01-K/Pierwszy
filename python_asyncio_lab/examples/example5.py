import asyncio
import time


async def operacja(nazwa, czas_trwania):
    print(f"Start: {nazwa}")
    await asyncio.sleep(czas_trwania)
    print(f"Koniec: {nazwa}")
    return f"Wynik z {nazwa}"


async def main():
    start_time = time.time()

    wyniki = await asyncio.gather(
        operacja("A", 3),
        operacja("B", 1),
        operacja("C", 2),
    )

    print(f"Wyniki: {wyniki}")

    end_time = time.time()
    print(f"Czas całkowity: {end_time - start_time:.2f}s")


asyncio.run(main())
