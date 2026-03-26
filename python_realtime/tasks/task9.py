import asyncio
from aiohttp import web
from typing import Set, Dict

# 🔥 aktywne połączenia
active_connections: Set[web.WebSocketResponse] = set()

# 🔥 mapa websocket → nick
client_nicks: Dict[web.WebSocketResponse, str] = {}


async def broadcast(message: str):
    """Wyślij wiadomość do wszystkich klientów"""
    for ws in active_connections:
        if not ws.closed:
            await ws.send_str(message)


async def chat_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # dodaj klienta
    active_connections.add(ws)
    print(f"✅ Nowy klient. Aktywnych: {len(active_connections)}")

    try:
        # 🔥 PIERWSZA wiadomość = nick
        msg = await ws.receive()

        if msg.type == web.WSMsgType.TEXT:
            nick = msg.data.strip()
            client_nicks[ws] = nick

            await ws.send_str(f"Witaj {nick}!")
            await broadcast(f"🟢 {nick} dołączył do chatu")

        # 🔥 kolejne wiadomości
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                nick = client_nicks.get(ws, "Unknown")
                text = msg.data.strip()

                broadcast_msg = f"{nick}: {text}"
                print(f"💬 {broadcast_msg}")

                await broadcast(broadcast_msg)

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd: {ws.exception()}")

    finally:
        # sprzątanie
        active_connections.discard(ws)

        nick = client_nicks.pop(ws, "Unknown")
        await broadcast(f"🔴 {nick} opuścił chat")

        print(f"❌ Klient rozłączony. Zostało: {len(active_connections)}")

    return ws


app = web.Application()
app.router.add_get("/ws", chat_handler)

if __name__ == "__main__":
    print("🚀 Chat server działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)