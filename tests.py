import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols
                )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows
                )
    def test_maze_create_cells2(self):
        num_cols = 8
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols
                )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows
                )

    def test_break_entrance_and_exit(self):
        num_cols = 8
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
                m1._cells[0][0].has_top_wall,
                False
                )
        self.assertEqual(
                m1._cells[m1.num_cols - 1][m1.num_rows - 1].has_bottom_wall,
                False
                )

    def test_reset_cells_visited(self):
        num_rows = 12
        num_cols = 6
        m = Maze(0, 0, num_rows, num_cols, 50, 50)
        m._break_walls_r(0, 0)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(m._cells[i][j].visited, True)
        m._reset_cells_visited()
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(m._cells[i][j].visited, False)

    def test_break_walls_r(self):
        r = Maze(0, 0, 2, 2, 50, 50, seed=0)
        self.assertEqual(r._cells[0][0].has_left_wall, True)
        self.assertEqual(r._cells[0][0].has_right_wall, False)
        self.assertEqual(r._cells[0][0].has_top_wall, False)
        self.assertEqual(r._cells[0][0].has_bottom_wall, False)

        self.assertEqual(r._cells[0][1].has_left_wall, True)
        self.assertEqual(r._cells[0][1].has_right_wall, False)
        self.assertEqual(r._cells[0][1].has_top_wall, False)
        self.assertEqual(r._cells[0][1].has_bottom_wall, True)

        self.assertEqual(r._cells[1][0].has_left_wall, False)
        self.assertEqual(r._cells[1][0].has_right_wall, True)
        self.assertEqual(r._cells[1][0].has_top_wall, True)
        self.assertEqual(r._cells[1][0].has_bottom_wall, True)

        self.assertEqual(r._cells[1][1].has_left_wall, False)
        self.assertEqual(r._cells[1][1].has_right_wall, True)
        self.assertEqual(r._cells[1][1].has_top_wall, True)
        self.assertEqual(r._cells[1][1].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()
