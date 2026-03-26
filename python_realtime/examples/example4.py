# examples/example4.py

from aiohttp import web


async def websocket_handler(request):
    """
    Prosty echo server WebSocket.
    Zwraca każdą wiadomość z prefixem "Echo:".
    """

    # 🔌 Tworzymy WebSocket
    ws = web.WebSocketResponse()

    # 🤝 handshake (upgrade HTTP → WebSocket)
    await ws.prepare(request)

    print("✅ Nowy klient połączony!")

    # 👂 nasłuchiwanie wiadomości
    async for msg in ws:

        # 📨 wiadomość tekstowa
        if msg.type == web.WSMsgType.TEXT:
            print(f"📥 Otrzymano: {msg.data}")

            # 📤 odsyłamy echo
            await ws.send_str(f"Echo: {msg.data}")

        # ❌ błąd
        elif msg.type == web.WSMsgType.ERROR:
            print(f"Błąd WebSocket: {ws.exception()}")

    print("❌ Klient rozłączony")
    return ws


# -------------------------------
# APLIKACJA
# -------------------------------

app = web.Application()
app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Serwer działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)