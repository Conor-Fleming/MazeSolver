from window import Window, Line, Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(30, 60),Point(75, 400))
    line2 = Line( Point(100, 80),Point(7, 200))
    win.draw_line(line1, "green")
    win.draw_line(line2, "red")
    win.wait_for_close()

main()