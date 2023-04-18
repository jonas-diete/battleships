class Board:
    def __init__(self, size):
        self.rows = []
        for i in size:
            row = []
            for j in size:
                row.append("O")
            self.rows.append(row)