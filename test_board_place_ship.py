from board import Board
from ship import Ship

def test_place_ship_horizontal1():
    board = Board(7)
    ship = Ship(3, [1, 3], "horizontal")
    board.place_ship(ship)
    assert board.rows == [["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "#", "#", "#", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"]]

def test_place_ship_horizontal2():
    board = Board(7)
    ship = Ship(4, [2, 0], "horizontal")
    board.place_ship(ship)
    assert board.rows == [["O", "O", "#", "#", "#", "#", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"]]

def test_place_ship_horizontal3():
    board = Board(7)
    ship = Ship(2, [0, 5], "horizontal")
    board.place_ship(ship)
    assert board.rows == [["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"], ["#", "#", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O"]]