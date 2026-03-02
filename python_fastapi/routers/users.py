from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

users_db = {}

@router.get("/")
async def get_users():
    return list(users_db.values())

@router.get("/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@router.post("/")
async def create_user(user: dict):
    new_id = max(users_db.keys()) + 1 if users_db else 1
    user["id"] = new_id
    users_db[new_id] = user
    return user