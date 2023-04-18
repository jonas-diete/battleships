class Board:
    def __init__(self, size):
        self.rows = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append("O")
            self.rows.append(row)