from ctypes.wintypes import POINT
from curses import window
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

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
    
    def close(self):
        self.__running = False

class Cell:
    def __init__(self, window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.window = window

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            border = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(border, "black")
        if self.has_right_wall:
            border = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(border, "black")
        if self.has_top_wall:
            border = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(border, "black")
        if self.has_bottom_wall:
            border = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(border, "black")

class Line:
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = fill_color, width = 2)
        canvas.pack(fill = BOTH, expand = True)

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y