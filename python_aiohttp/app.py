from aiohttp import web
from db.base import SessionLocal, init_db
from db.models import Product


async def on_startup(app):
    await init_db()


# POST /products
async def create_product(request):
    data = await request.json()

    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        raise web.HTTPBadRequest(text="Brak name lub price")

    async with SessionLocal() as session:
        product = Product(name=name, price=price)
        session.add(product)
        await session.commit()
        await session.refresh(product)

    return web.json_response(
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
        },
        status=201
    )


app = web.Application()
app.router.add_post("/products", create_product)

app.on_startup.append(on_startup)

web.run_app(app, port=8080)