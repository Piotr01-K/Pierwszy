import asyncio
import random


async def losowe_zadanie(nr):
    """
    Korutyna śpi losowy czas (1–10 s)
    i zwraca ten czas.
    """
    czas = random.randint(1, 10)
    print(f"Zadanie {nr} śpi przez {czas} sekund")
    await asyncio.sleep(czas)
    return czas


async def main():
    # Tworzymy 5 zadań
    zadania = [
        asyncio.create_task(losowe_zadanie(i))
        for i in range(1, 6)
    ]

    # Czekamy tylko na pierwsze zakończone zadanie
    zakonczone, oczekujace = await asyncio.wait(
        zadania,
        return_when=asyncio.FIRST_COMPLETED
    )

    # Pobieramy wynik pierwszego zakończonego zadania
    for zadanie in zakonczone:
        print(f"\n🏆 Pierwsze zakończone zadanie! Czas snu: {zadanie.result()} s")

    # (opcjonalnie) anulujemy pozostałe zadania
    for zadanie in oczekujace:
        zadanie.cancel()


if __name__ == "__main__":
    asyncio.run(main())
