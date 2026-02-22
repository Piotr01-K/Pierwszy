import asyncio
import time


async def przygotuj_danie(nazwa, czas_przygotowania):
    print(f"Rozpoczynam przygotowanie: {nazwa}")

    # asyncio.sleep to asynchroniczna wersja time.sleep
    await asyncio.sleep(czas_przygotowania)

    print(f"Danie gotowe: {nazwa}")
    return f"Serwuję {nazwa}"


async def main():
    wynik = await przygotuj_danie("Pizza", 2)
    print(wynik)


# Uruchomienie głównej korutyny
asyncio.run(main())
