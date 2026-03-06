import asyncio


async def odliczanie(nazwa, start):
    """
    Korutyna, która co sekundę wypisuje,
    ile sekund pozostało do końca odliczania.
    """
    for pozostalo in range(start, 0, -1):
        print(f"{nazwa}: zostało {pozostalo} sekund")
        await asyncio.sleep(1)

    print(f"{nazwa}: koniec!")


async def main():
    """
    Główna korutyna uruchamiająca kilka odliczań współbieżnie.
    """
    await asyncio.gather(
        odliczanie("Timer A", 5),
        odliczanie("Timer B", 3),
        odliczanie("Timer C", 7),
    )


if __name__ == "__main__":
    asyncio.run(main())
