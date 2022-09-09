import unittest
import sys
from maze import Maze


class Test_create_cells(unittest.TestCase):

    def setUp(self):
        pass

    def test_Rows_Cols1(self):
        rows = 100
        cols = 50
        maze1 = Maze(0, 0, rows, cols, 50, 50)
        
        self.assertEqual(len(maze1.cells), maze1.columns, "columns is not correct")
       
        self.assertEqual(len(maze1.cells[0]), maze1.rows, "rows are not correct")
       


    def test_Rows_Cols2(self):
        rows = 4
        cols = 77
        maze2 = Maze(0, 0, rows, cols, 50, 50)

        self.assertEqual(len(maze2.cells), maze2.columns, "columns is not correct")
  
        self.assertEqual(len(maze2.cells[0]), maze2.rows, "rows are not correct")
       

    def test_Rows_Cols3(self):
        rows = 3
        cols = 2
        maze3 = Maze(0, 0, rows, cols, 50, 50)

        self.assertEqual(len(maze3.cells), maze3.columns, "columns is not correct")
    
        self.assertEqual(len(maze3.cells[0]), maze3.rows, "rows are not correct")

class Test_break_walls(unittest.TestCase):
    def setUp(self):
        pass

    def test_entrance(self):
        rows = 10
        cols = 10
        maze = Maze(0, 0, rows, cols, 10, 10)
        self.assertEqual(maze.cells[0][0].has_top_wall, False)

    def test_exit(self):
        rows = 10
        cols = 10
        maze = Maze(0, 0, rows, cols, 10, 10)
        self.assertEqual(maze.cells[cols-1][rows-1].has_bottom_wall, False)

class Test_reset_visited(unittest.TestCase):
    def setUp(self):
        pass

    sys.setrecursionlimit(10000)

    def test_visited(self):
        maze = Maze(0, 0, 10, 10, 2, 2)
        check = True
        for i in range(maze.columns):
            for j in range(maze.rows):
                if maze.cells[i][j] == True:
                    check = False
                    return

        self.assertTrue(check)        

if __name__ == "__main__":
    unittest.main() 