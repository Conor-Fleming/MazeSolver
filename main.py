from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    c0 = Cell(win)
    c0.has_right_wall = False
    c0.draw(50, 50, 100, 100)

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.has_right_wall = False
    c1.draw(100, 50, 150, 100)

    c0.draw_move(c1)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(150, 50, 200, 100)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_bottom_wall = False
    c3.draw(150, 100, 200, 150)

    c2.draw_move(c3)

    win.wait_for_close()

main()