from aiohttp import web
import json


async def handle_data_demo(request: web.Request):
    """
    Handler demonstrujący odczyt różnych typów danych.
    POST /api/demo/{id}?kategoria=test
    """

    # 1. Dynamiczna część ścieżki
    user_id = request.match_info.get("id")

    # 2. Query params
    category = request.query.get("kategoria", "domyślna")

    # 3. Dane z body (JSON)
    data_source = "brak danych w ciele"

    if request.content_type == "application/json":
        try:
            json_data = await request.json()
            data_source = json_data.get("source", "nieznany")
        except json.JSONDecodeError:
            raise web.HTTPBadRequest(text="Niepoprawny format JSON")

    response_data = {
        "dynamic_path_id": user_id,
        "query_param_category": category,
        "body_data_source": data_source,
        "status": "przetworzono"
    }

    return web.json_response(response_data, status=200)


app = web.Application()
app.router.add_post("/api/demo/{id}", handle_data_demo)

if __name__ == "__main__":
    web.run_app(app, port=8080)
