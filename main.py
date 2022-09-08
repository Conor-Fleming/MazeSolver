from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(5, 5, 10, 10, 50, 50, win)

    win.wait_for_close()

main()