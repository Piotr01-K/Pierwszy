import asyncio
import random


async def producent(queue: asyncio.Queue):
    """
    Producent: co 0.5 sekundy wrzuca liczbę (1–20) do kolejki
    """
    for _ in range(20):
        liczba = random.randint(1, 20)
        await queue.put(liczba)
        print(f"Producent dodał liczbę: {liczba}")
        await asyncio.sleep(0.5)

    # sygnał zakończenia – None dla każdego konsumenta
    await queue.put(None)
    await queue.put(None)


async def konsument(numer: int, queue: asyncio.Queue):
    """
    Konsument: pobiera liczby z kolejki i je przetwarza
    """
    while True:
        liczba = await queue.get()

        if liczba is None:
            # sygnał zakończenia pracy
            break

        print(f"Konsument {numer} przetworzył liczbę: {liczba}")
        await asyncio.sleep(0.1)  # symulacja przetwarzania


async def main():
    queue = asyncio.Queue()

    # uruchamiamy producenta i 2 konsumentów
    producer_task = asyncio.create_task(producent(queue))
    consumer_1 = asyncio.create_task(konsument(1, queue))
    consumer_2 = asyncio.create_task(konsument(2, queue))

    await asyncio.gather(producer_task, consumer_1, consumer_2)


if __name__ == "__main__":
    asyncio.run(main())
