import strawberry
from typing import Optional, List
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

# ========================================
# 🗄️ FAKE BAZA
# ========================================

fake_users_db = [
    {"id": 1, "name": "Jan Kowalski", "email": "jan@example.com"},
    {"id": 2, "name": "Anna Nowak", "email": "anna@example.com"},
    {"id": 3, "name": "Piotr Wiśniewski", "email": "piotr@example.com"},
]

# ========================================
# 🧩 Typ GraphQL
# ========================================

@strawberry.type
class User:
    id: int
    name: str
    email: str

# ========================================
# 🔍 Query
# ========================================

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        """Zwraca użytkownika po ID"""
        for u in fake_users_db:
            if u["id"] == id:
                return User(**u)
        return None

# dodane lesson 34 task 5
    @strawberry.field
    def users(self) -> List[User]:
        """Zwraca wszystkich użytkowników"""
        return [User(**u) for u in fake_users_db]
    
# dodane lesson 34 task 6
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        """Tworzy nowego użytkownika"""

        # wyliczamy nowe ID
        new_id = max([u["id"] for u in fake_users_db]) + 1

        # tworzymy usera
        new_user_dict = {
            "id": new_id,
            "name": name,
            "email": email,
        }

        # dodajemy do fake bazy
        fake_users_db.append(new_user_dict)

        # zwracamy obiekt User
        return User(**new_user_dict)

# ========================================
# 🚀 Schema + app
# ========================================

#  schema = strawberry.Schema(query=Query)
schema = strawberry.Schema(query=Query, mutation=Mutation)   # zmienione lesson 34 task 6

app = web.Application()

app.router.add_route(
    "*",
    "/graphql",
    GraphQLView(schema=schema),
)

# ========================================
# ▶️ RUN
# ========================================

if __name__ == "__main__":
    print("🚀 GraphQL działa na http://localhost:8000/graphql")
    web.run_app(app, host="localhost", port=8000)