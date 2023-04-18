from board import Board
from ship import Ship

class Game:
    def start_game(self):
        board = Board(7)
        self.display_board(board)
        ship = Ship(3, [1, 3], "horizontal")
        board.place_ship(ship)
        print("")
        self.display_board(board)

    def display_board(self, board):
        for row in board.rows:
            print(" ".join(row))