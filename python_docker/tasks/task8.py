# task 8 custom_network_dns
# Backend API + klient w tej samej sieci Docker

import socket
from aiohttp import web


async def hello(request):
    hostname = socket.gethostname()
    return web.json_response({
        "message": "Hello from backend",
        "container": hostname
    })


app = web.Application()
app.router.add_get("/", hello)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8000)