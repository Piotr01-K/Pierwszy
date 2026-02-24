import asyncio
from aiohttp import web
from typing import Dict, Set

# ================================
#   ROOMS STORAGE
# ================================

rooms: Dict[str, Set[web.WebSocketResponse]] = {}


# ================================
#   BROADCAST DO POKOJU
# ================================

async def broadcast_to_room(room: str, message: str):
    if room not in rooms:
        return

    dead_connections = set()

    for ws in rooms[room]:
        if ws.closed:
            dead_connections.add(ws)
            continue

        try:
            await ws.send_str(message)
        except Exception:
            dead_connections.add(ws)

    # sprzątanie martwych połączeń
    for ws in dead_connections:
        rooms[room].discard(ws)


# ================================
#   HANDLER
# ================================

async def chat_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    current_room = None

    print("✅ Nowy klient połączony")

    try:
        async for msg in ws:

            if msg.type == web.WSMsgType.TEXT:
                text = msg.data.strip()

                # =====================
                # KOMENDA /join
                # =====================
                if text.startswith("/join "):
                    room_name = text.split("/join ", 1)[1]

                    # opuść poprzedni pokój
                    if current_room and ws in rooms.get(current_room, set()):
                        rooms[current_room].discard(ws)

                    # dołącz do nowego
                    current_room = room_name
                    rooms.setdefault(room_name, set()).add(ws)

                    await ws.send_str(f"✅ Dołączyłeś do pokoju: {room_name}")
                    print(f"👤 Klient dołączył do {room_name}")
                    continue

                # =====================
                # zwykła wiadomość
                # =====================
                if not current_room:
                    await ws.send_str("⚠️ Najpierw dołącz do pokoju: /join nazwa")
                    continue

                await broadcast_to_room(
                    current_room,
                    f"[{current_room}] {text}",
                )

            elif msg.type == web.WSMsgType.ERROR:
                print("❌ WebSocket error:", ws.exception())

    finally:
        # sprzątanie przy rozłączeniu
        if current_room and ws in rooms.get(current_room, set()):
            rooms[current_room].discard(ws)

        print("❌ Klient rozłączony")

    return ws


# ================================
#   APP
# ================================

app = web.Application()
app.router.add_get("/ws", chat_handler)

# ================================
#   RUN
# ================================

if __name__ == "__main__":
    print("🚀 Chat rooms server: ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)