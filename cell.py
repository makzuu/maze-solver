from point import Point
from line import Line

class Cell:
    def __init__(self, win,
                 has_left_wall=True, has_right_wall=True,
                 has_top_wall=True, has_bottom_wall=True
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.win = win

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        fill_color = "#ccc"
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)),
                               fill_color)
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)),
                               fill_color)
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)),
                               fill_color)
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)),
                               fill_color)

    def center(self):
        width = self.x2 - self.x1
        xcenter = self.x1 + (width / 2)
        height = self.y2 - self.y1
        ycenter = self.y1 + (height / 2)
        return Point(xcenter, ycenter)

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"
        line = Line(self.center(), to_cell.center())
        self.win.draw_line(line, fill_color)
