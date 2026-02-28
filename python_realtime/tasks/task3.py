from aiohttp import web
import asyncio

# 🔢 licznik aktywnych połączeń
active_connections = 0


async def websocket_handler(request):
    global active_connections

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # ➕ nowy klient
    active_connections += 1
    print(f"✅ Nowy klient. Aktywnych: {active_connections}")

    # 📩 informacja dla klienta
    await ws.send_str(f"Jesteś klientem numer {active_connections}")

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                print(f"📥 Otrzymano: {msg.data}")
                await ws.send_str(f"Server: {msg.data}")

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd: {ws.exception()}")

    finally:
        # ➖ klient się rozłączył
        active_connections -= 1
        print(f"❌ Klient rozłączony. Aktywnych: {active_connections}")

    return ws


app = web.Application()
app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Echo WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)