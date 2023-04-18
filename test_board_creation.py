from board import Board

def test_board_creates_size_two():
    board = Board(2)
    assert board.rows == [["O", "O"], ["O", "O"]]

def test_board_creates_size_four():
    board = Board(4)
    assert board.rows == [["O", "O", "O", "O"], ["O", "O", "O", "O"], ["O", "O", "O", "O"], ["O", "O", "O", "O"]]

def test_board_creates_size_seven():
    board = Board(7)
    assert board.rows == [["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"]]