from board import Board

class Game:
    def start_game(self):
        board = Board(7)
        self.display_board(board)
        pass

    def display_board(self, board):
        for row in board.rows:
            print(" ".join(row))