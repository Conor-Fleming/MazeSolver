from ctypes.wintypes import POINT
from curses import window
from textwrap import fill
from tkinter import Tk, BOTH, Canvas
from turtle import width

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Root Window")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg = "white", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = True)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def close(self):
        print("closing window...")
        self.__running = False

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = fill_color, width = 2)
        canvas.pack(fill = BOTH, expand = True)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y