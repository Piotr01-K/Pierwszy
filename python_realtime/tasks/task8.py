import asyncio
import time
from aiohttp import web

# ======================================
# ZBIÓR AKTYWNYCH POŁĄCZEŃ
# ======================================
active_connections = set()


async def broadcast(message: str):
    """
    Wysyła wiadomość do wszystkich klientów.
    """
    for ws in active_connections.copy():
        if not ws.closed:
            await ws.send_str(message)


async def websocket_handler(request):
    """
    WebSocket handler mierzący czas połączenia klienta.
    """
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # 🕒 zapamiętujemy moment połączenia
    connect_time = time.time()

    active_connections.add(ws)
    print(f"✅ Nowy klient. Aktywnych: {len(active_connections)}")

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                user_message = msg.data
                print(f"📥 Otrzymano: {user_message}")

                await broadcast(f"📢 {user_message}")

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd: {ws.exception()}")

    finally:
        # 🕒 liczymy czas połączenia
        disconnect_time = time.time()
        duration = disconnect_time - connect_time

        active_connections.discard(ws)

        print(
            f"❌ Klient rozłączony. "
            f"Czas połączenia: {duration:.2f}s. "
            f"Zostało: {len(active_connections)}"
        )

    return ws


# ======================================
# APLIKACJA
# ======================================
app = web.Application()
app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Server z pomiarem czasu: ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)

'''
# po uruchomieniu serwera w terminalu:
🚀 Server z pomiarem czasu: ws://localhost:8080/ws
======== Running on http://localhost:8080 ========
(Press CTRL+C to quit)
✅ Nowy klient. Aktywnych: 1
📥 Otrzymano: Test czasu
❌ Klient rozłączony. Czas połączenia: 78.86s. Zostało: 0
'''