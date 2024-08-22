import random


class TicTacToe:

    def __init__(self):
        self.player = "X"
        self.computer = "O"
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

    def make_player_move(self, row: int, col: int):
        self.board[row-1][col-1] = self.player
        return self.print_board()

    def make_computer_move(self):
        random_row = random.randint(0, 2)
        random_col = random.randint(0, 2)
        while self.board[random_row][random_col] != "_":
            random_row = random.randint(0, 2)
            random_col = random.randint(0, 2)
        self.board[random_row][random_col] = self.computer

    def is_a_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False
