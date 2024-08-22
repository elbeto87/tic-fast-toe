from collections import Counter
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from database import add_game_to_history, get_game_history
from logger import logger
from tic_tac_toe import TicTacToe

app = FastAPI()

tic_tac_toe = TicTacToe()


class MakeMoveRequest(BaseModel):
    row: int
    col: int


@app.post("/")
def start_game():
    return {
        "message": f"Welcome to Tic Fast Toe",
        "board": tic_tac_toe.start_game()
    }


@app.post("/make_move_request")
def make_move(make_move_request: MakeMoveRequest):
    logger.info(f"Player is making a move at row: {make_move_request.row} and column: {make_move_request.col}")
    tic_tac_toe.make_player_move(make_move_request.row, make_move_request.col)
    logger.info(f"Verifying if player {tic_tac_toe.player} is a winner")
    if tic_tac_toe.is_a_winner(tic_tac_toe.player):
        add_game_to_history(timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), winner=tic_tac_toe.player)
        return {
            "message": f"Player {tic_tac_toe.player} wins!",
            "board": tic_tac_toe.print_board()
        }
    logger.info(f"Computer is making a random move")
    tic_tac_toe.make_computer_move()
    logger.info(f"Verifying if player {tic_tac_toe.computer} is a winner")
    if tic_tac_toe.is_a_winner(tic_tac_toe.computer):
        add_game_to_history(timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), winner=tic_tac_toe.computer)
        return {
            "message": f"Player {tic_tac_toe.computer} wins!",
            "board": tic_tac_toe.print_board()
        }
    return {
        "message": "Move made successfully",
        "board": tic_tac_toe.print_board()
    }


@app.get("/game_history")
def game_history():
    return {
        "game_history": get_game_history()
    }


@app.get("/count_of_wins")
def count_of_player_wins():
    game_history = get_game_history()
    winners = [game["winner"] for game in game_history]
    counts = Counter(winners)

    return {
        "player_wins": counts.get("X", 0),
        "computer_wins": counts.get("O", 0)
    }
