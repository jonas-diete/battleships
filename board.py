class Board:
    def __init__(self, size):
        self.rows = self.create_rows(size)

    
    def create_rows(self, size):
        rows = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append("O")
            rows.append(row)
        return rows
    
    def place_ship(self, ship):
        for i in range(ship.size):
            if ship.orientation == "horizontal":
                self.rows[ship.top_left_coordinate[1]][ship.top_left_coordinate[0] + i] = "#"
