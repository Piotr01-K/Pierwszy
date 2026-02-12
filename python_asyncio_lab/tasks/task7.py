import asyncio


async def pobierz_pogode(miasto):
    await asyncio.sleep(1.5)
    return {
        "miasto": miasto,
        "temperatura": 25,
        "stan": "słonecznie"
    }


async def main():
    miasta = ["Warszawa", "Kraków", "Gdańsk"]

    zadania = [
        pobierz_pogode(miasto)
        for miasto in miasta
    ]

    wyniki = await asyncio.gather(*zadania)

    for pogoda in wyniki:
        print(pogoda)


asyncio.run(main())
