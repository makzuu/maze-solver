from tkinter import Tk, BOTH, Canvas
from maze import Maze

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
    m = Maze(50, 50, 10, 14, 50, 50, window)
    m._break_entrance_and_exit()
    m._break_walls_r(1, 1)
    m._reset_cells_visited()

    window.wait_for_close()
