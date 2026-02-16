from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, List
import re

app = FastAPI()


class Product(BaseModel):
    name: str = Field(..., min_length=3)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    discount_percent: Optional[float] = Field(None, ge=0, le=100)
    category: str
    tags: List[str] = []

    @field_validator("name")
    def name_must_be_alphanumeric(cls, v):
        if not re.match(r"^[a-zA-Z0-9\s]+$", v):
            raise ValueError("Name must contain only letters, numbers and spaces")
        return v.strip().title()

    @field_validator("category")
    def category_must_be_valid(cls, v):
        valid_categories = ["Electronics", "Clothing", "Books", "Food"]
        if v not in valid_categories:
            raise ValueError(f"Category must be one of: {valid_categories}")
        return v

    @field_validator("tags")
    def tags_must_be_lowercase(cls, v):
        return [tag.lower().strip() for tag in v]

    @model_validator(mode="after")
    def check_discount_logic(self):
        if self.price and self.discount_percent:
            if self.price > 1000 and self.discount_percent > 20:
                raise ValueError(
                    "Expensive products (>1000) cannot have discount >20%"
                )
        return self

    @property
    def final_price(self) -> float:
        if self.discount_percent:
            return self.price * (1 - self.discount_percent / 100)
        return self.price


@app.post("/products", response_model=Product)
async def create_product(product: Product):
    return product