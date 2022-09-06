from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(50, 50, 100, 100)

    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell1.has_bottom_wall = False
    cell.draw(100, 50, 150, 100)

    cell1.draw_move(cell)

    win.wait_for_close()

main()