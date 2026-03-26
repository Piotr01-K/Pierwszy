from aiohttp import web


async def handle_post(request):
    data = await request.json()

    name = data.get("name", "Anonim")
    age = data.get("age", "nieznany")

    return web.json_response(
        {
            "message": f"Cześć {name}",
            "age": age,
        }
    )


app = web.Application()
app.router.add_post("/hello", handle_post)

web.run_app(app, port=8080)


# Opcja B - z curl - do wklejenia w terminalu:
# curl.exe --% -X POST http://127.0.0.1:8080/hello -H "Content-Type: application/json" -d "{\"name\":\"Paweł\",\"age\":40}"