from cell import Cell


class Maze:
    def __init__(self, x1, y1, rows, columns, cell_size_x, cell_size_y, window,):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.columns = columns
        self.cell_size_x = cell_size_x
        self.cell_sixe_y = cell_size_y
        self.window = window

        self.creat_cells()

    def create_cells():
        cells = []

        for col in self.columns:
            column = []
            for row in self.rows:
                column.append(Cell(self.window))
            cells.append(column)
        
    #calc x,y of cell with i, j and cell sizes     
    def draw_cell(self, i, j):
        None

    def animate(self):
        None




