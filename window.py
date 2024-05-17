from tkinter import Tk, BOTH, Canvas
from cell import Cell

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
    c1 = Cell(window, has_right_wall=False)
    c2 = Cell(window, has_left_wall=False, has_bottom_wall=False)
    c3 = Cell(window, has_top_wall=False)
    c1.draw(10, 10, 50, 50)
    c2.draw(50, 10, 90, 50)
    c3.draw(50, 50, 90, 90)

    c1.draw_move(c2)
    c2.draw_move(c3)
    c3.draw_move(c2, undo=True)

    window.wait_for_close()
