from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Создаем экземпляр FastAPI
app = FastAPI()

# Определяем маршрут
@app.get("/")
def read_root():
    return {"message": "This is test_server_2"}
