

# DESAFIO BSALE

BSALE Test - API Products


## Installation

Instalar virtualenv globalmente con Python >=3.10

```bash
  pip install virtualenv
```

## Run Locally

Ir al directorio del proyecto

```bash
  cd bsale-test
```
Crear entorno virtual

```bash
  python -m virtualenv env -p python3
```
Ingresar al entorno virtual 

```bash
  "env/Scripts/activate"
```
Instalar dependencias

```bash
  pip install -r requirement.txt
```

Start the server

```bash
  uvicorn main:app --port 8000 --reload
```



## API Reference

#### Obtener todos los productos

```http
  GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `skip`      | `integer` | **Required**. Skip to pagination |
|  `limit`      | `integer` | **Required**. Limit to pagination |

#### Obtener todos los productos por categoría

```http
  GET /api/categories/${id}/products
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of category to fetch |
| `skip`      | `integer` | **Required**. Skip to pagination |
|  `limit`      | `integer` | **Required**. Limit to pagination |




## Documentacion

[Documentacion de la API](https://bsale-products-api.herokuapp.com/redoc)


## Authors

- [@oliveraluis11](https://www.github.com/oliveraluis11)


## References

 - [Fastapi](https://fastapi.tiangolo.com/es/)
 - [Deploying FastAPI to Heroku](https://medium.com/fastapi-tutorials/deploying-fastapi-to-heroku-cd00bdcf3be4)

