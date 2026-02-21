# examples/example3.py

import asyncio


class WebSocketConnection:
    """
    Symulacja cyklu życia połączenia WebSocket.
    """

    def __init__(self):
        self.is_connected = False

    async def connect(self):
        """Symulacja połączenia"""
        self.is_connected = True
        print("✅ Połączono z serwerem WebSocket")
        await self.send_message({"type": "hello", "client": "Python"})

    async def send_message(self, message):
        """Symulacja wysyłania wiadomości"""
        if self.is_connected:
            print(f"📤 Wysłano: {message}")

    async def receive_messages(self):
        """Symulacja odbierania wiadomości"""
        print("👂 Nasłuchiwanie wiadomości...")

        # symulujemy 3 wiadomości
        fake_messages = [
            {"type": "notification", "text": "Nowy użytkownik"},
            {"type": "ping"},
            {"type": "notification", "text": "Masz nowe powiadomienie"},
        ]

        for msg in fake_messages:
            await asyncio.sleep(1)
            print(f"📥 Otrzymano: {msg}")
            await self.handle_message(msg)

    async def handle_message(self, message):
        """Obsługa wiadomości"""
        msg_type = message.get("type")

        if msg_type == "ping":
            await self.send_message({"type": "pong"})

        elif msg_type == "notification":
            print(f"🔔 Powiadomienie: {message.get('text')}")

    async def disconnect(self):
        """Rozłączenie"""
        if self.is_connected:
            self.is_connected = False
            print("❌ Rozłączono z serwerem")


# -------------------------------
# URUCHOMIENIE DEMO
# -------------------------------

async def main():
    conn = WebSocketConnection()

    await conn.connect()
    await conn.receive_messages()
    await conn.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

'''
Wynik otrzymany w terminalu
✅ Połączono z serwerem WebSocket
📤 Wysłano: {'type': 'hello', 'client': 'Python'}
👂 Nasłuchiwanie wiadomości...
📥 Otrzymano: {'type': 'notification', 'text': 'Nowy użytkownik'}
🔔 Powiadomienie: Nowy użytkownik
📥 Otrzymano: {'type': 'ping'}
📤 Wysłano: {'type': 'pong'}
📥 Otrzymano: {'type': 'notification', 'text': 'Masz nowe powiadomienie'}
🔔 Powiadomienie: Masz nowe powiadomienie
❌ Rozłączono z serwerem
'''