import asyncio


async def obsluz_klienta(reader: asyncio.StreamReader,
                          writer: asyncio.StreamWriter):
    """
    Obsługuje pojedynczego klienta:
    - odbiera dane
    - odsyła je z powrotem
    - zamyka połączenie
    """
    addr = writer.get_extra_info("peername")
    print(f"Połączono z klientem: {addr}")

    dane = await reader.read(1024)
    wiadomosc = dane.decode()

    print(f"Odebrano: {wiadomosc}")

    writer.write(dane)
    await writer.drain()

    print("Odesłano wiadomość, zamykam połączenie")
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        obsluz_klienta,
        host="127.0.0.1",
        port=8888
    )

    addr = server.sockets[0].getsockname()
    print(f"Serwer nasłuchuje na {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
