from typing import Optional, List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    url_image: Optional[str]
    price: Optional[float]
    discount: Optional[int]


class Product(ProductBase):
    id: int
    category: Optional[int]

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int
    products: Optional[List[Product]] = []

    class Config:
        orm_mode = True
