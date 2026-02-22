import strawberry
from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# =========================
# FAKE BAZA DANYCH
# =========================

@strawberry.type
class User:
    id: int
    name: str
    email: str


fake_users_db = [
    User(id=1, name="Jan Kowalski", email="jan@example.com"),
    User(id=2, name="Anna Nowak", email="anna@example.com"),
]

# =========================
# QUERY
# =========================

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        for user in fake_users_db:
            if user.id == id:
                return user
        return None

    @strawberry.field
    def users(self) -> List[User]:
        return fake_users_db

# =========================
# MUTATION
# =========================

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        new_id = max(u.id for u in fake_users_db) + 1
        new_user = User(id=new_id, name=name, email=email)
        fake_users_db.append(new_user)
        return new_user

# =========================
# APP
# =========================

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = web.Application()
app.router.add_route(
    "*",
    "/graphql",
    GraphQLView(schema=schema),
)

if __name__ == "__main__":
    print("🚀 GraphQL działa na http://localhost:8000/graphql")
    web.run_app(app, host="localhost", port=8000)