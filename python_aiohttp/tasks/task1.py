import asyncio
import time


async def sleeper(seconds: int):
    print(f" Start zadania ({seconds}s)")
    await asyncio.sleep(seconds)
    print(f" Koniec zadania ({seconds}s)")


async def main():
    start = time.time()

    await asyncio.gather(
        sleeper(1),
        sleeper(4),
        sleeper(2),
    )

    end = time.time()
    print(f"\n Całkowity czas wykonania: {end - start:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())