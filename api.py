from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.db import db


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/customers/birthday")
async def customers_birthday():

    cursor = db.cursor()

    cursor.execute(
        "SELECT id, `name` "
        "FROM customer "
        "WHERE (MONTH(birthdate) = MONTH(NOW())) AND (DAY(birthdate) = DAY(NOW()))"
    )

    class Customer(BaseModel):
        customer_id: int
        customer_first_name: str

    response = []
    for (id, name) in cursor:

        response.append({
            'customer_id': id,
            'customer_first_name': name
        })

    cursor.close()

    return response
