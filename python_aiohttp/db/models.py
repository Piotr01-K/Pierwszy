from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from .base import Base

# dodane lesson 32 task 7
# class Base(DeclarativeBase):
#     pass

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)