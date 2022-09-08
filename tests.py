import unittest
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
       


if __name__ == "__main__":
    unittest.main() 