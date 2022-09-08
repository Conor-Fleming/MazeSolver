from cell import Cell
from window import Window, Line, Point 


class Maze:
    def __init__(self, x1, y1, rows, columns, cell_size_x, cell_size_y, window,):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.columns = columns
        self.cell_size_x = cell_size_x
        self.cell_sixe_y = cell_size_y
        self.window = window

        self.create_cells()

    def create_cells(self):
        self.cells = []

        for col in self.columns:
            column = []
            for row in self.rows:
                column.append(Cell(self.window))
            cells.append(column)
        
        for i in cells:
            for j in cells[i]:
                j.draw_cell(i, j)
        
    #calc x,y of cell with i, j and cell sizes     
    def draw_cell(self, i, j):
        self.startX = i + self.x1
        self.startY = j + self.y1
        self.endX = startX + self.cell_size_x
        self.endY = startY + self.cell_sixe_y
        self.draw(self.startX, self.startY, self.endX, self.endY)
        
    def animate(self):
        self.window.redraw()
        time.sleep(.05)




