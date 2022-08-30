from textwrap import fill
from tkinter import Tk, BOTH, Canvas
from turtle import width

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title = "Root Window"
        self.__canvas = Canvas(self.__root, bg = "white", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, Line, fill_color):
        Line.draw(Line, fill_color)


    
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
    
    def close(self):
        self.__root = False

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, Point1, Point2) -> None:
        self.__point1 = Point1
        self.__point2 = Point2

#working on the canvas item here
    def draw(self, Canvas, fill_color):
        .create_line(self.__point1, self.__point2, fill = fill_color, width = 2)
        .pack(fill = BOTH, expand = True)

        

def main():
    win = Window(800, 600)
    line1 = Line(Point(3, 6),Point(7, 10))
    line2 = Line( Point(1, 8),Point(7, 2))
    win.draw_line(line1, "green")
    win.draw_line(line2, "red")
    win.wait_for_close()

main()
