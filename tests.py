import unittest
from maze import Maze


class Test_create_cells(unittest.TestCase):
    def runTest1(self):
        maze = Maze(1, 1, 100, 50, 50, 50)

        self.assertEqual(len(maze.cells), maze.columns, "columns is not correct")
        print(f"{len(maze.cells)} columns")
        self.assertEqual(len(maze.cells[0]), maze.rows, "rows are not correct")
        print(f"{len(maze.cells[0])} rows")


    def runTest2(self):
        maze = Maze(1, 1, 4, 77, 50, 50)

        self.assertEqual(len(maze.cells), maze.columns, "columns is not correct")
        print(f"{len(maze.cells)} columns")
        self.assertEqual(len(maze.cells[0]), maze.rows, "rows are not correct")
        print(f"{len(maze.cells[0])} rows")

if __name__ == '__main__':
    unittest.main() 