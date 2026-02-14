from aiohttp import web
from sqlalchemy import select

from db.base import SessionLocal, init_db
from db.models import Product
from db import models  # ważne: rejestruje modele w SQLAlchemy


# =========================
# GET /products  (lista)
# =========================
async def list_products(request):
    async with SessionLocal() as session:
        result = await session.execute(select(Product))
        products = result.scalars().all()

    data = [
        {"id": p.id, "name": p.name, "price": p.price}
        for p in products
    ]

    return web.json_response(data)


# =========================
# POST /products (tworzenie)
# =========================
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
        {"id": product.id, "name": product.name, "price": product.price},
        status=201,
    )


# =========================
# TWORZENIE APPKI
# =========================
async def create_app():
    await init_db()  # tworzy tabelę przy starcie

    app = web.Application()
    app.add_routes([
        web.get("/products", list_products),
        web.post("/products", create_product),
        web.get("/products/{id}", get_product),   # dodane Lesson 32 task 11
    ])
    return app

# dodane lesson 32 task 11
# GET /products/{id}
async def get_product(request):
    product_id = int(request.match_info["id"])

    async with SessionLocal() as session:
        result = await session.execute(
            select(Product).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()

    if product is None:
        raise web.HTTPNotFound(text="Produkt nie istnieje")

    return web.json_response(
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
        }
    )


# =========================
# START SERWERA
# =========================
if __name__ == "__main__":
    web.run_app(create_app())