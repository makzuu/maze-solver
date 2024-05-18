from time import sleep
from cell import Cell

class Maze:
    def __init__(self, x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

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
