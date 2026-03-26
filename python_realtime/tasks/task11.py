import asyncio
import time
from aiohttp import web

# ================================
#   USTAWIENIA
# ================================

PING_INTERVAL = 30      # co ile sekund wysyłamy ping
TIMEOUT = 60            # po ilu sekundach bez pong rozłączamy


# ================================
#   HANDLER
# ================================

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    print("✅ Klient połączony")

    last_pong = time.time()
    running = True

    # ================================
    #   TASK: wysyłanie pingów
    # ================================

    async def ping_loop():
        nonlocal running
        while running:
            await asyncio.sleep(PING_INTERVAL)

            if not running:
                break

            try:
                print("📤 Wysyłam ping")
                await ws.send_str("ping")

                # sprawdź timeout
                if time.time() - last_pong > TIMEOUT:
                    print("❌ Brak pong — rozłączam klienta")
                    await ws.close()
                    running = False
                    break

            except Exception as e:
                print("❌ Błąd ping:", e)
                running = False
                break

    ping_task = asyncio.create_task(ping_loop())

    # ================================
    #   odbieranie wiadomości
    # ================================

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                text = msg.data.strip()
                print("📥 Otrzymano:", text)

                if text == "pong":
                    last_pong = time.time()
                    print("🏓 Pong OK")

            elif msg.type == web.WSMsgType.ERROR:
                print("❌ Błąd:", ws.exception())

    finally:
        running = False
        ping_task.cancel()
        print("❌ Klient rozłączony")

    return ws


# ================================
#   APP
# ================================

app = web.Application()
app.router.add_get("/ws", websocket_handler)


# ================================
# ▶  RUN
# ================================

if __name__ == "__main__":
    print("🚀 Ping-Pong server: ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)