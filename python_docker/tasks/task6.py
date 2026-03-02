# task 6 compose_backend

import asyncio
import os
from aiohttp import web
import asyncpg

DB_HOST = os.getenv("DB_HOST", "database")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "postgres")


async def init_db(app):
    print("Connecting to database...")

    for attempt in range(10):
        try:
            app["db"] = await asyncpg.create_pool(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
            )
            print("✅ Connected to PostgreSQL")
            return
        except Exception as e:
            print(f"❌ DB not ready (attempt {attempt+1}/10): {e}")
            await asyncio.sleep(2)

    raise RuntimeError("Could not connect to database")


async def close_db(app):
    await app["db"].close()


async def health(request):
    try:
        async with request.app["db"].acquire() as conn:
            await conn.fetchval("SELECT 1")
        return web.json_response({"status": "ok"})
    except Exception as e:
        return web.json_response({"status": "error", "detail": str(e)})


app = web.Application()
app.router.add_get("/", health)

app.on_startup.append(init_db)
app.on_cleanup.append(close_db)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8000)