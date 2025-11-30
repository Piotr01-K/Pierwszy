from app import db

# -------------------------------
#  MODEL MESSAGE (Twój dotychczasowy)
# -------------------------------

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Message {self.text}>"


# -------------------------------
#  RELACJA ONE-TO-MANY (1:N)
#  Category -> Product
# -------------------------------

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)

    # relacja 1:N — lista produktów
    products = db.relationship(
        "Product",
        backref="category",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "product_count": len(self.products)
        }


# -------------------------------
#  TABELA ŁĄCZĄCA — Many-to-Many (M:N)
# -------------------------------

product_tags = db.Table(
    "product_tags",
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
    db.Column("added_at", db.DateTime, default=db.func.now())
)


# -------------------------------
#  MODEL TAG
# -------------------------------

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    color = db.Column(db.String(7), default="#6c757d")

    def __repr__(self):
        return f"<Tag {self.name}>"


# -------------------------------
#  MODEL PRODUCT (z relacjami 1:N i M:N)
# -------------------------------

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=db.func.now())

    # klucz obcy do Category (1:N)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    # relacja M:N (z tagami)
    tags = db.relationship(
        "Tag",
        secondary=product_tags,
        lazy="subquery",
        backref=db.backref("products", lazy=True)
    )

    def __repr__(self):
        return f"<Product {self.name} ({self.price} PLN)>"


# -------------------------------
#  RELACJA ONE-TO-ONE (1:1)
#  User -> Profile
# -------------------------------

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # relacja 1:1
    profile = db.relationship(
        "Profile",
        backref="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email}>"


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)

    full_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255))
    phone = db.Column(db.String(20))

    def __repr__(self):
        return f"<Profile for user_id={self.user_id}>"

