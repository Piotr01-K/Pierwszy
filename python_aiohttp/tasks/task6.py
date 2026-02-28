from aiohttp import web
from datetime import datetime


async def hello(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )


async def witaj(request):
    imie = request.match_info["imie"]
    return web.Response(text=f"Witaj, {imie}!")


async def api_status(request):
    data = {
        "status": "OK",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return web.json_response(data)


async def api_search(request):
    q = request.query.get("q")

    if q:
        return web.json_response({"szukana_fraza": q})
    else:
        return web.json_response({"błąd": "Brak parametru q"})


async def api_echo(request):
    data = await request.json()
    return web.json_response(data)


app = web.Application()
app.router.add_get("/", hello)
app.router.add_get("/witaj/{imie}", witaj)
app.router.add_get("/api/status", api_status)
app.router.add_get("/api/search", api_search)
app.router.add_post("/api/echo", api_echo)

web.run_app(app, port=8080)