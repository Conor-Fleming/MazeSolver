from cell import Cell
from window import Window, Line, Point 
import time
import random


class Maze:
    def __init__(self, x1, y1, rows, columns, cell_size_x, cell_size_y, window, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.columns = columns
        self.cell_size_x = cell_size_x
        self.cell_sixe_y = cell_size_y
        self.window = window
        if seed != None:
            random.seed(seed)
        
        self.cells = []
        self.create_cells()
        self.create_entrance_exit()
        self.create_maze(0, 0)

    def create_cells(self):
        for col in range(self.columns):
            column = []
            for row in range(self.rows):
                column.append(Cell(self.window))
            self.cells.append(column)
        
        for i in range(self.columns):
            for j in range(self.rows):
                self.draw_cell(i, j)
        
    def create_entrance_exit(self):
        #entrance wall broken
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)

        #exit wall broken
        self.cells[self.columns-1][self.rows-1].has_bottom_wall = False
        self.draw_cell(self.columns-1, self.rows-1)

    def create_maze(self, i, j):
        self.cells[i][j].visited = True

        while self.cells[i][j] != None:
            #using dictionary to make it easier to see what way we are going
            to_visit = []
            #adjacent cells -> top cells[i][j-1] / bottom cells[i][j+1] / left cells[i-1][j] / right cells[i+1][j]

            if self.cells[i][j-1].visited == False:
                coordinate = [i, j-1]
                print(coordinate)
                to_visit.append(coordinate)

            if self.cells[i][j+1].visited == False:
                coordinate = [i, j+1]
                print(coordinate)
                to_visit.append(coordinate)

            if self.cells[i-1][j].visited == False:
                coordinate = [i-1, j]
                print(coordinate)
                to_visit.append(coordinate)

            if self.cells[i+1][j].visited == False:
                coordinate = [i+1, j]
                print(coordinate)
                to_visit.append(coordinate)
            
            if not to_visit:
                self.draw_cell(i, j)
                return
            
            print(to_visit)

            direction = random.randrange(0, len(to_visit))
            print(direction)
            if to_visit[direction][1] < j:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
                self.create_maze(i, j-1)
            if to_visit[direction][1] > j:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
                self.create_maze(i, j+1)
            if to_visit[direction][0] < i:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
                self.create_maze(i-1, j)
            if to_visit[direction][0] > i:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
                self.create_maze(i+1, j)


    #calc x,y of cell with i, j and cell sizes     
    def draw_cell(self, i, j):
        if self.window == None:
            return
        
        self.startX = self.x1 + i * self.cell_size_x
        self.startY = self.y1 + j * self.cell_sixe_y
        self.endX = self.startX + self.cell_size_x
        self.endY = self.startY + self.cell_sixe_y
        self.cells[i][j].draw(self.startX, self.startY, self.endX, self.endY)
        self.animate()
        
    def animate(self):
        self.window.redraw()
        time.sleep(.05)




