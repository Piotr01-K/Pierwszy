import asyncio


async def zadanie_io(nazwa, czas):
    print(f"{nazwa}: start (czekam {czas}s)")
    await asyncio.sleep(czas)
    print(f"{nazwa}: koniec")


async def main():
    await asyncio.gather(
        zadanie_io("Zadanie A", 2),
        zadanie_io("Zadanie B", 3),
        zadanie_io("Zadanie C", 1),
    )


asyncio.run(main())
