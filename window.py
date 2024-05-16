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
    Cell(window).draw(10, 10, 50, 50)
    Cell(window, has_top_wall=False).draw(70, 10, 110, 50)
    Cell(window, has_right_wall=False).draw(130, 10, 170, 50)
    Cell(window, has_left_wall=False).draw(190, 10, 230, 50)
    Cell(window, has_bottom_wall=False).draw(250, 10, 290, 50)
    window.wait_for_close()
