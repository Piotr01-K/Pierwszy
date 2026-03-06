from aiohttp import web
import json


async def create_user(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.json_response(
            {"error": "Niepoprawny JSON"},
            status=400
        )

    name = data.get("name")
    age = data.get("age")

    if not name or not age:
        return web.json_response(
            {"error": "Brak wymaganych pól: name, age"},
            status=400
        )

    return web.json_response(
        {
            "message": "Użytkownik utworzony",
            "user": {
                "name": name,
                "age": age
            }
        },
        status=201
    )


app = web.Application()
app.router.add_post("/users", create_user)

web.run_app(app, port=8080)