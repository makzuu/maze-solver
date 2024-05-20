from time import sleep
from cell import Cell
import random

class Maze:
    def __init__(self, x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        for _ in range(self.num_cols):
            col = []
            for _ in range(self.num_rows):
                col.append(Cell(self.win))
            self._cells.append(col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = i * self.cell_size_x + self.x1
        x2 = x1 + self.cell_size_x
        y1 = j * self.cell_size_y + self.y1
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        i = 0
        j = 0
        w = self.num_cols - 1
        z = self.num_rows - 1
        top_left_cell = self._cells[i][j]
        bottom_right_cell = self._cells[w][z]
        top_left_cell.has_top_wall = False
        bottom_right_cell.has_bottom_wall = False
        self._draw_cell(i, j)
        self._draw_cell(w, z)

    # TODO: create your own _break_walls_r method
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))
            if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if j + 1 < self.num_rows and not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            index = random.randrange(len(to_visit))
            if to_visit[index][0] < i:
                self._cells[i][j].has_left_wall = False
            if to_visit[index][0] > i:
                self._cells[i][j].has_right_wall = False
            if to_visit[index][1] < j:
                self._cells[i][j].has_top_wall = False
            if to_visit[index][1] > j:
                self._cells[i][j].has_bottom_wall = False

            w, z = to_visit[index]
            self._break_walls_r(w, z)


