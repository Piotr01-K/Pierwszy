from aiohttp import web
import time

# --- Middleware ---
@web.middleware
async def timing_middleware(request, handler):
    start_time = time.time()
    print(f"[MIDDLEWARE] Przychodzące zapytanie: {request.method} {request.path}")

    response = await handler(request)

    duration = time.time() - start_time
    print(f"[MIDDLEWARE] Zakończono w {duration:.4f}s")

    return response


# --- Handler ---
async def handle_hello(request):
    await asyncio.sleep(1)  # symulacja wolnej operacji I/O
    return web.Response(text="Hello from middleware example!")


# --- Aplikacja ---
def create_app():
    app = web.Application(middlewares=[timing_middleware])
    app.router.add_get("/", handle_hello)
    return app


if __name__ == "__main__":
    import asyncio
    app = create_app()
    web.run_app(app, port=8080)