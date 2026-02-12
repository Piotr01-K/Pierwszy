import asyncio
import aiofiles


async def zapisz_log(numer: int, lock: asyncio.Lock):
    """
    Korutyna generująca log i zapisująca go do pliku
    """
    tekst = f"Log z korutyny {numer}\n"

    # LOCK — tylko jedna korutyna naraz zapisuje do pliku
    async with lock:
        async with aiofiles.open("logs.txt", mode="a", encoding="utf-8") as plik:
            await plik.write(tekst)

    # symulacja innych działań
    await asyncio.sleep(0.2)


async def main():
    lock = asyncio.Lock()

    zadania = [
        asyncio.create_task(zapisz_log(i, lock))
        for i in range(1, 6)
    ]

    await asyncio.gather(*zadania)


if __name__ == "__main__":
    asyncio.run(main())
