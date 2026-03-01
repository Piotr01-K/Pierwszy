# task 9 redis_cache_api

import asyncio
import json
from aiohttp import web
import redis.asyncio as redis

REDIS_URL = "redis://redis:6379"


async def get_data():
    """Symulacja wolnej bazy danych"""
    await asyncio.sleep(2)
    return {"message": "Data from database"}


async def handler(request):
    app = request.app
    redis_client = app["redis"]

    cache_key = "my_data"

    # 🔥 sprawdź cache
    cached = await redis_client.get(cache_key)

    if cached:
        return web.json_response({
            "source": "cache",
            "data": json.loads(cached)
        })

    # ❌ brak w cache → symulacja DB
    data = await get_data()

    # 💾 zapisz do cache (60 sekund)
    await redis_client.set(cache_key, json.dumps(data), ex=60)

    return web.json_response({
        "source": "database",
        "data": data
    })


async def init_redis(app):
    print("Connecting to Redis...")
    app["redis"] = redis.from_url(REDIS_URL)
    print("✅ Connected to Redis")


async def close_redis(app):
    await app["redis"].close()


app = web.Application()
app.router.add_get("/", handler)
app.on_startup.append(init_redis)
app.on_cleanup.append(close_redis)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8000)