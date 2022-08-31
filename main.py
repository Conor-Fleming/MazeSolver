from window import Cell, Window, Line, Point

def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(10, 10, 100, 100)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(10, 10, 100, 100)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(100, 100, 50, 50)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(20, 10, 20, 10)

    win.wait_for_close

main()