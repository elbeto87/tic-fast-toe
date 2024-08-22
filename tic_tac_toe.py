class TicTacToe:

    def __init__(self, player_1: str = "X", player_2: str = "O"):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = None

    def reset_board(self):
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]
        return self.board

    def print_board(self):
        return [" | ".join(row) for row in self.board]

    def start_game(self):
        self.reset_board()
        return self.print_board()
