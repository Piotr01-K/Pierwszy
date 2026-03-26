# tasks/task2.py

import asyncio
import aiohttp


async def websocket_client():
    """
    Klient WebSocket:
    - łączy się z serwerem
    - wysyła 3 wiadomości
    - odbiera odpowiedzi
    """

    url = "ws://localhost:8080/ws"

    print("🔌 Łączenie z serwerem...")

    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(url) as ws:
            print("✅ Połączono z serwerem")

            messages = [
                "Cześć",
                "Jak się masz?",
                "Do widzenia"
            ]

            # 🔁 wysyłamy wiadomości
            for msg in messages:
                print(f"📤 Wysyłam: {msg}")
                await ws.send_str(msg)

                # 📥 czekamy na odpowiedź serwera
                response = await ws.receive()

                if response.type == aiohttp.WSMsgType.TEXT:
                    print(f"📥 Odpowiedź: {response.data}")

                await asyncio.sleep(1)  # mała przerwa

            print("❌ Zamykam połączenie")
            await ws.close()


if __name__ == "__main__":
    asyncio.run(websocket_client())

'''
# po uruchomieniu otrzymałem w terminalu:
     Łączenie z serwerem...
✅ Połączono z serwerem
📤 Wysyłam: Cześć
📥 Odpowiedź: Server: Cześć
📤 Wysyłam: Jak się masz?
📥 Odpowiedź: Server: Jak się masz?
📤 Wysyłam: Do widzenia
📥 Odpowiedź: Server: Do widzenia
❌ Zamykam połączenie
'''