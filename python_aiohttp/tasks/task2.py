from aiohttp import web


async def hello(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )


app = web.Application()
app.router.add_get("/", hello)

web.run_app(app, port=8080)