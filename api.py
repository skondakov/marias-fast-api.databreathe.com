from fastapi import FastAPI
from fastapi.responses import JSONResponse
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

    db_conn = db()
    cursor = db_conn.cursor()

    cursor.execute(
        "SELECT id, `name` "
        "FROM customer "
        "WHERE (MONTH(birthdate) = MONTH(NOW())) AND (DAY(birthdate) = DAY(NOW()))"
    )

    response = {'customers': []}
    for (id, name) in cursor:

        response['customers'].append({
            'customer_id': id,
            'customer_first_name': name
        })

    cursor.close()

    return JSONResponse(content=response, headers={'Content-Type': 'application/json'})
