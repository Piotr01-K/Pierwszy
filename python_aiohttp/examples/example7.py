from aiohttp import web


async def hello(request):
    return web.json_response({"message": "OK"})


async def error(request):
    raise web.HTTPBadRequest(text="To jest błąd 400")


app = web.Application()
app.router.add_get("/", hello)
app.router.add_get("/error", error)

web.run_app(app, port=8080)