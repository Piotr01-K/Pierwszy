import asyncio


async def oblicz_potege(liczba, potega):
    await asyncio.sleep(2)
    return liczba ** potega


async def main():
    wynik = await oblicz_potege(2, 5)
    print(f"Wynik potęgowania: {wynik}")


asyncio.run(main())
