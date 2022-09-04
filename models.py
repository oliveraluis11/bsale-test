from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)

    products = relationship("Product", back_populates="category_owner")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    url_image = Column(String(100))
    price = Column(Float)
    discount = Column(Integer)
    category = Column(Integer, ForeignKey('category.id'), nullable=False, index=True)

    category_owner = relationship("Category", back_populates="products")
