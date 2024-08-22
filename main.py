from fastapi import FastAPI
from pydantic import BaseModel

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


@app.post("/make_move")
def make_move(make_move: MakeMoveRequest):
    logger.info(f"Player is making a move at row: {make_move.row} and column: {make_move.col}")
    tic_tac_toe.make_player_move(make_move.row, make_move.col)
    logger.info(f"Verifying if player {tic_tac_toe.player} is a winner")
    if tic_tac_toe.is_a_winner(tic_tac_toe.player):
        return {
            "message": f"Player {tic_tac_toe.player} wins!",
            "board": tic_tac_toe.print_board()
        }
    logger.info(f"Computer is making a random move")
    tic_tac_toe.make_computer_move()
    logger.info(f"Verifying if player {tic_tac_toe.computer} is a winner")
    if tic_tac_toe.is_a_winner(tic_tac_toe.computer):
        return {
            "message": f"Player {tic_tac_toe.computer} wins!",
            "board": tic_tac_toe.print_board()
        }
    return {
        "message": "Move made successfully",
        "board": tic_tac_toe.print_board()
    }
