from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Создаем экземпляр FastAPI
app = FastAPI()

# Определяем маршрут
@app.get("/test")
def read_root():
    return {"message": "hello from root"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/", response_class=HTMLResponse)
async def get_names():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lorem Ipsum</title>
    </head>
    <body>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis lectus at purus luctus, sit amet consequat ante suscipit.</p>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)