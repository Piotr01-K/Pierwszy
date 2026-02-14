import asyncio
import aiohttp

URL = "http://127.0.0.1:8080/api/status"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json()

            print("Odpowiedź z API:")
            print(data)


asyncio.run(main())