from aiohttp import web

# Handler: /witaj/{imie}
async def witaj(request):
    imie = request.match_info.get("imie")

    # 🔒 Sprawdzenie warunku
    if imie == "admin":
        raise web.HTTPForbidden(text="Dostęp dla admina zabroniony")

    return web.Response(text=f"Witaj, {imie}!")

app = web.Application()
app.router.add_get("/witaj/{imie}", witaj)

web.run_app(app, host="127.0.0.1", port=8080)