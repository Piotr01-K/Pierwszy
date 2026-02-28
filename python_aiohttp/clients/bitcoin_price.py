import asyncio
import aiohttp


URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


async def main():
    # 1. Tworzymy asynchroniczną sesję HTTP
    async with aiohttp.ClientSession() as session:

        # 2. Wysyłamy zapytanie GET
        async with session.get(URL) as response:

            # 3. Odbieramy odpowiedź jako JSON
            data = await response.json()

            # 4. Wyciągamy cenę BTC w USD
            price_usd = data["bpi"]["USD"]["rate"]

            # 5. Wypisujemy wynik
            print(f"Cena Bitcoina (USD): {price_usd}")


if __name__ == "__main__":
    asyncio.run(main())