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

@app.get("/")
def read_root():
    return {"message": "This is test_server_2"}