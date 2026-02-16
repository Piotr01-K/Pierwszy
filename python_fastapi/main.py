from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List

from database import get_db, init_db
from models import UserORM, OrderORM
from schemas import UserCreate, UserUpdate, UserResponse, UserWithOrders
from schemas import OrderCreate, OrderResponse

app = FastAPI(title="FastAPI with Database")

# uruchamia się przy starcie serwera
@app.on_event("startup")
async def startup_event():
    await init_db()
    print("Database initialized!")

# ===============================
# CREATE USER
# ===============================
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    # sprawdzamy czy username istnieje
    result = await db.execute(
        select(UserORM).where(UserORM.username == user.username)
    )
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Username already exists")

    db_user = UserORM(**user.model_dump())

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return db_user


# ===============================
# GET ALL USERS
# ===============================
@app.get("/users", response_model=List[UserResponse])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(UserORM)
        .offset(skip)
        .limit(limit)
        .order_by(UserORM.created_at.desc())
    )
    users = result.scalars().all()
    return users


# ===============================
# GET USER BY ID
# ===============================
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(UserORM).where(UserORM.id == user_id)
    )
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# ===============================
# GET USER WITH ORDERS
# ===============================
@app.get("/users/{user_id}/with-orders", response_model=UserWithOrders)
async def get_user_with_orders(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(UserORM)
        .options(selectinload(UserORM.orders))
        .where(UserORM.id == user_id)
    )
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# ===============================
# UPDATE USER
# ===============================
@app.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(UserORM).where(UserORM.id == user_id)
    )
    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_user, field, value)

    await db.commit()
    await db.refresh(db_user)

    return db_user


# ===============================
# DELETE USER
# ===============================
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(UserORM).where(UserORM.id == user_id)
    )
    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(db_user)
    await db.commit()

    return None


# ===============================
# CREATE ORDER
# ===============================
@app.post("/orders", response_model=OrderResponse, status_code=201)
async def create_order(
    order: OrderCreate,
    db: AsyncSession = Depends(get_db)
):
    # sprawdz czy user istnieje
    result = await db.execute(
        select(UserORM).where(UserORM.id == order.user_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="User not found")

    db_order = OrderORM(**order.model_dump())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)

    return db_order