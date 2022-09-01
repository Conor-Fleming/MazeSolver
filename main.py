from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.has_right_wall = False
    cell.has_top_wall = False
    cell.draw(3, 3, 50, 50)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.has_left_wall = False
    cell.has_bottom_wall = False
    cell.draw(50, 5, 100, 50)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(100, 5, 150, 50)
    


    win.wait_for_close()

main()