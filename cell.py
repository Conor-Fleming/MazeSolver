from window import Window, Line, Point

class Cell:
    def __init__(self, window):
        self.visited = False
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
        if self.window == None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            border = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(border, "black")
        else:
            border = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(border, "white")

        if self.has_right_wall:
            border = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(border, "black")
        else:
            border = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(border, "white")

        if self.has_top_wall:
            border = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(border, "black")
        else:
            border = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(border, "white")

        if self.has_bottom_wall:
            border = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(border, "black")
        else:
            border = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(border, "white")

    def draw_move(self, to_cell, undo = False):
        if self.window == None:
            return
         
        startX = (self.x2 + self.x1) / 2
        startY = (self.y2 + self.y1) / 2
        endX = (to_cell.x2 + to_cell.x1) / 2
        endY = (to_cell.y2 + to_cell.y1) / 2
        
        color = "red"
        if undo:
            color = "grey"

        move = Line(Point(startX, startY), Point(endX, endY))
        self.window.draw_line(move, color)

        

     

        

