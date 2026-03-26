import asyncio
from aiohttp import web

# ======================================
# ZBIÓR AKTYWNYCH POŁĄCZEŃ
# ======================================
active_connections = set()


async def broadcast(message: str):
    """
    Wysyła wiadomość do wszystkich podłączonych klientów.
    """
    for ws in active_connections.copy():
        if not ws.closed:
            await ws.send_str(message)


async def websocket_handler(request):
    """
    WebSocket handler z broadcastem.
    """
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # dodajemy klienta
    active_connections.add(ws)
    print(f"✅ Nowy klient. Aktywnych: {len(active_connections)}")

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                user_message = msg.data
                print(f"📥 Otrzymano: {user_message}")

                # 🔥 broadcast do wszystkich
                await broadcast(f"📢 {user_message}")

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd: {ws.exception()}")

    finally:
        # usuwamy klienta przy rozłączeniu
        active_connections.discard(ws)
        print(f"❌ Klient rozłączony. Zostało: {len(active_connections)}")

    return ws


# ======================================
# APLIKACJA
# ======================================
app = web.Application()
app.router.add_get("/ws", websocket_handler)


if __name__ == "__main__":
    print("🚀 Broadcast server: ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)