from aiohttp import web
import time


@web.middleware
async def logging_middleware(request, handler):
    start_time = time.time()

    print(f"➡️ {request.method} {request.path}")

    response = await handler(request)

    duration = time.time() - start_time
    print(f"⬅️ {request.method} {request.path} [{response.status}] "
          f"({duration:.4f}s)")

    return response


async def hello(request):
    return web.json_response({"message": "Hello from aiohttp!"})


app = web.Application(middlewares=[logging_middleware])
app.router.add_get("/", hello)

web.run_app(app, port=8080)