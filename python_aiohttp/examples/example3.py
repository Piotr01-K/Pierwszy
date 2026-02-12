from aiohttp import web

# --- Handlery ---

async def handle_index(request):
    """ Handler dla strony głównej. """
    # Odczyt stanu aplikacji
    counter = request.app["app_counter"]
    return web.Response(
        text=f"Strona główna. Licznik startów serwera: {counter}"
    )


async def handle_user(request):
    """ Handler dla dynamicznej ścieżki użytkownika. """
    user_id = request.match_info.get("id", "0")

    try:
        user_id_int = int(user_id)
        return web.Response(
            text=f"Dane użytkownika o ID: {user_id_int}"
        )
    except ValueError:
        raise web.HTTPBadRequest(
            text="ID użytkownika musi być liczbą"
        )


# --- Sygnały startowe / czyszczące ---

async def on_startup(app):
    print("Serwer startuje! Inicjalizuję zasoby...")

    # zapisujemy dane w stanie aplikacji
    app["app_counter"] = app.get("app_counter", 0) + 1


async def on_cleanup(app):
    print("Serwer się zamyka. Czyszczę zasoby.")


# --- Fabryka aplikacji ---

def create_app():
    app = web.Application()

    # routing
    app.router.add_get("/", handle_index)
    app.router.add_get("/user/{id}", handle_user)

    # sygnały
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)

    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="127.0.0.1", port=8080)
