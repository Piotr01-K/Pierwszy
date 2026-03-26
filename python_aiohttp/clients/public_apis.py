import asyncio
import aiohttp


URLS = [
    "https://api.publicapis.org/random?auth=null",
    "https://api.publicapis.org/random?auth=null",
    "https://api.publicapis.org/random?auth=null",
]


async def fetch(session, url):
    """
    Pobiera dane JSON z podanego URL-a
    """
    async with session.get(url) as response:
        data = await response.json()
        return data


async def main():
    async with aiohttp.ClientSession() as session:

        # Tworzymy listę zadań (korutyn)
        tasks = [
            fetch(session, url)
            for url in URLS
        ]

        # Uruchamiamy wszystkie zadania JEDNOCZEŚNIE
        results = await asyncio.gather(*tasks)

        # Wypisujemy wyniki
        for i, result in enumerate(results, start=1):
            entry = result["entries"][0]
            print(f"\nAPI {i}:")
            print(f"  Nazwa: {entry['API']}")
            print(f"  Opis:  {entry['Description']}")
            print(f"  Link:  {entry['Link']}")


if __name__ == "__main__":
    asyncio.run(main())