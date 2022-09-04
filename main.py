from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi

import crud
import schemas
from database import SessionLocal


app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/categories", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    categories = crud.get_categories(db)
    return categories


@app.get("/products", response_model=List[schemas.Product])
def read_products(skip: int = 0, category_id: int = -1, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit) \
        if category_id == -1 else crud.get_products_by_category(db, category_id)
    return products


@app.get("/products/{id}", response_model=schemas.Product)
def read_product_by_id(id: int, db: Session = Depends(get_db)):
    product = crud.get_products_by_id(db, product_id=id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="BSALE Test",
        version="2.5.0",
        description="Desafio BSALE - Documentacion",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi