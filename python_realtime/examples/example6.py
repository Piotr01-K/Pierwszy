from aiohttp import web
import asyncio
from typing import Set

# zbiór aktywnych połączeń
active_connections: Set[web.WebSocketResponse] = set()


async def broadcast_message(message: str, sender=None):
    """
    Wysyła wiadomość do wszystkich klientów.
    """
    for connection in active_connections:
        if connection != sender and not connection.closed:
            try:
                await connection.send_str(message)
            except Exception as e:
                print(f"❌ Błąd wysyłania: {e}")


async def chat_handler(request):
    """
    WebSocket chat handler.
    """
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    active_connections.add(ws)
    print(f"✅ Nowy klient. Aktywnych: {len(active_connections)}")

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                user_message = msg.data
                print(f"💬 Wiadomość: {user_message}")

                await broadcast_message(
                    f"💬 Użytkownik: {user_message}",
                    sender=ws,
                )

    finally:
        active_connections.discard(ws)
        print(f"❌ Klient rozłączony. Zostało: {len(active_connections)}")

    return ws


app = web.Application()
app.router.add_get("/chat", chat_handler)

if __name__ == "__main__":
    print("🚀 Chat server działa na ws://localhost:8080/chat")
    web.run_app(app, host="localhost", port=8080)

'''
Otrzymałem w terminalu po uruchomieniu serwera:
✅ Nowy klient. Aktywnych: 1
✅ Nowy klient. Aktywnych: 2
💬 Wiadomość: Halo z karty 1
'''