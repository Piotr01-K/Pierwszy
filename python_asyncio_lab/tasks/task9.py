import asyncio
import aiohttp


async def sprawdz_status(session, url):
    try:
        async with session.get(url) as response:
            return f"{url} - Status: {response.status}"
    except Exception as e:
        return f"{url} - Błąd: {e}"


async def main():
    urls = [
        "https://google.com",
        "https://github.com",
        "https://python.org",
        "https://stackoverflow.com",
        "https://nonexistent.example"
    ]

    async with aiohttp.ClientSession() as session:
        zadania = [
            sprawdz_status(session, url)
            for url in urls
        ]

        wyniki = await asyncio.gather(*zadania)

        for wynik in wyniki:
            print(wynik)


asyncio.run(main())
