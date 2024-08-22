from fastapi import FastAPI

from logger import logger
from tic_tac_toe import TicTacToe

app = FastAPI()


tic_tac_toe = TicTacToe()


@app.post("/start_game")
def start_game():
    return {
        "message": f"Welcome to Tic Fast Toe",
        "board": tic_tac_toe.start_game()
    }


@app.post("/make_move")
def make_move(row: int, col: int):
    logger.info(f"Making move at row: {row} and column: {col}")
    tic_tac_toe.make_player_move(row, col)
    if tic_tac_toe.is_a_winner(tic_tac_toe.player):
        return {
            "message": f"Player {tic_tac_toe.player} wins!",
            "board": tic_tac_toe.print_board()
        }
    tic_tac_toe.make_computer_move()
    if tic_tac_toe.is_a_winner(tic_tac_toe.computer):
        return {
            "message": f"Player {tic_tac_toe.computer} wins!",
            "board": tic_tac_toe.print_board()
        }
    return {
        "message": "Move made successfully",
        "board": tic_tac_toe.print_board()
    }
