import asyncio
import random


async def dlugie_obliczenia():
    """
    Korutyna symulująca długie obliczenia.
    Po losowym czasie (2–5 s) zwraca losową liczbę (1–100).
    """
    czas = random.uniform(2, 5)
    await asyncio.sleep(czas)

    wynik = random.randint(1, 100)
    print(f"Zakończono po {czas:.2f}s, wynik = {wynik}")
    return wynik


async def main():
    """
    Uruchamia 10 korutyn współbieżnie
    i sumuje ich wyniki.
    """
    zadania = [dlugie_obliczenia() for _ in range(10)]

    wyniki = await asyncio.gather(*zadania)

    suma = sum(wyniki)
    print(f"\nSUMA WYNIKÓW: {suma}")


if __name__ == "__main__":
    asyncio.run(main())
