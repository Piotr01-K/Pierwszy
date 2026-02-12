from aiohttp import web


async def handle_hello(request):
    """
    Handler obsługujący zapytania GET na '/'.
    """
    name = request.query.get("name", "Świecie")
    return web.Response(
        text=f"Witaj, {name}!",
        content_type="text/html"
    )


app = web.Application()
app.router.add_get("/", handle_hello)


if __name__ == "__main__":
    print("Uruchamiam serwer na http://127.0.0.1:8080")
    web.run_app(app, host="127.0.0.1", port=8080)
