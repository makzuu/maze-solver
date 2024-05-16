from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="#181818", width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

if __name__ == "__main__":
    window = Window(800, 600)
    window.draw_line(Line(Point(0, 300), Point(800, 300)), "#ccc")
    window.draw_line(Line(Point(100, 80), Point(700, 520)), "#ccc")
    window.draw_line(Line(Point(100, 200), Point(700, 400)), "#ccc")
    window.wait_for_close()
