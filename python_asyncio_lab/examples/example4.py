import asyncio
import time


async def pobierz_dane_uzytkownika(user_id):
    print(f"Pobieram dane dla użytkownika {user_id}...")
    await asyncio.sleep(2)
    print("Dane użytkownika pobrane.")
    return {"id": user_id, "name": "Jan Kowalski"}


async def pobierz_zamowienia_uzytkownika(user_id):
    print(f"Pobieram zamówienia dla użytkownika {user_id}...")
    await asyncio.sleep(3)
    print("Zamówienia pobrane.")
    return ["książka", "długopis", "zeszyt"]


async def main():
    start_time = time.time()

    # 🔹 tworzymy ZADANIA (Taski)
    task_dane = asyncio.create_task(pobierz_dane_uzytkownika(1))
    task_zamowienia = asyncio.create_task(pobierz_zamowienia_uzytkownika(1))

    # 🔹 czekamy na wyniki
    dane = await task_dane
    zamowienia = await task_zamowienia

    print(f"Użytkownik: {dane['name']}, zamówienia: {zamowienia}")

    end_time = time.time()
    print(f"Czas całkowity: {end_time - start_time:.2f}s")


asyncio.run(main())
