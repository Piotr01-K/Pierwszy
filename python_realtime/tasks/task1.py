# tasks/task1.py

from aiohttp import web


async def websocket_handler(request):
    """
    Prosty echo server WebSocket.
    Otrzymuje wiadomość i odsyła ją z prefixem "Server: ".
    """

    # 🔌 tworzymy obiekt WebSocket
    ws = web.WebSocketResponse()

    # 🤝 handshake (upgrade HTTP → WebSocket)
    await ws.prepare(request)

    print("✅ Klient połączony")

    try:
        # 🔁 nasłuchujemy wiadomości od klienta
        async for msg in ws:

            # 📩 jeśli przyszła wiadomość tekstowa
            if msg.type == web.WSMsgType.TEXT:
                print("📥 Otrzymano:", msg.data)

                # 📤 odsyłamy echo z prefixem
                await ws.send_str(f"Server: {msg.data}")

            elif msg.type == web.WSMsgType.ERROR:
                print("❌ Błąd:", ws.exception())

    finally:
        print("❌ Klient rozłączony")

    return ws


# 🚀 tworzymy aplikację aiohttp
app = web.Application()

# rejestrujemy endpoint websocket
app.router.add_get("/ws", websocket_handler)


if __name__ == "__main__":
    print("🚀 Echo WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)