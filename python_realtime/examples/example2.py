# examples/example2.py

"""
Przykład pokazujący handshake WebSocket.

UWAGA:
To jest symulacja edukacyjna — nie otwieramy prawdziwego połączenia.
"""

print("=== WEBSOCKET HANDSHAKE DEMO ===\n")

# -------------------------------
# Żądanie klienta (HTTP Upgrade)
# -------------------------------

http_request = """
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
"""

print("📤 Klient wysyła żądanie upgrade:\n")
print(http_request)

# -------------------------------
# Odpowiedź serwera
# -------------------------------

http_response = """
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
"""

print("📥 Serwer odpowiada:\n")
print(http_response)

print("✅ Połączenie zostało przełączone na WebSocket!")