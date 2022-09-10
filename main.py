from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    #control size of output window with parameters in Window(x, y)
    win = Window(525, 525)
    
    #creating maze object, you can tweak settings of maze with these parameters
    #space between top of window and top of grid
    x_Padding = 5
    #space between left of window and left of grid
    y_Padding = 5
    columns = 10
    rows = 10
    #x, y size of cells
    cell_x = 50
    cell_y = 50
    maze = Maze(x_Padding, y_Padding, rows, columns, cell_x, cell_y, win)

    #solving the created maze
    maze.solve()

    win.wait_for_close()

main()