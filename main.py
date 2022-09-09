from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(5, 5, 5, 5, 50, 50, win)
    maze.solve()

    win.wait_for_close()

main()