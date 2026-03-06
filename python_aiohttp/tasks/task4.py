from aiohttp import web
from datetime import datetime


async def hello(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )


async def witaj(request):
    imie = request.match_info["imie"]
    return web.Response(
        text=f"Witaj, {imie}!",
        content_type="text/plain"
    )


async def api_status(request):
    data = {
        "status": "OK",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return web.json_response(data)


app = web.Application()
app.router.add_get("/", hello)
app.router.add_get("/witaj/{imie}", witaj)
app.router.add_get("/api/status", api_status)

web.run_app(app, port=8080)