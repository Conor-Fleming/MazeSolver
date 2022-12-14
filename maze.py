from cell import Cell
from window import Window, Line, Point 
import time
import random


class Maze:
    #constructor
    def __init__(self, x1, y1, columns, rows, cell_size_x, cell_size_y, window, seed=None):
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
        self.reset_visited()
    
    
    def solve(self):
        return self.solve_maze(0, 0)
    
    def solve_maze(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if self.cells[i][j] == self.cells[self.columns-1][self.rows-1]:
            return True

        direction = [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]

        #check each direction and visited status
        for col, row in direction:
            #move to the right
            if col > i and col <= self.columns - 1:
                if self.cells[col][row].has_left_wall == False and self.cells[col][row].visited == False:
                    self.cells[i][j].draw_move(self.cells[col][row])
                    if self.solve_maze(col, row):
                        return True
                    self.cells[i][j].draw_move(self.cells[col][row], True)
            #move to the left
            if col < i and col >= 0:
                if self.cells[col][row].has_right_wall == False and self.cells[col][row].visited == False:
                    self.cells[i][j].draw_move(self.cells[col][row])
                    if self.solve_maze(col, row):
                        return True
                    self.cells[i][j].draw_move(self.cells[col][row], True)
            #move down
            if row > j and row <= self.rows - 1:
                if self.cells[col][row].has_top_wall == False and self.cells[col][row].visited == False:
                    self.cells[i][j].draw_move(self.cells[col][row])
                    if self.solve_maze(col, row):
                        return True
                    self.cells[i][j].draw_move(self.cells[col][row], True)
            #move up
            if row < j and row >= 0:
                if self.cells[col][row].has_bottom_wall == False and self.cells[col][row].visited == False:
                    self.cells[i][j].draw_move(self.cells[col][row])
                    if self.solve_maze(col, row):
                        return True
                    self.cells[i][j].draw_move(self.cells[col][row], True)
        return False

    def create_cells(self):
        #looping through number of specified rows and columns and creating cells to be addded to cells[][] matric
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
            #list to store potential next cells coordinates
            to_visit = []
            
            #adjacent cells -> top cells[i][j-1] / bottom cells[i][j+1] / left cells[i-1][j] / right cells[i+1][j]
            #adding nested ifs to keep index in range, will look into a better way to do this but for now this seems to work
            if j -1 >= 0:
                if self.cells[i][j-1].visited == False:
                    coordinate = [i, j-1]
                    to_visit.append(coordinate)

            if j + 1 <= self.rows - 1:
                if self.cells[i][j+1].visited == False:
                    coordinate = [i, j+1]
                    to_visit.append(coordinate)

            if i - 1 >= 0:
                if self.cells[i-1][j].visited == False:
                    coordinate = [i-1, j]
                    to_visit.append(coordinate)

            if i + 1 <= self.columns - 1:
                if self.cells[i+1][j].visited == False:
                    coordinate = [i+1, j]
                    to_visit.append(coordinate)
                
            if not to_visit:
                self.draw_cell(i, j)
                return

            direction = random.randrange(0, len(to_visit))
            #looking to see the direction we are moving based on i, j coordinates
            # removing walls and recursively calling create_maze() method  
            if to_visit[direction][1] < j:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
                self.create_maze(i, j-1)

            #looking to see the direction we are moving based on i, j coordinates
            # removing walls and recursively calling create_maze() method  
            if to_visit[direction][1] > j:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
                self.create_maze(i, j+1)

            #looking to see the direction we are moving based on i, j coordinates
            # removing walls and recursively calling create_maze() method  
            if to_visit[direction][0] < i:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
                self.create_maze(i-1, j)

            #looking to see the direction we are moving based on i, j coordinates
            # removing walls and recursively calling create_maze() method    
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
        
    #sleeping before each redraw call as to slow down the visuals so a human can follow
    def animate(self):
        self.window.redraw()
        time.sleep(.05)

    #resetting visited property after creating maze so we can reference visited when solving
    def reset_visited(self):
        for i in range(self.columns):
            for j in range(self.rows):
                self.cells[i][j].visited = False