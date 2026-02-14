from aiohttp import web
from sqlalchemy import select

from db.base import SessionLocal, init_db
from db.models import Product
from db import models  # ważne: rejestruje modele w SQLAlchemy


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
# TWORZENIE APPKI
# =========================
async def create_app():
    await init_db()  # tworzy tabelę przy starcie

    app = web.Application()
    app.add_routes([
        web.get("/products", list_products),
        web.post("/products", create_product),
        web.get("/products/{id}", get_product),   # dodane Lesson 32 task 11
        web.patch("/products/{id}", update_product),  # dodane Lesson 32 task 14
        web.put("/products/{id}", update_product),    # dodane Lesson 32 task 14
        web.delete("/products/{id}", delete_product),   # dodane Lesson 32 task 15
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


    # PATCH /products/{id}
async def update_product(request):
    product_id = int(request.match_info["id"])
    data = await request.json()

    async with SessionLocal() as session:
        # 1️⃣ pobieramy produkt z bazy
        result = await session.execute(
            select(Product).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()

        if not product:
            raise web.HTTPNotFound(text="Produkt nie istnieje")

        # 2️⃣ aktualizujemy tylko pola które przyszły w JSON
        if "name" in data:
            product.name = data["name"]

        if "price" in data:
            product.price = data["price"]

        # 3️⃣ zapis do bazy
        await session.commit()
        await session.refresh(product)

    return web.json_response({
        "id": product.id,
        "name": product.name,
        "price": product.price,
    })

# dodane lesson 32 task 15
# DELETE /products/{id}
async def delete_product(request):
    product_id = int(request.match_info["id"])

    async with SessionLocal() as session:
        # 1️⃣ Szukamy produktu
        result = await session.execute(
            select(Product).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()

        # 2️⃣ Jeśli nie istnieje → 404
        if product is None:
            raise web.HTTPNotFound(text="Produkt nie istnieje")

        # 3️⃣ Usuwamy produkt
        await session.delete(product)
        await session.commit()

    # 4️⃣ Zwracamy PUSTĄ odpowiedź z kodem 204
    return web.Response(status=204)

# =========================
# START SERWERA
# =========================
if __name__ == "__main__":
    web.run_app(create_app())

