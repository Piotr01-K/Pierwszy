import asyncio
import random
import time


async def popros_ai_o_analize(tekst):
    """Symuluje zapytanie do API analizującego sentyment tekstu."""
    print(f"Wysyłam do analizy: '{tekst[:20]}...'")

    # Symulacja losowego czasu odpowiedzi sieci i modelu
    czas_oczekiwania = random.uniform(1, 4)
    await asyncio.sleep(czas_oczekiwania)

    wynik = random.choice(["pozytywny", "negatywny", "neutralny"])
    print(f"Otrzymano odpowiedź dla: '{tekst[:20]}...' -> {wynik}")

    return {"tekst": tekst, "sentyment": wynik}


async def main():
    zdania = [
        "To był absolutnie fantastyczny film!",
        "Obsługa klienta jest poniżej krytyki.",
        "Pogoda dzisiaj jest całkiem w porządku.",
        "Nie mogę się doczekać wakacji.",
        "Znowu utknąłem w korku, co za dzień.",
    ]

    start_time = time.time()

    # Tworzymy listę korutyn do wykonania
    zadania = [popros_ai_o_analize(z) for z in zdania]

    # Uruchamiamy wszystkie analizy współbieżnie
    wyniki_analizy = await asyncio.gather(*zadania)

    print("\n--- Wyniki końcowe ---")
    for wynik in wyniki_analizy:
        print(f"'{wynik['tekst']}' ma sentyment: {wynik['sentyment']}")

    end_time = time.time()
    print(f"\nCałkowity czas analizy: {end_time - start_time:.2f}s")


asyncio.run(main())
