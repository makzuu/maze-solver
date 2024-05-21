from window import Window
from maze import Maze

window = Window(800, 600)
result = Maze(50, 50, 10, 14, 50, 50, window).solve()
print("Reached end cell:", result)

window.wait_for_close()
