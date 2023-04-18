from board import Board

def test_board_creates_size_four():
    board = Board(4)
    assert board.rows == [["O", "O", "O", "O"], ["O", "O", "O", "O"], ["O", "O", "O", "O"], ["O", "O", "O", "O"]]