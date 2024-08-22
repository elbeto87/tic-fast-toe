from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/start_game")
def start_game():
    return {"Game": "Started"}
