from window import Cell, Window, Line, Point

def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.has_right_wall = False
    cell.has_bottom_wall = False
    cell.draw(500, 500, 100, 100)



    win.wait_for_close()

main()