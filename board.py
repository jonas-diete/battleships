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
        pass
