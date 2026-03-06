import asyncio
import time


class RateLimiter:
    def __init__(self, max_calls: int, period: float = 1.0):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.monotonic()

            # usuń stare wywołania (starsze niż okres)
            self.calls = [
                t for t in self.calls
                if now - t < self.period
            ]

            if len(self.calls) < self.max_calls:
                # można wykonać zapytanie
                self.calls.append(now)
                return

            # trzeba poczekać
            najstarsze = self.calls[0]
            wait_time = self.period - (now - najstarsze)

        # czekanie POZA lockiem
        if wait_time > 0:
            await asyncio.sleep(wait_time)

        # po czekaniu próbujemy jeszcze raz
        await self.acquire()


async def worker(nr: int, limiter: RateLimiter):
    for i in range(3):
        await limiter.acquire()
        print(f"[{time.strftime('%X')}] Zadanie {nr} — wykonanie {i + 1}")


async def main():
    limiter = RateLimiter(max_calls=5, period=1.0)

    tasks = [
        asyncio.create_task(worker(i, limiter))
        for i in range(1, 21)
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
