from fastapi import FastAPI

from logger import logger
from tic_tac_toe import TicTacToe

app = FastAPI()


@app.get("/start_game")
def start_game():
    logger.info("Starting Tic Tac Toe Game")
    return {
        "message": "Welcome to Tic Fast Toe",
        "board": TicTacToe().start_game()
    }
