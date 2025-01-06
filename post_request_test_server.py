from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Модель данных для запроса
class Data(BaseModel):
    id: int
    name: str
    price: float
    description: str = None

app = FastAPI()

@app.post("/post_test/")
def process_test_post_request(rdata: Data):
    id = rdata.id
    name = rdata.name
    price = rdata.price
    descr = rdata.description
    return {
        "message": f"This is test POST request. The values you just sent:\n"
                   f"id: {id}\n"
                   f"name: {name}\n"
                   f"price: {price}\n"
                   f"description: {descr}\n"
    }
